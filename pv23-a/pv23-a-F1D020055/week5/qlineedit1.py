import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def window():
    app = QApplication(sys.argv)
    win = QWidget()

    flo = QFormLayout()

    e1 = QLineEdit()
    e1.setValidator(QIntValidator())
    e1.setMaxLength(10)
    e1.setAlignment(Qt.AlignRight)
    e1.setFont(QFont("Arial", 40))
    flo.addRow("integer validator", e1)

    win.setLayout(flo)
    win.setWindowTitle("PyQt")
    win.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
