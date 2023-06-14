import sys
from PyQt5.QtWidgets import *


def window():
    app = QApplication(sys.argv)
    win = QWidget()

    b1 = QPushButton("Button1")

    box1 = QVBoxLayout()
    box1.addWidget(b1)
    box1.addStretch()

    box2 = QHBoxLayout()
    b2 = QPushButton("Button2")
    b3 = QPushButton("Button3")
    box2.addWidget(b2)
    box2.addStretch()
    box2.addWidget(b3)
    box1.addLayout(box2)
    
    b4 = QPushButton("Button4")
    box1.addWidget(b4)
    box1.addStretch()
    
    win.setLayout(box1)

    win.setWindowTitle("PyQt")
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
