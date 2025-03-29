from tkinter import ttk
from typing import Callable, Optional
import tkinter.messagebox as messagebox

from fractions_app.constants import (
    REDUCE_MESSAGE,
    CONVERT_TO_PROPER_FRACTION_MESSAGE,
)
from fractions_app.math import Fraction
from fractions_app.helper import Exercise, check_answer, AnswerStatus
from fractions_app.widgets.exercise_canvas import ExerciseCanvas
from fractions_app.widgets.control_buttons import ControlButtons
from fractions_app.windows.congratulation_window import CongratulationWindow


class ExerciseBox(ttk.Frame):
    def __init__(
        self,
        master,
        on_exit_btn_pressed: Callable,
        on_correct_answer_entered: Callable,
        on_try_again_btn_pressed: Optional[Callable] = None,
    ) -> None:
        super().__init__(master)

        self.showed = False
        self.correct_answer = Fraction(0, 1, 0)
        self._on_correct_answer_entered = on_correct_answer_entered
        self._init_widgets(on_exit_btn_pressed, on_try_again_btn_pressed)

    def _init_widgets(
        self,
        on_exit_btn_pressed: Callable,
        on_try_again_btn_pressed: Optional[Callable],
    ) -> None:
        for row in range(2):
            self.grid_rowconfigure(row, weight=1)
        for column in range(1):
            self.grid_columnconfigure(column, weight=1)

        self.exercise_canvas = ExerciseCanvas(self)
        self.control_buttons = ControlButtons(
            self,
            on_exit_btn_pressed=on_exit_btn_pressed,
            on_check_btn_pressed=self._check_user_input,
            on_try_again_btn_pressed=on_try_again_btn_pressed,
        )

        self.exercise_canvas.grid(row=0, column=0, sticky="nwse")
        self.control_buttons.grid(row=1, column=0, sticky="swe", pady=10)

    def _check_user_input(self) -> None:
        user_input = self.exercise_canvas.get_user_input()
        status, spinboxes_color = check_answer(user_input, self.correct_answer)
        self.control_buttons.reset_buttons()
        self.exercise_canvas.color_spinboxes(spinboxes_color)

        if status is AnswerStatus.CORRECT:
            if not self.showed:
                CongratulationWindow(self)
                self.control_buttons.correct_answer()
                self.showed = True
                return

            self._on_correct_answer_entered()

        elif status is AnswerStatus.NEED_REDUCING:
            messagebox.showinfo(
                title="Дріб потрібно скоротити!",
                message=REDUCE_MESSAGE,
            )
            self.showed = False

        elif status is AnswerStatus.NEED_CONVERTION_TO_PROPER:
            messagebox.showinfo(
                title="Потрібно виділити цілу частину!",
                message=CONVERT_TO_PROPER_FRACTION_MESSAGE,
            )
            self.showed = False
        elif status is AnswerStatus.WRONG:
            self.showed = False

    def on_resize(self, width: int, height: int) -> None:
        self.exercise_canvas.on_resize(width, height)

    def display_exercise(self, exercise: Exercise) -> None:
        self.correct_answer = exercise.answer

        self.control_buttons.reset_buttons()
        self.exercise_canvas.clear_input_boxes()
        self.exercise_canvas.display_exercise(exercise)
