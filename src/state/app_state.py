from pathlib import Path
from dataclasses import dataclass, field

@dataclass
class AppState:
    current_file: Path | None = None
    text: str = ""
    is_dirty: bool = False

    @property
    def filename(self):
        return self.current_file.name if self.current_file else "Untitled"

    @filename.setter
    def filename(self, value):
        self._filename = value

    def set_dirty(self, dirty=True):
        self.is_dirty = dirty