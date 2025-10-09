import flet as ft
import os


# ---- NEW FILE ----
def new_file(page, state, editor, update_title):
    editor.value = ""
    state.filename = None
    state.modified = False
    update_title()
    page.update()


# ---- OPEN FILE ----
def open_file(page, state, editor, update_title):
    file_picker = ft.FilePicker()

    def on_result(e: ft.FilePickerResultEvent):
        if not e.files:
            return
        file = e.files[0]
        try:
            with open(file.path, "r", encoding="utf-8") as f:
                editor.value = f.read()
            state.filename = file.path
            state.modified = False
            update_title()
            page.update()
        except Exception as err:
            print("Error opening file:", err)

    file_picker.on_result = on_result

    # Add picker to overlay FIRST
    page.overlay.append(file_picker)
    page.update()

    # Only THEN trigger the dialog
    file_picker.pick_files(allow_multiple=False)


# ---- SAVE FILE ----
def save_file(page, state, editor, update_title):
    if state.filename:
        try:
            with open(state.filename, "w", encoding="utf-8") as f:
                f.write(editor.value)
            state.modified = False
            update_title()
        except Exception as err:
            print("Error saving file:", err)
    else:
        save_as_file(page, state, editor, update_title)


# ---- SAVE AS FILE ----
def save_as_file(page, state, editor, update_title):
    file_picker = ft.FilePicker()

    def on_result(e: ft.FilePickerResultEvent):
        if not e.path:
            return
        try:
            with open(e.path, "w", encoding="utf-8") as f:
                f.write(editor.value)
            state.filename = e.path
            state.modified = False
            update_title()
            page.update()
        except Exception as err:
            print("Error saving file:", err)

    file_picker.on_result = on_result

    page.overlay.append(file_picker)
    page.update()

    file_picker.save_file()
