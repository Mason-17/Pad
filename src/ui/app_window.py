import flet as ft
from ui.menu_bar import MenuBar
from ui.text_editor import TextEditor
from state.app_state import AppState
from logic.shortcuts import register_shortcuts

class AppWindow(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__(expand=True)
        self.page = page
        self.state = AppState()

        self.update_title = self._update_title

        self.editor = TextEditor(self.state, on_text_change=self.update_title)

        self.menu = MenuBar(self.page, self.state, self.editor, self.update_title)

        register_shortcuts(self.page, self.state, self.editor.text_area, self.update_title)

        # Layout
        self.controls = [
            self.menu,
            ft.Divider(),
            self.editor
        ]

        self.update_title()

    def _update_title(self, *args):
        """Updates window title to reflect current file name."""
        filename = self.state.filename or "Untitled"
        self.page.title = f"{filename} - Flet Notepad"
        self.page.update()
