import sys
from PyQt5.QtWidgets import *


def window():
    app = QApplication(sys.argv)
    win = QWidget()
    grid = QGridLayout()

    # rows
    for i in range(1, 3):
        # columns
        for j in range(1, 6):
            grid.addWidget(QPushButton("B" + str(i) + str(j)), i, j)

    grid.addWidget(QPushButton("B31"), 3, 1)
    grid.addWidget(QPushButton("B43"), 4, 3)
    grid.addWidget(QPushButton("B92"), 9, 2)
    grid.addWidget(QPushButton("B102"), 10, 2)

    win.setLayout(grid)
    # win.setGeometry(100, 100, 200, 100)
    win.setWindowTitle("PyQt")
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
