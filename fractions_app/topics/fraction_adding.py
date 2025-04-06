from fractions_app.math import Fraction
from fractions_app.helper import (
    Exercise,
    Topic,
    Subtopic,
    Levels,
    generate_proper_fractions_with_unlike_denominators,
    generate_proper_fractions_with_like_denominators,
    generate_mixed_fractions,
)


class FractionAdding(Topic):
    """This topic contains exercises related to fraction adding."""

    def __init__(self):
        self.title = "Додавання дробів"
        self.subtopics = [
            Subtopic(
                "Додавання дробів з однаковими знаменниками",
                self.first_exercise,
                Levels.GRADE_5,
            ),
            Subtopic(
                "Додавання дробів із різними знаменниками",
                self.second_exercise,
                Levels.GRADE_6,
            ),
            Subtopic("Додавання мішаних чисел", self.third_exercise, Levels.GRADE_5),
        ]

    def first_exercise(self) -> Exercise:
        """This exercise cover adding two fractions with like denominators."""

        (
            first_fraction,
            second_fraction,
        ) = generate_proper_fractions_with_like_denominators()

        return self._generate_exercise(first_fraction, second_fraction)

    def second_exercise(self) -> Exercise:
        """This exercise cover adding two fractions with unlike denominators."""

        (
            first_fraction,
            second_fraction,
        ) = generate_proper_fractions_with_unlike_denominators()

        return self._generate_exercise(first_fraction, second_fraction)

    def third_exercise(self) -> Exercise:
        """This exercise cover adding two mixed fractions."""

        first_fraction, second_fraction = generate_mixed_fractions()

        return self._generate_exercise(first_fraction, second_fraction)

    def _generate_exercise(
        self,
        operand_1: Fraction,
        operand_2: Fraction,
    ) -> Exercise:
        answer = operand_1 + operand_2
        return Exercise(
            operand_1=operand_1,
            operand_2=operand_2,
            operation="+",
            answer=answer.simplify(),
        )
