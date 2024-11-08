from tkinter import Canvas
from typing import Union


from fractions_app.helper import Exercise
from fractions_app.math import Fraction
from fractions_app.widgets.spinbox import Spinbox


CHARACTER_SIZE = 40
# TODO Somehow reduce number of magic values


class ExerciseCanvas(Canvas):
    def __init__(self, parent, **kwargs):
        Canvas.__init__(self, parent, **kwargs)

    def display_exercise(self, exercise: Exercise):
        """Display whole `exercise` on canvas.

        Arg:
            `exercise`: Exercise to be displayed.
        """

        self.delete("all")

        x = 45
        y = 40

        self.x_offset = self._display_operand(
            exercise.operand_1, x, y, inital_offset=CHARACTER_SIZE
        )

        x += CHARACTER_SIZE + self.x_offset
        x += self._display_text(exercise.operation, x, y)

        self.x_offset = self._display_operand(exercise.operand_2, x, y)

        x += CHARACTER_SIZE + self.x_offset
        x += self._display_text("=", x, y)

        self._display_inner_widgets(x, y)

        self.on_resize()

    def _display_operand(
        self, operand: Union[int, Fraction], x: int, y: int, inital_offset: int = 0
    ) -> int:
        offset = inital_offset
        if isinstance(operand, int):
            self._display_text(operand, x + offset, y)
            return offset

        if operand.integer != 0:
            offset = round(CHARACTER_SIZE / 1.5)
            self._display_text(operand.integer, x, y)

        self._display_text(operand.numerator, x + offset, y - 12)
        self.create_line(x - 15 + offset, y, x + 15 + offset, y, width=5)
        self._display_text(operand.denominator, x + offset, y + 12)
        return offset

    def _display_text(self, text: Union[float, str], x: int, y: int) -> int:
        font = ("Times New Roman", 80, "bold")

        self.create_text(
            x,
            y,
            text=text,
            fill="black",
            font=font,
        )
        return CHARACTER_SIZE

    def _display_inner_widgets(self, x: int, y: int):
        self.create_window(x, y, window=self._intenger_input)
        x += CHARACTER_SIZE + 8
        self.create_window(x, y - 12, window=self._numerator_input)
        self.create_line(x - 20, y, x + 20, y, width=5)
        self.create_window(x, y + 12, window=self._denominator_input)

    def on_resize(self, event=None):
        wscale = (
            self.master.winfo_width() / 1000 + self.master.winfo_height() / 1000
        ) * 2
        self.scale("all", 0, 0, wscale, wscale)

    def add_user_input(
        self,
        intenger_input: Spinbox,
        numerator_input: Spinbox,
        denominator_input: Spinbox,
    ):
        self._intenger_input = intenger_input
        self._numerator_input = numerator_input
        self._denominator_input = denominator_input
