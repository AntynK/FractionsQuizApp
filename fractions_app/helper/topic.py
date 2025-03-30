from typing import Callable

from dataclasses import dataclass

from fractions_app.helper.exercise import Exercise


@dataclass
class Subtopic:
    title: str
    generate_exercise: Callable[..., Exercise]


@dataclass
class Topic:
    title: str
    subtopics: list[Subtopic]
