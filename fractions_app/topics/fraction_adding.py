from random import randrange

from ..helper import Exercise, Topic, Subtopic
from ..math import Fraction


class FractionAdding(Topic):
    def __init__(self):
        self.title = "Додавання дробів"
        self.subtopics = [
            Subtopic("Додавання дробів з спільними знаменниками", self.first_exercise),
            Subtopic("Додавання дробів з різними знаменниками", self.second_exercise),
            Subtopic("Додавання мішаних дробів", self.third_exercise),
        ]

    def first_exercise(self) -> Exercise:
        first_fraction = Fraction(randrange(1, 10), randrange(20))
        denominator = first_fraction.denominator
        second_fraction = Fraction(randrange(1, 10), denominator)

        while (first_fraction.numerator + second_fraction.numerator) >= denominator:
            denominator += 2

        first_fraction.denominator = denominator
        second_fraction.denominator = denominator

        result = first_fraction + second_fraction
        expression = f"{first_fraction} + {second_fraction} = ?"

        return Exercise(expression=expression, fraction=result)

    def second_exercise(self) -> Exercise:
        first_fraction = Fraction(randrange(1, 10), randrange(15))
        second_fraction = Fraction(randrange(1, 10), randrange(15))

        while first_fraction.numerator >= first_fraction.denominator:
            first_fraction.denominator += 2

        while second_fraction.numerator >= second_fraction.denominator:
            second_fraction.denominator += 2

        if first_fraction.denominator == second_fraction.denominator:
            first_fraction.denominator += 1

        result = first_fraction + second_fraction
        expression = f"{first_fraction} + {second_fraction} = ?"

        return Exercise(expression=expression, fraction=result)

    def third_exercise(self) -> Exercise:
        first_fraction = Fraction(randrange(1, 10), randrange(15), randrange(1, 4))
        second_fraction = Fraction(randrange(1, 10), randrange(15), randrange(1, 4))

        while first_fraction.numerator >= first_fraction.denominator:
            first_fraction.denominator += 2

        while second_fraction.numerator >= second_fraction.denominator:
            second_fraction.denominator += 2

        result = first_fraction + second_fraction
        expression = f"{first_fraction} + {second_fraction} = ?"

        return Exercise(expression=expression, fraction=result)
