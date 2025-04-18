from typing import Callable

from dataclasses import dataclass

from fractions_app.helper.exercise import Exercise
from fractions_app.helper.level import Levels


@dataclass
class Subtopic:
    title: str
    generate_exercise: Callable[..., Exercise]
    level: Levels


@dataclass
class Topic:
    title: str
    subtopics: list[Subtopic]
