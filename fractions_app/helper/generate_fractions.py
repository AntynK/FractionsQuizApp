from random import randrange

from fractions_app.math import Fraction


def generate_proper_fraction(
    numerator_max: int = 10, denominator_max: int = 10
) -> Fraction:
    fraction = Fraction(randrange(1, numerator_max), randrange(1, denominator_max))

    while fraction.numerator >= fraction.denominator:
        fraction.denominator += 1

    return fraction


def generate_proper_fractions_with_like_denominators() -> tuple[Fraction, Fraction]:
    first_fraction = generate_proper_fraction()
    denominator = first_fraction.denominator
    numerator = randrange(1, denominator - 1 if denominator > 2 else denominator)
    second_fraction = Fraction(numerator, denominator)

    return first_fraction, second_fraction


def generate_proper_fractions_with_unlike_denominators() -> tuple[Fraction, Fraction]:
    first_fraction = generate_proper_fraction(6, 10)
    second_fraction = generate_proper_fraction(6, 10)

    if first_fraction.denominator == second_fraction.denominator:
        first_fraction.denominator += 1

    return first_fraction, second_fraction


def generate_mixed_fractions() -> tuple[Fraction, Fraction]:
    (
        first_fraction,
        second_fraction,
    ) = generate_proper_fractions_with_unlike_denominators()
    first_fraction.integer = randrange(1, 4)
    second_fraction.integer = randrange(1, 4)

    return first_fraction, second_fraction
