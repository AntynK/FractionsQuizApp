from random import randrange

from ..math import Fraction


def generate_proper_fractions_with_same_denominator() -> tuple[Fraction, Fraction]:
    first_fraction = Fraction(randrange(1, 10), randrange(1, 10))
    denominator = first_fraction.denominator
    second_fraction = Fraction(randrange(1, 10), denominator)

    while (first_fraction.numerator + second_fraction.numerator) >= denominator:
        denominator += 1

    first_fraction.denominator = denominator
    second_fraction.denominator = denominator
    return first_fraction, second_fraction


def generate_proper_fractions_with_different_denominators() -> (
    tuple[Fraction, Fraction]
):
    first_fraction = Fraction(randrange(1, 6), randrange(1, 10))
    second_fraction = Fraction(randrange(1, 6), randrange(1, 10))

    while first_fraction.numerator >= first_fraction.denominator:
        first_fraction.denominator += 1

    while second_fraction.numerator >= second_fraction.denominator:
        second_fraction.denominator += 1

    if first_fraction.denominator == second_fraction.denominator:
        first_fraction.denominator += 1

    return first_fraction, second_fraction


def generate_mixed_fractions() -> tuple[Fraction, Fraction]:
    (
        first_fraction,
        second_fraction,
    ) = generate_proper_fractions_with_different_denominators()
    first_fraction.integer = randrange(1, 4)
    second_fraction.integer = randrange(1, 4)

    return first_fraction, second_fraction
