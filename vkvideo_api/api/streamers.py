from ._base import BaseApi
from .api_class import *
from ..config import *


class StreamersApi(BaseApi):
    def get_subscription_streamers(self, limit: int = 30, offset: int = 0, load_all: bool = False) -> VkapiSubscriptionStreamers:
        if not load_all:
            req = self.request(STREAMERS_SUBSCRIPTIONS_URL.format(limit, offset), "GET")
            req_json = req.json()
            req_class = VkapiSubscriptionStreamers(req_json)
            self.callback.trigger(VKAPIEventName.SUBSCRIPTION_STREAMERS, user_id=self.account_id, message=req_class)
            return req_class
        else:
            return_data = None
            limit = limit
            offset = 0
            while True:
                subscription_streamers = self.get_subscription_streamers(limit, offset)
                offset += len(subscription_streamers.data)
                if not return_data:
                    return_data = subscription_streamers
                else:
                    return_data.data.extend(subscription_streamers.data)

                if return_data.total <= offset:
                    break
            return return_data

    def get_drop_streamers(self, limit: int = 40, offset: int = 0, load_all: bool = False) -> VkapiDropStreamers:
        if not load_all:
            req = self.request(STREAMERS_DROP_URL.format(limit, offset), "GET")
            req_json = req.json()
            req_class = VkapiDropStreamers(req_json)
            self.callback.trigger(VKAPIEventName.DROP_STREAMERS, user_id=self.account_id, message=req_class)
            return req_class
        else:
            return_data = None
            limit = limit
            offset = 0
            while True:
                drop_streamers = self.get_drop_streamers(limit, offset)
                offset = drop_streamers.extra.offset
                if not return_data:
                    return_data = drop_streamers
                else:
                    return_data.data.stream_blogs.extend(drop_streamers.data.stream_blogs)

                if drop_streamers.extra.is_last:
                    break
            return return_data
