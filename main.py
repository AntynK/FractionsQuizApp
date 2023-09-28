import sys
import subprocess

from PyQt5.QtWidgets import QApplication

from fractions_app.app import AppMainWindow


if __name__ == "__main__":
    subprocess.run("convert.bat")
    app = QApplication(sys.argv)
    main_window = AppMainWindow()
    main_window.show()

    app.exec()
    
# cx_Freeze
