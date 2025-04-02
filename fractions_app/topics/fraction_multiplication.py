from typing import Union
from random import randrange

from fractions_app.math import Fraction
from fractions_app.helper import (
    Exercise,
    Topic,
    Subtopic,
    Level,
    generate_proper_fractions_with_unlike_denominators,
    generate_mixed_fractions,
    generate_proper_fraction,
)


class FractionMultiplication(Topic):
    """This topic contains exercises related to fraction multiplication."""

    def __init__(self):
        self.title = "Множення дробів"
        self.subtopics = [
            Subtopic(
                "Множення дробу на натуральне число", self.first_exercise, Level.GRADE_6
            ),
            Subtopic(
                "Множення дробів із різними знаменниками",
                self.second_exercise,
                Level.GRADE_6,
            ),
            Subtopic("Множення мішаних чисел", self.third_exercise, Level.GRADE_6),
        ]

    def first_exercise(self) -> Exercise:
        """This exercise cover multiplication fraction by integer."""

        fraction = generate_proper_fraction()
        number = randrange(2, 10)

        return self._generate_exercise(fraction, number)

    def second_exercise(self) -> Exercise:
        """This exercise cover multiplication two fractions with unlike denominators."""

        (
            first_fraction,
            second_fraction,
        ) = generate_proper_fractions_with_unlike_denominators()

        return self._generate_exercise(first_fraction, second_fraction)

    def third_exercise(self) -> Exercise:
        """This exercise cover multiplication two mixed fractions."""

        first_fraction, second_fraction = generate_mixed_fractions()

        return self._generate_exercise(first_fraction, second_fraction)

    def _generate_exercise(
        self,
        operand_1: Fraction,
        operand_2: Union[Fraction, int],
    ) -> Exercise:
        answer = operand_1 * operand_2
        return Exercise(
            operand_1=operand_1,
            operand_2=operand_2,
            operation="∙",
            answer=answer.simplify(),
        )
