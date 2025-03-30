from tkinter import ttk, Misc
from typing import Optional

from fractions_app.widgets import make_grid


class Window(ttk.Frame):
    ROWS = 0
    COLUMNS = 0

    def __init__(self, previous_state: "Window", master: Optional["Window"] = None) -> None:
        super().__init__(master)
        self.previous_state = previous_state

        self.init()

    def init(self) -> None: ...

    def show(self, *args, **kwargs) -> None:
        self.grid(row=0, column=0, sticky="nwse")
        make_grid(self, self.ROWS, self.COLUMNS)
