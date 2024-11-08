from random import randrange

from fractions_app.helper import (
    Exercise,
    Topic,
    Subtopic,
    generate_proper_fractions_with_unlike_denominators,
    generate_mixed_fractions,
    generate_proper_fraction,
)


class FractionMultiplication(Topic):
    """This topic contains exercises related to fraction multiplication."""

    def __init__(self):
        self.title = "Множення дробів"
        self.subtopics = [
            Subtopic("Множення дробу на натуральне число", self.first_exercise),
            Subtopic("Множення дробів із різними знаменниками", self.second_exercise),
            Subtopic("Множення мішаних дробів", self.third_exercise),
        ]

    def first_exercise(self) -> Exercise:
        """This exercise cover multiplication fraction by integer."""

        fraction = generate_proper_fraction()
        number = randrange(2, 10)

        result = fraction * number

        return Exercise(
            operand_1=fraction, operand_2=number, operation="∙", result=result
        )

    def second_exercise(self) -> Exercise:
        """This exercise cover multiplication two fractions with unlike denominators."""

        (
            first_fraction,
            second_fraction,
        ) = generate_proper_fractions_with_unlike_denominators()

        result = first_fraction * second_fraction

        return Exercise(
            operand_1=first_fraction,
            operand_2=second_fraction,
            operation="∙",
            result=result,
        )

    def third_exercise(self) -> Exercise:
        """This exercise cover multiplication two mixed fractions."""

        first_fraction, second_fraction = generate_mixed_fractions()
        result = first_fraction * second_fraction

        return Exercise(
            operand_1=first_fraction,
            operand_2=second_fraction,
            operation="∙",
            result=result,
        )
