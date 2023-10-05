class Fraction:
    def __init__(
        self, numerator=0, denominator=1, integer=0
    ):
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
