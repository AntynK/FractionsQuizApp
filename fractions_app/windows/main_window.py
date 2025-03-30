from tkinter import ttk

from fractions_app.constants import PROGRAM_TITLE, VERSION, AUTHOR
from fractions_app.windows.topic_window import TopicWindow
from fractions_app.windows.window import Window


class MainWindow(Window):
    ROWS = 3
    COLUMNS = 3

    def init(self) -> None:
        self.topic_window = TopicWindow(self)
        ttk.Label(
            self, text=PROGRAM_TITLE, style="Title.TLabel", justify="center"
        ).grid(row=0, column=1, sticky="nwse")
        ttk.Button(self, text="Розпочати", command=self.show_topic_window).grid(
            row=1, column=1, sticky="nwse"
        )

        ttk.Label(self, text=f"Версія: {VERSION}\n\n©{AUTHOR}").grid(
            row=2, column=1, sticky="nwse"
        )

    def show_topic_window(self) -> None:
        self.grid_forget()
        self.topic_window.show()
