import json
from pathlib import Path


from .constants import EXERCISES_DIR
from .widgets.exercise_button import ExerciseButton
from .exercise import Exercise


class ExercisesGroup:
    def __init__(self, name: str) -> None:
        self.name = name
        self.children = []

    def convert_expressions(self, expressions: list) -> list[Exercise]:
        result = []
        for expression in expressions:
            result.append(Exercise(**expression))
        return result

    def parse_file(self, callback):
        with open(Path(EXERCISES_DIR, f"{self.name}.json"), encoding="utf-8") as file:
            data = json.load(file)

        for exercise in data:
            exercise_name = exercise.get("name", "Name error")
            self.children.append(
                ExerciseButton(
                    exercise_name,
                    callback,
                    self.convert_expressions(exercise.get("expressions", [])),
                    exercise_name,
                )
            )
