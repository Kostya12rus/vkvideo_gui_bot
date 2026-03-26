from ._base import BaseApi
from .api_class import *
from ..config import *


class StreamerApi(BaseApi):
    @staticmethod
    def __get_streamer_referer(streamer_nickname: str) -> dict[str, str]:
        return {
            "origin": BASE_URL.rstrip("/"),
            "referer": BASE_URL + streamer_nickname,
        }


    def get_streamer_info(self, streamer_nickname: str) -> VkapiStreamerInfo:
        if not streamer_nickname:
            return VkapiStreamerInfo()
        req = self.request(
            STREAMER_INFO_URL.format(streamer_nickname),
            "GET",
            headers=self.__get_streamer_referer(streamer_nickname)
        )
        req_json = req.json()
        req_class = VkapiStreamerInfo(req_json)
        self.callback.trigger(
            VKAPIEventName.STREAMER_INFO, streamer_id=req_class.owner.id,
            user_id=self.user_id, message=req_class
        )
        return req_class

    def get_streamer_stream_info(self, streamer_nickname: str) -> VkapiStreamerStreamInfo:
        if not streamer_nickname:
            return VkapiStreamerStreamInfo()
        req = self.request(
            STREAMER_STREAM_INFO_URL.format(streamer_nickname),
            "GET",
            headers=self.__get_streamer_referer(streamer_nickname)
        )
        req_json = req.json()
        req_class = VkapiStreamerStreamInfo(req_json)
        self.callback.trigger(
            VKAPIEventName.STREAMER_STREAM_INFO, streamer_id=req_class.data.stream.user.id,
            user_id=self.user_id, message=req_class
        )
        return req_class


    def streamer_raid(self, streamer_nickname: str) -> dict:
        if not streamer_nickname:
            return {}
        req = self.request(
            STREAMER_RAID_URL.format(streamer_nickname),
            "GET",
            headers=self.__get_streamer_referer(streamer_nickname)
        )
        req_json = req.json()
        return req_json

    def streamer_raid_user_state(self, streamer_nickname: str) -> dict:
        if not streamer_nickname:
            return {}
        req = self.request(
            STREAMER_RAID_USER_STATE_URL.format(streamer_nickname),
            "GET",
            headers=self.__get_streamer_referer(streamer_nickname)
        )
        req_json = req.json()
        return req_json

    def streamer_raid_viewer(self, streamer_nickname: str, raid_to_streamer_nickname: str) -> dict:
        if not streamer_nickname or not raid_to_streamer_nickname:
            return {}
        headers = self.__get_streamer_referer(streamer_nickname)
        headers["Content-Type"] = "application/x-www-form-urlencoded"
        headers["referer"] = BASE_URL + f"{raid_to_streamer_nickname}?raid_from={streamer_nickname}"
        req = self.request(
            STREAMER_RAID_VIEWER_URL.format(streamer_nickname),
            "PUT",
            headers=headers
        )
        req_json = req.json()
        return req_json


    def streamer_follow(self, streamer_nickname: str) -> bool:
        if not streamer_nickname:
            return False
        req = self.request(
            STREAMER_FOLLOW_URL.format(streamer_nickname),
            "POST",
            headers=self.__get_streamer_referer(streamer_nickname)
        )
        req_json = req.json()
        return req_json["status"]

    def streamer_unfollow(self, streamer_nickname: str) -> bool:
        if not streamer_nickname:
            return False
        req = self.request(
            STREAMER_UNFOLLOW_URL.format(streamer_nickname),
            "POST",
            headers=self.__get_streamer_referer(streamer_nickname)
        )
        req_json = req.json()
        return req_json["status"]


    def streamer_set_like(self, streamer_nickname: str, stream_id: str) -> bool:
        if not streamer_nickname or not stream_id:
            return False
        send_json = {
            "contentId": f"{stream_id}",
            "contentType": "stream",
            "reactionType": "heart"
        }
        req = self.request(
            STREAMER_LIKE_URL,
            "POST",
            headers=self.__get_streamer_referer(streamer_nickname),
            json=send_json
        )
        return req.ok

    def streamer_del_like(self, streamer_nickname: str, stream_id: str) -> bool:
        if not streamer_nickname or not stream_id:
            return False
        send_json = {
            "contentId": f"{stream_id}",
            "contentType": "stream",
        }
        req = self.request(
            STREAMER_LIKE_URL,
            "DELETE",
            headers=self.__get_streamer_referer(streamer_nickname),
            json=send_json
        )
        return req.ok


    def get_streamer_pending_bonus(self, streamer_nickname: str) -> VkapiStreamerPendingBonus:
        if not streamer_nickname:
            return VkapiStreamerPendingBonus()
        req = self.request(
            STREAMER_PENDING_BONUS_URL.format(streamer_nickname),
            "GET",
            headers=self.__get_streamer_referer(streamer_nickname)
        )
        _streamer_nickname, _streamer_id = self.get_streamer_data(streamer_nickname=streamer_nickname)
        req_json = req.json()
        req_class = VkapiStreamerPendingBonus(req_json)
        self.callback.trigger(
            VKAPIEventName.STREAMER_PENDING_BONUS, streamer_id=_streamer_id,
            user_id=self.user_id, message=req_class
        )
        return req_class

    def streamer_pending_bonus_gather(self, streamer_nickname: str, bonus_id: str) -> bool:
        if not streamer_nickname or not bonus_id:
            return False
        headers = self.__get_streamer_referer(streamer_nickname)
        headers["content-type"] = "application/x-www-form-urlencoded"
        req = self.request(
            STREAMER_PENDING_BONUS_GATHER_URL.format(streamer_nickname, bonus_id),
            "PUT",
            headers=headers,
        )
        return req.ok

    def drop_campaign_products_request(self, streamer_nickname: str,  campaign_id: int | str) -> dict:
        if not streamer_nickname or not campaign_id:
            return {}
        headers = self.__get_streamer_referer(streamer_nickname)
        headers["content-type"] = "application/x-www-form-urlencoded"
        req = self.request(
            DROP_CAMPAING_PRODUCTS_REQUEST_URL.format(str(campaign_id)),
            "PUT",
            headers=headers,
        )
        req_json = req.json()
        return req_json


    def get_streamer_subscription_level(self, streamer_nickname: str) -> VkapiStreamerSubscriptionLevel:
        if not streamer_nickname:
            return VkapiStreamerSubscriptionLevel()
        req = self.request(
            STREAMER_GET_SUBSCRIPTION_LEVEL_URL.format(streamer_nickname),
            "GET",
            headers=self.__get_streamer_referer(streamer_nickname)
        )
        _streamer_nickname, _streamer_id = self.get_streamer_data(streamer_nickname=streamer_nickname)
        req_json = req.json()
        req_class = VkapiStreamerSubscriptionLevel(req_json)
        self.callback.trigger(
            VKAPIEventName.STREAMER_SUBSCRIPTION_LEVEL, streamer_id=_streamer_id,
            user_id=self.user_id, message=req_class
        )
        return req_class


    def get_streamer_chat(self, streamer_nickname: str, limit: int | str = 50) -> dict:
        """ Получает последние сообщения в чате стримера в количестве limit """
        if not streamer_nickname or not limit:
            return {}
        req = self.request(
            STREAMER_CHAT_URL.format(streamer_nickname, limit),
            "GET",
            headers=self.__get_streamer_referer(streamer_nickname)
        )
        req_json = req.json()
        return req_json
