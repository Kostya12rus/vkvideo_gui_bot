from ._base import BaseApi
from ..config import *


class UserApi(BaseApi):
    def actor_info(self) -> dict:
        req = self.request(USER_INFO_URL, "GET")
        req_json = req.json()
        return req_json

    def current_user_info(self) -> dict:
        req = self.request(USER_CURRENT_URL, "GET")
        req_json = req.json()
        return req_json

    def user_stream_views_info(self, limit: int = 3) -> dict:
        req = self.request(USER_STREAM_VIEWS_URL.format(str(limit)), "GET")
        req_json = req.json()
        return req_json
