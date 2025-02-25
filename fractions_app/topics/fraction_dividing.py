from typing import Union
from random import randrange

from fractions_app.math import Fraction
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

        return self._generate_exercise(fraction, number)

    def second_exercise(self) -> Exercise:
        """This exercise cover dividing integer by fraction."""

        fraction = generate_proper_fraction()
        number = randrange(2, 10)

        return self._generate_exercise(fraction, number, True)

    def third_exercise(self) -> Exercise:
        """This exercise cover dividing two fractions with unlike denominators."""

        (
            first_fraction,
            second_fraction,
        ) = generate_proper_fractions_with_unlike_denominators()

        return self._generate_exercise(first_fraction, second_fraction)

    def fourth_exercise(self) -> Exercise:
        """This exercise cover dividing two mixed fractions."""
        first_fraction, second_fraction = generate_mixed_fractions()

        return self._generate_exercise(first_fraction, second_fraction)

    def _generate_exercise(
        self,
        operand_1: Fraction,
        operand_2: Union[Fraction, int],
        divide_by_int: bool = False,
    ) -> Exercise:
        if divide_by_int and isinstance(operand_2, int):
            result = operand_1.divide_by_number(operand_2)
            operand_1, operand_2 = operand_2, operand_1  # type: ignore
        else:
            result = operand_1 / operand_2

        return Exercise(
            operand_1=operand_1,
            operand_2=operand_2,
            operation=":",
            result=result,
        )
