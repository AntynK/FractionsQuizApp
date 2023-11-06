import tkinter as tk

from .windows.main_window import MainWindow


class Application(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        self.main_window = MainWindow(self)
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.main_window.show()

    def start(self) -> None:
        self.title("Програма для покращення знань з дробів")
        self.geometry("400x300")
        self.mainloop()
