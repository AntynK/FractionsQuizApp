from tkinter import ttk

from fractions_app.helper import Level
from fractions_app.windows.window import Window
from fractions_app.widgets import ExerciseBox
from fractions_app.topic_handler import TopicHandler


class MixedExerciseWindow(Window):
    ROWS = 2
    COLUMNS = 3

    def init(self) -> None:
        self.title_label = ttk.Label(self, text="Title")
        self.title_label.grid(row=0, column=1, sticky="news")

        self.exercise_box = ExerciseBox(self, self.show_previous_window, print)
        self.exercise_box.grid(row=1, column=0, columnspan=3, sticky="news")
        
        self.bind("<Configure>", self.on_resize)

    def on_resize(self, *unused) -> None:
        self.exercise_box.on_resize(self.winfo_width(), self.winfo_height())

    def show(self, level: Level, exercise_count: int) -> None:
        super().show()
        self.level = level
        self.exercise_count = exercise_count
        self.exercises = TopicHandler().get_subtopics_by_level(level)
        self.exercise_box.display_exercise(self.exercises[0].generate_exercise())
