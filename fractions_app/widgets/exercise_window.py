from PyQt5.QtWidgets import QWidget

from ..ui.exercise_window import Ui_Form
from ..helper import Subtopic


class ExerciseWindow(QWidget):
    def __init__(self, previous_state: QWidget) -> None:
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.hide()

        self.previous_state = previous_state
        self.ui.check_btn.pressed.connect(self.check)
        self.ui.exit_btn.pressed.connect(self.show_select_exercise_window)
        self.ui.try_again_btn.pressed.connect(self.reload_subtopic)

    def reload_subtopic(self):
        self.load_subtopic(self.subtopics, self.index)

    def load_subtopic(self, subtopics: list[Subtopic], index: int):
        self.clear_input_boxes()
        self.subtopics = subtopics
        self.current_subtopic = subtopics[index]
        self.index = index

        self.ui.title.setText(self.current_subtopic.title)
        self.current_exercise = self.current_subtopic.exercises()
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
                    self.ui.intenger_input, self.current_exercise.integer
                ),
                self._check_value(
                    self.ui.numerator_input, self.current_exercise.numerator
                ),
                self._check_value(
                    self.ui.denominator_input, self.current_exercise.denominator
                ),
            )
        ):
            return

    def display_expression(self):
        result = ""
        for symbol in self.current_exercise.expression.split(" "):
            if "/" in symbol:
                numerator, denominator = symbol.split("/")
                result += f"<sup>{numerator}</sup>/<sub>{denominator}</sub>"
                continue
            result += f" {symbol} "

        self.ui.expression.setText(result)

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
