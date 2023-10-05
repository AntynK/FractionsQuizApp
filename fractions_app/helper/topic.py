from dataclasses import dataclass

from .subtopic import Subtopic


@dataclass
class Topic:
    title: str
    subtopics: list[Subtopic]
