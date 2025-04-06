import tkinter as tk
from tkinter.font import Font

from fractions_app.helper import get_font_scale


class Spinbox(tk.Spinbox):
    def __init__(
        self,
        master,
        width: int = 3,
        to: int = 200,
        from_: int = 0,
        font_weight: float = 2,
    ) -> None:
        super().__init__(
            master,
            validate="all",
            justify="center",
            width=width,
            to=to,
            from_=from_,
            increment=1,
        )
        self.bind("<FocusIn>", self._spinbox_focus_in)
        self.bind("<FocusOut>", self._spinbox_check_value)

        self.bind("<Return>", self._spinbox_return_pressed)
        self.validate_entered_text = (self.register(self._validate_spinbox_text), "%P")
        self.configure(validatecommand=self.validate_entered_text)
        self.min_value = from_
        self.weight = font_weight

    def _spinbox_focus_in(self, *unused) -> None:
        self.selection_clear()

    def _spinbox_check_value(self, *unused) -> None:
        if not self.get():
            self.insert(0, str(self.min_value))

        spinbox_value = self.value
        if spinbox_value < self.min_value:
            spinbox_value = self.min_value
        self.value = spinbox_value

        self._spinbox_return_pressed()

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

    def on_resize(self, width: int, height: int) -> None:
        scale = get_font_scale(width, height)
        font_size = scale * self.weight
        self.update_font_size(int(font_size))

    @property
    def value(self) -> int:
        return int(super().get())

    @value.setter
    def value(self, value: int) -> None:
        self.delete(0, tk.END)
        self.insert(0, str(value))
