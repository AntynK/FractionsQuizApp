from random import randrange

from ..helper import Fraction, Exercise, Topic, Subtopic


class FractionMultiplicating(Topic):
    def __init__(self):
        self.title = "Множення дробів"
        self.subtopics = [
            Subtopic("Множення дробу на натуральне число", self.first_exercise),
            Subtopic("Множення дробів з різними знаменниками", self.second_exercise),
            Subtopic("Множення мішаних дробів", self.third_exercise),
        ]

    def first_exercise(self) -> Exercise:
        fraction = Fraction(randrange(1, 10), randrange(20))
        number = randrange(2, 10)

        result = fraction * number
        expression = f"{fraction} ∙ {number} = ?"

        return Exercise(expression=expression, fraction=result)

    def second_exercise(self) -> Exercise:
        first_fraction = Fraction(randrange(1, 10), randrange(15))
        second_fraction = Fraction(randrange(1, 10), randrange(15))

        while first_fraction.numerator >= first_fraction.denominator:
            first_fraction.denominator += 2

        while second_fraction.numerator >= second_fraction.denominator:
            second_fraction.denominator += 2
        while first_fraction.numerator <= second_fraction.numerator:
            first_fraction.numerator += 2

        if first_fraction.denominator == second_fraction.denominator:
            first_fraction.denominator += 1

        result = first_fraction * second_fraction
        expression = f"{first_fraction} ∙ {second_fraction} = ?"

        return Exercise(expression=expression, fraction=result)

    def third_exercise(self) -> Exercise:
        first_fraction = Fraction(randrange(1, 10), randrange(15), randrange(1, 4))
        second_fraction = Fraction(randrange(1, 10), randrange(15), randrange(1, 4))

        while first_fraction.numerator >= first_fraction.denominator:
            first_fraction.denominator += 2

        while second_fraction.numerator >= second_fraction.denominator:
            second_fraction.denominator += 2

        while first_fraction.numerator <= second_fraction.numerator:
            first_fraction.numerator += 2

        result = first_fraction * second_fraction
        expression = f"{first_fraction} ∙ {second_fraction} = ?"

        return Exercise(expression=expression, fraction=result)
