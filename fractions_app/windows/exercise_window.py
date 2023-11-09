from tkinter import ttk, END
import tkinter.messagebox as msg_box

import unicodeit

from ..helper import Topic, Fraction


class ExerciseWindow(ttk.Frame):
    def __init__(self, previous_state) -> None:
        super().__init__()

        self.previous_state = previous_state

        self.init_widgets()

    def init_buttons(self):
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
            self.buttons_frame, text="Перевірити", command=self.check_input
        )
        self.check_button.grid(row=3, column=2, padx=2, sticky="nwse")
        self.buttons_frame.grid(row=3, column=1, padx=113, sticky="nwe")

    def init_widgets(self):
        self.subtopic_title_label = ttk.Label(self, text="Title", style="Title.TLabel")
        self.subtopic_title_label.grid(row=0, column=1, sticky="ns")

        self.expression_label = ttk.Label(
            self, text="Expression", style="Expression.TLabel"
        )
        self.expression_label.grid(row=1, column=1, sticky="ns")

        self.answer_box = ttk.Frame(self, borderwidth=3, relief="groove")
        for row in range(3):
            self.answer_box.grid_rowconfigure(row, weight=1)

        self.answer_box.grid_columnconfigure(0, weight=1)
        self.answer_box.grid_columnconfigure(1, weight=5)

        ttk.Label(self.answer_box, text="Ціле:").grid(row=0, column=0, sticky="nwse")
        ttk.Label(self.answer_box, text="Чисельник:").grid(
            row=1, column=0, sticky="nwse"
        )
        ttk.Label(self.answer_box, text="Знаменник:").grid(
            row=2, column=0, sticky="nwse"
        )

        self.intenger_input = ttk.Spinbox(
            self.answer_box,
            from_=-50,
            to=50,
            increment=1,
            justify="center",
        )
        self.intenger_input.grid(row=0, column=1, sticky="nwse")

        self.numerator_input = ttk.Spinbox(
            self.answer_box,
            from_=-50,
            to=50,
            increment=1,
            justify="center",
        )
        self.numerator_input.grid(row=1, column=1, sticky="nwse")

        self.denominator_input = ttk.Spinbox(
            self.answer_box,
            from_=-50,
            to=50,
            increment=1,
            justify="center",
        )
        self.denominator_input.grid(row=2, column=1, sticky="nwse")

        self.init_buttons()

        self.answer_box.grid(row=2, column=1, sticky="nwse")

    def reload_subtopic(self):
        self.show(self.topic, self.index)

    def configure_grid(self):
        self.grid(row=0, column=0, sticky="nwse")
        for row in range(4):
            self.grid_rowconfigure(row, weight=1)
        for column in range(3):
            self.grid_columnconfigure(column, weight=1)

    def show(self, topic: Topic, index: int):
        self.configure_grid()

        self.clear_input_boxes()
        self.intenger_input.delete(0, END)
        self.intenger_input.insert(0, "0")

        self.showed = False
        self.topic = topic
        self.subtopics = topic.subtopics
        self.current_subtopic = self.subtopics[index]
        self.index = index

        self.current_exercise = self.current_subtopic.exercises()
        self.result = self.current_exercise.fraction
        self.redused_result = self.result.reduce()
        if self.result == self.redused_result:
            self.result = None

        self.check_button.configure(text="Перевірити")
        self.subtopic_title_label.configure(text=self.current_subtopic.title)
        self.display_expression()

    def _check_value(self, widget: ttk.Spinbox, value: int, ok_color: str):
        if int(widget.get()) != value:
            widget.configure(background="red")
            return False
        widget.configure(background=ok_color)
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

        if len(self.subtopics) <= self.index + 1:
            self.show_main_window()
            return
        self.show(self.topic, self.index + 1)

    def display_expression(self):
        result = ""
        for symbol in self.current_exercise.expression.split(" "):
            if "*" in symbol:
                multiplier, symbol = symbol.split("*")
                result += multiplier
            if "/" in symbol:
                numerator, denominator = symbol.split("/")
                result += unicodeit.replace(f"^{{{numerator}}}/_{{{denominator}}}")
                continue
            result += f" {symbol} "

        self.expression_label.configure(text=result)

    def show_main_window(self):
        self.grid_forget()
        self.previous_state.show()

    def clear_input_boxes(self):
        for widget in (
            self.numerator_input,
            self.intenger_input,
            self.denominator_input,
        ):
            widget.delete(0, END)
            widget.insert(0, "1")
            widget.configure(background="white")
