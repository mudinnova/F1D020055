import sys
from PyQt5.QtWidgets import *


def window():
    app = QApplication(sys.argv)

    w = QWidget()
    b = QLabel(w)

    w.setGeometry(500, 100, 200, 50)
    w.setWindowTitle("PyQt5")

    b.setText("Hello World!")
    b.move(50, 20)

    w.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
