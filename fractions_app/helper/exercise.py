from dataclasses import dataclass
from ..math import Fraction

@dataclass
class Exercise:
    expression: str
    fraction: Fraction