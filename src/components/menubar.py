import flet as ft

class MenuBar(ft.MenuBar):
    def __init__(self):
        super().__init__(controls=[
            ft.SubmenuButton(
                content=ft.Text("File")
            ),
            ft.SubmenuButton(
                content=ft.Text("Edit")
            ),
            ft.SubmenuButton(
                content=ft.Text("View")
            )
        ])
        self.expand = True
        

