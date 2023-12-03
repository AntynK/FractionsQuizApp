from tkinter import Canvas
from typing import Union


from ..helper import Exercise
from ..math import Fraction

# https://stackoverflow.com/questions/22835289/how-to-get-tkinter-canvas-to-dynamically-resize-to-window-width

CHARACTER_SIZE = 30


class ExerciseCanvas(Canvas):
    def __init__(self, parent, **kwargs):
        Canvas.__init__(self, parent, **kwargs)

    def on_resize(self, event=None):
        wscale = (
            self.master.winfo_width() / 1000 + self.master.winfo_height() / 1000
        ) * 2
        self.scale("all", 0, 0, wscale, wscale)

    def display_exercise(self, exercise: Exercise):
        print(exercise)
        self.delete("all")
        x = 100
        y = 30
        offset = self.display_operand(exercise.operand_1, x, y)
        x += CHARACTER_SIZE - offset
        self.display_text(exercise.operation, x, y)
        x += CHARACTER_SIZE + offset
        self.display_operand(exercise.operand_2, x, y)
        x += CHARACTER_SIZE - offset
        self.display_text("=", x, y, bigger=True)
        x += 10
        self.display_text("?", x, y, bigger=True)
        self.on_resize()

    def display_text(
        self, text: Union[float, str], x: int, y: int, bigger: bool = True
    ):
        font = ("Times New Roman", 20) if bigger else ("Times New Roman", 15)

        self.create_text(
            x,
            y,
            text=text,
            fill="black",
            font=font,
        )

    def display_operand(self, operand: Union[int, Fraction], x: int, y: int):
        if isinstance(operand, int):
            self.display_text(operand, x, y)
            return 0
        offset = 0
        if operand.integer != 0:
            offset = 20
            self.display_text(operand.integer, x - 20 - offset, y, bigger=True)

        self.display_text(operand.numerator, x - offset, y - 5)
        self.create_line(x - 15 - offset, y, x + 15 - offset, y)
        self.display_text(operand.denominator, x - offset, y + 5)
        return offset
