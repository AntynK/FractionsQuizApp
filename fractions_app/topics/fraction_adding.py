from ..helper import (
    Exercise,
    Topic,
    Subtopic,
    generate_proper_fractions_with_different_denominators,
    generate_proper_fractions_with_same_denominator,
    generate_mixed_fractions,
)


class FractionAdding(Topic):
    """This topic contains exercises related to fraction adding."""

    def __init__(self):
        self.title = "Додавання дробів"
        self.subtopics = [
            Subtopic("Додавання дробів із спільними знаменниками", self.first_exercise),
            Subtopic("Додавання дробів із різними знаменниками", self.second_exercise),
            Subtopic("Додавання мішаних дробів", self.third_exercise),
        ]

    def first_exercise(self) -> Exercise:
        """This exercise cover adding two fractions with same denominators."""
        (
            first_fraction,
            second_fraction,
        ) = generate_proper_fractions_with_same_denominator()
        result = first_fraction + second_fraction

        return Exercise(
            operand_1=first_fraction,
            operand_2=second_fraction,
            operation="+",
            result=result,
        )

    def second_exercise(self) -> Exercise:
        """This exercise cover adding two fractions with different denominators."""
        (
            first_fraction,
            second_fraction,
        ) = generate_proper_fractions_with_different_denominators()

        result = first_fraction + second_fraction

        return Exercise(
            operand_1=first_fraction,
            operand_2=second_fraction,
            operation="+",
            result=result,
        )

    def third_exercise(self) -> Exercise:
        """This exercise cover adding two mixed fractions."""
        first_fraction, second_fraction = generate_mixed_fractions()

        result = first_fraction + second_fraction

        return Exercise(
            operand_1=first_fraction,
            operand_2=second_fraction,
            operation="+",
            result=result,
        )
