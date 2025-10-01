import flet as ft

def main(page: ft.Page):
    page.title = "Icon Test"
    page.icon = "icon.png"   # must be PNG inside assets/
    page.add(ft.Text("Does the icon show?"))

ft.app(target=main, assets_dir="assets")
