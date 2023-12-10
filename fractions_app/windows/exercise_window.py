from tkinter import ttk, END
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

    def _init_buttons(self):
        self.buttons_frame = ttk.Frame(self)

        self.buttons_frame.grid_rowconfigure(0, weight=1)
        for column in range(3):
            self.buttons_frame.grid_columnconfigure(column, weight=1)

        self.exit_button = ttk.Button(
            self.buttons_frame, text="Вийти", command=self.show_main_window
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
        self.buttons_frame.grid(row=3, column=1, padx=113, sticky="nwe")

    def _init_widgets(self):
        self.subtopic_title_label = ttk.Label(self, text="Title", style="Title.TLabel")
        self.subtopic_title_label.grid(row=0, column=1, sticky="ns")

        self.exercise_canvas = ExerciseCanvas(self)
        self.exercise_canvas.grid(row=1, column=1, sticky="nwse")
        self.bind("<Configure>", self.on_resize)
        self.bind("<FocusIn>", self.check_user_input)

        self.answer_box = ttk.Frame(self, borderwidth=3, relief="groove")

        for row in range(3):
            self.answer_box.grid_rowconfigure(row, weight=1)

        self.answer_box.grid_columnconfigure(0, weight=1)

        ttk.Label(self.answer_box, text="Ціле:").grid(row=0, column=0, sticky="nwse")
        ttk.Label(self.answer_box, text="Чисельник:").grid(
            row=1, column=0, sticky="nwse"
        )
        ttk.Label(self.answer_box, text="Знаменник:").grid(
            row=2, column=0, sticky="nwse"
        )

        self.intenger_input = Spinbox(
            self.answer_box,
            validate="all",
            font=("Times New Roman", 65, "bold"),
            justify="center",
            style="Intenger.TSpinbox",
        )
        self.intenger_input.grid(row=0, column=2, sticky="nwse")

        self.numerator_input = Spinbox(
            self.answer_box,
            validate="all",
            font=("Times New Roman", 65, "bold"),
            justify="center",
            style="Numerator.TSpinbox",
        )
        self.numerator_input.grid(row=1, column=2, sticky="nwse")

        self.denominator_input = Spinbox(
            self.answer_box,
            validate="all",
            font=("Times New Roman", 65, "bold"),
            justify="center",
            style="Denominator.TSpinbox",
        )
        self.denominator_input.grid(row=2, column=2, sticky="nwse")

        self._init_buttons()
        self.answer_box.grid(row=2, column=1, sticky="nwse")

    def reload_subtopic(self):
        self.show(self.topic, self.index)

    def _configure_grid(self):
        self.grid(row=0, column=0, sticky="nwse")
        for row in range(4):
            self.grid_rowconfigure(row, weight=1)
        for column in range(3):
            self.grid_columnconfigure(column, weight=1)

    def on_resize(self, event):
        self.exercise_canvas.display_exercise(self.current_exercise)
        self.check_user_input()

    def show(self, topic: Topic, index: int):
        self._configure_grid()

        self._clear_input_boxes()
        self.intenger_input.delete(0, END)
        self.intenger_input.insert(0, "0")

        self.showed = False
        self.topic = topic
        self.subtopics = topic.subtopics
        self.current_subtopic = self.subtopics[index]
        self.index = index

        self.current_exercise = self.current_subtopic.generate_exercise()
        self.result = self.current_exercise.result.simplify()

        self.check_button.configure(text="Перевірити")
        self.subtopic_title_label.configure(text=self.current_subtopic.title)
        self.exercise_canvas.display_exercise(self.current_exercise)

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
            widget.update_backgound(default_color)
            if answer:
                widget.update_backgound(ok_color)

    def check_user_input(self, event=None) -> bool:
        self.user_input.numerator = int(self.numerator_input.get())
        self.user_input.denominator = int(self.denominator_input.get())
        self.user_input.integer = int(self.intenger_input.get())

        user_answer = self._compare_user_input_with_result()
        self._update_spinboxes_bg(user_answer, "green")

        if self.user_input.reduce() != self.user_input:
            if event == "BUTTON_PRESSED":
                messagebox.showerror(
                    title="Помилка",
                    message="Дріб потрібно скоротити!",
                )
            self.numerator_input.update_backgound("orange")
            self.denominator_input.update_backgound("orange")
            return False

        if self.user_input.convert_to_proper_fraction() != self.user_input:
            if event == "BUTTON_PRESSED":
                messagebox.showerror(
                    title="Помилка",
                    message="Потрібно виділити цілу частину!",
                )
            self.numerator_input.update_backgound("orange")
            self.intenger_input.update_backgound("orange")
            return False

        if self.user_input != self.result:
            self.check_button.configure(text="Перевірити")
            self.showed = False
            return False
        return True

    def show_next_exercise(self):
        if not self.check_user_input("BUTTON_PRESSED"):
            return

        if not self.showed:
            CongratulationWindow(self)

            self.check_button.configure(text="Наступне")
            self.showed = True
            return

        if len(self.subtopics) <= self.index + 1:
            self.show_main_window()
            return
        self.show(self.topic, self.index + 1)

    def show_main_window(self):
        self.grid_forget()
        self.previous_state.show()

    def _clear_input_boxes(self):
        for widget in (
            self.numerator_input,
            self.intenger_input,
            self.denominator_input,
        ):
            widget.delete(0, END)
            widget.insert(0, "1")
            widget.update_backgound("white")
