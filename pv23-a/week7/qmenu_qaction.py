import sys
from PyQt5.QtWidgets import *


class menudemo(QMainWindow):
    def __init__(self, parent=None):
        super(menudemo, self).__init__(parent)

        bar = self.menuBar()

        file = bar.addMenu("File")

        # file.addAction("New...")
        new = file.addMenu("New")
        # new.addAction("Page")
        new_page = new.addMenu("Page")
        new_page_portrait = new_page.addAction("Portrait")
        new_page.addAction("Landscape")
        new.addAction("Sheet")

        save = file.addAction("Save")
        save.triggered.connect(self.save_triggered)
        # save = QAction("Save", self)

        save.setShortcut("Ctrl+S")
        # file.addAction(save)

        edit = file.addMenu("Edit")
        edit.addAction("copy")
        # edit.addAction("paste")
        paste = edit.addMenu("paste")
        paste.addAction("by reference")
        # paste.addAction("by value")

        paste_value = QAction("by value", self)
        paste_value.triggered.connect(self.file_edit_paste_value_triggered)
        paste.addAction(paste_value)

        quit = QAction("Quit", self)
        quit.triggered.connect(self.quit_triggered)
        file_quit = file.addAction(quit)

        # File
        # - New
        #     - Page
        #         - Portrait
        #         - Landscape
        #     - Sheet
        # - Save (Ctrl+S)
        # - Edit
        #     - copy
        #     - paste
        #         - by reference
        #         - by value
        # - Quit

        help = bar.addMenu("Help")
        help.addAction("?")
        # help2 = help.addMenu("??")
        # help2.addAction("???")
        # help2.addAction("????")

        # Help
        # - ?

        file.triggered[QAction].connect(self.processtrigger)

        self.setWindowTitle("menu demo")

    def processtrigger(self, q):
        print(q.text() + " is triggered")

    def file_edit_paste_value_triggered(self):
        print("edit paste value triggered")

    def save_triggered(self):
        print("save triggered")

    def quit_triggered(self):
        exit()


def main():
    app = QApplication(sys.argv)
    ex = menudemo()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
