from fractions_app.math import Fraction
from fractions_app.helper import (
    Exercise,
    Topic,
    Subtopic,
    generate_proper_fractions_with_like_denominators,
    generate_proper_fractions_with_unlike_denominators,
    generate_mixed_fractions,
)


class FractionSubtracting(Topic):
    """This topic contains exercises related to fraction subtracting."""

    def __init__(self):
        self.title = "Віднімання дробів"
        self.subtopics = [
            Subtopic(
                "Віднімання дробів з однаковими знаменниками", self.first_exercise
            ),
            Subtopic("Віднімання дробів із різними знаменниками", self.second_exercise),
            Subtopic("Віднімання мішаних чисел", self.third_exercise),
        ]

    def first_exercise(self) -> Exercise:
        """This exercise cover subtrating two fractions with like denominators."""

        (
            first_fraction,
            second_fraction,
        ) = generate_proper_fractions_with_like_denominators()

        return self._generate_exercise(first_fraction, second_fraction)

    def second_exercise(self) -> Exercise:
        """This exercise cover subtrating two fractions with unlike denominators."""

        (
            first_fraction,
            second_fraction,
        ) = generate_proper_fractions_with_unlike_denominators()

        return self._generate_exercise(first_fraction, second_fraction)

    def third_exercise(self) -> Exercise:
        """This exercise cover subtrating two mixed fractions."""

        first_fraction, second_fraction = generate_mixed_fractions()

        return self._generate_exercise(first_fraction, second_fraction)

    def check_fractions(
        self, fraction_1: Fraction, fraction_2: Fraction
    ) -> tuple[Fraction, Fraction]:
        """Check if result of `fraction_1` - `fraction_2` is negative return `fraction_2`, `fraction_1`.
        Otherwise return `fraction_1`, `fraction_2`.
        """

        res = fraction_1 - fraction_2
        if res < 0:
            return fraction_2, fraction_1
        return fraction_1, fraction_2

    def _generate_exercise(
        self,
        operand_1: Fraction,
        operand_2: Fraction,
    ) -> Exercise:
        operand_1, operand_2 = self.check_fractions(operand_1, operand_2)

        answer = operand_1 - operand_2
        return Exercise(
            operand_1=operand_1,
            operand_2=operand_2,
            operation="-",
            answer=answer.simplify(),
        )
