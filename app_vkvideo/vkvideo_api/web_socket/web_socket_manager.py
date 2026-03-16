import re
import threading
from typing import TYPE_CHECKING, Optional

from loguru import logger

from app_vkvideo.utils import CallbackManager
from app_vkvideo.vkvideo_api.api.api_class import (
    VKAPIEventName,
    VkapiCatalogStreamers,
    VkapiOnlineSubscriptionStreamers,
    VkapiStreamerStreamInfo,
)
from app_vkvideo.vkvideo_api.config import WSS_TYPE_MESSAGE_RE
from .web_socket_client import WebSocketClient
from .web_socket_model import WebSocketEventClass, WebSocketEventName

if TYPE_CHECKING:
    from ..vkvideo_main import VKVideoApi


class Streamer:
    def __init__(self, streamer_nickname: str, streamer_id: Optional[int] = None):
        self.streamer_nickname = self.normalize_nickname(streamer_nickname)
        self.streamer_id: Optional[int] = streamer_id
        self.web_socket_channels: set[str] = set()
        self.subscribed_channels: set[str] = set()
        self.assigned_client_id: Optional[int] = None
        self.is_enabled: bool = True

    @staticmethod
    def normalize_nickname(streamer_nickname: str) -> str:
        return str(streamer_nickname).strip().lower()

    def update_info(self, streamer_id: Optional[int] = None, channels: Optional[set[str]] = None) -> None:
        if streamer_id:
            self.streamer_id = int(streamer_id)

        if channels is None:
            return

        clean_channels = {str(channel).strip() for channel in channels if channel}
        if not clean_channels:
            return

        self.web_socket_channels |= clean_channels

    def update_channels_from_dict(self, data: dict) -> None:
        if not isinstance(data, dict) or not self.streamer_id:
            return

        streamer_id_str = str(self.streamer_id)
        channels = {
            value
            for key, value in data.items()
            if isinstance(key, str)
               and key.startswith("ws")
               and isinstance(value, str)
               and streamer_id_str in value
        }
        self.update_info(channels=channels)


class _ClientBucket:
    def __init__(self, bucket_id: int, client: WebSocketClient):
        self.bucket_id = bucket_id
        self.client = client
        self.streamer_nicknames: set[str] = set()
        self.is_authenticated: bool = False


