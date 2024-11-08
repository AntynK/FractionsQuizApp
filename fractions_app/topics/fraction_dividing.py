from random import randrange

from fractions_app.helper import (
    Exercise,
    Topic,
    Subtopic,
    generate_proper_fractions_with_unlike_denominators,
    generate_mixed_fractions,
    generate_proper_fraction,
)


class FractionDividing(Topic):
    """This topic contains exercises related to fraction multiplication."""

    def __init__(self):
        self.title = "Ділення дробів"
        self.subtopics = [
            Subtopic("Ділення дробу на натуральне число", self.first_exercise),
            Subtopic("Ділення натурального числа на дріб", self.second_exercise),
            Subtopic("Ділення дробів із різними знаменниками", self.third_exercise),
            Subtopic("Ділення мішаних дробів", self.fourth_exercise),
        ]

    def first_exercise(self) -> Exercise:
        """This exercise cover dividing fraction by integer."""

        fraction = generate_proper_fraction()
        number = randrange(2, 10)

        result = fraction / number

        return Exercise(
            operand_1=fraction, operand_2=number, operation=":", result=result
        )

    def second_exercise(self) -> Exercise:
        """This exercise cover dividing integer by fraction."""

        fraction = generate_proper_fraction()
        number = randrange(2, 10)

        result = fraction.divide_by_number(number)

        return Exercise(
            operand_1=number, operand_2=fraction, operation=":", result=result
        )

    def third_exercise(self) -> Exercise:
        """This exercise cover dividing two fractions with unlike denominators."""

        (
            first_fraction,
            second_fraction,
        ) = generate_proper_fractions_with_unlike_denominators()

        result = first_fraction / second_fraction

        return Exercise(
            operand_1=first_fraction,
            operand_2=second_fraction,
            operation=":",
            result=result,
        )

    def fourth_exercise(self) -> Exercise:
        """This exercise cover dividing two mixed fractions."""
        first_fraction, second_fraction = generate_mixed_fractions()

        result = first_fraction / second_fraction

        return Exercise(
            operand_1=first_fraction,
            operand_2=second_fraction,
            operation=":",
            result=result,
        )
