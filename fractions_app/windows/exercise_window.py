from tkinter import ttk

from fractions_app.helper import Topic
from fractions_app.math import Fraction


from fractions_app.widgets.exercise_box import ExerciseBox


class ExerciseWindow(ttk.Frame):
    def __init__(self, previous_state) -> None:
        super().__init__()

        self.previous_state = previous_state
        self.user_input = Fraction(1, 1)

        self._init_widgets()

    def _init_widgets(self):
        self.subtopic_title_label = ttk.Label(self, text="Title", style="Title.TLabel")
        self.subtopic_title_label.grid(row=0, column=1, sticky="ns")

        self.exercise_box = ExerciseBox(
            self, self.show_topic_window, self.show_next_exercise, self.reload_subtopic
        )
        self.exercise_box.grid(row=1, column=0, sticky="nwse", columnspan=3, padx=10)
        self.bind("<Configure>", self.on_resize)

    def on_resize(self, *unused) -> None:
        self.exercise_box.on_resize(self.winfo_width(), self.winfo_height())

    def show_next_exercise(self) -> None:
        if len(self.topic.subtopics) <= self.subtopic_index + 1:
            self.show_topic_window()
            return
        self.show(self.topic, self.subtopic_index + 1)

    def show_topic_window(self) -> None:
        self.grid_forget()
        self.previous_state.show()

    def reload_subtopic(self) -> None:
        self.show(self.topic, self.subtopic_index)

    def show(self, topic: Topic, subtopic_index: int) -> None:
        self._configure_grid()

        self.topic = topic
        current_subtopic = topic.subtopics[subtopic_index]
        self.subtopic_index = subtopic_index

        self.current_exercise = current_subtopic.generate_exercise()

        self.subtopic_title_label.configure(text=current_subtopic.title)
        self.exercise_box.display_exercise(self.current_exercise)

    def _configure_grid(self) -> None:
        self.grid(row=0, column=0, sticky="nwse")
        for row in range(2):
            self.grid_rowconfigure(row, weight=1)
        for column in range(3):
            self.grid_columnconfigure(column, weight=1)