class WebSocketManager:
    _lock_create_web_socket_manager = threading.Lock()
    _instances: dict[str, "WebSocketManager"] = {}

    def __init__(self, vk_api: "VKVideoApi", max_streamers_per_client: int = 30):
        self.vk_api = vk_api
        self.max_streamers_per_client = max(1, int(max_streamers_per_client))

        self._callback = CallbackManager()
        self._lock = threading.RLock()
        self._is_run = False
        self.is_debug = False

        self._next_bucket_id = 1

        self._streamers: dict[str, Streamer] = {}
        self._buckets: dict[int, _ClientBucket] = {}

        self._init_callbacks()

    # ---- Factory / lifecycle -------------------------------------------------

    @classmethod
    def get_or_create_web_socket_manager(cls, vk_api: "VKVideoApi") -> Optional["WebSocketManager"]:
        if not vk_api or not getattr(vk_api, "user_id", None):
            return None

        key = str(vk_api.user_id)
        with cls._lock_create_web_socket_manager:
            if key not in cls._instances:
                cls._instances[key] = WebSocketManager(vk_api=vk_api)
            return cls._instances[key]

    @property
    def is_run(self) -> bool:
        return self._is_run

    @is_run.setter
    def is_run(self, value: bool) -> None:
        if not isinstance(value, bool):
            return

        with self._lock:
            if self._is_run == value:
                return
            self._is_run = value

        if value:
            self._start_all_clients()
        else:
            self.stop_all()

    # ---- Public API ----------------------------------------------------------

    def stop_all(self) -> None:
        with self._lock:
            buckets = list(self._buckets.values())

        for bucket in buckets:
            bucket.client.stop()

        with self._lock:
            self._buckets.clear()
            for streamer in self._streamers.values():
                streamer.assigned_client_id = None
                streamer.subscribed_channels.clear()
            self._update_web_socket_state_metrics_locked()

    def subscribe_streamer(
            self,
            streamer_nickname: str,
            web_socket_channels: list[str] | set[str] | None = None,
            streamer_id: Optional[int] = None,
    ) -> None:
        if not streamer_nickname:
            return

        should_inc_subscriptions_total = False
        with self._lock:
            streamer = self._get_or_create_streamer(streamer_nickname)
            was_enabled = streamer.is_enabled
            had_assignment = streamer.assigned_client_id is not None

            streamer.is_enabled = True
            streamer.update_info(streamer_id=streamer_id, channels=set(web_socket_channels or []))
            bucket = self._ensure_bucket_for_streamer(streamer)
            self._update_web_socket_state_metrics_locked()

            if (not was_enabled) or (not had_assignment and bucket is not None):
                should_inc_subscriptions_total = True

        if not self._is_run:
            self.is_run = True

        if bucket:
            bucket.client.run()
            self._sync_streamer_subscription(streamer.streamer_nickname)

        if should_inc_subscriptions_total:
            self.vk_api.inc_metric("vkapp_wss_subscriptions_total")

    def unsubscribe_streamer(self, streamer_nickname: str) -> None:
        if not streamer_nickname:
            return

        clear_nickname = Streamer.normalize_nickname(streamer_nickname)
        should_inc_unsubscriptions_total = False
        with self._lock:
            streamer = self._streamers.get(clear_nickname)
            if not streamer:
                return

            was_effectively_subscribed = (
                streamer.is_enabled
                or streamer.assigned_client_id is not None
                or bool(streamer.subscribed_channels)
            )

            streamer.is_enabled = False
            assigned_bucket_id = streamer.assigned_client_id

        if assigned_bucket_id is not None:
            self._unsubscribe_streamer_channels(clear_nickname)

        with self._lock:
            streamer = self._streamers.get(clear_nickname)
            if not streamer:
                return
            assigned_bucket_id = streamer.assigned_client_id
            if assigned_bucket_id is not None and assigned_bucket_id in self._buckets:
                self._buckets[assigned_bucket_id].streamer_nicknames.discard(clear_nickname)
            streamer.assigned_client_id = None
            streamer.subscribed_channels.clear()

            self._remove_empty_buckets_locked()
            if not self._streamers_with_assignment_locked():
                self._is_run = False
            self._update_web_socket_state_metrics_locked()

            should_inc_unsubscriptions_total = was_effectively_subscribed

        if should_inc_unsubscriptions_total:
            self.vk_api.inc_metric("vkapp_wss_unsubscriptions_total")

    def update_web_socket_channels(
            self,
            streamer_nickname: str,
            web_socket_channels: list[str] | set[str] | None,
            streamer_id: Optional[int] = None,
    ) -> None:
        if not streamer_nickname:
            return

        with self._lock:
            streamer = self._get_or_create_streamer(streamer_nickname)
            streamer.update_info(streamer_id=streamer_id, channels=set(web_socket_channels or []))

        if streamer.is_enabled:
            self.subscribe_streamer(
                streamer_nickname=streamer.streamer_nickname,
                web_socket_channels=list(streamer.web_socket_channels),
                streamer_id=streamer.streamer_id,
            )

    @staticmethod
    def generate_web_socket_channel_from_dict(data: dict, streamer_id: int | str) -> set[str]:
        if not streamer_id or not data or not isinstance(data, dict):
            return set()

        str_streamer_id = str(streamer_id)
        return {
            value
            for key, value in data.items()
            if isinstance(key, str)
               and key.startswith("ws")
               and isinstance(value, str)
               and str_streamer_id in value
        }

    # ---- Callback wiring -----------------------------------------------------

    def _init_callbacks(self) -> None:
        if hasattr(self, "_callbacks_initialized"):
            return

        self._callbacks_initialized = True
        self._callback.register(VKAPIEventName.STREAMER_STREAM_INFO, self.__on_streamer_stream_info)
        self._callback.register(VKAPIEventName.ONLINE_SUBSCRIPTION_STREAMERS, self.__on_online_subscription_streamers)
        self._callback.register(VKAPIEventName.CATALOG_STREAMERS, self.__on_catalog_streamers)

        self._callback.register(WebSocketEventName.WEB_SOCKET_ON_AUTHENTICATED, self.__on_web_socket_authenticated)
        self._callback.register(WebSocketEventName.WEB_SOCKET_ON_CLOSE, self.__on_web_socket_close)
        self._callback.register(WebSocketEventName.WEB_SOCKET_ON_MESSAGE, self.__on_web_socket_message)
        self._callback.register(WebSocketEventName.WEB_SOCKET_ON_ERROR, self.__on_web_socket_error)

    # ---- VK API callbacks ----------------------------------------------------

    def __on_streamer_stream_info(self, streamer_id: int, user_id: int, message: VkapiStreamerStreamInfo) -> None:
        streamer_nickname = message.data.stream.embed_url.split("/")[-1]
        stream_data = message.data.stream._data_json
        channels = self.generate_web_socket_channel_from_dict(stream_data, streamer_id=streamer_id)
        if not channels:
            return

        self.update_web_socket_channels(
            streamer_nickname=streamer_nickname,
            web_socket_channels=channels,
            streamer_id=streamer_id,
        )

    def __on_online_subscription_streamers(self, user_id: int, message: VkapiOnlineSubscriptionStreamers) -> None:
        for stream_blog in message.data.stream_blogs:
            stream_json = stream_blog.stream._data_json
            streamer_id = stream_blog.blog.owner.id
            streamer_nickname = stream_blog.blog.blog_url
            channels = self.generate_web_socket_channel_from_dict(stream_json, streamer_id=streamer_id)
            if not channels:
                continue

            self.update_web_socket_channels(
                streamer_nickname=streamer_nickname,
                web_socket_channels=channels,
                streamer_id=streamer_id,
            )

    def __on_catalog_streamers(self, user_id: int, message: VkapiCatalogStreamers) -> None:
        for stream_blog in message.data.stream_blogs:
            stream_json = stream_blog.stream._data_json
            streamer_id = stream_blog.blog.owner.id
            streamer_nickname = stream_blog.blog.blog_url
            channels = self.generate_web_socket_channel_from_dict(stream_json, streamer_id=streamer_id)
            if not channels:
                continue

            self.update_web_socket_channels(
                streamer_nickname=streamer_nickname,
                web_socket_channels=channels,
                streamer_id=streamer_id,
            )

    # ---- WebSocket callbacks -------------------------------------------------

    def __on_web_socket_authenticated(self, client: WebSocketClient, status: bool) -> None:
        bucket_id = self._get_bucket_id_by_client(client)
        if bucket_id is None:
            return

        with self._lock:
            bucket = self._buckets.get(bucket_id)
            if not bucket:
                return
            bucket.is_authenticated = bool(status)

            if not status:
                for streamer_nickname in bucket.streamer_nicknames:
                    streamer = self._streamers.get(streamer_nickname)
                    if streamer:
                        streamer.subscribed_channels.clear()
                self._update_web_socket_state_metrics_locked()
                return

            nicknames = list(bucket.streamer_nicknames)

        for nickname in nicknames:
            self._sync_streamer_subscription(nickname)

        with self._lock:
            self._update_web_socket_state_metrics_locked()

    def __on_web_socket_close(self, client: WebSocketClient, _code: int, _reason: str) -> None:
        bucket_id = self._get_bucket_id_by_client(client)
        if bucket_id is None:
            return

        with self._lock:
            bucket = self._buckets.get(bucket_id)
            if not bucket:
                return

            bucket.is_authenticated = False
            for streamer_nickname in bucket.streamer_nicknames:
                streamer = self._streamers.get(streamer_nickname)
                if streamer:
                    streamer.subscribed_channels.clear()
            self._update_web_socket_state_metrics_locked()

    def __on_web_socket_error(self, client: WebSocketClient, exception: Exception) -> None:
        if self._get_bucket_id_by_client(client) is None:
            return
        logger.warning(f"[{self.vk_api.user_id}] WebSocketManager: client error: {exception}")

    def __on_web_socket_message(self, client: WebSocketClient, message: dict | list) -> None:
        if self._get_bucket_id_by_client(client) is None:
            return

        self.vk_api.inc_metric("vkapp_wss_responses")

        if message == {}:
            self._resync_all_streamers_for_client(client)
            return

        if not isinstance(message, dict):
            return

        event_name, streamer_id, event_user_id = self._parse_message_event(message)
        if not event_name or streamer_id is None:
            return

        self.vk_api.inc_metric("vkapp_wss_message_type_response_total", message_name=event_name.value)
        event_class = WebSocketEventClass.get(event_name)
        if event_class:
            self.vk_api.callback.trigger(
                event_name,
                streamer_id=streamer_id,
                user_id=event_user_id,
                message=event_class(message),
            )

    # ---- Streaming sync ------------------------------------------------------

    def _sync_streamer_subscription(self, streamer_nickname: str) -> None:
        clear_nickname = Streamer.normalize_nickname(streamer_nickname)

        with self._lock:
            streamer = self._streamers.get(clear_nickname)
            if not streamer or not streamer.is_enabled:
                return

            if streamer.assigned_client_id is None:
                return

            bucket = self._buckets.get(streamer.assigned_client_id)
            if not bucket or not bucket.is_authenticated:
                return

            to_subscribe = streamer.web_socket_channels - streamer.subscribed_channels
            to_unsubscribe = streamer.subscribed_channels - streamer.web_socket_channels

            subscribe_messages = [
                {
                    "subscribe": {"channel": channel},
                    "id": self._client_request_id(bucket.client),
                }
                for channel in sorted(to_subscribe)
            ]
            unsubscribe_messages = [
                {
                    "unsubscribe": {"channel": channel},
                    "id": self._client_request_id(bucket.client),
                }
                for channel in sorted(to_unsubscribe)
            ]

        if unsubscribe_messages:
            status = bucket.client.send_list(unsubscribe_messages)
            logger.info(
                f"[{self.vk_api.user_id}] WebSocketManager: [{streamer_nickname}] отписался "
                f"от '{len(unsubscribe_messages)}' событий. Статус = {status}"
            )
            if status:
                self.vk_api.inc_metric("vkapp_wss_requests", amount=float(len(unsubscribe_messages)))
                with self._lock:
                    streamer = self._streamers.get(clear_nickname)
                    if streamer:
                        streamer.subscribed_channels -= set(to_unsubscribe)
                    self._update_web_socket_state_metrics_locked()

        if subscribe_messages:
            status = bucket.client.send_list(subscribe_messages)
            logger.info(
                f"[{self.vk_api.user_id}] WebSocketManager: [{streamer_nickname}] подписался "
                f"на '{len(subscribe_messages)}' событий. Статус = {status}"
            )
            if status:
                self.vk_api.inc_metric("vkapp_wss_requests", amount=float(len(subscribe_messages)))
                with self._lock:
                    streamer = self._streamers.get(clear_nickname)
                    if streamer:
                        streamer.subscribed_channels |= set(to_subscribe)
                    self._update_web_socket_state_metrics_locked()

    def _unsubscribe_streamer_channels(self, streamer_nickname: str) -> None:
        clear_nickname = Streamer.normalize_nickname(streamer_nickname)

        with self._lock:
            streamer = self._streamers.get(clear_nickname)
            if not streamer or streamer.assigned_client_id is None:
                return

            bucket = self._buckets.get(streamer.assigned_client_id)
            if not bucket or not bucket.is_authenticated:
                streamer.subscribed_channels.clear()
                return

            channels = set(streamer.subscribed_channels)
            messages = [
                {
                    "unsubscribe": {"channel": channel},
                    "id": self._client_request_id(bucket.client),
                }
                for channel in sorted(channels)
            ]

        if messages:
            status = bucket.client.send_list(messages)
            logger.info(
                f"[{self.vk_api.user_id}] WebSocketManager: [{streamer_nickname}] отписался "
                f"от '{len(messages)}' событий. Стату = {status}"
            )
            if status:
                self.vk_api.inc_metric("vkapp_wss_requests", amount=float(len(messages)))

        with self._lock:
            streamer = self._streamers.get(clear_nickname)
            if streamer:
                streamer.subscribed_channels.clear()
            self._update_web_socket_state_metrics_locked()

    def _resync_all_streamers_for_client(self, client: WebSocketClient) -> None:
        bucket_id = self._get_bucket_id_by_client(client)
        if bucket_id is None:
            return

        with self._lock:
            bucket = self._buckets.get(bucket_id)
            if not bucket or not bucket.is_authenticated:
                return
            nicknames = list(bucket.streamer_nicknames)

        for nickname in nicknames:
            self._sync_streamer_subscription(nickname)

    # ---- Bucket allocation ---------------------------------------------------

    def _get_or_create_streamer(self, streamer_nickname: str) -> Streamer:
        clear_nickname = Streamer.normalize_nickname(streamer_nickname)
        streamer = self._streamers.get(clear_nickname)
        if streamer:
            return streamer

        streamer = Streamer(streamer_nickname=clear_nickname)
        self._streamers[clear_nickname] = streamer
        return streamer

    def _ensure_bucket_for_streamer(self, streamer: Streamer) -> Optional[_ClientBucket]:
        if streamer.assigned_client_id is not None:
            existing_bucket = self._buckets.get(streamer.assigned_client_id)
            if existing_bucket:
                existing_bucket.streamer_nicknames.add(streamer.streamer_nickname)
                return existing_bucket

        candidate = self._pick_bucket_with_free_slots_locked()
        if not candidate:
            candidate = self._create_bucket_locked()
            if not candidate:
                return None

        candidate.streamer_nicknames.add(streamer.streamer_nickname)
        streamer.assigned_client_id = candidate.bucket_id
        return candidate

    def _pick_bucket_with_free_slots_locked(self) -> Optional[_ClientBucket]:
        candidates = [
            bucket
            for bucket in self._buckets.values()
            if len(bucket.streamer_nicknames) < self.max_streamers_per_client
        ]
        if not candidates:
            return None
        return min(candidates, key=lambda item: len(item.streamer_nicknames))

    def _create_bucket_locked(self) -> Optional[_ClientBucket]:
        client = WebSocketClient(self.vk_api)
        bucket_id = self._next_bucket_id
        self._next_bucket_id += 1

        bucket = _ClientBucket(bucket_id=bucket_id, client=client)
        self._buckets[bucket_id] = bucket
        logger.info(f"[{self.vk_api.user_id}] WebSocketManager: created ws client bucket_id={bucket_id}")
        self._update_web_socket_state_metrics_locked()
        return bucket

    def _remove_empty_buckets_locked(self) -> None:
        empty_bucket_ids = [bucket_id for bucket_id, bucket in self._buckets.items() if not bucket.streamer_nicknames]
        for bucket_id in empty_bucket_ids:
            bucket = self._buckets.pop(bucket_id)
            bucket.client.stop()
            logger.info(f"[{self.vk_api.user_id}] WebSocketManager: removed empty ws client bucket_id={bucket_id}")
        self._update_web_socket_state_metrics_locked()

    # ---- Utility -------------------------------------------------------------

    def _start_all_clients(self) -> None:
        with self._lock:
            buckets = list(self._buckets.values())

        for bucket in buckets:
            bucket.client.run()

    def _streamers_with_assignment_locked(self) -> bool:
        return any(
            streamer.assigned_client_id is not None for streamer in self._streamers.values() if streamer.is_enabled)

    @staticmethod
    def _client_request_id(client: WebSocketClient) -> int:
        return int(client.get_request_id())

    def _get_bucket_id_by_client(self, client: WebSocketClient) -> Optional[int]:
        with self._lock:
            for bucket_id, bucket in self._buckets.items():
                if bucket.client is client:
                    return bucket_id
        return None

    @staticmethod
    def _parse_message_event(message: dict) -> tuple[Optional[WebSocketEventName], Optional[int], Optional[int]]:
        try:
            message_type = message["push"]["pub"]["data"]["type"]
            channel = message["push"]["channel"]
        except (KeyError, TypeError):
            return None, None, None

        if not channel or not message_type:
            return None, None, None

        match = re.search(WSS_TYPE_MESSAGE_RE, channel)
        if not match:
            return None, None, None

        channel_type = match.group(1)
        streamer_id_raw = match.group(2)
        user_id_raw = match.group(3)

        streamer_id = int(streamer_id_raw) if streamer_id_raw and streamer_id_raw.isdigit() else None
        user_id = int(user_id_raw) if user_id_raw and user_id_raw.isdigit() else None

        normalized = re.sub(r"[^a-zA-Z]+", "_", f"{message_type}_{channel_type}")
        event_name_value = re.sub(r"_+", "_", normalized).strip("_").lower()

        try:
            event_name = WebSocketEventName(event_name_value)
        except ValueError:
            return None, None, None

        return event_name, streamer_id, user_id

    def _active_subscribed_streamers_count(self) -> int:
        with self._lock:
            return sum(1 for streamer in self._streamers.values() if streamer.subscribed_channels)

    def _update_web_socket_state_metrics_locked(self) -> None:
        clients_active = len(self._buckets)
        has_authenticated_client = any(bucket.is_authenticated for bucket in self._buckets.values())
        streamers_all = sum(
            1
            for streamer in self._streamers.values()
            if streamer.is_enabled and streamer.assigned_client_id is not None
        )
        streamers_active = sum(1 for streamer in self._streamers.values() if streamer.subscribed_channels)

        self.vk_api.set_gauge("vkapp_wss_clients_active", float(clients_active))
        self.vk_api.set_gauge("vkapp_wss_active", 1.0 if has_authenticated_client else 0.0)
        self.vk_api.set_gauge("vkapp_wss_streamers_all", float(streamers_all))
        self.vk_api.set_gauge("vkapp_wss_streamers_active", float(streamers_active))
