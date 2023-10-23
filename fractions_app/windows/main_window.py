from functools import partial
import tkinter as tk

from .select_exercise_window import SelectExerciseWindow
from ..topic_handler import TopicHandler


class MainWindow(tk.Frame):
    def __init__(self, master) -> None:
        super().__init__(master)

        self.select_subtopic_window = SelectExerciseWindow(self)
        self.load_topics()

    def load_topics(self):
        for topic in TopicHandler().get_topics():
            button = tk.Button(
                self, text=topic.title, command=partial(self.show_subtopics, topic)
            )
            button.pack()

    def show_subtopics(self, topic):
        self.pack_forget()
        self.select_subtopic_window.show(topic)
