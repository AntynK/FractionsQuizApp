from tkinter import Canvas, BooleanVar, ttk
from tkinter.font import Font
from typing import Union

from fractions_app.helper import Exercise
from fractions_app.math import Fraction
from fractions_app.widgets.spinbox import Spinbox
from fractions_app.constants import BASE_WIDTH, BASE_HEIGHT

CHARACTER_SIZE = 0.09
BAR_SIZE = 0.005


class ExerciseCanvas(Canvas):
    def __init__(self, parent) -> None:
        super().__init__(parent)

        self._exercise = None
        self._label_font = Font(family="Times New Roman", size=60, weight="bold")
        self.width, self.height = BASE_WIDTH, BASE_HEIGHT
        self._spacing = 0

        self._init_checkbutton()
        self._init_answer_box()

    def _init_checkbutton(self) -> None:
        self.show_fraction = BooleanVar()
        self.show_fraction_checkbox = ttk.Checkbutton(
            self.master,
            text="Приховати",
            onvalue=True,
            offvalue=False,
            variable=self.show_fraction,
            command=self._hide_fraction,
        )

    def _init_answer_box(self) -> None:
        self._last_numerator_value = "0"
        self._last_denominator_value = "1"

        self._intenger_input = Spinbox(self, width=2)
        self._numerator_input = Spinbox(self)
        self._denominator_input = Spinbox(self, from_=1)

    def display_exercise(self, exercise: Exercise) -> None:
        """Display whole `exercise` on canvas.

        Arg:
            `exercise`: Exercise to be displayed.
        """
        self._update_spacing()

        self._exercise = exercise
        self.delete("all")

        x = self.character_width() * 2 + self._spacing
        y = self.character_height() * 2.5

        x += self._display_operand(exercise.operand_1, x, y) * 1.5 + self._spacing

        x += self._display_text(exercise.operation, x, y) * 1.8 + self._spacing

        x += self._display_operand(exercise.operand_2, x, y) + self._spacing

        x += self._display_text("=", x, y) * 1.5 + self._spacing // 2

        self._display_user_input(x, y)
        self.create_window(
            self.character_width() * 9.6,
            self.character_height() * 5,
            window=self.show_fraction_checkbox,
        )

    def _display_operand(
        self, operand: Union[int, Fraction], x: float, y: float
    ) -> float:
        offset = 0
        size = self.character_width()
        if isinstance(operand, int):
            self._display_text(operand, x, y)
            return size

        if operand.integer != 0:
            offset = self.character_width()
            self._display_text(operand.integer, x - offset, y)

        self._display_text(operand.numerator, x, y - self.character_height())
        self.create_line(
            x - self.character_width() // 2,
            y,
            x + self.character_width() // 2,
            y,
            width=self.bar_width(),
        )
        self._display_text(operand.denominator, x, y + self.character_height())
        return size

    def _display_text(self, text: Union[float, str], x: float, y: float) -> float:
        self.create_text(
            x,
            y,
            text=text,
            fill="black",
            font=self._label_font,
        )
        return self.character_width()

    def _display_user_input(self, x: float, y: float) -> None:
        self.create_window(x, y, window=self._intenger_input)
        x += self.character_width() * 2

        if not self.show_fraction.get():
            self.create_window(
                x, y - self.character_height(), window=self._numerator_input
            )
            self.create_line(
                x - self.character_width(),
                y,
                x + self.character_width(),
                y,
                width=self.bar_width(),
            )
            self.create_window(
                x,
                y + self.character_height(),
                window=self._denominator_input,
            )

    def _update_spacing(self) -> None:
        if self.show_fraction.get():
            self._spacing = self.character_width() // 2
        else:
            self._spacing = 0

    def _hide_fraction(self) -> None:
        if self._exercise is None:
            return

        if self.show_fraction.get():
            self._last_numerator_value = self._numerator_input.get()
            self._last_denominator_value = self._denominator_input.get()
            self._numerator_input.set("0")
            self._denominator_input.set("1")
        else:
            self._numerator_input.set(self._last_numerator_value)
            self._denominator_input.set(self._last_denominator_value)

        self.display_exercise(self._exercise)

    def bar_width(self) -> float:
        return self.width * BAR_SIZE

    def character_width(self) -> float:
        return self.width * CHARACTER_SIZE

    def character_height(self) -> float:
        return self.height * CHARACTER_SIZE

    def clear_input_boxes(self) -> None:
        for widget in (
            self._numerator_input,
            self._intenger_input,
            self._denominator_input,
        ):
            widget.set("0")
            widget.update_background("white")
        self._denominator_input.set("1")

    def color_spinboxes(self, colors: list[str]) -> None:
        for color, spinbox in zip(
            colors,
            (self._numerator_input, self._denominator_input, self._intenger_input),
        ):
            spinbox.update_background(color)

    def on_resize(self, width: int, height: int) -> None:
        self.width, self.height = width, height

        wscale = (self.width / 1000 + self.height / 1000) * 2
        self.scale("all", 0, 0, wscale, wscale)
        self._update_font()
        if self._exercise is not None:
            self.display_exercise(self._exercise)

    def get_user_input(self) -> Fraction:
        numerator = int(self._numerator_input.get())
        denominator = int(self._denominator_input.get())
        integer = int(self._intenger_input.get())
        return Fraction(numerator, denominator, integer)

    def _update_font(self) -> None:
        k = (self.width // 100 + self.height // 100) * 5
        self._label_font.configure(size=int(k * 0.8))
        self._intenger_input.update_font_size(int(k * 0.9))
        self._denominator_input.update_font_size(int(k * 0.7))
        self._numerator_input.update_font_size(int(k * 0.7))
