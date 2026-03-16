import json
import random
import threading
import time
from io import BytesIO
from typing import Any, Unpack, Optional, Union, TypedDict, TYPE_CHECKING, TypeVar
from urllib.parse import urlparse

from curl_cffi.requests.exceptions import Timeout
from loguru import logger

import curl_cffi
from curl_cffi.requests.session import HttpMethod

from app_vkvideo.utils import CallbackManager
from ..config import *

if TYPE_CHECKING:
    from ..vkvideo_main import VKVideoApi  # noqa

TVKVideoApi = TypeVar("TVKVideoApi", bound="VKVideoApi")


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

    def __init__(self: TVKVideoApi, user_id: int, cookies: list[dict[str, Any]]):
        self.user_id = user_id
        self._cookies_list = cookies.copy()
        self.session = self._create_session()
        self.__request_semaphore = threading.Semaphore(MAX_REQUEST_IN_TIME)

    @property
    def cookies(self: TVKVideoApi) -> list[dict[str, Any]]:
        return self._cookies_list

    @cookies.setter
    def cookies(self: TVKVideoApi, cookies: list[dict[str, Any]]) -> None:
        self._cookies_list = cookies.copy()
        self.session = self._create_session()

    def _create_session(self: TVKVideoApi) -> curl_cffi.Session:
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

    def request(self: TVKVideoApi, url_path: str, method: HttpMethod, **kwargs: Unpack[RequestParams]) -> curl_cffi.Response:
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
            req: Optional[curl_cffi.Response] = None
            with curl_cffi.Session(**default_kwargs) as session:
                for _ in range(MAX_RETRIES):
                    req = None
                    try:
                        time_min, time_max = min(HTTP_REQUESTS_TIME_SLEEP), max(HTTP_REQUESTS_TIME_SLEEP)
                        time.sleep(random.randint(int(time_min * 10000), int(time_max * 10000)) / 10000)

                        req = session.request(method=method, url=full_url, timeout=MAX_TIMEOUT_IN_SECONDS, **kwargs)
                        break
                    except Exception as e:
                        logger.error(f"[{e.__class__.__name__}] Источник не прислал ответ на запрос: {method}, {full_url}")
                        self.inc_metric("vkapp_requests_with_error", code=e.__class__.__name__.lower())
                        continue
                    finally:
                        self.inc_metric("vkapp_requests_all")
                        if req is not None:
                            if req.ok:
                                self.inc_metric("vkapp_requests_success")
                            else:
                                self.inc_metric("vkapp_requests_with_error", code=str(req.status_code))
                                logger.error(f"{method}, {req.status_code}, {req.elapsed}, {full_url}")
                        else:
                            logger.error(f"{method}, {full_url}")

                if req is None:
                    raise RuntimeError(f"Request failed after retries: {method} {full_url}")

                return req
