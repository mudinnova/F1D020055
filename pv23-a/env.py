import os
import sys

from PyQt5.QtWidgets import QApplication, QMessageBox

app = QApplication(sys.argv)
msg = QMessageBox()
msg.setIcon(QMessageBox.Information)
msg.setText('OS Environments')
msg.setInformativeText(os.environ.__str__())
sys.exit(msg.exec_())
