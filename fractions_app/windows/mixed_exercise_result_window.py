from tkinter import ttk

from fractions_app.helper import ExerciseResult
from fractions_app.windows.window import Window
from fractions_app.widgets import UserProgressDiagram


class MixedExerciseResultWindow(Window):
    ROWS = 5
    COLUMNS = 1

    def init(self) -> None:
        ttk.Label(self, text="Результати", style="Title.TLabel", justify="center").grid(
            row=0, column=0
        )
        self.user_diagram = UserProgressDiagram(self)
        self.user_diagram.grid(row=1, column=0, padx=10, sticky="ew")

        self.level_label = ttk.Label(self, text="Рівень")
        self.level_label.grid(row=2, column=0)

        self.result_label = ttk.Label(self, text="Результат")
        self.result_label.grid(row=3, column=0)

        ttk.Button(self, text="Вийти", command=self.show_previous_window).grid(
            row=4, column=0
        )

    def show(self, result: ExerciseResult) -> None:
        super().show()
        self.user_diagram.from_result(result)
        self.level_label.configure(text=f"Рівень: {result.level.value}")
        self.result_label.configure(
            text=f"Результат: {round(result.calculate_mark(),1)} балів"
        )

    def on_resize(self, *unused) -> None:
        self.user_diagram.on_resize(self.winfo_width(), self.winfo_height())
