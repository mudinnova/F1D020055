import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *


def window():
    app = QApplication(sys.argv)
    win = QWidget()

    l1 = QLabel()
    l2 = QLabel()
    l3 = QLabel()
    l4 = QLabel()

    l1.setText("Hello World")
    l2.setText("<a href='#'>welcome to Python GUI Programming</a>")
    l3.setPixmap(QPixmap("img/py.png"))
    l4.setText("<a href='#'>Tutorials</a>")

    l1.setAlignment(Qt.AlignCenter)
    # l1.setAlignment(132)
    l3.setAlignment(Qt.AlignCenter)
    # l3.setAlignment(132)
    l4.setAlignment(Qt.AlignRight)
    # l4.setAlignment(2)

    vbox = QVBoxLayout()
    vbox.addWidget(l1)
    vbox.addStretch()
    vbox.addWidget(l2)
    vbox.addStretch()
    vbox.addWidget(l3)
    vbox.addStretch()
    vbox.addWidget(l4)

    l1.setOpenExternalLinks(True)
    l1.setTextInteractionFlags(Qt.TextSelectableByMouse)

    l2.linkHovered.connect(hovered)
    l4.linkActivated.connect(clicked)

    win.setLayout(vbox)

    win.setWindowTitle("QLabel Demo")
    win.show()
    sys.exit(app.exec_())


def hovered():
    print('hovering')


def clicked():
    print('clicked')


if __name__ == '__main__':
    window()
