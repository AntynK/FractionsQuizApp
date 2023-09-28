from PyQt5.QtWidgets import QWidget

from ..ui.select_exercise_window import Ui_Form
from ..exercises_group import ExercisesGroup
from .exercise_window import ExerciseWindow


class SelectExerciseWindow(QWidget):
    def __init__(self, previous_state: QWidget) -> None:
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.hide()

        self.previous_state = previous_state
        self.group = None
        self.exercise_window = ExerciseWindow(self)
        self.ui.back_btn.pressed.connect(self.show_main_window)

    def add_to_layout(self, layout):
        layout.addWidget(self)
        layout.addWidget(self.exercise_window)
        
    def add_group(self, group: ExercisesGroup):
        if self.group is None:
            self.group = group
            self.group.parse_file(self.show_exercise)
            self.load_exercises()
            self.ui.title.setText(self.group.name)

    def load_exercises(self):
        if self.group is None:
            return
        scroll_area_layout = self.ui.scrollAreaWidgetContents.layout()
        for exercise in self.group.children:
            scroll_area_layout.addWidget(exercise)

    def show_exercise(self, exercise: list, title:str):
        self.hide()
        self.exercise_window.load_exercise(exercise, title)
        self.exercise_window.show()

    def show_main_window(self):
        self.hide()
        self.previous_state.show()
