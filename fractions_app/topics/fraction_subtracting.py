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
            Subtopic("Віднімання дробів зі спільним знаменником", self.first_exercise),
            Subtopic("Віднімання дробів із різними знаменниками", self.second_exercise),
            Subtopic("Віднімання мішаних дробів", self.third_exercise),
        ]

    def first_exercise(self) -> Exercise:
        """This exercise cover subtrating two fractions with like denominators."""

        (
            first_fraction,
            second_fraction,
        ) = generate_proper_fractions_with_like_denominators()
        first_fraction, second_fraction = self.check_fractions(
            first_fraction, second_fraction
        )
        result = first_fraction - second_fraction

        return Exercise(
            operand_1=first_fraction,
            operand_2=second_fraction,
            operation="-",
            result=result,
        )

    def second_exercise(self) -> Exercise:
        """This exercise cover subtrating two fractions with unlike denominators."""

        (
            first_fraction,
            second_fraction,
        ) = generate_proper_fractions_with_unlike_denominators()
        first_fraction, second_fraction = self.check_fractions(
            first_fraction, second_fraction
        )

        result = first_fraction - second_fraction

        return Exercise(
            operand_1=first_fraction,
            operand_2=second_fraction,
            operation="-",
            result=result,
        )

    def third_exercise(self) -> Exercise:
        """This exercise cover subtrating two mixed fractions."""

        first_fraction, second_fraction = generate_mixed_fractions()
        first_fraction, second_fraction = self.check_fractions(
            first_fraction, second_fraction
        )

        result = first_fraction - second_fraction

        return Exercise(
            operand_1=first_fraction,
            operand_2=second_fraction,
            operation="-",
            result=result,
        )

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
