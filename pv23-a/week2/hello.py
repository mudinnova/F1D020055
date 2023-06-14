import sys
from PyQt5.QtWidgets import *


def window():
    app = QApplication(sys.argv)

    w = QWidget()
    b = QLabel(w)

    w.setGeometry(100, 100, 500, 300)
    w.setWindowTitle('Hello PyQt5')

    b.setText('Hello World!')
    b.setGeometry(100, 1000, 100, 100)
    b.move(50, 50)
    b.setToolTip('Tes Tooltips')

    w.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
