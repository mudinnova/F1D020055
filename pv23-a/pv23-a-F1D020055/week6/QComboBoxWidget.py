import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class combodemo(QWidget):
   def __init__(self, parent = None):
      super(combodemo, self).__init__(parent)
      
      layout = QHBoxLayout()
      self.cb = QComboBox()
      self.cb.addItem("bandung")
      self.cb.addItem("jakarta")
      self.cb.addItems(["sumatera", "kalimantan", "papua"])
      self.cb.currentIndexChanged.connect(self.selectionchange)
		
      layout.addWidget(self.cb)
      self.setLayout(layout)
      self.setGeometry(100, 100, 250, 50)
      self.setWindowTitle("combo box demo")

   def selectionchange(self,i):
      print ("Items in the list are :")
		
      for count in range(self.cb.count()):
         print (self.cb.itemText(count))
      print ("Current index",i,"selection changed ",self.cb.currentText())
		
def main():
   app = QApplication(sys.argv)
   ex = combodemo()
   ex.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main()