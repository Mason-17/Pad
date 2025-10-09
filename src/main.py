import flet as ft
from ui.app_window import AppWindow

def main(page: ft.Page):
    page.window_width = 800
    page.window_height = 600
    #page.window.maximized = True
    page.title = "Pad"

    app = AppWindow(page)
    page.add(app)

ft.app(target=main)
