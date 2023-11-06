from functools import partial
import tkinter as tk

from .exercise_window import ExerciseWindow
from ..helper import Topic, Subtopic


class SelectExerciseWindow(tk.Frame):
    def __init__(self, previous_state) -> None:
        super().__init__()

        self.previous_state = previous_state
        self.topic = None
        self.exercise_window = ExerciseWindow(self)

    def load_subtopics(self):
        if self.topic is None:
            return

        for widget in list(self.children.values()):
            widget.destroy()

        subtopic_index = 0
        for subtopic_index, subtopic in enumerate(self.topic.subtopics):
            button = tk.Button(
                self,
                text=subtopic.title,
                command=partial(self.show_exercise, self.topic, subtopic_index),
            )
            self.grid_rowconfigure(subtopic_index, weight=1)
            button.grid(row=subtopic_index, column=0, pady=20, padx=40, sticky="nwse")

        tk.Button(self, text="Вийти", command=self.show_main_window).grid(
            row=subtopic_index + 1, column=0, pady=20, padx=40, sticky="nwse"
        )

    def show_exercise(self, topic: Topic, index: int):
        self.grid_forget()
        self.exercise_window.show(topic, index)

    def show_main_window(self):
        self.grid_forget()
        self.previous_state.show()

    def show(self, topic: Topic):
        self.topic = topic
        self.load_subtopics()
        
        self.grid(row=0, column=0, sticky="nwse")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
