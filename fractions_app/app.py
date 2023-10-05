from PyQt5.QtWidgets import QMainWindow

from .ui.main_window import Ui_MainWindow
from .widgets.exercise_button import ExerciseButton
from .widgets.select_exercise_window import SelectExerciseWindow
from .topic_handler import TopicHandler
from .helper import Topic


class AppMainWindow:
    def __init__(self) -> None:
        self.window = QMainWindow()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.select_exercise_window = SelectExerciseWindow(self.ui.frame)

        self.select_exercise_window.add_to_layout(self.ui.verticalLayout)

        self.load_exercises()

    def load_exercises(self):
        scroll_area_layout = self.ui.scrollAreaWidgetContents.layout()
        for topic in TopicHandler().get_topics():
            scroll_area_layout.addWidget(
                ExerciseButton(topic.title, self.show_substopic, topic)
            )

    def show_substopic(self, topic: Topic):
        self.ui.frame.hide()
        self.select_exercise_window.add_topic(topic)
        self.select_exercise_window.show()

    def show(self):
        self.window.show()
