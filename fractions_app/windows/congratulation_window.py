from tkinter import ttk, Toplevel, PhotoImage, Canvas

from fractions_app.constants import CONGRATULATION_IMAGE_BASE64, CONGRATULATION_TITLE


class CongratulationWindow(Toplevel):
    def __init__(self, master: ttk.Frame):
        super().__init__(master=master)

        self.title(CONGRATULATION_TITLE)
        self.resizable(False, False)

        width, height = master.winfo_width() - 250, master.winfo_height() - 180
        x, y = master.winfo_x() + 150, master.winfo_y() + 100

        self.geometry(f"{width}x{height}+{x}+{y}")
        self.img = PhotoImage(data=CONGRATULATION_IMAGE_BASE64)
        self.canvas = Canvas(self, width=self.img.width(), height=self.img.height())
        self.canvas.create_image(
            self.img.width(),
            self.img.height() // 2 + 20,
            image=self.img,
        )
        self.canvas.pack(fill="both", expand=True)
