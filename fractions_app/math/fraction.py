from __future__ import annotations
from typing import Union

from .helper import get_highest_common_divider


class Fraction:
    """Instance of Fraction class. Fraction object is immutable."""

    def __init__(self, numerator: int, denominator: int, integer: int = 0):
        self.numerator = numerator
        self.denominator = denominator
        self.integer = integer

    def __add__(self, adder: Union[int, Fraction]) -> Fraction:
        """Add `adder` to `self`, result is new a Fraction.

        Arg:
            `adder`: Union[int, Fraction]
        Returns:
            Fraction: new Fraction(may be improper).
        """

        if isinstance(adder, int):
            return Fraction(self.numerator, self.denominator, self.integer + adder)

        elif isinstance(adder, Fraction):
            result = self.convert_to_improper_fraction()
            adder = adder.convert_to_improper_fraction()

            result.numerator = (result.numerator * adder.denominator) + (
                adder.numerator * result.denominator
            )
            result.denominator = result.denominator * adder.denominator
            return result

        return self.copy()

    def __sub__(self, subtractor: Union[int, Fraction]) -> Fraction:
        """Subtract `self` by `subtractor`, result is new a Fraction.

        Arg:
            `subtractor`: Union[int, Fraction].

        Returns:
            Fraction: new Fraction(may be improper).
        """

        if isinstance(subtractor, int):
            subtractor = Fraction(subtractor, 1)
            return self - subtractor
        elif isinstance(subtractor, Fraction):
            result = self.convert_to_improper_fraction()
            subtractor = subtractor.convert_to_improper_fraction()

            result.numerator = (result.numerator * subtractor.denominator) - (
                subtractor.numerator * result.denominator
            )
            result.denominator = result.denominator * subtractor.denominator
            return result

        return self.copy()

    def __mul__(self, mulpiplier: Union[int, Fraction]) -> Fraction:
        """Multiply `self` by `adder`, result is new a Fraction.

        Arg:
            `mulpiplier`: Union[int, Fraction]
        Returns:
            Fraction: new Fraction(may be improper).
        """

        if isinstance(mulpiplier, int):
            result = self.copy()
            if result.integer != 0:
                result.numerator += result.denominator * result.integer
                result.integer = 0
            result.numerator *= mulpiplier

            return result

        elif isinstance(mulpiplier, Fraction):
            result = self.convert_to_improper_fraction()
            mulpiplier = mulpiplier.convert_to_improper_fraction()

            result.numerator = result.numerator * mulpiplier.numerator
            result.denominator = result.denominator * mulpiplier.denominator
            return result

        return self.copy()

    def __truediv__(self, divider: Union[int, Fraction]) -> Fraction:
        """Divide `self` by `divider`, result is new a Fraction.

        Arg:
            `divider`: Union[int, Fraction]
        Returns:
            Fraction: new Fraction(may be improper).
        """

        if isinstance(divider, int):
            return Fraction(self.numerator, self.denominator * divider, self.integer)
        elif isinstance(divider, Fraction):
            result = self.convert_to_improper_fraction()
            divider = divider.convert_to_improper_fraction()

            result.numerator = result.numerator * divider.denominator
            result.denominator = result.denominator * divider.numerator
            return result

        return self.copy()

    def convert_to_improper_fraction(self) -> Fraction:
        """Convert proper fraction to improper. Create new Fraction instance.

        Returns:
            Fraction: new improper Fraction.
        """

        result = Fraction(self.numerator, self.denominator, self.integer)
        result.numerator += result.denominator * result.integer
        result.integer = 0

        return result

    def divide_by_number(self, number: int):
        """Divide `number` by `self`."""

        return Fraction(self.denominator, self.numerator) * number

    def __repr__(self):
        integer = "" if self.integer == 0 else f"{self.integer}*"

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
        """Reduce fraction. Create new Fraction instance.

        Returns:
            Fraction: new reduced Fraction.
        """

        common_divider = get_highest_common_divider(self.denominator, self.numerator)
        reduced_numerator = self.numerator // common_divider
        reduced_denominator = self.denominator // common_divider

        return Fraction(
            reduced_numerator,
            reduced_denominator,
            self.integer,
        )

    def convert_to_proper_fraction(self):
        """Convert improper fraction to proper. Create new Fraction instance.

        Returns:
            Fraction: new proper Fraction.
        """

        result = self.copy()
        if (
            abs(result.numerator) >= result.denominator
            and result.numerator != 1
            and result.denominator != 0
        ):
            result.integer, result.numerator = divmod(
                result.numerator, result.denominator
            )
        return result

    def simplify(self):
        return self.reduce().convert_to_proper_fraction()

    def get_lowest_common_denominator(self, fraction: Fraction) -> tuple[int, int]:
        """Get factors for fraction denominators. Multiply factor to corresponding denominator to get common denominator.
        If fractions don't have common denominator, (1, 1) will be return.

        Returns:
            tuple[int, int]: factors, first is for self, second is for `fraction` argument.
        """

        for factor_1 in range(1, 20):
            for factor_2 in range(1, 20):
                if self.denominator * factor_1 == fraction.denominator * factor_2:
                    return (factor_1, factor_2)
        return (1, 1)
