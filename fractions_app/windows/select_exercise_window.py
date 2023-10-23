from functools import partial
import tkinter as tk

from .exercise_window import ExerciseWindow
from ..helper import Topic, Subtopic


class SelectExerciseWindow(tk.Frame):
    def __init__(self, previous_state: tk.Frame) -> None:
        super().__init__()

        self.pack_configure(pady=20)
        self.previous_state = previous_state
        self.topic = None
        self.exercise_window = ExerciseWindow(self)

    def load_subtopics(self):
        if self.topic is None:
            return
        for index, subtopic in enumerate(self.topic.subtopics):
            button = tk.Button(
                self,
                text=subtopic.title,
                command=partial(self.show_exercise, self.topic.subtopics, index),
            )
            button.pack(pady=2)

    def show_exercise(self, subtopics: list[Subtopic], index: int):
        self.pack_forget()
        self.exercise_window.load_subtopic(subtopics, index)
        self.exercise_window.pack()

    def show_main_window(self):
        self.pack_forget()
        self.previous_state.pack()

    def show(self, topic: Topic):
        self.topic = topic
        self.load_subtopics()
        self.pack()
