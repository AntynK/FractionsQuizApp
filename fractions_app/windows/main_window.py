from tkinter import ttk

from fractions_app.constants import PROGRAM_TITLE, VERSION, AUTHOR
from fractions_app.windows.topic_window import TopicWindow
from fractions_app.windows.window import Window
from fractions_app.windows.mixed_exercise_init_window import MixedExerciseInitWindow
from fractions_app.widgets import make_grid


class MainWindow(Window):
    ROWS = 3
    COLUMNS = 3

    def init(self) -> None:
        self.topic_window = TopicWindow(self)
        self.exercise_init_window = MixedExerciseInitWindow(self)

        ttk.Label(
            self, text=PROGRAM_TITLE, style="Title.TLabel", justify="center"
        ).grid(row=0, column=1, sticky="nwse")

        self.buttons_frame = ttk.Frame(self)
        make_grid(self.buttons_frame, 1, 2)
        ttk.Button(
            self.buttons_frame,
            text="Завдання за темами",
            command=self.show_topic_window,
        ).grid(row=0, column=0, sticky="nwse")
        ttk.Button(
            self.buttons_frame, text="Мішані завдання", command=self.show_exercise_init_window
        ).grid(row=0, column=1, sticky="nwse")

        self.buttons_frame.grid(row=1, column=1, sticky="news")

        ttk.Label(self, text=f"Версія: {VERSION}\n\n©{AUTHOR}").grid(
            row=2, column=1, sticky="nwse"
        )

    def show_topic_window(self) -> None:
        self.grid_forget()
        self.topic_window.show()

    def show_exercise_init_window(self) -> None:
        self.grid_forget()
        self.exercise_init_window.show()
