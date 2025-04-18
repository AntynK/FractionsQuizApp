from tkinter import Canvas
from tkinter.font import Font

from fractions_app.helper import get_font_scale, ExerciseResult, Levels
from fractions_app.constants import CHARACTER_SIZE

OUTLINE_OFFSET = 5


class UserProgressDiagram(Canvas):
    def __init__(self, master) -> None:
        super().__init__(master)

        self.width, self.height = 500, 100
        self.result = ExerciseResult(0, 0, 0, 0, Levels.GRADE_5)
        self.diagram_offset = 0
        self.legend_offset = 0
        self._legend_font = Font(family="Times New Roman", size=15, weight="bold")
        self._value_label_font = Font(family="Times New Roman", size=20, weight="bold")

    def from_result(self, result: ExerciseResult) -> None:
        self.result = result
        self._display()

    def _display(self) -> None:
        self.diagram_offset = OUTLINE_OFFSET
        self.legend_offset = OUTLINE_OFFSET
        self.delete("all")

        self._display_segment("Правильні", self.result.correct_answers, "green")
        self._display_segment("Неправильні", self.result.failed_answers, "red")
        self._display_segment("Пропущені", self.result.skipped_exercises, "grey")

    def _display_segment(self, legend: str, value: int, color: str) -> None:
        width = self.get_width(value) + self.diagram_offset

        self.create_rectangle(
            self.diagram_offset,
            OUTLINE_OFFSET,
            width,
            self.rect_dim(),
            outline="black",
            fill=color,
            width=1,
        )
        if value > 0:
            self.create_text(
                (width - self.diagram_offset) // 2 + self.diagram_offset,
                self.rect_dim() // 2,
                text=str(value),
                font=self._value_label_font,
            )
        self.diagram_offset = width
        self._display_legend(legend, color)

    def _display_legend(self, legend: str, color: str) -> None:
        legend_area = self.rect_dim() * 1.5
        rect_size = self.rect_dim() // 2

        self.create_rectangle(
            OUTLINE_OFFSET + self.legend_offset,
            legend_area * 1.2,
            rect_size + OUTLINE_OFFSET + self.legend_offset,
            legend_area * 1.2 - rect_size,
            fill=color,
        )
        self.create_text(
            self.character_width() * 2.1 + self.legend_offset,
            legend_area + self.rect_dim() * 0.1,
            text=legend,
            font=self._legend_font,
        )
        self.legend_offset += self.character_width() * 3.5

    def character_width(self) -> float:
        return self.width * CHARACTER_SIZE

    def rect_dim(self) -> int:
        return round(
            (self.width - OUTLINE_OFFSET * 6) / self.result.total_exercises_count
        )

    def get_width(self, value: int) -> float:
        return self.rect_dim() * value

    def on_resize(self, width: int, height: int) -> None:
        self.width, self.height = width, height
        scale = get_font_scale(self.width, self.height)
        self._legend_font.configure(size=round(scale * 1.5))
        self._value_label_font.configure(size=round(scale * 2))
        self.configure(height=self.rect_dim() * 2)
        self._display()
