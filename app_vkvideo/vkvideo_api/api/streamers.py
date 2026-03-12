from ._base import BaseApi
from .api_class import *
from ..config import *


class StreamersApi(BaseApi):
    def get_subscription_streamers(self, limit: int = 30, offset: int = 0, load_all: bool = False) -> VkapiSubscriptionStreamers:
        if not load_all:
            req = self.request(STREAMERS_SUBSCRIPTIONS_URL.format(limit, offset), "GET")
            req_json = req.json()
            req_class = VkapiSubscriptionStreamers(req_json)
            self.callback.trigger(VKAPIEventName.SUBSCRIPTION_STREAMERS, user_id=self.user_id, message=req_class)
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

    def get_online_subscription_streamers(self, limit: int = 50, offset: int = 0, load_all: bool = False) -> VkapiOnlineSubscriptionStreamers:
        if not load_all:
            req = self.request(STREAMERS_ONLINE_SUBSCRIPTIONS_URL.format(limit, offset), "GET")
            req_json = req.json()
            req_class = VkapiOnlineSubscriptionStreamers(req_json)
            self.callback.trigger(VKAPIEventName.ONLINE_SUBSCRIPTION_STREAMERS, user_id=self.user_id, message=req_class)
            return req_class
        else:
            return_data = None
            limit = limit
            offset = 0
            while True:
                streamers = self.get_online_subscription_streamers(limit, offset)
                offset += len(streamers.data.stream_blogs)
                if not return_data:
                    return_data = streamers
                else:
                    return_data.data.stream_blogs.extend(streamers.data.stream_blogs)

                if streamers.extra.is_last:
                    break
            return return_data

    def get_drop_streamers(self, limit: int = 40, offset: int = 0, load_all: bool = False) -> VkapiDropStreamers:
        if not load_all:
            req = self.request(STREAMERS_DROP_URL.format(limit, offset), "GET")
            req_json = req.json()
            req_class = VkapiDropStreamers(req_json)
            self.callback.trigger(VKAPIEventName.DROP_STREAMERS, user_id=self.user_id, message=req_class)
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

    def get_catalog_streamers(self, catalog_id: str, limit: int = 20, offset: int = 0, load_all: bool = False) -> VkapiCatalogStreamers:
        if not load_all:
            req = self.request(STREAMERS_CATALOG_URL.format(catalog_id, limit, offset), "GET")
            req_json = req.json()
            req_class = VkapiCatalogStreamers(req_json)
            self.callback.trigger(VKAPIEventName.CATALOG_STREAMERS, user_id=self.user_id, message=req_class)
            return req_class
        else:
            return_data = None
            limit = limit
            offset = 0
            while True:
                catalog_streamers = self.get_catalog_streamers(catalog_id, limit, offset)
                offset = catalog_streamers.extra.offset
                if not return_data:
                    return_data = catalog_streamers
                else:
                    return_data.data.stream_blogs.extend(catalog_streamers.data.stream_blogs)

                if catalog_streamers.extra.is_last:
                    break
            return return_data
