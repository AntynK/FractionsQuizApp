from random import randrange

from ..helper import Exercise, Topic, Subtopic
from ..math import Fraction

class FractionSubstracting(Topic):
    def __init__(self):
        self.title = "Віднімання дробів"
        self.subtopics = [
            Subtopic("Віднімання дробів з спільним знаменником", self.first_exercise),
            Subtopic("Віднімання дробів з різними знаменниками", self.second_exercise),
            Subtopic("Віднімання мішаних дробів", self.third_exercise),
        ]

    def first_exercise(self) -> Exercise:
        first_fraction = Fraction(randrange(1, 10), randrange(1, 10))
        denominator = first_fraction.denominator
        second_fraction = Fraction(randrange(1, 10), denominator)

        while (first_fraction.numerator + second_fraction.numerator) >= denominator:
            denominator += 1

        while first_fraction.numerator <= second_fraction.numerator:
            first_fraction.numerator += 1

        first_fraction.denominator = denominator
        second_fraction.denominator = denominator

        result = first_fraction - second_fraction

        return Exercise(operand_1=first_fraction, operand_2=second_fraction, operation="-", result=result)

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

        result = first_fraction - second_fraction

        return Exercise(operand_1=first_fraction, operand_2=second_fraction, operation="-", result=result)

    def third_exercise(self) -> Exercise:
        first_fraction = Fraction(randrange(1, 10), randrange(1, 10), randrange(1, 4))
        second_fraction = Fraction(randrange(1, 10), randrange(1, 10), randrange(1, 4))

        while first_fraction.numerator >= first_fraction.denominator:
            first_fraction.denominator += 1

        while second_fraction.numerator >= second_fraction.denominator:
            second_fraction.denominator += 1

        while first_fraction.numerator <= second_fraction.numerator:
            first_fraction.numerator += 1

        result = first_fraction - second_fraction
 
        return Exercise(operand_1=first_fraction, operand_2=second_fraction, operation="-", result=result)
