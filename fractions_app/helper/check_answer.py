from enum import Enum

from fractions_app.math import Fraction


class AnswerStatus(Enum):
    CORRECT = 0
    WRONG = 1
    NEED_CONVERTION_TO_PROPER = 2
    NEED_REDUCING = 3


def _color_spinboxes(user_input: Fraction, correct_answer: Fraction) -> list[str]:
    answers = (
        user_input.numerator == correct_answer.numerator,
        user_input.denominator == correct_answer.denominator,
        user_input.integer == correct_answer.integer,
    )
    return ["green" if answer else "red" for answer in answers]


def check_answer(
    user_input: Fraction, correct_answer: Fraction
) -> tuple[AnswerStatus, list[str]]:
    spinboxes_color = _color_spinboxes(user_input, correct_answer)
    answer = AnswerStatus.WRONG

    if user_input.simplify() == correct_answer:
        answer = AnswerStatus.CORRECT

    if user_input.simplify() != correct_answer:
        answer = AnswerStatus.WRONG

    elif user_input.reduce() != user_input and user_input.numerator != 0:
        answer = AnswerStatus.NEED_REDUCING
        spinboxes_color[2] = "orange"
        spinboxes_color[1] = "orange"

    elif user_input.to_proper_fraction() != user_input:
        answer = AnswerStatus.NEED_CONVERTION_TO_PROPER
        spinboxes_color[0] = "orange"
        spinboxes_color[2] = "orange"

    return (answer, spinboxes_color)
