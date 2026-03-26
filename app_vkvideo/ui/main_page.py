import flet as ft
from screeninfo import get_monitors

from app_vkvideo.models import Setting
from app_vkvideo.utils import CallbackManager, EventName
from .pages import BasePage, page_manager
from .widgets import ThemeToggleButton, ColorMenuButton

callback_manager = CallbackManager()


class MainPageContent(ft.Row):  # pylint: disable=too-many-instance-attributes
    def __init__(self):
        super().__init__()

        callback_manager.register(EventName.ON_SET_SNACK_BAR_TEST, self.set_snack_bar)

        self.expand = True
        self.spacing = 0

        self._pages = self.get_pages_list()
        self.navigation_widget = ft.Column(expand=True, scroll=ft.ScrollMode.AUTO)
        self.navigation_widget.spacing = 0
        self.navigation_widget.alignment = ft.MainAxisAlignment.CENTER
        self.navigation_widget.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.navigation_widget.controls = self._pages

        self.design_editor = ft.Row(spacing=0)
        self.design_editor.alignment = ft.MainAxisAlignment.CENTER
        self.design_editor.vertical_alignment = ft.CrossAxisAlignment.CENTER
        self.design_editor.controls = [
            ThemeToggleButton(),
            ColorMenuButton()
        ]

        self.navigation_column = ft.Column(spacing=0)
        self.navigation_column.alignment = ft.MainAxisAlignment.CENTER
        self.navigation_column.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.navigation_column.controls = [
            self.navigation_widget,
            self.design_editor
        ]

        self.content_page = ft.Column(controls=[], expand=True, spacing=1)

        self.controls = [
            self.navigation_column,
            ft.VerticalDivider(),
            self.content_page
        ]

    def get_pages_list(self) -> list[BasePage]:
        pages = page_manager.get_pages()
        for page in pages:
            page.on_click = self.on_rail_change
        return pages

    def set_snack_bar(self, text: str):
        if self.page and text:
            self.page.show_dialog(
                ft.SnackBar(
                    ft.Text(
                        str(text),
                        expand=True,
                        text_align=ft.TextAlign.CENTER
                    ),
                    show_close_icon=True
                )
            )

    def set_page(self, page: BasePage):
        for p in self._pages:
            p.set_select_page(p == page)

        select_page = next((p for p in self._pages if p == page), None)
        if select_page:
            if select_page.page_content in self.content_page.controls:
                return
            select_page.set_select_page(True)
            self.content_page.controls = [select_page.page_content]
            if self.page:
                self.content_page.update()

    def on_rail_change(self, event: ft.ControlEvent = None, set_page: BasePage = None):
        if event is None and set_page is None:
            if self._pages:
                self.set_page(self._pages[0])
        elif event and event.control:
            self.set_page(event.control)
        elif set_page:
            self.set_page(set_page)

    def window_event(self, event: ft.WindowEvent):
        if not event:
            return

        if event.type == ft.WindowEventType.MOVED:
            left = event.page.window.left
            top = event.page.window.top
            if self.is_window_visible_on_any_screen(left, top):
                Setting.set_value("window_x_position", str(left))
                Setting.set_value("window_y_position", str(top))

        elif event.type == ft.WindowEventType.RESIZED:
            height = event.page.window.height
            width = event.page.window.width
            if event.page.window.min_width <= width and event.page.window.min_height <= height:
                Setting.set_value("window_width", str(width))
                Setting.set_value("window_height", str(height))

    def set_position_window(self, page: ft.Page = None):
        window_width = Setting.get_or_create_setting("window_width")
        window_height = Setting.get_or_create_setting("window_height")
        window_x_position = Setting.get_or_create_setting("window_x_position")
        window_y_position = Setting.get_or_create_setting("window_y_position")
        if window_width.value and window_height.value:
            window_width_value = float(window_width.value)
            window_height_value = float(window_height.value)
            if page.window.min_width <= window_width_value:
                page.window.width = window_width_value
            if page.window.min_height <= window_height_value:
                page.window.height = window_height_value

        if window_x_position.value and window_y_position.value:
            window_x_position_value = float(window_x_position.value)
            window_y_position_value = float(window_y_position.value)
            if self.is_window_visible_on_any_screen(window_x_position_value, window_y_position_value):
                page.window.left = window_x_position_value
                page.window.top = window_y_position_value

    @staticmethod
    def is_window_visible_on_any_screen(x: float | int, y: float | int) -> bool:
        """Проверяет, что окно хотя бы частично находится в пределах одного из экранов."""
        for monitor in get_monitors():
            mx, my = monitor.x, monitor.y
            mw, mh = monitor.width, monitor.height

            if mx <= x < mx + mw and my <= y < my + mh:
                return True
        return False


class MainPage:  # pylint: disable=too-few-public-methods
    def __init__(self, title: str = None):
        self.title = title or "NoName Project"
        self.page = None
        self.page_content = MainPageContent()

    def build(self, page: ft.Page):
        self.page = page
        self.page.window.min_width = 1130
        self.page.window.min_height = 600
        self.page.padding = 2
        self.page.title = self.title
        self.page.spacing = 1
        self.page.controls = [self.page_content]

        self.page_content.set_position_window(self.page)

        self.page.window.on_event = self.page_content.window_event

        self.page.update()
        self.page_content.on_rail_change()
