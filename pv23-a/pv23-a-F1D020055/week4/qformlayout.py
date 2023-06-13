import sys
from PyQt5.QtWidgets import *


def window():
    app = QApplication(sys.argv)
    win = QWidget()
    fbox = QFormLayout()

    # l1 = QLabel("Name")
    # l1 = QLabel()
    # l1.setText('Name')
    # nm = QLineEdit()
    # fbox.addRow(l1, nm)
    # fbox.addRow('Nama', nm)
    fbox.addRow(QLabel('Nama'), QLineEdit())
    fbox.addRow('NIM', QLineEdit())
    fbox.addRow('Prodi', QLineEdit())
    fbox.addRow('Fakultas', QLineEdit())

    # l2 = QLabel("Address")
    add1 = QLineEdit()
    add2 = QLineEdit()
    vbox = QVBoxLayout()
    vbox.addWidget(add1)
    vbox.addWidget(add2)
    # fbox.addRow(l2, vbox)
    # fbox.addRow(QLabel('Address'), vbox)
    fbox.addRow('Address', vbox)

    r1 = QRadioButton("Male")
    r2 = QRadioButton("Female")
    hbox = QHBoxLayout()
    hbox.addWidget(r1)
    hbox.addWidget(r2)
    hbox.addStretch()
    fbox.addRow("Gender", hbox)

    vbox = QVBoxLayout()
    vbox.addWidget(QPushButton("Submit"))
    vbox.addWidget(QPushButton("Cancel"))
    fbox.addRow("", vbox)

    win.setLayout(fbox)

    win.setWindowTitle("PyQt")
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
