from ..helper import (
    Exercise,
    Topic,
    Subtopic,
    generate_proper_fractions_with_same_denominator,
    generate_proper_fractions_with_different_denominators,
    generate_mixed_fractions,
)


class FractionSubtracting(Topic):
    """This topic contains exercises related to fraction subtracting."""

    def __init__(self):
        self.title = "Віднімання дробів"
        self.subtopics = [
            Subtopic("Віднімання дробів з спільним знаменником", self.first_exercise),
            Subtopic("Віднімання дробів з різними знаменниками", self.second_exercise),
            Subtopic("Віднімання мішаних дробів", self.third_exercise),
        ]

    def first_exercise(self) -> Exercise:
        """This exercise cover subtrating two fractions with same denominators."""
        (
            first_fraction,
            second_fraction,
        ) = generate_proper_fractions_with_same_denominator()
        result = first_fraction - second_fraction

        return Exercise(
            operand_1=first_fraction,
            operand_2=second_fraction,
            operation="-",
            result=result,
        )

    def second_exercise(self) -> Exercise:
        """This exercise cover subtrating two fractions with different denominators."""
        (
            first_fraction,
            second_fraction,
        ) = generate_proper_fractions_with_different_denominators()

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

        result = first_fraction - second_fraction

        return Exercise(
            operand_1=first_fraction,
            operand_2=second_fraction,
            operation="-",
            result=result,
        )
