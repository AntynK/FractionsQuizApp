from tkinter import ttk, Toplevel


class CongratulationWindow(Toplevel):
    def __init__(self, master: ttk.Frame):
        super().__init__(master=master)

        self.title("Молодець!")

        width, height = master.winfo_width() - 250, master.winfo_height() - 250
        x, y = master.winfo_x() + 150, master.winfo_y() + 150

        self.geometry(f"{width}x{height}+{x}+{y}")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        ttk.Label(
            self,
            text="Все правильно! Молодець!!!!!",
            font=("Times New Roman", 40),
            justify="center",
        ).grid(column=0, row=0, sticky="ns")
