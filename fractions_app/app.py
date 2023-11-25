import time

import tkinter as tk
from tkinter.ttk import Style

from .constants import VERSION, ICON_BASE64, SPINBOX_LAYOUT
from .windows.main_window import MainWindow


class Application(tk.Tk):
    """Main application class."""

    def __init__(self) -> None:
        super().__init__()

        self.last_callback_time = time.time()

        self.style = Style()

        self.main_window = MainWindow(self)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.bind("<Configure>", self.resize_event)

        self.main_window.show()

    def start(self) -> None:
        """Initialize window and start mainloop."""

        self.title(f"Програма для покращення знань з дробів - {VERSION}")
        self.geometry("500x450")
        self.iconphoto(
            False,
            tk.PhotoImage(data=ICON_BASE64),
        )
        self.mainloop()

    def resize_event(self, event=None):
        """This method change font size according to window size."""

        cur_time = time.time()
        if (cur_time - self.last_callback_time) < 0.1:
            return
        self.last_callback_time = cur_time

        k = self.winfo_width() // 100 + self.winfo_height() // 100

        self.style.configure(
            "TButton",
            font=("Times New Roman", round(k * 1.3)),
        )

        self.style.configure("TLabel", font=("Times New Roman", round(k * 1.5)))

        self.style.configure("Title.TLabel", font=("Times New Roman", k * 2, "bold"))
        self.style.configure(
            "Expression.TLabel", font=("Times New Roman", round(k * 2.5))
        )

        for stylename in ("Intenger", "Numerator", "Denominator"):
            self.style.layout(f"{stylename}.TSpinbox", *SPINBOX_LAYOUT)
            self.style.configure(
                f"{stylename}.TSpinbox",
                fieldbackground="white",
            )
