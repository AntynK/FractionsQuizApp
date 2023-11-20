from typing import Callable

from dataclasses import dataclass


from .exercise import Exercise


@dataclass
class Subtopic:
    title: str
    generate_exercise: Callable[..., Exercise]
