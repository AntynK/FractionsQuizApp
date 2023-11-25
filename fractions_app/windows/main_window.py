from functools import partial

from tkinter import ttk, Tk

from .exercise_window import ExerciseWindow
from ..topic_handler import TopicHandler
from ..helper import Topic


class MainWindow(ttk.Frame):
    def __init__(self, master: Tk) -> None:
        super().__init__(master)

        self.exercise_window = ExerciseWindow(self)

        self.subtopic_frame = ttk.Frame(self, borderwidth=3, relief="groove")
        self.subtopic_frame.grid(
            row=0, column=1, rowspan=4, pady=5, padx=5, sticky="nwse"
        )

        self._load_topics()

    def _load_topics(self):
        for row, topic in enumerate(TopicHandler().get_topics()):
            button = ttk.Button(
                self,
                text=topic.title,
                command=partial(self._show_subtopics, topic),
            )
            self.grid_rowconfigure(row, weight=1)
            button.grid(row=row, column=0, pady=5, padx=15, sticky="nwse")

    def _show_subtopics(self, topic: Topic):
        for widget in list(self.subtopic_frame.children.values()):
            widget.destroy()

        self.subtopic_frame.grid_columnconfigure(0, weight=1)
        for row, subtopic in enumerate(topic.subtopics):
            button = ttk.Button(
                self.subtopic_frame,
                text=subtopic.title,
                command=partial(self.show_exercise, topic, row),
            )
            self.subtopic_frame.grid_rowconfigure(row, weight=1)
            button.grid(row=row, column=0, pady=5, padx=15, sticky="nwse")

    def show_exercise(self, topic: Topic, index: int):
        self.grid_forget()
        self.exercise_window.show(topic, index)

    def show(self):
        self.grid(row=0, column=0, sticky="nwse")
        for column in range(2):
            self.grid_columnconfigure(column, weight=1)

        self.grid_columnconfigure(1, weight=5)
