from tkinter import ttk, END


class Spinbox(ttk.Spinbox):
    def __init__(self, master, *args, **kwargs) -> None:
        super().__init__(master, *args, **kwargs)
        self.bind("<FocusIn>", self._spinbox_focus_in)
        self.bind("<FocusOut>", self._spinbox_check_value)

        self.bind("<Return>", self._spinbox_return_presed)
        self.validate_enetered_text = (self.register(self._validate_spinbox_text), "%P")
        self.configure(validatecommand=self.validate_enetered_text)

    def update_backgound(self, color: str):
        ttk.Style().configure(self["style"], fieldbackground=color)

    def _validate_spinbox_text(self, text: str) -> bool:
        if text and text[0] == "-":
            text = text[1:]

        if not text.isdigit() and text:
            self.bell()
            return False
        return True

    def _spinbox_focus_in(self, event):
        self.select_clear()
        self.select_range(0, END)

    def _spinbox_return_presed(self, event):
        self.select_clear()
        self.master.focus()

    def _spinbox_check_value(self, event):
        if not self.get():
            self.insert(0, "1")
        spinbox_text = self.get()
        if spinbox_text == "-":
            spinbox_text = "-1"
        self.delete(0, END)
        self.insert(0, str(int(spinbox_text)))

        self._spinbox_return_presed(event)
