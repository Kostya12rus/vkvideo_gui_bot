import flet as ft


class Title(ft.Row):
    def __init__(
            self,
            title_text: str,
            size: int = 20,
            color: ft.Colors = ft.Colors.BLUE,
            text_align: ft.TextAlign = ft.TextAlign.CENTER
    ) -> None:
        super().__init__(
            spacing=0,
            run_spacing=0,
            alignment=ft.MainAxisAlignment.CENTER
        )

        self.text_widget = ft.Text(
            size=size,
            color=color,
            value=title_text,
            text_align=text_align,
            weight=ft.FontWeight.BOLD
        )

        self.container = ft.Container(
            padding=0,
            expand=True,
            content=self.text_widget
        )

        self.controls = [self.container]


class BasePage(ft.Container):  # pylint: disable=too-many-instance-attributes
    load_position: int = 99

    name: str | None = None
    label: str | None = None
    icon = ft.Icons.HOURGLASS_EMPTY
    selected_icon = ft.Icons.HOURGLASS_EMPTY_ROUNDED

    disabled = False

    def __init__(self) -> None:
        super().__init__()

        self.page_content: ft.Control | None = None
        self._text_widget: ft.Text | None = None
        self._button_widget: ft.Icon | None = None

    def build(self) -> "BasePage":
        self._text_widget = ft.Text(
            size=14,
            max_lines=2,
            value=f"{self.label}",
            text_align=ft.TextAlign.CENTER,
        )

        self._button_widget = ft.Icon(
            self.icon,
            color=ft.Colors.GREY if self.disabled else ft.Colors.BLUE
        )

        column_widget = ft.Column(
            spacing=0,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self._text_widget,
                self._button_widget
            ]
        )

        self.content = ft.Container(
            width=110,
            padding=0,
            border=ft.border.all(1),
            border_radius=ft.border_radius.all(5),
            alignment=ft.Alignment.CENTER,
            content=column_widget
        )

        self.ink = True
        return self

    def set_select_page(self, is_select: bool) -> None:
        self._text_widget.weight = (
            ft.FontWeight.BOLD if is_select else ft.FontWeight.NORMAL
        )

        self._button_widget.color = (
            ft.Colors.GREEN if is_select
            else ft.Colors.GREY if self.disabled
            else ft.Colors.BLUE
        )

        self._button_widget.name = (
            self.selected_icon if is_select else self.icon
        )

        if self.page:
            self.update()

    def will_unmount(self) -> None:
        ...

    def did_mount(self) -> None:
        ...

    def before_update(self) -> None:
        ...

    def is_isolated(self) -> bool:
        return True
