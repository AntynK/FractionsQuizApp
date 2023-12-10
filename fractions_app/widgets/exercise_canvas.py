from tkinter import Canvas
from typing import Union


from ..helper import Exercise
from ..math import Fraction

# https://stackoverflow.com/questions/22835289/how-to-get-tkinter-canvas-to-dynamically-resize-to-window-width

CHARACTER_SIZE = 40


class ExerciseCanvas(Canvas):
    def __init__(self, parent, **kwargs):
        Canvas.__init__(self, parent, **kwargs)

    def on_resize(self, event=None):
        wscale = (
            self.master.winfo_width() / 1000 + self.master.winfo_height() / 1000
        ) * 2
        self.scale("all", 0, 0, wscale, wscale)

    def display_exercise(self, exercise: Exercise):
        """Display whole `exercise` on canvas.

        Arg:
            `exercise`: Exercise to be displayed.
        """

        # TODO Make this method more readable.

        self.delete("all")
        x = 45
        y = 30

        offset = self._display_operand(
            exercise.operand_1, x, y, inital_offset=CHARACTER_SIZE
        )

        x += CHARACTER_SIZE + offset
        x += self._display_text(exercise.operation, x, y)

        offset = self._display_operand(exercise.operand_2, x, y)

        x += CHARACTER_SIZE + offset
        x += self._display_text("=", x, y)

        self._display_text("?", x, y)
        self.on_resize()

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
