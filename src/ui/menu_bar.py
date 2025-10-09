import flet as ft
from logic import file_ops

class MenuBar(ft.Row):
    def __init__(self, page: ft.Page, state, editor, update_title):
        super().__init__(spacing=10)
        self.page = page
        self.state = state
        self.editor = editor
        self.update_title = update_title

        self.controls = [
            ft.TextButton("New", on_click=self.new_file),
            ft.TextButton("Open", on_click=self.open_file),
            ft.TextButton("Save", on_click=self.save_file),
            ft.TextButton("Save As", on_click=self.save_as_file),
        ]

    # Event handlers
    def new_file(self, e):
        file_ops.new_file(self.state, self.editor.text_area, self.update_title)

    def open_file(self, e):
        file_ops.open_file(self.page, self.state, self.editor.text_area, self.update_title)

    def save_file(self, e):
        file_ops.save_file(self.page, self.state, self.editor.text_area, self.update_title)

    def save_as_file(self, e):
        file_ops.save_as_file(self.page, self.state, self.editor.text_area, self.update_title)
