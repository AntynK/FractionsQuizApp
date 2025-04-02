import tkinter as tk
from tkinter.ttk import Style

from fractions_app.constants import (
    ICON_BASE64,
    PROGRAM_TITLE,
    BASE_WIDTH,
    BASE_HEIGHT,
)
from fractions_app.windows.main_window import MainWindow
from fractions_app.helper import get_font_scale


class Application(tk.Tk):
    """Main application class."""

    def __init__(self) -> None:
        super().__init__()

        self.style = Style()

        self.main_window = MainWindow(self, master=self)  # type: ignore
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.bind("<Configure>", self.resize_event)

        self.main_window.show()

    def resize_event(self, *unused) -> None:
        """This method change font size according to window size."""

        k = get_font_scale(self.winfo_width(), self.winfo_height())

        self.style.configure(
            "TButton",
            font=("Times New Roman", round(k * 1.3), "bold"),
        )

        self.style.configure("TLabel", font=("Times New Roman", round(k * 1.5), "bold"))
        self.style.configure("Title.TLabel", font=("Times New Roman", k * 2, "bold"))
        self.style.configure(
            "Expression.TLabel", font=("Times New Roman", round(k * 2.5))
        )

        self.style.configure(
            "TCheckbutton", font=("Times New Roman", round(k * 1.5), "bold")
        )

    def start(self) -> None:
        """Initialize window and start mainloop."""

        self.title(f"{PROGRAM_TITLE}")
        self.geometry(f"{BASE_WIDTH}x{BASE_HEIGHT}")
        self.iconphoto(
            True,
            tk.PhotoImage(data=ICON_BASE64),
        )
        self.mainloop()
