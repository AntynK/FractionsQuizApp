from PyQt5.QtWidgets import QMainWindow

from .ui.main_window import Ui_MainWindow
from .widgets.exercise_button import ExerciseButton
from .widgets.select_exercise_window import SelectExerciseWindow


from .constants import EXERCISES_DIR
from .exercises_group import ExercisesGroup


class AppMainWindow:
    def __init__(self) -> None:
        self.window = QMainWindow()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.select_exercise_window = SelectExerciseWindow(
            self.ui.frame
        )

        self.select_exercise_window.add_to_layout(self.ui.verticalLayout)
        self.load_exercises()

    def load_exercises(self):
        scroll_area_layout = self.ui.scrollAreaWidgetContents.layout()
        for filename in EXERCISES_DIR.glob("*.json"):
            group = ExercisesGroup(filename.stem)
            scroll_area_layout.addWidget(
                ExerciseButton(group.name, self.show_exercises, group)
            )

    def show_exercises(self, group: ExercisesGroup):
        self.ui.frame.hide()
        self.select_exercise_window.add_group(group)
        self.select_exercise_window.show()

    def show(self):
        self.window.show()


# cx_Freeze
