import flet as ft

class TextEditor(ft.Container):
    def __init__(self, state, on_text_change=None):
        super().__init__(expand=True)
        self.state = state
        self.on_text_change = on_text_change

        self.text_area = ft.TextField(
            multiline=True,
            expand=True,
            autofocus=True,
            hint_text="Start typing...",
            border=ft.InputBorder.NONE,
            on_change=self._on_change
        )

        self.content = ft.Column(
            controls=[self.text_area],
            expand=True
        )

    def _on_change(self, e: ft.ControlEvent):
        """Triggered whenever the text changes."""
        self.state.modified = True
        if self.on_text_change:
            self.on_text_change()

    # Helper methods
    def get_text(self):
        return self.text_area.value

    def set_text(self, content: str):
        self.text_area.value = content
        self.text_area.update()

    def clear_text(self):
        self.text_area.value = ""
        self.text_area.update()
