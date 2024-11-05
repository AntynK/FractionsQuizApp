import tkinter as tk
from tkinter.ttk import Style

from fractions_app.constants import VERSION, ICON_BASE64, PROGRAM_TITLE, BASE_WIDTH, BASE_HEIGHT
from fractions_app.windows.main_window import MainWindow


class Application(tk.Tk):
    """Main application class."""

    def __init__(self) -> None:
        super().__init__()

        self.style = Style()

        self.main_window = MainWindow(self)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.bind("<Configure>", self.resize_event)

        self.main_window.show()

    def resize_event(self, event=None):
        """This method change font size according to window size."""

        k = self.winfo_width() // 100 + self.winfo_height() // 100

        self.style.configure(
            "TButton",
            font=("Times New Roman", round(k * 1.3), "bold"),
        )

        self.style.configure("TLabel", font=("Times New Roman", round(k * 1.5), "bold"))

        self.style.configure("Title.TLabel", font=("Times New Roman", k * 2, "bold"))
        self.style.configure(
            "Expression.TLabel", font=("Times New Roman", round(k * 2.5))
        )

    def start(self) -> None:
        """Initialize window and start mainloop."""

        self.title(f"{PROGRAM_TITLE} - {VERSION}")
        self.geometry(f"{BASE_WIDTH}x{BASE_HEIGHT}")
        self.iconphoto(
            False,
            tk.PhotoImage(data=ICON_BASE64),
        )
        self.mainloop()
