from typing import Union
from dataclasses import dataclass
from ..math import Fraction


@dataclass
class Exercise:
    operand_1: Union[int, Fraction]
    operand_2: Union[int, Fraction]
    operation: str
    result: Fraction
