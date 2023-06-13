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
    e1.setMaxLength(4)
    e1.setAlignment(Qt.AlignRight)
    e1.setFont(QFont("Arial", 40))
    flo.addRow("Integer Validator", e1)

    e2 = QLineEdit()
    e2.setValidator(QDoubleValidator(0.99, 99.9, 2))
    flo.addRow("Double Validator", e2)

    e3 = QLineEdit()
    # +62 (08) 171 7361 722
    # e3.setInputMask('+62 (99) 999 9999 9999')
    # 2002-08-12
    # e3.setInputMask('9999-99-99')
    # flo.addRow("Input Mask", e3)
    e3.setInputMask('99.999.999.9-999.999')
    flo.addRow("Input Mask", e3)

    e4 = QLineEdit()
    e4.textChanged.connect(textchanged)
    flo.addRow("Text Changed", e4)

    e5 = QLineEdit()
    # e5.setEchoMode(QLineEdit.Password)
    e5.setEchoMode(QLineEdit.PasswordEchoOnEdit)
    # e5.editingFinished.connect(enterPress)
    e5.returnPressed.connect(enterPress)
    flo.addRow("Password", e5)

    e51 = QLineEdit()
    e51.setEchoMode(QLineEdit.PasswordEchoOnEdit)
    flo.addRow("Password", e51)

    e6 = QLineEdit("Hello Python")
    e6.setReadOnly(True)
    flo.addRow("Read Only", e6)

    win.setLayout(flo)
    win.setWindowTitle("PyQt")
    win.show()

    sys.exit(app.exec_())

def textchanged(tes):
    print("contents of the box: ", tes)

def enterPress():
    print("Edited")

if __name__ == '__main__':
    window()
