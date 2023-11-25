from typing import Union, Literal
from functools import partial

from tkinter import ttk, END
import tkinter.messagebox as messagebox

from ..helper import Topic, ResizingCanvas
from ..math import Fraction


class ExerciseWindow(ttk.Frame):
    def __init__(self, previous_state) -> None:
        super().__init__()

        self.previous_state = previous_state
        self.validate_enetered_text = (self.register(self._validate_spinbox_text), "%P")

        self._init_widgets()

    def _validate_spinbox_text(self, text: str):
        if not text.isdigit() and len(text) != 0:
            self.bell()
            return False
        return True

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

    def _spinbox_focus_in(self, event, spinbox: ttk.Spinbox):
        spinbox.select_clear()
        spinbox.select_range(0, END)

    def _spinbox_return_presed(self, event, spinbox: ttk.Spinbox):
        spinbox.select_clear()
        self.focus()

    def _spinbox_check_value(self, event, spinbox: ttk.Spinbox):
        if spinbox.get() == "":
            spinbox.insert(0, "1")

        self._spinbox_return_presed(event, spinbox)

    def _init_spinboxes_events(self):
        for spinbox in (
            self.numerator_input,
            self.denominator_input,
            self.intenger_input,
        ):
            spinbox.bind("<FocusIn>", partial(self._spinbox_focus_in, spinbox=spinbox))
            spinbox.bind(
                "<FocusOut>", partial(self._spinbox_check_value, spinbox=spinbox)
            )
            spinbox.bind(
                "<Return>", partial(self._spinbox_return_presed, spinbox=spinbox)
            )

    def _init_widgets(self):
        self.subtopic_title_label = ttk.Label(self, text="Title", style="Title.TLabel")
        self.subtopic_title_label.grid(row=0, column=1, sticky="ns")

        self.expression_canvas = ResizingCanvas(self)
        self.expression_canvas.grid(row=1, column=1, sticky="nwse")
        self.bind("<Configure>", self.on_resize)

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
            validate="all",
            font=("Times New Roman", 40),
            validatecommand=self.validate_enetered_text,
            justify="center",
            style="Intenger.TSpinbox",
        )
        self.intenger_input.grid(row=0, column=1, sticky="nwse")

        self.numerator_input = ttk.Spinbox(
            self.answer_box,
            validate="all",
            font=("Times New Roman", 40),
            validatecommand=self.validate_enetered_text,
            justify="center",
            style="Numerator.TSpinbox",
        )
        self.numerator_input.grid(row=1, column=1, sticky="nwse")

        self.denominator_input = ttk.Spinbox(
            self.answer_box,
            validate="all",
            font=("Times New Roman", 40),
            validatecommand=self.validate_enetered_text,
            justify="center",
            style="Denominator.TSpinbox",
        )
        self.denominator_input.grid(row=2, column=1, sticky="nwse")

        self._init_buttons()
        self._init_spinboxes_events()
        self.answer_box.grid(row=2, column=1, sticky="nwse")

    def reload_subtopic(self):
        self.show(self.topic, self.index)

    def _configure_grid(self):
        self.grid(row=0, column=0, sticky="nwse")
        for row in range(4):
            self.grid_rowconfigure(row, weight=1)
        for column in range(3):
            self.grid_columnconfigure(column, weight=1)

    def on_resize(self, e):
        self._display_expression()
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
        self.result = self.current_exercise.result
        self.redused_result = self.result.reduce()
        if self.result == self.redused_result:
            self.result = None

        self.check_button.configure(text="Перевірити")
        self.subtopic_title_label.configure(text=self.current_subtopic.title)
        self._display_expression()

    def _update_filedbackgound(self, widget: ttk.Spinbox, color: str):
        ttk.Style().configure(widget["style"], fieldbackground=color)

    def _check_value(self, widget: ttk.Spinbox, value: int):
        return int(widget.get()) == value

    def _compare_user_input_with_fraction(
        self, fraction: Fraction
    ) -> tuple[bool, bool, bool]:
        return (
            self._check_value(self.intenger_input, fraction.integer),
            self._check_value(self.numerator_input, fraction.numerator),
            self._check_value(self.denominator_input, fraction.denominator),
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
            self._update_filedbackgound(widget, default_color)
            if answer:
                self._update_filedbackgound(widget, ok_color)

    def show_message(
        self, title: str, message: str, msg_type: Literal["error", "info"]
    ):
        self._update_spinboxes_bg((True, True, True), "white")
        if msg_type == "error":
            messagebox.showerror(title=title, message=message)
        else:
            messagebox.showinfo(title=title, message=message)

    def check_user_input(self):
        if self.result is not None:
            user_answer = self._compare_user_input_with_fraction(self.result)
            if all(user_answer):
                if int(self.numerator_input.get()) > int(self.denominator_input.get()):
                    self.show_message(
                        title="Помилка",
                        message="Потрібно виділити цілу частину!",
                        msg_type="error",
                    )
                    self._update_spinboxes_bg(user_answer, "orange")
                    self._update_filedbackgound(self.denominator_input, "green")
                    return False
                self.show_message(
                    title="Помилка", message="Дріб можна скоротити!", msg_type="error"
                )
                self._update_spinboxes_bg(user_answer, "orange")
                return False

        user_answer = self._compare_user_input_with_fraction(self.redused_result)
        self._update_spinboxes_bg(user_answer, "green")
        if not all(user_answer):
            self.check_button.configure(text="Перевірити")
            self.showed = False
            return False
        return True

    def show_next_exercise(self):
        if not self.check_user_input():
            return

        if not self.showed:
            self.show_message(
                title="Чудово", message="Все правильно молодець!", msg_type="info"
            )
            self._update_spinboxes_bg((True, True, True), "green")
            self.check_button.configure(text="Наступне")
            self.showed = True
            return

        if len(self.subtopics) <= self.index + 1:
            self.show_main_window()
            return
        self.show(self.topic, self.index + 1)

    def _display_expression(self, e=None):
        CHARACTER_SIZE = 30
        self.expression_canvas.delete("all")
        x = 100
        y = 30
        offset = self._display_operand(self.current_exercise.operand_1, x, y)
        x += CHARACTER_SIZE - offset
        self._display_text(self.current_exercise.operation, x, y)
        x += CHARACTER_SIZE + offset
        self._display_operand(self.current_exercise.operand_2, x, y)
        x += CHARACTER_SIZE - offset
        self._display_text("=", x, y, bigger=True)
        x += 10
        self._display_text("?", x, y, bigger=True)
        self.expression_canvas.on_resize()

    def _display_text(
        self, text: Union[float, str], x: int, y: int, bigger: bool = True
    ):
        font = ("Times New Roman", 20) if bigger else ("Times New Roman", 15)

        self.expression_canvas.create_text(
            x,
            y,
            text=text,
            fill="black",
            font=font,
        )

    def _display_operand(self, operand: Union[int, Fraction], x: int, y: int):
        if isinstance(operand, int):
            self._display_text(operand, x, y)
            return 0
        offset = 0
        if operand.integer != 0:
            offset = 20
            self._display_text(operand.integer, x - 20 - offset, y, bigger=True)

        self._display_text(operand.numerator, x - offset, y - 5)
        self.expression_canvas.create_line(x - 15 - offset, y, x + 15 - offset, y)
        self._display_text(operand.denominator, x - offset, y + 5)
        return offset

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
            self._update_filedbackgound(widget, "white")
