from asyncio.windows_events import NULL
import flet as ft
import os
from components.box import Box
from components.menubar import MenuBar





def main(page: ft.Page):
    if os.path.exists("assets/icon.ico"):
        print("icon found")
    else:
        print("icon missing")
    page.icon = "icon.png"
    print(page.icon)
    page.title = 'Pad'
    page.scroll = True
    page.add(MenuBar(),Box())

    page.update()

ft.app(target=main, assets_dir="assets")