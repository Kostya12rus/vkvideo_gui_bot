import json
import threading
from typing import Any

from seleniumbase import SB

from ..config import BASE_URL


class AuthModule:
    _lock_use_selenium = threading.Lock()
    __TIMEOUT = 160

    def auth_from_selenium(self) -> list[dict[str, Any]]:
        with AuthModule._lock_use_selenium:
            kwargs = self._get_default_selenium_kwargs()
            with SB(**kwargs) as sb:
                sb.open_url(BASE_URL)

                login_btn_selector = '//button[contains(text(), "Войти")]'
                sb.wait_for_element(login_btn_selector, timeout=self.__TIMEOUT)
                sb.click(login_btn_selector)
                return self._wait_final_access(sb)

    def refresh_from_selenium(self, cookies: list[dict[str, Any]]) -> list[dict[str, Any]]:
        with AuthModule._lock_use_selenium:
            kwargs = self._get_default_selenium_kwargs()
            kwargs["headless2"] = True
            with SB(**kwargs) as sb:
                sb.open_url(BASE_URL)
                sb.add_cookies(cookies)
                sb.refresh()
                return self._wait_final_access(sb)

    def get_web_socket_token_from_selenium(self, cookies: list[dict[str, Any]]) -> str:
        with AuthModule._lock_use_selenium:
            kwargs = self._get_default_selenium_kwargs()
            kwargs["headless2"] = True
            with SB(**kwargs) as sb:
                sb.open_url(BASE_URL)
                sb.add_cookies(cookies)
                sb.refresh()
                if not self._wait_final_access(sb):
                    return ""

                script_app_config_text = ""
                while not script_app_config_text:
                    script_app_config = sb.get_element(
                        'script[type="text/plain"][id="app-config"]', timeout=self.__TIMEOUT
                    )
                    script_app_config_text = script_app_config.get_attribute('innerHTML')
                    if not script_app_config_text:
                        sb.sleep(1)

                script_app_config_json = json.loads(script_app_config_text)
                return script_app_config_json["websocket"]["token"]

    def _get_default_selenium_kwargs(self) -> dict[str, Any]:
        return {
            "browser": "chrome",
            "incognito": True,
            "dark_mode": True,
            "undetectable": True,
            "time_limit": self.__TIMEOUT
        }

    def _wait_final_access(self, sb) -> list[dict[str, Any]]:
        sb.wait_for_element('span[class^="Icon_block_"][class*="ProfileMenu_arrow_"]', timeout=self.__TIMEOUT)
        return sb.get_cookies()
