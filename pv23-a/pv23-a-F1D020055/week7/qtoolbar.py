import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class tooldemo(QMainWindow):
    def __init__(self, parent=None):
        super(tooldemo, self).__init__(parent)
        # layout = QVBoxLayout()

        tb = self.addToolBar("File")
        tb.setOrientation(Qt.Vertical)
        tb.setMovable(False)

        new = QAction(QIcon("new.png"), "membuat file baru", self)
        # new.actionTriggered.connect(self.toolbtnpressed)
        tb.addAction(new)

        open = QAction(QIcon("open.png"), "open", self)
        tb.addAction(open)
        save = QAction(QIcon("save.png"), "save", self)
        tb.addAction(save)

        # new.actionTriggered.connect(self.toolbtnpressed)
        # open.actionTriggered.connect(self.toolbtnpressed)
        # save.actionTriggered.connect(self.toolbtnpressed)

        tb.actionTriggered[QAction].connect(self.toolbtnpressed)

        tb2 = self.addToolBar("Edit")
        tb2.setOrientation(Qt.Horizontal)
        tb2.setMovable(False)
        new2 = QAction(QIcon("new.png"), "new", self)
        tb2.addAction(new2)

        # self.setLayout(layout)
        self.setWindowTitle("toolbar demo")

    def toolbtnpressed(self, a):
        print("pressed tool button is", a.text())


def main():
    app = QApplication(sys.argv)
    ex = tooldemo()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
