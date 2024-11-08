from tkinter import ttk

from fractions_app.constants import PROGRAM_TITLE, VERSION, AUTHOR
from fractions_app.windows.topic_window import TopicWindow


class MainWindow(ttk.Frame):
    def __init__(self, master) -> None:
        super().__init__(master)

        self.topic_window = TopicWindow(self)
        ttk.Label(self, text=PROGRAM_TITLE, style="Title.TLabel", justify="center").grid(
            row=0, column=1, sticky="nwse"
        )
        ttk.Button(self, text="Розпочати", command=self.show_topic_window).grid(
            row=1, column=1, sticky="nwse"
        )

        ttk.Label(self, text=f"Версія: {VERSION}\n\n©{AUTHOR}").grid(
            row=2, column=1, sticky="nwse"
        )

    def show_topic_window(self):
        self.grid_forget()
        self.topic_window.show()

    def show(self):
        self.grid(row=0, column=0, sticky="nwse")
        for i in range(3):
            self.rowconfigure(i, weight=1)
            self.columnconfigure(i, weight=1)
