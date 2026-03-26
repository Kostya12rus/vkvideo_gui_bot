# pylint: skip-file
import flet as ft

from .base import BasePage, Title


class ExamplePageContent(ft.Column):
    def __init__(self) -> None:
        super().__init__(expand=True)

        self.title = Title("EXAMPLE PAGE")

        self.controls = [ self.title ]


class ExamplePage(BasePage):
    load_position = 99

    name = "example"
    label = "Example"
    icon = ft.Icons.LIGHTBULB_OUTLINE
    selected_icon = ft.Icons.LIGHTBULB

    # разрешить пользователю нажимать на виджет
    disabled = False
    # не блокировать при входе/выходе
    not_disabled = True
    # не блокировать при входе
    disabled_is_login = False
    # не блокировать при выходе
    disabled_is_logout = False

    def __init__(self) -> None:
        super().__init__()
        self.page_content = ExamplePageContent()