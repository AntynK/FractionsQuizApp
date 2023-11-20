from random import randrange

from ..helper import Exercise, Topic, Subtopic
from ..math import Fraction

class FractionMultiplicating(Topic):
    def __init__(self):
        self.title = "Множення дробів"
        self.subtopics = [
            Subtopic("Множення дробу на натуральне число", self.first_exercise),
            Subtopic("Множення дробів з різними знаменниками", self.second_exercise),
            Subtopic("Множення мішаних дробів", self.third_exercise),
        ]

    def first_exercise(self) -> Exercise:
        fraction = Fraction(randrange(1, 10), randrange(1, 10))
        number = randrange(2, 10)

        result = fraction * number

        return Exercise(operand_1=fraction, operand_2=number, operation="∙", result=result)

    def second_exercise(self) -> Exercise:
        first_fraction = Fraction(randrange(1, 10), randrange(1, 10))
        second_fraction = Fraction(randrange(1, 10), randrange(1, 10))

        while first_fraction.numerator >= first_fraction.denominator:
            first_fraction.denominator += 1

        while second_fraction.numerator >= second_fraction.denominator:
            second_fraction.denominator += 1
        while first_fraction.numerator <= second_fraction.numerator:
            first_fraction.numerator += 1

        if first_fraction.denominator == second_fraction.denominator:
            first_fraction.denominator += 1

        result = first_fraction * second_fraction
   
        return Exercise(operand_1=first_fraction, operand_2=second_fraction, operation="∙", result=result)

    def third_exercise(self) -> Exercise:
        first_fraction = Fraction(randrange(1, 10), randrange(1, 10), randrange(1, 4))
        second_fraction = Fraction(randrange(1, 10), randrange(1, 10), randrange(1, 4))

        while first_fraction.numerator >= first_fraction.denominator:
            first_fraction.denominator += 1

        while second_fraction.numerator >= second_fraction.denominator:
            second_fraction.denominator += 1

        while first_fraction.numerator <= second_fraction.numerator:
            first_fraction.numerator += 1

        result = first_fraction * second_fraction
 
        return Exercise(operand_1=first_fraction, operand_2=second_fraction, operation="∙", result=result)
