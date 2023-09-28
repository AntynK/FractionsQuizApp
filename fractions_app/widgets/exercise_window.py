import random

from PyQt5.QtWidgets import QWidget, QMessageBox

from ..ui.exercise_window import Ui_Form
from ..exercise import Exercise


class ExerciseWindow(QWidget):
    def __init__(self, previous_state: QWidget) -> None:
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.hide()

        self.previous_state = previous_state
        self.ui.check_btn.pressed.connect(self.check)
        self.ui.exit_btn.pressed.connect(self.show_select_exercise_window)
        self.ui.try_again_btn.pressed.connect(self.reload_exercise)

    def reload_exercise(self):
        self.load_exercise(self.expressions, self.ui.title.text())

    def load_exercise(self, expressions: list[Exercise], title: str):
        self.clear_input_boxes()

        self.ui.title.setText(title)
        self.expressions = expressions
        if len(expressions) != 0:
            self.current_expression = random.choice(expressions)
            self.display_expression()

    def _check_value(self, widget, value):
        if widget.value() != value:
            widget.setStyleSheet("background-color:red;")
            return False
        widget.setStyleSheet("background-color: #4a964a;")
        return True

    def check(self):
        if not all(
            (
                self._check_value(
                    self.ui.intenger_input, self.current_expression.integer
                ),
                self._check_value(
                    self.ui.numerator_input, self.current_expression.numerator
                ),
                self._check_value(
                    self.ui.denominator_input, self.current_expression.denominator
                ),
            )
        ):
            return

    def display_expression(self):
        self.ui.expression.setText(self.current_expression.expression)

    def show_select_exercise_window(self):
        self.hide()
        self.previous_state.show()

    def clear_input_boxes(self):
        for element in (
            self.ui.numerator_input,
            self.ui.intenger_input,
            self.ui.denominator_input,
        ):
            element.setValue(0)
            element.setStyleSheet("background-color: none;")
