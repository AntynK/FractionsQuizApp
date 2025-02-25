from tkinter import ttk, Toplevel, PhotoImage, Canvas

from fractions_app.constants import CONGRATULATION_IMAGE_BASE64, CONGRATULATION_TITLE


class CongratulationWindow(Toplevel):
    def __init__(self, master: ttk.Frame) -> None:
        super().__init__(master)

        self.title(CONGRATULATION_TITLE)
        self.resizable(False, False)

        width, height = round(master.winfo_width() / 2), round(
            master.winfo_height() / 1.5
        )
        x, y = round(master.winfo_width() // 3.5), round(master.winfo_height() / 4)

        self.geometry(f"{width}x{height}+{x}+{y}")
        self.img = PhotoImage(data=CONGRATULATION_IMAGE_BASE64)

        self.canvas = Canvas(self, width=width, height=height)
        self.canvas.create_image(
            self.img.width() // 1.5,
            self.img.height() // 2,
            image=self.img,
        )
        self.canvas.pack(fill="both", expand=True)
