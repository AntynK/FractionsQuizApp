from typing import Union
from dataclasses import dataclass

from fractions_app.math import Fraction
from fractions_app.helper.level import Level


@dataclass
class Exercise:
    operand_1: Union[int, Fraction]
    operand_2: Union[int, Fraction]
    operation: str
    answer: Fraction


@dataclass
class ExerciseResult:
    total_exercises_count: int
    correct_answers: int
    skipped_exercises: int
    failed_answers: int
    level: Level

    def get_completed_exercise_count(self) -> int:
        return self.correct_answers + self.failed_answers + self.skipped_exercises
