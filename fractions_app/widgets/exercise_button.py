from typing import Callable


from PyQt5.QtWidgets import QPushButton


class ExerciseButton(QPushButton):
    def __init__(self, text: str, callback: Callable, *callback_args) -> None:
        super().__init__()
        self.setText(text)
        self.callback = callback
        self.callback_args = callback_args

    def mousePressEvent(self, e) -> None:
        self.callback(*self.callback_args)
        return super().mousePressEvent(e)
