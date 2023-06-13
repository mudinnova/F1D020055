import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def window():
    app = QApplication(sys.argv)
    win = QWidget()

    flo = QFormLayout()

    e5 = QLineEdit()
    e5.setEchoMode(QLineEdit.Password)
    flo.addRow("Password", e5)

    win.setLayout(flo)
    win.setWindowTitle("PyQt")
    win.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
