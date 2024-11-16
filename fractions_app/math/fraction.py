from typing import Union


def get_highest_common_divider(num_1: int, num_2: int) -> int:
    """Returns `1` if `num_1` and `num_2` don't have common divider. Otherwise retruns common divider."""

    for factor in range(100, 0, -1):
        if num_1 % factor != 0:
            continue
        if num_2 % factor != 0:
            continue
        return factor
    return 1


class Fraction:
    """Instance of Fraction class. Fraction object is immutable."""

    def __init__(self, numerator: int, denominator: int, integer: int = 0):
        if not isinstance(numerator, int):
            raise ValueError(
                f"Numerator must be type int, not type: '{type(numerator)}'"
            )
        if not isinstance(denominator, int):
            raise ValueError(
                f"Denominator must be type int, not type: '{type(denominator)}'"
            )
        if not isinstance(integer, int):
            raise ValueError(f"Integer must be type int, not type: '{type(integer)}'")

        if denominator <= 0:
            raise ValueError("Denominator cannot be zero or negative.")

        self.numerator = numerator
        self.denominator = denominator
        self.integer = integer

    def __add__(self, adder: Union[int, "Fraction"]) -> "Fraction":
        """Add `adder` to `self`, result is new a Fraction.

        Arg:
            `adder`: Union[int, Fraction]
        Returns:
            Fraction: new Fraction(may be improper).
        """

        if isinstance(adder, int):
            return Fraction(self.numerator, self.denominator, self.integer + adder)

        elif isinstance(adder, Fraction):
            result = self.to_improper_fraction()
            adder = adder.to_improper_fraction()

            result.numerator = (result.numerator * adder.denominator) + (
                adder.numerator * result.denominator
            )
            result.denominator = result.denominator * adder.denominator
            return result

        return self.copy()

    def __sub__(self, subtractor: Union[int, "Fraction"]) -> "Fraction":
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
            result = self.to_improper_fraction()
            subtractor = subtractor.to_improper_fraction()

            result.numerator = (result.numerator * subtractor.denominator) - (
                subtractor.numerator * result.denominator
            )
            result.denominator = result.denominator * subtractor.denominator
            return result

        return self.copy()

    def __mul__(self, mulpiplier: Union[int, "Fraction"]) -> "Fraction":
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
            result = self.to_improper_fraction()
            mulpiplier = mulpiplier.to_improper_fraction()

            result.numerator = result.numerator * mulpiplier.numerator
            result.denominator = result.denominator * mulpiplier.denominator
            return result

        return self.copy()

    def __truediv__(self, divider: Union[int, "Fraction"]) -> "Fraction":
        """Divide `self` by `divider`, result is new a Fraction.

        Arg:
            `divider`: Union[int, Fraction]
        Returns:
            Fraction: new Fraction(may be improper).
        """

        if isinstance(divider, int):
            return Fraction(self.numerator, self.denominator * divider, self.integer)
        elif isinstance(divider, Fraction):
            result = self.to_improper_fraction()
            divider = divider.to_improper_fraction()

            result.numerator = result.numerator * divider.denominator
            result.denominator = result.denominator * divider.numerator
            return result

        return self.copy()

    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self.to_float() < other.to_float()

        return self.to_float() < other

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

    def to_float(self) -> float:
        return (self.numerator + self.integer * self.denominator) / self.denominator

    def simplify(self):
        return self.reduce().to_proper_fraction()

    def reduce(self) -> "Fraction":
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

    def to_proper_fraction(self):
        """Convert improper fraction to proper. Create new Fraction instance.

        Returns:
            Fraction: new proper Fraction.
        """

        result = self.copy()
        if abs(result.numerator) >= result.denominator:
            result.integer = int(result.numerator / result.denominator)
            if result.integer < 0:
                result.numerator *= -1

            result.numerator -= result.denominator * abs(result.integer)

        return result

    def to_improper_fraction(self) -> "Fraction":
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

    def copy(self) -> "Fraction":
        return Fraction(self.numerator, self.denominator, self.integer)

    def get_lowest_common_denominator(self, fraction: "Fraction") -> tuple[int, int]:
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
