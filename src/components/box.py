import flet as ft

class Box(ft.TextField):
    def __init__(self):
        super().__init__()
        self.multiline = True
        self.autofocus = True
        self.border = ft.InputBorder.NONE
        self.min_lines = 40
        self.content_padding = 30
        self.cursor_color = 'purple'
        self.on_change=self.save_text

    def save_text(self, e: ft.ControlEvent):
        with open('save.txt', 'w') as f:
            f.write(self.value)

    def read_text(self):
        try:
            with open('save.txt', 'r') as f:
                return f.read()
        except FileNotFoundError:
            self.hint_text = 'Welcome to Pad!'

    def build(self):
        self.value = self.read_text()