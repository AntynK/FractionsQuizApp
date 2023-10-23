import tkinter as tk
import tkinter.messagebox as msg_box

import unicodeit

from ..helper import Subtopic, Fraction


class ExerciseWindow(tk.Frame):
    def __init__(self, previous_state: tk.Frame) -> None:
        super().__init__()

        self.previous_state = previous_state

        self.init_widgets()

    def init_buttons(self):
        self.exit_button = tk.Button(
            self, text="Вийти", command=self.show_select_exercise_window
        )

        self.exit_button.grid(row=4, column=0)

        self.again_button = tk.Button(self, text="Ще раз", command=self.reload_subtopic)
        self.again_button.grid(row=4, column=1)

        self.check_button = tk.Button(self, text="Перевірити", command=self.check_input)
        self.check_button.grid(row=4, column=2)

    def init_widgets(self):
        self.subtopic_title_label = tk.Label(
            self, text="Title", font=("Times New Roman", 12, "bold")
        )
        self.subtopic_title_label.grid(columnspan=3)

        self.expression_label = tk.Label(
            self, text="Expression", font=("Times New Roman", 14)
        )
        self.expression_label.grid(columnspan=3)

        self.answer_box = tk.Frame(self, borderwidth=3, relief="groove")

        tk.Label(self.answer_box, text="Ціле:").grid(row=0, column=0)
        self.intenger_input = tk.Spinbox(self.answer_box, from_=0, to=30, increment=1)
        self.intenger_input.grid(row=0, column=1)

        tk.Label(self.answer_box, text="Чисельник:").grid(row=1, column=0)
        self.numerator_input = tk.Spinbox(self.answer_box, from_=0, to=30, increment=1)
        self.numerator_input.grid(row=1, column=1)

        tk.Label(self.answer_box, text="Знаменник:").grid(row=2, column=0)
        self.denominator_input = tk.Spinbox(
            self.answer_box,
            from_=1,
            to=30,
            increment=1,
        )
        self.denominator_input.grid(row=2, column=1)

        self.init_buttons()

        self.answer_box.grid(row=2, columnspan=4)

    def reload_subtopic(self):
        self.load_subtopic(self.subtopics, self.index)

    def load_subtopic(self, subtopics: list[Subtopic], index: int):
        self.clear_input_boxes()
        self.showed = False
        self.subtopics = subtopics
        self.current_subtopic = subtopics[index]
        self.index = index

        self.current_exercise = self.current_subtopic.exercises()
        self.result = self.current_exercise.fraction
        self.redused_result = self.result.reduce()
        if self.result == self.redused_result:
            self.result = None

        self.check_button.configure(text="Перевірити")
        self.subtopic_title_label.configure(text=self.current_subtopic.title)
        self.display_expression()

    def _check_value(self, widget: tk.Spinbox, value: int, ok_color: str):
        if int(widget.get()) != value:
            widget.configure(bg="red")
            return False
        widget.configure(bg=ok_color)
        return True

    def compare_user_input_with_fraction(
        self, fraction: Fraction, ok_color="green"
    ) -> bool:
        return all(
            (
                self._check_value(self.intenger_input, fraction.integer, ok_color),
                self._check_value(self.numerator_input, fraction.numerator, ok_color),
                self._check_value(
                    self.denominator_input, fraction.denominator, ok_color
                ),
            )
        )

    def check_input(self):
        if self.result is not None:
            if self.compare_user_input_with_fraction(self.result, ok_color="orange"):
                msg_box.showinfo(title="Помилка", message="Дріб можна скоротити!")
                return
        if not self.compare_user_input_with_fraction(self.redused_result):
            return

        self.show_next_exercise()

    def show_next_exercise(self):
        if not self.showed:
            self.check_button.configure(text="Наступне")
            self.showed = True
            return

        if len(self.subtopics) >= self.index:
            self.show_select_exercise_window()
            return
        self.load_subtopic(self.subtopics, self.index + 1)

    def display_expression(self):
        result = ""
        for symbol in self.current_exercise.expression.split(" "):
            if "/" in symbol:
                numerator, denominator = symbol.split("/")
                result += unicodeit.replace(f"^{{{numerator}}}/_{{{denominator}}}")
                continue
            result += f" {symbol} "

        self.expression_label.configure(text=result)

    def show_select_exercise_window(self):
        self.pack_forget()
        self.previous_state.pack()

    def clear_input_boxes(self):
        for widget in (
            self.numerator_input,
            self.intenger_input,
            self.denominator_input,
        ):
            widget.delete(0, tk.END)
            widget.insert(0, "0")
            widget.configure(bg="white")
