from typing import Union
from functools import partial
from tkinter import ttk, END
import tkinter.messagebox as messagebox

from ..helper import Topic, ResizingCanvas
from ..math import Fraction


class ExerciseWindow(ttk.Frame):
    def __init__(self, previous_state) -> None:
        super().__init__()

        self.previous_state = previous_state
        self.validate_enetered_text = (self.register(self.validate_spinbox), "%P")

        self.init_widgets()

    def validate_spinbox(self, text: str):
        if not text.isdigit() and len(text) != 0:
            self.bell()
            return False
        return True

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

    def spinbox_focus_in(self, event, spinbox: ttk.Spinbox):
        spinbox.select_clear()
        spinbox.select_range(0, END)

    def spinbox_return_presed(self, event, spinbox: ttk.Spinbox):
        spinbox.select_clear()
        self.focus()

    def spinbox_check_value(self, event, spinbox: ttk.Spinbox):
        if spinbox.get() == "":
            spinbox.insert(0, "1")

        self.spinbox_return_presed(event, spinbox)

    def init_spinboxes_events(self):
        for spinbox in (
            self.numerator_input,
            self.denominator_input,
            self.intenger_input,
        ):
            spinbox.bind("<FocusIn>", partial(self.spinbox_focus_in, spinbox=spinbox))
            spinbox.bind(
                "<FocusOut>", partial(self.spinbox_check_value, spinbox=spinbox)
            )
            spinbox.bind(
                "<Return>", partial(self.spinbox_return_presed, spinbox=spinbox)
            )

    def init_widgets(self):
        self.subtopic_title_label = ttk.Label(self, text="Title", style="Title.TLabel")
        self.subtopic_title_label.grid(row=0, column=1, sticky="ns")

        self.expression_canvas = ResizingCanvas(self)
        self.expression_canvas.grid(row=1, column=1, sticky="nwse")
        self.bind("<Configure>", self.display_expression)

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

        self.init_buttons()
        self.init_spinboxes_events()
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

        self.current_exercise = self.current_subtopic.generate_exercise()
        self.result = self.current_exercise.result
        self.redused_result = self.result.reduce()
        if self.result == self.redused_result:
            self.result = None

        self.check_button.configure(text="Перевірити")
        self.subtopic_title_label.configure(text=self.current_subtopic.title)
        self.display_expression()

    def _check_value(self, widget: ttk.Spinbox, value: int, ok_color: str):
        style = ttk.Style()
        if int(widget.get()) != value:
            style.configure(widget["style"], fieldbackground="red")
            return False

        style.configure(widget["style"], fieldbackground=ok_color)
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
                if int(self.numerator_input.get()) >= int(self.denominator_input.get()):
                    messagebox.showerror(
                        title="Помилка", message="Потрібно виділити цілу частину!"
                    )
                    return
                messagebox.showerror(title="Помилка", message="Дріб можна скоротити!")
                return

        if not self.compare_user_input_with_fraction(self.redused_result):
            self.check_button.configure(text="Перевірити")
            self.showed = False
            return

        self.show_next_exercise()

    def show_next_exercise(self):
        if not self.showed:
            messagebox.showinfo("Чудово", "Все правильно молодець!")
            self.check_button.configure(text="Наступне")
            self.showed = True
            return

        if len(self.subtopics) <= self.index + 1:
            self.show_main_window()
            return
        self.show(self.topic, self.index + 1)

    def display_expression(self, e=None):
        CHARACTER_SIZE = 30
        self.expression_canvas.delete("all")
        x = 100
        y = 30
        offset = self._display_operand(self.current_exercise.operand_1, x, y)
        x += offset + CHARACTER_SIZE
        self._display_text(self.current_exercise.operation, x, y)
        x += CHARACTER_SIZE
        offset = self._display_operand(self.current_exercise.operand_2, x, y)
        x += offset + CHARACTER_SIZE
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
        x_offset = 0
        if operand.integer != 0:
            self._display_text(operand.integer, x, y, bigger=True)
            x_offset = 25

        self._display_text(operand.numerator, x + x_offset, y - 5)
        self.expression_canvas.create_line(x - 20 + x_offset, y, x + 20 + x_offset, y)
        self._display_text(operand.denominator, x + x_offset, y + 5)
        return x_offset

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
            ttk.Style().configure(widget["style"], fieldbackground="white")
