from tkinter import ttk, messagebox
from random import choices, shuffle

from fractions_app.helper import Levels, Subtopic, ExerciseResult
from fractions_app.windows.window import Window
from fractions_app.widgets import ExerciseBox, ButtonTypes
from fractions_app.topic_handler import TopicHandler
from fractions_app.constants import ATTEMPS_COUNT
from fractions_app.windows.mixed_exercise_result_window import MixedExerciseResultWindow


class MixedExerciseWindow(Window):
    ROWS = 2
    COLUMNS = 3

    def init(self) -> None:
        self.result_window = MixedExerciseResultWindow(self.previous_state)

        self.title_label = ttk.Label(self, text="Title")
        self.title_label.grid(row=0, column=1, sticky="news")

        self.exercise_box = ExerciseBox(
            self,
            self._on_correct,
            (ButtonTypes.COMPLETE_BTN, self._on_complete_pressed),
            (ButtonTypes.SKIP_BTN, self._on_skip_pressed),
            (ButtonTypes.CHECK_BTN, self._on_check_pressed),
        )
        self.exercise_box.grid(row=1, column=0, columnspan=3, sticky="news")

    def on_resize(self, *unused) -> None:
        self.exercise_box.on_resize(self.winfo_width(), self.winfo_height())

    def show(self, level: Levels, exercise_count: int) -> None:
        super().show()
        self.result = ExerciseResult(exercise_count, 0, 0, 0, level)

        self._fill_exercises()
        self._display_current_subtopic()

    def _fill_exercises(self) -> None:
        self.subtopics: list[Subtopic] = []
        self.current_subtopic = 0
        subtopics = TopicHandler().get_subtopics_by_level(self.result.level)
        self.subtopics.extend(subtopics)

        self.subtopics.extend(
            choices(
                subtopics, k=self.result.total_exercises_count - len(self.subtopics)
            )
        )
        shuffle(self.subtopics)

    def _display_current_subtopic(self) -> None:
        self._is_correct = False
        self._showed = False

        self.attempts = ATTEMPS_COUNT
        subtopic = self.subtopics[self.current_subtopic]

        self.title_label.configure(
            text=f"{subtopic.title} ({self.current_subtopic+1}/{self.result.total_exercises_count})"
        )
        self.exercise_box.display_exercise(subtopic.generate_exercise())

    def _display_next_subtopic(self) -> None:
        self.current_subtopic += 1
        if self.current_subtopic >= self.result.total_exercises_count:
            self._show_result_window()
            return

        self._display_current_subtopic()

    def _on_skip_pressed(self) -> None:
        response = messagebox.askyesno(
            "Ви впевнені?", "Ви хочете пропустити це завдання?"
        )
        if not response:
            return

        self.result.skipped_exercises += 1
        self._display_next_subtopic()

    def _on_complete_pressed(self) -> None:
        response = messagebox.askyesno("Ви впевнені?", "Ви хочете завершити тест?")
        if not response:
            return
        self.result.skipped_exercises += (
            self.result.total_exercises_count - self.result.get_total_exercise_count()
        )
        self._show_result_window()

    def _on_check_pressed(self) -> None:
        if self._showed:
            self._display_next_subtopic()
            return
        if self._is_correct:
            return

        if self.attempts <= 1:
            messagebox.showinfo(
                "Інформація",
                "У вас закінчились спроби, переходимо до наступного завдання.",
            )
            self.result.failed_answers += 1
            self._display_next_subtopic()
            return
        self.attempts -= 1

    def _on_correct(self, showed: bool) -> None:
        self._is_correct = True
        self._showed = showed
        if not showed:
            self.result.correct_answers += 1
            return

    def _show_result_window(self) -> None:
        self.grid_forget()
        self.result_window.show(self.result)
