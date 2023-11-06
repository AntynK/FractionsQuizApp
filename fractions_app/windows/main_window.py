from functools import partial
import tkinter as tk

from .select_exercise_window import SelectExerciseWindow
from ..topic_handler import TopicHandler


class MainWindow(tk.Frame):
    def __init__(self, master: tk.Tk) -> None:
        super().__init__(master)

        self.select_subtopic_window = SelectExerciseWindow(self)

        self.load_topics()

    def load_topics(self):
        for row, topic in enumerate(TopicHandler().get_topics()):
            button = tk.Button(
                self,
                text=topic.title,
                command=partial(self.show_subtopics, topic),
            )
            self.grid_rowconfigure(row, weight=1)
            button.grid(row=row, column=0, pady=20, padx=40, sticky="nwse")

    def show_subtopics(self, topic):
        self.grid_forget()
        self.select_subtopic_window.show(topic)

    def show(self):
        self.grid(row=0, column=0, sticky="nwse")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
