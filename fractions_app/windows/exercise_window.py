from tkinter import ttk
import tkinter.messagebox as messagebox

from ..helper import Topic
from ..widgets import Spinbox, ExerciseCanvas
from ..math import Fraction
from .congratulation_window import CongratulationWindow


class ExerciseWindow(ttk.Frame):
    def __init__(self, previous_state) -> None:
        super().__init__()

        self.previous_state = previous_state
        self.user_input = Fraction(0, 1)

        self._init_widgets()
        self._init_answer_box()
        self._init_buttons()

    def _init_widgets(self):
        self.subtopic_title_label = ttk.Label(self, text="Title", style="Title.TLabel")
        self.subtopic_title_label.grid(row=0, column=1, sticky="ns")

        self.exercise_canvas = ExerciseCanvas(self)
        self.exercise_canvas.grid(row=1, column=0, sticky="nwse", columnspan=3)
        self.bind("<Configure>", self.on_resize)

    def on_resize(self, event):
        self.exercise_canvas.display_exercise(self.current_exercise)

    def _init_answer_box(self):
        self.intenger_input = Spinbox(
            self.exercise_canvas,
            validate="all",
            font=("Times New Roman", 100, "bold"),
            justify="center",
            width=2,
            to=200,
            from_=-200,
            increment=1,
        )

        self.numerator_input = Spinbox(
            self.exercise_canvas,
            validate="all",
            font=("Times New Roman", 50, "bold"),
            justify="center",
            width=3,
            to=200,
            from_=-200,
            increment=1,
        )

        self.denominator_input = Spinbox(
            self.exercise_canvas,
            validate="all",
            font=("Times New Roman", 50, "bold"),
            justify="center",
            width=3,
            to=200,
            from_=-200,
            increment=1,
        )
        self.exercise_canvas.add_user_input(
            self.intenger_input, self.numerator_input, self.denominator_input
        )

    def _init_buttons(self):
        self.buttons_frame = ttk.Frame(self)

        self.buttons_frame.grid_rowconfigure(0, weight=1)
        for column in range(3):
            self.buttons_frame.grid_columnconfigure(column, weight=1)

        self.exit_button = ttk.Button(
            self.buttons_frame, text="Вийти", command=self.show_topic_window
        )
        self.exit_button.grid(row=3, column=0, sticky="nwse")

        self.again_button = ttk.Button(
            self.buttons_frame, text="Ще раз", command=self.reload_subtopic
        )
        self.again_button.grid(row=3, column=1, padx=2, sticky="nwse")

        self.check_button = ttk.Button(
            self.buttons_frame, text="Перевірити", command=self.show_next_exercise
        )
        self.check_button.grid(row=3, column=2, padx=2, sticky="nwse")
        self.buttons_frame.grid(row=2, column=1, sticky="swe", pady=10)

    def show_next_exercise(self):
        if not self.check_user_input():
            return

        if not self.showed:
            CongratulationWindow(self)

            self.check_button.configure(text="Наступне")
            self.showed = True
            return

        if len(self.subtopics) <= self.subtopic_index + 1:
            self.show_topic_window()
            return
        self.show(self.topic, self.subtopic_index + 1)

    def show_topic_window(self):
        self.grid_forget()
        self.previous_state.show()

    def reload_subtopic(self):
        self.show(self.topic, self.subtopic_index)

    def show(self, topic: Topic, subtopic_index: int):
        self._configure_grid()

        self._clear_input_boxes()
        self.intenger_input.set("0")

        self.showed = False
        self.topic = topic
        self.subtopics = topic.subtopics
        self.current_subtopic = self.subtopics[subtopic_index]
        self.subtopic_index = subtopic_index

        self.current_exercise = self.current_subtopic.generate_exercise()
        self.result = self.current_exercise.result.simplify()

        self.check_button.configure(text="Перевірити")
        self.subtopic_title_label.configure(text=self.current_subtopic.title)
        self.exercise_canvas.display_exercise(self.current_exercise)

    def _configure_grid(self):
        self.grid(row=0, column=0, sticky="nwse")
        for row in range(3):
            self.grid_rowconfigure(row, weight=1)
        for column in range(3):
            self.grid_columnconfigure(column, weight=1)

    def _clear_input_boxes(self):
        for widget in (
            self.numerator_input,
            self.intenger_input,
            self.denominator_input,
        ):
            widget.set("1")
            widget.update_background("white")

    def check_user_input(self) -> bool:
        self.user_input.numerator = int(self.numerator_input.get())
        self.user_input.denominator = int(self.denominator_input.get())
        self.user_input.integer = int(self.intenger_input.get())

        user_answer = self._compare_user_input_with_result()
        self._update_spinboxes_bg(user_answer, "green")

        if self.user_input.reduce() != self.user_input and self.user_input.numerator != 0:
            self.numerator_input.update_background("orange")
            self.denominator_input.update_background("orange")
            messagebox.showerror(
                title="Помилка",
                message="Дріб потрібно скоротити!",
            )
            return False

        if self.user_input.convert_to_proper_fraction() != self.user_input:
            self.numerator_input.update_background("orange")
            self.intenger_input.update_background("orange")
            messagebox.showerror(
                title="Помилка",
                message="Потрібно виділити цілу частину!",
            )

            return False

        if self.user_input != self.result:
            self.check_button.configure(text="Перевірити")
            self.showed = False
            return False
        return True

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
    ):
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
