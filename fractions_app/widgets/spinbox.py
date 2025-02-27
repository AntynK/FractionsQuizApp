import tkinter as tk
from tkinter.font import Font


class Spinbox(tk.Spinbox):
    def __init__(
        self, master, width: int = 3, from_: int = 0
    ) -> None:
        super().__init__(
            master,
            validate="all",
            justify="center",
            width=width,
            to=200,
            from_=from_,
            increment=1,
        )
        self.bind("<FocusIn>", self._spinbox_focus_in)
        self.bind("<FocusOut>", self._spinbox_check_value)

        self.bind("<Return>", self._spinbox_return_pressed)
        self.validate_entered_text = (self.register(self._validate_spinbox_text), "%P")
        self.configure(validatecommand=self.validate_entered_text)
        self.min_value = from_

    def _spinbox_focus_in(self, *unused) -> None:
        self.selection_clear()

    def _spinbox_check_value(self, *unused) -> None:
        if not self.get():
            self.insert(0, "1")

        spinbox_text = self.get()
        if int(spinbox_text) < self.min_value:
            spinbox_text = str(self.min_value)
        self.set(spinbox_text)

        self._spinbox_return_pressed()

    def set(self, value: str) -> None:
        self.delete(0, tk.END)
        self.insert(0, value)

    def _spinbox_return_pressed(self, *unused) -> None:
        self.selection_clear()
        if self.master.master:
            self.master.master.focus()

    def _validate_spinbox_text(self, text: str) -> bool:
        if not text.isdigit() and text:
            self.bell()
            return False
        return True

    def update_background(self, color: str) -> None:
        self.configure(background=color)

    def update_font_size(self, font_size: int) -> None:
        self.configure(
            font=Font(family="Times New Roman", size=font_size, weight="bold")
        )
