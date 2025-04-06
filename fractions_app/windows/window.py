from tkinter import ttk, Misc
from typing import Optional

from fractions_app.widgets import make_grid


class Window(ttk.Frame):
    ROWS = 0
    COLUMNS = 0

    def __init__(
        self, previous_state: "Window", master: Optional["Window"] = None
    ) -> None:
        super().__init__(master)
        self.previous_state = previous_state
        self.bind("<Configure>", self.on_resize)

        self.init()

    def init(self) -> None: ...

    def on_resize(self, *unused) -> None: ...

    def show(self, *args, **kwargs) -> None:
        self.grid(row=0, column=0, sticky="nwse")
        make_grid(self, self.ROWS, self.COLUMNS)

    def show_previous_window(self) -> None:
        self.grid_forget()
        self.previous_state.show()
