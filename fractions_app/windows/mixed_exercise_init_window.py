from tkinter import ttk

from fractions_app.helper import Level
from fractions_app.windows.window import Window
from fractions_app.widgets import Spinbox
from fractions_app.windows.mixed_exercise_window import MixedExerciseWindow


class MixedExerciseInitWindow(Window):
    ROWS = 3
    COLUMNS = 2

    def init(self) -> None:
        self.mixed_exercise_window = MixedExerciseWindow(self)

        ttk.Label(self, text="Рівень складності").grid(row=0, column=0)
        self.combo = ttk.Combobox(self, values=["5 клас", "6 клас"])
        self.combo.grid(row=0, column=1)

        ttk.Label(self, text="Кількість завдань").grid(row=1, column=0)
        self.exercise_count = Spinbox(self, width=4, from_=10, to=50)
        self.exercise_count.grid(row=1, column=1)

        ttk.Button(self, text="Назад", command=self.show_previous_window).grid(
            row=2, column=0
        )
        ttk.Button(
            self, text="Розпочати", command=self.show_mixed_exercise_window
        ).grid(row=2, column=1)

    def show_mixed_exercise_window(self) -> None:
        self.grid_forget()
        self.mixed_exercise_window.show(Level.GRADE_5, self.exercise_count.value)
