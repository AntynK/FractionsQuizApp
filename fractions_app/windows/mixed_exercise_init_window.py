from tkinter import ttk
from tkinter.font import Font

from fractions_app.helper import Levels, get_font_scale
from fractions_app.windows.window import Window
from fractions_app.widgets import Spinbox
from fractions_app.windows.mixed_exercise_window import MixedExerciseWindow


class MixedExerciseInitWindow(Window):
    ROWS = 4
    COLUMNS = 2

    def init(self) -> None:
        self.mixed_exercise_window = MixedExerciseWindow(self)
        ttk.Label(
            self,
            text="Налаштування мішаних завдань",
            style="Title.TLabel",
            justify="center",
        ).grid(row=0, column=0, columnspan=2)
        ttk.Label(self, text="Рівень складності").grid(row=1, column=0)
        self.combo = ttk.Combobox(
            self, state="readonly", values=[value for value in Levels]
        )
        self.combo.current(0)
        self.combo.grid(row=1, column=1)

        ttk.Label(self, text="Кількість завдань").grid(row=2, column=0)

        self.exercise_count = Spinbox(self, width=4, from_=10, to=50)
        self.exercise_count.grid(row=2, column=1)

        ttk.Button(self, text="Назад", command=self.show_previous_window).grid(
            row=3, column=0
        )
        ttk.Button(
            self, text="Розпочати", command=self.show_mixed_exercise_window
        ).grid(row=3, column=1)

    def show_mixed_exercise_window(self) -> None:
        self.grid_forget()
        self.mixed_exercise_window.show(
            Levels(self.combo.get()), self.exercise_count.value
        )

    def on_resize(self, *unused) -> None:
        width, height = self.winfo_width(), self.winfo_height()
        self.exercise_count.on_resize(width, height)

        scale = get_font_scale(width, height)
        self.combo.configure(
            font=Font(family="Times New Roman", size=round(scale * 1.5))
        )
