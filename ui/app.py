import flet as ft
from src.models import init_database
from src.utils.logger import logger

class VKVideoBotApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.setup_page()
        self.init_database()
        self.build_ui()
    
    def setup_page(self):
        self.page.title = "VK Video Bot"
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.padding = 20
        self.page.window_width = 1200
        self.page.window_height = 800
    
    def init_database(self):
        try:
            init_database()
            logger.info("Database initialized")
        except Exception as e:
            logger.error(f"Database initialization failed: {e}")
    
    def build_ui(self):
        self.tabs = ft.TabBar(
            tabs=[
                ft.Tabs(label="Аккаунты", icon=ft.Icons.PERSON),
                ft.Tab(label="Стримеры", icon=ft.Icons.VIDEO_LIBRARY),
                ft.Tab(label="Настройки", icon=ft.Icons.SETTINGS),
            ],
            expand=1,
        )
        
        self.page.add(
            ft.AppBar(
                title=ft.Text("VK Video Bot"),
                center_title=True,
                bgcolor=ft.Colors.SURFACE_BRIGHT,
            ),
            ft.Container(
                content=self.tabs,
                expand=True,
            ),
        )
    
    def run(self):
        self.page.update()

def main(page: ft.Page):
    app = VKVideoBotApp(page)

if __name__ == "__main__":
    ft.app(target=main)