from __future__ import annotations


from .helper import get_highest_common_divider


class Fraction:
    """Fraction(not float)."""

    def __init__(self, numerator: int, denominator: int, integer: int = 0):
        self.numerator = abs(numerator)
        self.denominator = abs(denominator)
        self.integer = integer

    def __add__(self, adder) -> Fraction:
        if isinstance(adder, int):
            return Fraction(self.numerator, self.denominator, self.integer + adder)

        elif isinstance(adder, Fraction):
            if self.denominator != adder.denominator:
                factor_1, factor_2 = self.get_lowest_common_denominator(adder)

                fraction_1 = Fraction(
                    self.numerator * factor_1, self.denominator * factor_1, self.integer
                )
                fraction_2 = Fraction(
                    adder.numerator * factor_2,
                    adder.denominator * factor_2,
                    adder.integer,
                )
                return fraction_1 + fraction_2

            return Fraction(
                self.numerator + adder.numerator,
                self.denominator,
                self.integer + adder.integer,
            )
        return self.copy()

    def __sub__(self, substractor) -> Fraction:
        if isinstance(substractor, Fraction):
            result = self.copy()
            if self.denominator != substractor.denominator:
                factor_1, factor_2 = self.get_lowest_common_denominator(substractor)
                fraction_1 = Fraction(
                    result.numerator * factor_1,
                    result.denominator * factor_1,
                    result.integer,
                )
                fraction_2 = Fraction(
                    substractor.numerator * factor_2,
                    substractor.denominator * factor_2,
                    substractor.integer,
                )

                return fraction_1 - fraction_2

            if (
                result.numerator < substractor.numerator
                and result.integer > substractor.integer
            ):
                result.numerator += result.denominator
                result.integer -= 1

            return Fraction(
                result.numerator - substractor.numerator,
                result.denominator,
                result.integer - substractor.integer,
            )

        return self.copy()

    def __mul__(self, mulpiplier) -> Fraction:
        if isinstance(mulpiplier, int):
            result = self.copy()
            if result.integer != 0:
                result.numerator += result.denominator * result.integer
                result.integer = 0
            result.numerator *= mulpiplier

            return result

        elif isinstance(mulpiplier, Fraction):
            result = self.copy()
            mulpiplier = mulpiplier.copy()
            if result.integer != 0:
                result.numerator += result.denominator * result.integer
                result.integer = 0
            if mulpiplier.integer != 0:
                mulpiplier.numerator += mulpiplier.denominator * mulpiplier.integer
                mulpiplier.integer = 0
            result.numerator *= mulpiplier.numerator
            result.denominator *= mulpiplier.denominator
            return result

        return self.copy()

    def __truediv__(self, divider) -> Fraction:
        if isinstance(divider, int):
            return Fraction(self.numerator, self.denominator * divider, self.integer)
        elif isinstance(divider, Fraction):
            result = self.copy()
            divider = divider.copy()
            if divider.integer != 0:
                divider.numerator += divider.denominator * divider.integer
                divider.integer = 0
            if result.integer != 0:
                result.numerator += result.denominator * result.integer
                result.integer = 0

            return result * Fraction(
                divider.denominator, divider.numerator, divider.integer
            )
        return self.copy()

    def divide_by_number(self, number: int):
        """Divide `number` by fraction."""

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
        """Create new reduced fraction."""
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
