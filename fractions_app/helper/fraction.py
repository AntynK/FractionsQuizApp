class Fraction:
    def __init__(self, numerator=0, denominator=1, integer=0):
        self.numerator = numerator
        self.denominator = denominator
        self.integer = integer

    def __add__(self, adder):
        if isinstance(adder, Fraction):
            return Fraction(
                self.numerator + adder.numerator,
                self.denominator,
                self.integer + adder.integer,
            )
        return Fraction()

    def __repr__(self):
        integer = ""
        if self.integer != 0:
            integer = f"{self.integer}*"

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

    def copy(self):
        return Fraction(self.numerator, self.denominator, self.integer)

    def reduce(self):
        for factor in range(20, 0, -1):
            d_temp = round(self.denominator / factor)
            n_temp = round(self.numerator / factor)
            if d_temp * factor != self.denominator:
                continue
            if n_temp * factor != self.numerator:
                continue

            return Fraction(n_temp, d_temp, self.integer)
        return self.copy()
