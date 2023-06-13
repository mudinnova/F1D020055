import sys
from PyQt5.QtWidgets import *


class Radiodemo(QWidget):

    def __init__(self, parent = None):
        super(Radiodemo, self).__init__(parent)

        layout = QHBoxLayout()
        self.b1 = QRadioButton("Button 1")
        self.b1.setChecked(True)
        self.b1.toggled.connect(lambda: self.btn1state())
        layout.addWidget(self.b1)

        self.b2 = QRadioButton("Button 2")
        self.b2.setChecked(True)
        self.b2.toggled.connect(lambda: self.btn2state())

        layout.addWidget(self.b2)
        self.setLayout(layout)
        self.setWindowTitle("Radiobutton Demo")

    def btn1state(self):
        if self.b1.isChecked():
            print("B1 is selected")
        else:
            print("B2 is selected")

    def btn2state(self):
        if self.b2.isChecked():
            print("B2 is selected")
        else:
            print("B1 is selected")

    # def btnstate(self, b):
    #     if b.text() == "Button 1":
    #         if b.isChecked():
    #             print(b.text() + "is selected")
    #         else:
    #             print(b.text() + "is deselected")
    #     if b.text() == "Button 2":
    #         if b.isChecked():
    #             print(b.text() + "is selected")
    #         else:
    #             print(b.text() + "is deselected")

def window():
    app = QApplication(sys.argv)
    ex = Radiodemo()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    window()
