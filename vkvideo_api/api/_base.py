import json
import random
import threading
from io import BytesIO
from typing import Any, Unpack, Optional, Union, TypedDict
from urllib.parse import urlparse
from loguru import logger

import curl_cffi
from curl_cffi.requests.session import HttpMethod

from utils import CallbackManager
from ..config import *


class RequestParams(TypedDict, total=False):
    params: Optional[Union[dict, list, tuple]]
    headers: Optional[dict]
    cookies: Optional[dict]
    json: Optional[dict | list]
    data: Optional[Union[dict[str, str], list[tuple], str, BytesIO, bytes]]
    files: Optional[dict]
    allow_redirects: Optional[bool]
    max_redirects: Optional[int]
    proxies: Optional[dict[str, str]]
    proxy: Optional[str]
    verify: Optional[bool]
    referer: Optional[str]
    stream: Optional[bool]


class BaseApi:
    callback = CallbackManager()

    def __init__(self, account_id: int, cookies: list[dict[str, Any]]):
        self.account_id = account_id
        self._cookies_list = cookies.copy()
        self.session = self._create_session()
        self.__request_semaphore = threading.Semaphore(MAX_REQUEST_IN_TIME)

    @property
    def cookies(self) -> list[dict[str, Any]]:
        return self._cookies_list

    @cookies.setter
    def cookies(self, cookies: list[dict[str, Any]]) -> None:
        self._cookies_list = cookies.copy()
        self.session = self._create_session()

    def _create_session(self) -> curl_cffi.Session:
        session = curl_cffi.Session()
        session.default_headers = True
        session.impersonate = random.choice([imp.value for imp in curl_cffi.BrowserType])

        for cookie in self.cookies:
            session.cookies.set(
                cookie['name'], cookie['value'],
                domain=cookie['domain'], path=cookie['path'], secure=cookie["secure"]
            )

        access_token = next(
            (json.loads(cookie['value'])["accessToken"] for cookie in self.cookies if "auth" == cookie['name']),
            None
        )
        session.headers.update({'Authorization': f'Bearer {access_token}'})

        return session

    def request(self, url_path: str, method: HttpMethod, **kwargs: Unpack[RequestParams]) -> curl_cffi.Response:
        if not self.session:
            self.session = self._create_session()

        default_kwargs = {
            "default_headers": True,
            "impersonate": self.session.impersonate,
            "cookies": self.session.cookies,
            "headers": self.session.headers,
        }
        if "headers" in kwargs:
            default_kwargs["headers"].update(kwargs["headers"])

        if "origin" not in default_kwargs["headers"]:
            default_kwargs["headers"]["origin"] = BASE_URL.rstrip("/")
        if "referer" not in default_kwargs["headers"]:
            default_kwargs["headers"]["referer"] = BASE_URL

        full_url = url_path
        if not urlparse(url_path).hostname:
            full_url = API_URL + url_path

        with self.__request_semaphore:
            with curl_cffi.Session(**default_kwargs) as session:
                req = session.request(method=method, url=full_url, timeout=MAX_TIMEOUT_IN_SECONDS, **kwargs)
                if not req.ok:
                    logger.error(f"{method}, {req.status_code}, {req.elapsed}, {full_url}")
                # else:
                #     logger.debug(f"{method}, {req.status_code}, {req.elapsed}, {full_url}")
                return req
