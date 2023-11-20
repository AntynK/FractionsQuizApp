from random import randrange

from ..helper import Exercise, Topic, Subtopic
from ..math import Fraction

class FractionDividing(Topic):
    def __init__(self):
        self.title = "Ділення дробів"
        self.subtopics = [
            Subtopic("Ділення дробу на натуральне число", self.first_exercise),
            Subtopic("Ділення натурального числа на дріб", self.second_exercise),
            Subtopic("Ділення дробів з різними знаменниками", self.third_exercise),
            Subtopic("Ділення мішаних дробів", self.fourth_exercise),
        ]

    def first_exercise(self) -> Exercise:
        fraction = Fraction(randrange(1, 10), randrange(1, 10))
        number = randrange(2, 10)

        result = fraction / number
 
        return Exercise(operand_1=fraction, operand_2=number, operation=":", result=result)

    def second_exercise(self) -> Exercise:
        fraction = Fraction(randrange(1, 10), randrange(1, 10))
        number = randrange(2, 10)

        result = fraction.divide_by_number(number)

        return Exercise(operand_1=number, operand_2=fraction, operation=":", result=result)

    def third_exercise(self) -> Exercise:
        first_fraction = Fraction(randrange(1, 10), randrange(1, 10))
        second_fraction = Fraction(randrange(1, 10), randrange(1, 10))

        while first_fraction.numerator >= first_fraction.denominator:
            first_fraction.denominator += 1

        while second_fraction.numerator >= second_fraction.denominator:
            second_fraction.denominator += 1

        if first_fraction.denominator == second_fraction.denominator:
            first_fraction.denominator += 1

        result = first_fraction / second_fraction
 
        return Exercise(operand_1=first_fraction, operand_2=second_fraction, operation=":", result=result)

    def fourth_exercise(self) -> Exercise:
        first_fraction = Fraction(randrange(1, 10), randrange(1, 10), randrange(1, 4))
        second_fraction = Fraction(randrange(1, 10), randrange(1, 10), randrange(1, 4))

        while first_fraction.numerator >= first_fraction.denominator:
            first_fraction.denominator += 1

        while second_fraction.numerator >= second_fraction.denominator:
            second_fraction.denominator += 1

        result = first_fraction / second_fraction
 
        return Exercise(operand_1=first_fraction, operand_2=second_fraction, operation=":", result=result)
