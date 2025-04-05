from functools import partial
from tkinter import ttk
from typing import Callable, Optional
from enum import Enum

from fractions_app.widgets.make_grid import make_grid


class ButtonTypes(Enum):
    BACK_BTN = "Назад"
    CHECK_BTN = "Перевірити"
    TRY_AGAIN_BTN = "Спробувати ще"
    SKIP_BTN = "Пропустити"


Callback = Optional[Callable]


class ControlButtons(ttk.Frame):
    def __init__(self, master, *buttons: tuple[ButtonTypes, Callback]) -> None:
        super().__init__(master)

        make_grid(self, 1, len(buttons))
        self.buttons: dict[ButtonTypes, list] = {}
        for index, button_data in enumerate(buttons):
            btn_type, callback = button_data
            text = btn_type.value

            button = ttk.Button(
                self, text=text, command=partial(self._on_btn_pressed, btn_type)
            )
            button.grid(row=0, column=index, sticky="we")
            self.buttons[btn_type] = [button, []]
            self.add_callback(btn_type, callback)

    def reset_buttons(self) -> None:
        self.get(ButtonTypes.CHECK_BTN).configure(text="Перевірити")
        if ButtonTypes.TRY_AGAIN_BTN in self:
            self.get(ButtonTypes.TRY_AGAIN_BTN).configure(state="disabled")

    def correct_answer(self) -> None:
        self.get(ButtonTypes.CHECK_BTN).configure(text="Далі")
        if ButtonTypes.TRY_AGAIN_BTN in self:
            self.get(ButtonTypes.TRY_AGAIN_BTN).configure(state="normal")

    def _on_btn_pressed(self, btn_type: ButtonTypes) -> None:
        for callback in self.buttons[btn_type][1]:
            if callable(callback):
                callback()

    def add_callback(self, btn_type: ButtonTypes, callback: Callback) -> None:
        self.buttons[btn_type][1].insert(0, callback)

    def __contains__(self, key: ButtonTypes) -> bool:
        return key in self.buttons

    def get(self, btn_type: ButtonTypes) -> ttk.Button:
        return self.buttons[btn_type][0]
