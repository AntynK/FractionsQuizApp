from tkinter import ttk

from fractions_app.helper import ExerciseResult
from fractions_app.windows.window import Window


class MixedExerciseResultWindow(Window):
    ROWS = 7
    COLUMNS = 1

    def init(self) -> None:
        ttk.Label(self, text="Результати", style="Title.TLabel", justify="center").grid(row=0, column=0)
        self.correct_label = ttk.Label(self, text="Правильних")
        self.correct_label.grid(row=1, column=0)

        self.failed_label = ttk.Label(self, text="Неправильних")
        self.failed_label.grid(row=2, column=0)

        self.skipped_label = ttk.Label(self, text="Пропущених")
        self.skipped_label.grid(row=3, column=0)

        self.level_label = ttk.Label(self, text="Рівень")
        self.level_label.grid(row=4, column=0)

        self.result_label = ttk.Label(self, text="Результат")
        self.result_label.grid(row=5, column=0)

        ttk.Button(self, text="Вийти", command=self.show_previous_window).grid(
            row=6, column=0
        )

    def show(self, results: ExerciseResult) -> None:
        super().show()
        self.correct_label.configure(text=f"Правильних: {results.correct_answers}")
        self.failed_label.configure(text=f"Неправильних: {results.failed_answers}")
        self.skipped_label.configure(text=f"Пропущених: {results.skipped_exercises}")
        self.level_label.configure(text=f"Рівень: {results.level.value}")
        self.result_label.configure(text=f"Результат: {results.calculate_mark()} балів")
