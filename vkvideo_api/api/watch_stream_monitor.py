import threading
import time
from typing import TYPE_CHECKING, TypeVar, Optional

from loguru import logger

from .api_class import *
from ..config import UPDATE_SUBSCRIPTIONS_LIST_INTERVAL, UPDATE_DROPS_LIST_INTERVAL
from ..heartbeat import HeartbeatApi
from ..heartbeat.wss_class import *

if TYPE_CHECKING:
    from ..vkvideo_main import VKVideoApi  # noqa

TVKVideoApi = TypeVar("TVKVideoApi", bound="VKVideoApi")


class WatchStreamMonitor:
    def start_watch_streamer(self: TVKVideoApi, streamer_nickname: str, streamer_id: int | None = None) -> None:
        if not hasattr(self, "init_callback"):
            self._initialize_callback()
            self.init_callback = True
        if streamer_nickname in self.streamers:
            return
        self.wss_api.subscribe_streamer(streamer_nickname=streamer_nickname, streamer_id=streamer_id)
        self.streamers[streamer_nickname] = HeartbeatApi(self, streamer_nickname)
        self.streamers[streamer_nickname].is_run = True

    def stop_watch_streamer(self: TVKVideoApi, streamer_nickname: str, streamer_id: int | None = None) -> None:
        if streamer_nickname not in self.streamers:
            return
        self.wss_api.unsubscribe_streamer(streamer_nickname=streamer_nickname, streamer_id=streamer_id)
        self.streamers[streamer_nickname].is_run = False


    def start_watch_all_subscribers(self: TVKVideoApi) -> None:
        if self.is_watch_all_subscribers:
            return
        self.is_watch_all_subscribers = True
        threading.Thread(target=self.__loop_watch_all_subscribers, daemon=True).start()

    def __loop_watch_all_subscribers(self: TVKVideoApi):
        while self.is_watch_all_subscribers:
            try:
                streamers = self.get_subscription_streamers(load_all=True)
                now_list = set(self.sub_streamers.copy())
                new_list = {(s.blog.blog_url, s.blog.owner.id) for s in streamers.data if
                    str(s.blog.blog_url) != str(s.blog.owner.id)}
                add_list = set(new_list) - set(now_list)
                del_list = set(now_list) - set(new_list)
                for streamer_nickname, streamer_id in add_list:
                    logger.info(
                        f"{streamer_nickname}[{streamer_id}] добавляю нового стримера из подписок, подключаю...")
                    self.sub_streamers.append((streamer_nickname, streamer_id))
                    threading.Thread(target=self.start_watch_streamer, args=(streamer_nickname, streamer_id)).start()
                for streamer_nickname, streamer_id in del_list:
                    logger.info(f"{streamer_nickname}[{streamer_id}] больше не в подписках, отключаю...")
                    self.sub_streamers.remove((streamer_nickname, streamer_id))
                    threading.Thread(target=self.stop_watch_streamer, args=(streamer_nickname, streamer_id)).start()
            except Exception:  # noqa
                logger.exception("Watch all subscribers failed", exc_info=True)
            finally:
                time.sleep(UPDATE_SUBSCRIPTIONS_LIST_INTERVAL)


    def stop_watch_all_subscribers(self: TVKVideoApi) -> None:
        if not self.is_watch_all_subscribers:
            return
        self.is_watch_all_subscribers = False
        if not self.sub_streamers:
            return
        for streamer_nickname, streamer_id in self.sub_streamers:
            threading.Thread(target=self.stop_watch_streamer, args=(streamer_nickname, streamer_id)).start()
        self.sub_streamers = []

    def start_watch_drop_streamers(self: TVKVideoApi) -> None:
        if self.is_watch_drop_streamers:
            return
        self.is_watch_drop_streamers = True
        threading.Thread(target=self.__loop_watch_drop_streamers, daemon=True).start()

    def __loop_watch_drop_streamers(self: TVKVideoApi):
        while self.is_watch_drop_streamers:
            try:
                streamers = self.get_drop_streamers(load_all=True)
                now_list = set(self.drop_streamers.copy())
                new_list = {(s.blog.blog_url, s.blog.owner.id) for s in streamers.data.stream_blogs if
                    str(s.blog.blog_url) != str(s.blog.owner.id)}
                add_list = set(new_list) - set(now_list)
                del_list = set(now_list) - set(new_list)
                for streamer_nickname, streamer_id in add_list:
                    logger.info(f"{streamer_nickname}[{streamer_id}] добавляю нового стримера для дропа, подключаю...")
                    self.drop_streamers.append((streamer_nickname, streamer_id))
                    threading.Thread(target=self.start_watch_streamer, args=(streamer_nickname, streamer_id)).start()
                for streamer_nickname, streamer_id in del_list:
                    logger.info(f"{streamer_nickname}[{streamer_id}] больше не дропает, отключаю...")
                    self.drop_streamers.remove((streamer_nickname, streamer_id))
                    threading.Thread(target=self.stop_watch_streamer, args=(streamer_nickname, streamer_id)).start()
            except Exception:  # noqa
                logger.exception("Watch all drop failed", exc_info=True)
            finally:
                time.sleep(UPDATE_DROPS_LIST_INTERVAL)

    def stop_watch_drop_subscribers(self: TVKVideoApi) -> None:
        if not self.is_watch_drop_streamers:
            return
        self.is_watch_drop_streamers = False
        if not self.drop_streamers:
            return
        for streamer_nickname, streamer_id in self.drop_streamers:
            threading.Thread(target=self.stop_watch_streamer, args=(streamer_nickname, streamer_id)).start()
        self.drop_streamers = []


    def get_streamer_data(self, streamer_nickname: str = "", streamer_id: int = None) -> tuple[Optional[str], Optional[int]]:
        if not streamer_nickname and not streamer_id:
            return None, None

        all_streamers: dict[str, int] = self.wss_api.streamers.copy()

        if streamer_nickname and streamer_id:
            return streamer_nickname.lower(), streamer_id
        elif streamer_nickname:
            return streamer_nickname.lower(), all_streamers.get(streamer_nickname.lower(), None)
        elif streamer_id:
            _streamer_nickname = next(
                (
                    _n
                    for _n, _i in all_streamers.items()
                    if str(_i) == str(streamer_id)
                )
            )
            return _streamer_nickname, streamer_id
        return None, None


    def _initialize_callback(self: TVKVideoApi) -> None:
        self.callback.register(VKAPIEventName.STREAMER_INFO, self.__on_streamer_info)
        self.callback.register(VKAPIEventName.STREAMER_PENDING_BONUS, self.__on_streamer_pending_bonus)
        self.callback.register(VKAPIEventName.STREAMER_STREAM_INFO, self.__on_streamer_stream_info)

        self.callback.register(WSSEventName.DROP_CAMPAIGN_PROGRESS_CHANNEL_INFO, self.__on_drop_campaign_progress)
        self.callback.register(WSSEventName.CP_BONUS_PENDING_CHANNEL_INFO, self.__on_cp_bonus_pending)
        self.callback.register(WSSEventName.CP_BALANCE_CHANGE_CHANNEL_INFO, self.__on_cp_balance_change)
        self.callback.register(WSSEventName.RAID_STATUS_CHANNEL_INFO, self.__on_raid_status_channel_info)
        self.callback.register(WSSEventName.STREAM_SLOT_START_CHANNEL_INFO, self.__on_stream_slot_start_channel_info)
        self.callback.register(WSSEventName.STREAM_SLOT_END_CHANNEL_INFO, self.__on_stream_slot_end_channel_info)


    def __on_streamer_info(self: TVKVideoApi, streamer_id: int, user_id: int, message: VkapiStreamerInfo):
        if str(user_id) != str(self.account_id):
            return
        _streamer_nickname, _streamer_id = self.get_streamer_data(streamer_id=streamer_id)
        # logger.debug(f"__on_streamer_info: {_streamer_nickname}, {_streamer_id}, {message}")

    def __on_streamer_stream_info(self: TVKVideoApi, streamer_id: int, user_id: int, message: VkapiStreamerStreamInfo):
        if str(user_id) != str(self.account_id):
            return
        _streamer_nickname, _streamer_id = self.get_streamer_data(streamer_id=streamer_id)
        # logger.debug(f"__on_streamer_stream_info: {_streamer_nickname}, {_streamer_id}, {message}")

        self.get_streamer_pending_bonus(_streamer_nickname)
        if not message.data.stream.is_online:
            return

        if not message.data.stream.is_liked:
            self.streamer_set_like(_streamer_nickname, message.data.stream.id)

    def __on_streamer_pending_bonus(self: TVKVideoApi, streamer_id: int, user_id: int, message: VkapiStreamerPendingBonus):
        if str(user_id) != str(self.account_id):
            return
        _streamer_nickname, _streamer_id = self.get_streamer_data(streamer_id=streamer_id)

        bonuses = message.data.bonuses
        for bonus in bonuses:
            # name = bonus.name
            # description = bonus.description
            # channel_point_amount = bonus.channel_point_amount
            # logger.info(
            #     f"{user_id}: '{_streamer_nickname}'[{_streamer_id}] "
            #     f"Получаю {channel_point_amount} поинтов за '{name}'({description})"
            # )
            if bonus.id:
                self.streamer_pending_bonus_gather(_streamer_nickname, bonus.id)
        # logger.debug(f"__on_streamer_pending_bonus: {_streamer_nickname}, {_streamer_id}, {message}")


    # WSSEventClass, WSSEventName
    def __on_drop_campaign_progress(self: TVKVideoApi, streamer_id: int, user_id: int, message: WssDropCampaignProgressChannelInfo):
        if str(user_id) != str(self.account_id):
            return
        _streamer_nickname, _streamer_id = self.get_streamer_data(streamer_id=streamer_id)

        drops = message.push.pub.data.data.drop_progresses
        for drop in drops:
            current = drop.current_rule.progress.current
            goal = drop.current_rule.progress.goal
            if not isinstance(current, int) or not isinstance(goal, int):
                continue
            progress_percent = (current / goal) * 100

            drop_title = ",".join([p.title for p in drop.current_rule.products])
            category_title = drop.campaign.category.title
            logger.info(
                f"{user_id}: '{_streamer_nickname}'[{_streamer_id}] "
                f"Прогресс дропа '{drop_title}'[{category_title}] равен {progress_percent:.1f}%"
            )

            if current == goal:
                self.drop_campaign_products_request(_streamer_nickname, drop.campaign.id)

    def __on_cp_bonus_pending(self: TVKVideoApi, streamer_id: int, user_id: int, message: WssCpBonusPendingChannelInfo):
        if str(user_id) != str(self.account_id):
            return
        _streamer_nickname, _streamer_id = self.get_streamer_data(streamer_id=streamer_id)

        bonus = message.push.pub.data.data
        # name = bonus.name
        # description = bonus.description
        # channel_point_amount = bonus.channel_point_amount
        # logger.info(
        #     f"{user_id}: '{_streamer_nickname}'[{_streamer_id}] "
        #     f"Получаю {channel_point_amount} поинтов за '{name}'({description})"
        # )
        if bonus.id:
            self.streamer_pending_bonus_gather(_streamer_nickname, bonus.id)

    def __on_cp_balance_change(self: TVKVideoApi, streamer_id: int, user_id: int, message: WssCpBalanceChangeChannelInfo):
        if str(user_id) != str(self.account_id):
            return
        _streamer_nickname, _streamer_id = self.get_streamer_data(streamer_id=streamer_id)

        data = message.push.pub.data.data
        old_balance = data.balance - data.delta
        logger.info(
            f"{user_id}: '{_streamer_nickname}'[{_streamer_id}] "
            f"Изменение баланса {data.delta} ({old_balance} -> {data.balance}) "
            f"за {data.reason.bonus.name or data.reason.type}({data.reason.bonus.description})"
        )

    def __on_raid_status_channel_info(self: TVKVideoApi, streamer_id: int, user_id: int, message: WssRaidStatusChannelInfo):
        if str(user_id) != str(self.account_id):
            return
        _streamer_nickname, _streamer_id = self.get_streamer_data(streamer_id=streamer_id)

        data = message.push.pub.data.data
        logger.info(
            f"{user_id}: '{_streamer_nickname}'[{_streamer_id}] "
            f"Изменил рейд на {data.target.owner.display_name} (ID: {data.target.owner.id}) {data.status}"
        )
        if data.status in ['started', 'created']:
            self.streamer_raid_user_state(_streamer_nickname)

    def __on_stream_slot_start_channel_info(self: TVKVideoApi, streamer_id: int, user_id: int, message: WssStreamSlotStartChannelInfo):
        if str(user_id) != str(self.account_id):
            return
        _streamer_nickname, _streamer_id = self.get_streamer_data(streamer_id=streamer_id)

        data = message.push.pub.data.data
        is_hosting = data.stream.is_hosting
        logger.info(
            f"{user_id}: '{_streamer_nickname}'[{_streamer_id}] "
            f"Начал новую трансляцию ({is_hosting=})"
        )

    def __on_stream_slot_end_channel_info(self: TVKVideoApi, streamer_id: int, user_id: int, message: WssStreamSlotEndChannelInfo):
        if str(user_id) != str(self.account_id):
            return
        _streamer_nickname, _streamer_id = self.get_streamer_data(streamer_id=streamer_id)

        logger.info(
            f"{user_id}: '{_streamer_nickname}'[{_streamer_id}] "
            f"Завершил трансляцию"
        )