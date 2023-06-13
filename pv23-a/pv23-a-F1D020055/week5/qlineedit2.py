import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def window():
    app = QApplication(sys.argv)
    win = QWidget()

    flo = QFormLayout()

    e3 = QLineEdit()
    e3.setInputMask('9999-99-99')
    flo.addRow("Tgl. lahir", e3)

    win.setLayout(flo)
    win.setWindowTitle("PyQt")
    win.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
