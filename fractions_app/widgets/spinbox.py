import tkinter as tk


class Spinbox(tk.Spinbox):
    def __init__(self, master, *args, **kwargs) -> None:
        super().__init__(master, *args, **kwargs)

        self.bind("<FocusIn>", self._spinbox_focus_in)
        self.bind("<FocusOut>", self._spinbox_check_value)

        self.bind("<Return>", self._spinbox_return_pressed)
        self.validate_entered_text = (self.register(self._validate_spinbox_text), "%P")
        self.configure(validatecommand=self.validate_entered_text)

    def _spinbox_focus_in(self, event):
        self.selection_clear()

    def _spinbox_check_value(self, event):
        if not self.get():
            self.insert(0, "1")
        spinbox_text = self.get()
        if spinbox_text == "-":
            spinbox_text = "-1"

        self.set(str(int(spinbox_text)))
        self._spinbox_return_pressed(event)

    def set(self, value: str):
        self.delete(0, tk.END)
        self.insert(0, value)

    def _spinbox_return_pressed(self, event):
        self.selection_clear()
        if master := self.master.master:
            master.focus()

    def _validate_spinbox_text(self, text: str) -> bool:
        if text and text[0] == "-":
            text = text[1:]

        if not text.isdigit() and text:
            self.bell()
            return False
        return True

    def update_background(self, color: str):
        self.configure(background=color)
