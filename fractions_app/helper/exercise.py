from dataclasses import dataclass
from .fraction import Fraction


@dataclass
class Exercise:
    expression: str
    fraction: Fraction