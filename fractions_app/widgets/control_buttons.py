from tkinter import ttk
from typing import Callable, Optional


class ControlButtons(ttk.Frame):
    def __init__(
        self,
        master,
        on_exit_btn_pressed: Callable,
        on_check_btn_pressed: Callable,
        on_try_again_btn_pressed: Optional[Callable] = None,
    ) -> None:
        super().__init__(master)

        self.grid_rowconfigure(0, weight=1)
        for column in range(3):
            self.grid_columnconfigure(column, weight=1)

        self.exit_button = ttk.Button(self, text="Назад", command=on_exit_btn_pressed)
        self.exit_button.grid(row=0, column=0, sticky="we")
        self.is_try_again_btn_used = False

        row_shift = 0
        if on_try_again_btn_pressed is not None:
            self.try_again_button = ttk.Button(
                self,
                text="Спробувати ще",
                state="disabled",
                command=on_try_again_btn_pressed,
            )
            self.try_again_button.grid(row=0, column=1, padx=2, sticky="we")
            self.is_try_again_btn_used = True
            row_shift += 1

        self.check_button = ttk.Button(
            self, text="Перевірити", command=on_check_btn_pressed
        )
        self.check_button.grid(row=0, column=1 + row_shift, padx=2, sticky="we")

    def reset_buttons(self) -> None:
        self.check_button.configure(text="Перевірити")
        if self.is_try_again_btn_used:
            self.try_again_button.configure(state="disabled")

    def correct_answer(self) -> None:
        self.check_button.configure(text="Далі")
        if self.is_try_again_btn_used:
            self.try_again_button.configure(state="normal")
