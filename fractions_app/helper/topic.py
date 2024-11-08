from __future__ import annotations
from dataclasses import dataclass

from fractions_app.helper.subtopic import Subtopic


@dataclass
class Topic:
    title: str
    subtopics: list[Subtopic]
