from pathlib import Path

VERSION = "1.4.0"
PROGRAM_TITLE = "Математичний тренажер для вивчення\n звичайних дробів"
CONGRATULATION_TITLE = "Прикинь ти"
AUTHOR = "Карандашов Андрій"

ATTEMPS_COUNT = 3
MAX_GRADE = 12

REDUCE_MESSAGE = "Поділи чисельник і знаменник дробу на їх найбільший спільний дільник. Частки від ділення запиши у дробову частину."

CONVERT_TO_PROPER_FRACTION_MESSAGE = "Для цього поділи чисельник дробу на знаменник. Частку запиши як ціле, а остачу залиш в чисельнику."

BASE_WIDTH, BASE_HEIGHT = 500, 450
CHARACTER_SIZE = 0.09
CWD = Path(".").absolute()
ICON_PATH = CWD.joinpath("assets", "icon.png")
CONGRATULATION_IMAGE_PATH = CWD.joinpath("assets", "congratulation.png")
