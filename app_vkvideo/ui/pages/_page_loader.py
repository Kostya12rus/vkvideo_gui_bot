import importlib
import os
import pathlib
import sys
from typing import Type, Optional

from app_vkvideo.utils import logger
from .base import BasePage


class PageManager:  # pylint: disable=too-few-public-methods
    def __init__(self) -> None:
        self.pages: list[Type[BasePage]] = []
        self.__parse_directories()

    def get_pages(self) -> list[BasePage]:
        if not self.pages:
            self.__load_pages()
        return [page() for page in self.pages]

    def __parse_directories(self) -> None:
        local_path = pathlib.Path()
        user_pages_path = local_path / "user_pages"
        user_pages_path.mkdir(parents=True, exist_ok=True)

        sys.path.append(local_path.absolute().as_posix())

        self.pages.extend(
            self.__load_pages(pathlib.Path(os.path.abspath(__file__)).parent)
        )

        imported_paths = []
        for sys_path in sys.path:
            if not sys_path:
                continue

            path_modules = pathlib.Path(sys_path) / "user_pages"
            if not path_modules.is_dir():
                continue
            if path_modules in imported_paths:
                continue

            imported_paths.append(path_modules)
            user_pages = self.__load_pages(path_modules)
            if user_pages:
                self.pages.extend(user_pages)

    @staticmethod
    def get_module_name_from_path(file_path: pathlib.Path, base_dir: pathlib.Path) -> str:
        relative = file_path.with_suffix("").relative_to(base_dir)
        return ".".join(relative.parts)

    def __load_pages(self, directory: Optional[pathlib.Path] = None) -> list[Type[BasePage]]:
        if not directory or not directory.is_dir():
            return []

        if directory not in sys.path:
            sys.path.append(directory.as_posix())

        pages: list[Type[BasePage]] = []

        for file in os.listdir(directory):
            if file.startswith("page_") and file.endswith(".py"):
                file_path = directory / file
                source_module_name = self.get_module_name_from_path(file_path, pathlib.Path().absolute())
                module_name = source_module_name.replace("src.", "")

                try:
                    module = importlib.import_module(module_name)
                    for attr in dir(module):
                        obj = getattr(module, attr)
                        if isinstance(obj, type) and issubclass(obj, BasePage) and obj is not BasePage:
                            pages.append(obj)
                except Exception:  # noqa: broad-except
                    logger.exception(f"Ошибка при импорте страницы {module_name}")

        pages.sort(key=lambda x: x.load_position)
        return pages


page_manager = PageManager()
