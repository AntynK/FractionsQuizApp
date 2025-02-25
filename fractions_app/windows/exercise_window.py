from tkinter import ttk
import tkinter.messagebox as messagebox

from fractions_app.helper import Topic
from fractions_app.widgets import Spinbox, ExerciseCanvas
from fractions_app.math import Fraction
from fractions_app.windows.congratulation_window import CongratulationWindow
from fractions_app.constants import (
    REDUCE_MESSAGE,
    CONVERT_TO_PROPER_FRACTION_MESSAGE,
)


class ExerciseWindow(ttk.Frame):
    def __init__(self, previous_state) -> None:
        super().__init__()

        self.previous_state = previous_state
        self.user_input = Fraction(1, 1)

        self._init_widgets()
        self._init_answer_box()
        self._init_buttons()

    def _init_widgets(self):
        self.subtopic_title_label = ttk.Label(self, text="Title", style="Title.TLabel")
        self.subtopic_title_label.grid(row=0, column=1, sticky="ns")

        self.exercise_canvas = ExerciseCanvas(self)
        self.exercise_canvas.grid(row=1, column=0, sticky="nwse", columnspan=3)
        self.bind("<Configure>", self.on_resize)

    def on_resize(self, *unused) -> None:
        self.exercise_canvas.display_exercise(self.current_exercise)

    def _init_answer_box(self) -> None:
        self.intenger_input = Spinbox(self.exercise_canvas, font_size=100, width=2)

        self.numerator_input = Spinbox(self.exercise_canvas)

        self.denominator_input = Spinbox(self.exercise_canvas, from_=1)
        self.exercise_canvas.add_user_input(
            self.intenger_input, self.numerator_input, self.denominator_input
        )

    def _init_buttons(self) -> None:
        self.buttons_frame = ttk.Frame(self)

        self.buttons_frame.grid_rowconfigure(0, weight=1)
        for column in range(3):
            self.buttons_frame.grid_columnconfigure(column, weight=1)

        self.exit_button = ttk.Button(
            self.buttons_frame, text="Назад", command=self.show_topic_window
        )
        self.exit_button.grid(row=3, column=0, sticky="nwse")

        self.try_again_button = ttk.Button(
            self.buttons_frame,
            text="Спробувати ще",
            command=self.reload_subtopic,
            state="disabled",
        )
        self.try_again_button.grid(row=3, column=1, padx=2, sticky="nwse")

        self.check_button = ttk.Button(
            self.buttons_frame, text="Перевірити", command=self.show_next_exercise
        )
        self.check_button.grid(row=3, column=2, padx=2, sticky="nwse")
        self.buttons_frame.grid(row=3, column=1, sticky="swe", pady=10)

    def show_next_exercise(self) -> None:
        if not self.check_user_input():
            return

        if not self.showed:
            CongratulationWindow(self)

            self.check_button.configure(text="Далі")
            self.try_again_button.configure(state="normal")
            self.showed = True
            return

        if len(self.subtopics) <= self.subtopic_index + 1:
            self.show_topic_window()
            return
        self.show(self.topic, self.subtopic_index + 1)

    def show_topic_window(self) -> None:
        self.grid_forget()
        self.previous_state.show()

    def reload_subtopic(self) -> None:
        self.show(self.topic, self.subtopic_index)

    def show(self, topic: Topic, subtopic_index: int) -> None:
        self._configure_grid()

        self._clear_input_boxes()
        self.denominator_input.set("1")

        self.topic = topic
        self.subtopics = topic.subtopics
        self.current_subtopic = self.subtopics[subtopic_index]
        self.subtopic_index = subtopic_index

        self.current_exercise = self.current_subtopic.generate_exercise()
        self.result = self.current_exercise.result.simplify()

        self.subtopic_title_label.configure(text=self.current_subtopic.title)
        self.exercise_canvas.display_exercise(self.current_exercise)

        self._reset_buttons()

    def _configure_grid(self) -> None:
        self.grid(row=0, column=0, sticky="nwse")
        for row in range(3):
            self.grid_rowconfigure(row, weight=1)
        for column in range(3):
            self.grid_columnconfigure(column, weight=1)

    def _clear_input_boxes(self) -> None:
        for widget in (
            self.numerator_input,
            self.intenger_input,
            self.denominator_input,
        ):
            widget.set("0")
            widget.update_background("white")

    def check_user_input(self) -> bool:
        self.user_input.numerator = int(self.numerator_input.get())
        self.user_input.denominator = int(self.denominator_input.get())
        self.user_input.integer = int(self.intenger_input.get())

        user_answer = self._compare_user_input_with_result()
        self._update_spinboxes_bg(user_answer, "green")

        if self.user_input.simplify() != self.result:
            self._reset_buttons()
            return False

        if (
            self.user_input.reduce() != self.user_input
            and self.user_input.numerator != 0
        ):
            self.numerator_input.update_background("orange")
            self.denominator_input.update_background("orange")
            messagebox.showerror(
                title="Помилка. Дріб потрібно скоротити!",
                message=REDUCE_MESSAGE,
            )
            self._reset_buttons()
            return False

        if self.user_input.to_proper_fraction() != self.user_input:
            self.numerator_input.update_background("orange")
            self.intenger_input.update_background("orange")
            messagebox.showerror(
                title="Помилка. Потрібно виділити цілу частину!",
                message=CONVERT_TO_PROPER_FRACTION_MESSAGE,
            )
            self._reset_buttons()
            return False

        return True

    def _reset_buttons(self) -> None:
        self.check_button.configure(text="Перевірити")
        self.try_again_button.configure(state="disabled")
        self.showed = False

    def _compare_user_input_with_result(self) -> tuple[bool, bool, bool]:
        return (
            self.user_input.integer == self.result.integer,
            self.user_input.numerator == self.result.numerator,
            self.user_input.denominator == self.result.denominator,
        )

    def _update_spinboxes_bg(
        self,
        answers: tuple[bool, bool, bool],
        ok_color: str,
        default_color: str = "red",
    ) -> None:
        for widget, answer in zip(
            (
                self.intenger_input,
                self.numerator_input,
                self.denominator_input,
            ),
            answers,
        ):
            widget.update_background(default_color)
            if answer:
                widget.update_background(ok_color)
