from __future__ import annotations
from .helper import get_highest_common_divider


class Fraction:
    def __init__(self, numerator=1, denominator=1, integer=0):
        self.numerator = numerator
        self.denominator = denominator
        self.integer = integer

    def __add__(self, adder) -> Fraction:
        if isinstance(adder, int):
            return Fraction(self.numerator, self.denominator, self.integer + adder)

        elif isinstance(adder, Fraction):
            if self.denominator != adder.denominator:
                factor_1, factor_2 = self.get_highest_common_denominator(adder)
                return self * factor_1 + adder * factor_2

            return Fraction(
                self.numerator + adder.numerator,
                self.denominator,
                self.integer + adder.integer,
            )
        return self.copy()

    def __mul__(self, mulpiplier) -> Fraction:
        if isinstance(mulpiplier, int):
            return Fraction(
                self.numerator * mulpiplier,
                self.denominator * mulpiplier,
                self.integer,
            )
        return self.copy()

    def __repr__(self):
        integer = ""
        integer = f"{self.integer}*" if self.integer > 0 else ""

        return f"{integer}{self.numerator}/{self.denominator}"

    def __eq__(self, value) -> bool:
        if not isinstance(value, Fraction):
            return False
        return all(
            (
                value.denominator == self.denominator,
                value.numerator == self.numerator,
                value.integer == self.integer,
            )
        )

    def copy(self) -> Fraction:
        return Fraction(self.numerator, self.denominator, self.integer)

    def reduce(self) -> Fraction:
        common_divider = get_highest_common_divider(self.denominator, self.numerator)
        integer = 0
        reduced_numerator = self.numerator // common_divider
        reduced_denominator = self.denominator // common_divider

        if reduced_numerator >= reduced_denominator:
            integer, reduced_numerator = divmod(reduced_numerator, reduced_denominator)

            if reduced_numerator == 0:
                reduced_numerator = 1

        return Fraction(
            reduced_numerator,
            reduced_denominator,
            self.integer + integer,
        )

    def get_highest_common_denominator(self, fraction: Fraction) -> tuple[int, int]:
        for factor_1 in range(1, 20):
            for factor_2 in range(1, 20):
                if self.denominator * factor_1 == fraction.denominator * factor_2:
                    return (factor_1, factor_2)
        return (1, 1)
