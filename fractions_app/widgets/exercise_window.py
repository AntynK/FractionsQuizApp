from PyQt5.QtWidgets import QWidget, QMessageBox

from ..ui.exercise_window import Ui_Form
from ..helper import Subtopic, Fraction


class ExerciseWindow(QWidget):
    def __init__(self, previous_state: QWidget) -> None:
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.hide()

        self.previous_state = previous_state
        self.ui.check_btn.pressed.connect(self.check_input)
        self.ui.exit_btn.pressed.connect(self.show_select_exercise_window)
        self.ui.try_again_btn.pressed.connect(self.reload_subtopic)

    def reload_subtopic(self):
        self.load_subtopic(self.subtopics, self.index)

    def load_subtopic(self, subtopics: list[Subtopic], index: int):
        self.clear_input_boxes()
        self.showed = False
        self.subtopics = subtopics
        self.current_subtopic = subtopics[index]
        self.index = index

        self.ui.title.setText(self.current_subtopic.title)
        self.current_exercise = self.current_subtopic.exercises()
        self.result = self.current_exercise.fraction
        self.redused_result = self.result.reduce()
        if self.result == self.redused_result:
            self.result = None

        self.display_expression()

    def _check_value(self, widget, value: int, ok_color: str):
        if widget.value() != value:
            widget.setStyleSheet("background-color:red;")
            return False
        widget.setStyleSheet(f"background-color: {ok_color};")
        return True

    def compare_user_input_with_fraction(
        self, fraction: Fraction, ok_color="#4a964a"
    ) -> bool:
        return all(
            (
                self._check_value(self.ui.intenger_input, fraction.integer, ok_color),
                self._check_value(
                    self.ui.numerator_input, fraction.numerator, ok_color
                ),
                self._check_value(
                    self.ui.denominator_input, fraction.denominator, ok_color
                ),
            )
        )

    def check_input(self):
        if self.result is not None:
            if self.compare_user_input_with_fraction(self.result, ok_color="orange"):
                QMessageBox.information(self, "Ще не все", "Дріб можна скоротити!")
                return

        if not self.compare_user_input_with_fraction(self.redused_result):
            return

        self.show_next_exercise()

    def show_next_exercise(self):
        if not self.showed:
            self.showed = True
            return

        if len(self.subtopics) >= self.index:
            self.show_select_exercise_window()
            return
        self.load_subtopic(self.subtopics, self.index + 1)

    # def show_previous_exercise(self):
    #     if self.index <= 0:
    #         self.show_select_exercise_window()
    #         return
    #     self.load_subtopic(self.subtopics, self.index - 1)

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
