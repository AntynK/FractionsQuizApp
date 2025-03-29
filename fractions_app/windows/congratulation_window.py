from io import BytesIO
from base64 import decodebytes
from PIL import Image, ImageTk
from tkinter import ttk, Toplevel, Canvas

from fractions_app.constants import CONGRATULATION_IMAGE_BASE64, CONGRATULATION_TITLE


class CongratulationWindow(Toplevel):
    def __init__(self, master: ttk.Frame) -> None:
        super().__init__(master)

        self.title(CONGRATULATION_TITLE)
        self.resizable(False, False)

        self.image = Image.open(BytesIO(decodebytes(CONGRATULATION_IMAGE_BASE64)))
        width = round(master.winfo_width() * 0.4)

        x, y = (
            master.master.winfo_x() + round(master.winfo_width() * 0.25),
            master.master.winfo_y() + round(master.winfo_height() * 0.15),
        )

        self.geometry(f"{width}x{width}+{x}+{y}")
        self.canvas = Canvas(self, width=width, height=width)
        self.canvas.pack(fill="both", expand=True)
        self.bind("<Configure>", self.on_resize)

    def on_resize(self, *unused) -> None:
        width = self.winfo_width()

        img = self.image.resize((width, width), Image.Resampling.LANCZOS)
        self.photo_image = ImageTk.PhotoImage(img)

        self.canvas.create_image(width // 2, width // 2, image=self.photo_image)
