from PyQt5.QtWidgets import QWidget, QLayout

from ..ui.select_exercise_window import Ui_Form
from ..widgets.exercise_button import ExerciseButton
from .exercise_window import ExerciseWindow
from ..helper import Topic, Subtopic


class SelectExerciseWindow(QWidget):
    def __init__(self, previous_state: QWidget) -> None:
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.hide()

        self.previous_state = previous_state
        self.topic = None
        self.exercise_window = ExerciseWindow(self)
        self.ui.back_btn.pressed.connect(self.show_main_window)

    def add_to_layout(self, layout: QLayout):
        layout.addWidget(self)
        layout.addWidget(self.exercise_window)

    def add_topic(self, topic: Topic):
        if self.topic is None:
            self.topic = topic
            self.load_subtopics()
            self.ui.title.setText(self.topic.title)

    def load_subtopics(self):
        if self.topic is None:
            return
        scroll_area_layout = self.ui.scrollAreaWidgetContents.layout()
        for index, subtopic in enumerate(self.topic.subtopics):
            scroll_area_layout.addWidget(
                ExerciseButton(
                    subtopic.title, self.show_exercise, self.topic.subtopics, index
                )
            )

    def show_exercise(self, subtopics: list[Subtopic], index: int):
        self.hide()
        self.exercise_window.load_subtopic(subtopics, index)
        self.exercise_window.show()

    def show_main_window(self):
        self.hide()
        self.previous_state.show()
