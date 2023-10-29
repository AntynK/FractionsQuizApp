from random import randrange

from ..helper import Fraction, Exercise, Topic, Subtopic


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
        fraction = Fraction(randrange(1, 10), randrange(20))
        number = randrange(2, 10)

        result = fraction / number
        expression = f"{fraction} : {number} = ?"

        return Exercise(expression=expression, fraction=result)

    def second_exercise(self) -> Exercise:
        fraction = Fraction(randrange(1, 10), randrange(20))
        number = randrange(2, 10)

        result = fraction.divide_by_number(number)
        expression = f"{number} : {fraction} = ?"

        return Exercise(expression=expression, fraction=result)

    def third_exercise(self) -> Exercise:
        first_fraction = Fraction(randrange(1, 10), randrange(15))
        second_fraction = Fraction(randrange(1, 10), randrange(15))

        while first_fraction.numerator >= first_fraction.denominator:
            first_fraction.denominator += 2

        while second_fraction.numerator >= second_fraction.denominator:
            second_fraction.denominator += 2

        if first_fraction.denominator == second_fraction.denominator:
            first_fraction.denominator += 1

        result = first_fraction / second_fraction
        expression = f"{first_fraction} : {second_fraction} = ?"

        return Exercise(expression=expression, fraction=result)

    def fourth_exercise(self) -> Exercise:
        first_fraction = Fraction(randrange(1, 10), randrange(15), randrange(1, 4))
        second_fraction = Fraction(randrange(1, 10), randrange(15), randrange(1, 4))

        while first_fraction.numerator >= first_fraction.denominator:
            first_fraction.denominator += 2

        while second_fraction.numerator >= second_fraction.denominator:
            second_fraction.denominator += 2

        result = first_fraction / second_fraction
        expression = f"{first_fraction} : {second_fraction} = ?"

        return Exercise(expression=expression, fraction=result)
