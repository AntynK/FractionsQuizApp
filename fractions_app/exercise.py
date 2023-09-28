from dataclasses import dataclass


@dataclass
class Exercise:
    expression: str
    integer: int
    numerator: int
    denominator: int
