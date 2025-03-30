from functools import partial
from tkinter import ttk

from fractions_app.windows.window import Window
from fractions_app.windows.exercise_window import ExerciseWindow
from fractions_app.topic_handler import TopicHandler
from fractions_app.helper import Topic


class TopicWindow(Window):
    ROWS = 2
    COLUMNS = 2

    def init(self) -> None:
        self.exercise_window = ExerciseWindow(self)
        self.topic_frame = ttk.Frame(self)
        self.topic_frame.grid(row=0, column=0, rowspan=4, sticky="nwse")

        self.subtopic_frame = ttk.Frame(self, borderwidth=3, relief="groove")
        self.subtopic_frame.grid(
            row=0, column=1, rowspan=4, pady=5, padx=5, sticky="nwse"
        )

    def _load_topics(self) -> None:
        for row, widget in enumerate(list(self.topic_frame.children.values())):
            widget.destroy()

        ttk.Button(self.topic_frame, text="Вийти", command=self.show_main_window).grid(
            row=0, column=0, pady=5
        )

        for row, topic in enumerate(TopicHandler().get_topics(), 1):
            button = ttk.Button(
                self.topic_frame,
                text=topic.title,
                command=partial(self._show_subtopics, topic),
            )
            self.topic_frame.grid_rowconfigure(row, weight=1)
            button.grid(row=row, column=0, pady=5, padx=15, sticky="nwse")

    def _show_subtopics(self, topic: Topic) -> None:
        for row, widget in enumerate(list(self.subtopic_frame.children.values())):
            widget.destroy()
            self.subtopic_frame.grid_rowconfigure(row, weight=0)

        self.subtopic_frame.grid_columnconfigure(0, weight=1)
        for row, subtopic in enumerate(topic.subtopics):
            button = ttk.Button(
                self.subtopic_frame,
                text=subtopic.title,
                command=partial(self.show_exercise, topic, row),
            )
            self.subtopic_frame.grid_rowconfigure(row, weight=1)
            button.grid(row=row, column=0, pady=5, padx=15, sticky="nwse")

    def show_exercise(self, topic: Topic, index: int) -> None:
        self.grid_forget()
        self.exercise_window.show(topic, index)

    def show(self) -> None:
        super().show()

        for index in range(self.COLUMNS):
            self.grid_columnconfigure(index, weight=index)

        self._load_topics()

    def show_main_window(self) -> None:
        self.grid_forget()
        self.previous_state.show()
