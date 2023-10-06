from random import randrange

from ..helper import Fraction, Exercise, Topic, Subtopic


class FractionAdding(Topic):
    def __init__(self):
        self.title = "Додавання дробів"
        self.subtopics = [
            Subtopic("Додавання дробів зі спільним знаменником", self.first_exercise)
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
