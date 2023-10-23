import tkinter as tk

from .windows.main_window import MainWindow


class Application(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        self.main_window = MainWindow(self)
        self.main_window.pack()

    def start(self):
        self.title("Програма для покращення знань з дробів")
        self.geometry("400x300")
        self.resizable(width=False, height=False)
        self.mainloop()
