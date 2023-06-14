import sys
from PyQt5.QtWidgets import *


class Checkdemo(QWidget):

    def __init__(self, parent = None):
        super(Checkdemo, self).__init__(parent)

        layout = QHBoxLayout()
        self.b1 = QCheckBox("Button 1")
        self.b1.setChecked(True)
        self.b1.stateChanged.connect(lambda: self.btnstate(self.b1))
        layout.addWidget(self.b1)

        self.b2 = QCheckBox("Button 2")
        self.b2.stateChanged.connect(lambda: self.btnstate(self.b2))

        layout.addWidget(self.b2)
        self.setLayout(layout)
        self.setWindowTitle("Radiobutton Demo")

    def btnstate(self, b):
        if b.text() == "Button 1":
            if b.isChecked():
                print(b.text() + " is selected")
            else:
                print(b.text() + " is deselected")
        if b.text() == "Button 2":
            if b.isChecked():
                print(b.text() + " is selected")
            else:
                print(b.text() + " is deselected")

def window():
    app = QApplication(sys.argv)
    ex = Checkdemo()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    window()
