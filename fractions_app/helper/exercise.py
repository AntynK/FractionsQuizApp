from dataclasses import dataclass
from . import Fraction


@dataclass
class Exercise:
    expression: str
    fraction: Fraction