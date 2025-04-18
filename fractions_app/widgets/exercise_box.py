from tkinter import ttk
import tkinter.messagebox as messagebox
from typing import Callable, Optional

from fractions_app.constants import (
    REDUCE_MESSAGE,
    CONVERT_TO_PROPER_FRACTION_MESSAGE,
)
from fractions_app.math import Fraction
from fractions_app.helper import Exercise, check_answer, AnswerStatus
from fractions_app.widgets.exercise_canvas import ExerciseCanvas
from fractions_app.widgets.control_buttons import ControlButtons, ButtonTypes
from fractions_app.windows.congratulation_popup import CongratulationPopup
from fractions_app.widgets.make_grid import make_grid


class ExerciseBox(ttk.Frame):
    def __init__(
        self,
        master,
        on_correct_answer_entered: Callable,
        *buttons: tuple[ButtonTypes, Optional[Callable]]
    ) -> None:
        super().__init__(master)

        make_grid(self, 2, 1)

        self.showed = False
        self.correct_answer = Fraction(0, 1, 0)
        self.control_buttons = ControlButtons(self, *buttons)

        self._on_correct_answer_entered = on_correct_answer_entered
        self.control_buttons.add_callback(ButtonTypes.CHECK_BTN, self._check_user_input)

        self.exercise_canvas = ExerciseCanvas(self)

        self.exercise_canvas.grid(row=0, column=0, sticky="nwse")
        self.control_buttons.grid(row=1, column=0, sticky="swe", pady=10, padx=10)

    def _check_user_input(self) -> None:
        user_input = self.exercise_canvas.get_user_input()
        status, spinboxes_color = check_answer(user_input, self.correct_answer)
        self.control_buttons.reset_buttons()
        self.exercise_canvas.color_spinboxes(spinboxes_color)

        if status is AnswerStatus.CORRECT:
            if not self.showed:
                CongratulationPopup(self)
                self.control_buttons.correct_answer()
            self._on_correct_answer_entered(self.showed)
            self.showed = True

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
        self.showed = False

        self.correct_answer = exercise.answer

        self.control_buttons.reset_buttons()
        self.exercise_canvas.clear_input_boxes()
        self.exercise_canvas.display_exercise(exercise)
