import sys

from PyQt5.QtWidgets import QApplication

from fractions_app.app import AppMainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = AppMainWindow()
    main_window.show()

    app.exec()