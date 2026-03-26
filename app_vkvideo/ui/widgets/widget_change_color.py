import flet as ft

COLORS = [
    {"color": ft.Colors.INDIGO, "name": "Indigo"},
    {"color": ft.Colors.BLUE, "name": "Blue (default)"},
    {"color": ft.Colors.TEAL, "name": "Teal"},
    {"color": ft.Colors.GREEN, "name": "Green"},
    {"color": ft.Colors.YELLOW, "name": "Yellow"},
    {"color": ft.Colors.ORANGE, "name": "Orange"},
    {"color": ft.Colors.DEEP_ORANGE, "name": "Deep orange"},
    {"color": ft.Colors.PINK, "name": "Pink"},
    {"color": ft.Colors.RED, "name": "Red"},
    {"color": ft.Colors.PURPLE, "name": "Purple"},
    {"color": ft.Colors.DEEP_PURPLE, "name": "Deep Purple"},
    {"color": ft.Colors.CYAN, "name": "Cyan"},
    {"color": ft.Colors.LIGHT_GREEN, "name": "Light Green"},
    {"color": ft.Colors.LIME, "name": "Lime"},
    {"color": ft.Colors.BROWN, "name": "Brown"},
    {"color": ft.Colors.GREY, "name": "Grey"},
    {"color": ft.Colors.BLUE_GREY, "name": "Blue Grey"}
]


class ColorMenuItem(ft.PopupMenuItem):
    def __init__(self, color, name):
        super().__init__()

        self.icon_widget = ft.Icon(ft.Icons.COLOR_LENS_OUTLINED, color=color)
        self.text_widget = ft.Text(name)

        self.content = ft.Row()
        self.content.controls = [
            self.icon_widget,
            self.text_widget
        ]

        self.on_click = self.change_color
        self.data = color

    def change_color(self, *_, **__):
        self.page.theme = self.page.dark_theme = ft.Theme(color_scheme_seed=self.data)
        self.page.update()


class ColorMenuButton(ft.PopupMenuButton):
    def __init__(self):
        super().__init__()
        self.tooltip = "Change colors"
        self.icon = ft.Icons.COLOR_LENS_OUTLINED
        self.items = [
            ColorMenuItem(color=data['color'], name=data['name'])
            for data in COLORS
        ]
