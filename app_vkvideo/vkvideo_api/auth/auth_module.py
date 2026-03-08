from typing import Any

from seleniumbase import SB
from ..config import BASE_URL


class AuthModule:
    __TIMEOUT = 160

    def auth_from_selenium(self) -> list[dict[str, Any]]:
        kwargs = self._get_default_selenium_kwargs()
        with SB(**kwargs) as sb:
            sb.open_url(BASE_URL)

            login_btn_selector = '//button[contains(text(), "Войти")]'
            sb.wait_for_element(login_btn_selector, timeout=self.__TIMEOUT)
            sb.click(login_btn_selector)
            return self._wait_final_access(sb)

    def refresh_from_selenium(self, cookies: list[dict[str, Any]]) -> list[dict[str, Any]]:
        kwargs = self._get_default_selenium_kwargs()
        kwargs["headless2"] = True
        with SB(**kwargs) as sb:
            sb.open_url(BASE_URL)
            sb.add_cookies(cookies)
            sb.refresh()
            return self._wait_final_access(sb)

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
