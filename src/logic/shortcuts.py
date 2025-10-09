import flet as ft
from logic.file_ops import open_file, save_file, new_file

def register_shortcuts(page, state, text_area, update_title):
    def handle_shortcut(e: ft.KeyboardEvent):
        # CTRL+N — New File
        if e.ctrl and e.key == "n":
            new_file(state, text_area)
            update_title()

        # CTRL+O — Open File
        elif e.ctrl and e.key == "o":
            open_file(state, text_area)
            update_title()

        # CTRL+S — Save File
        elif e.ctrl and e.key == "s":
            save_file(state, text_area)
            update_title()

    page.on_keyboard_event = handle_shortcut
