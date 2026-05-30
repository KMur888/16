import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon
from game import Ui_MainWindow2

class CurrencyConv(QtWidgets.QMainWindow):
    def __init__(self):
        super(CurrencyConv, self).__init__()
        self.ui = Ui_MainWindow2()
        self.ui.setupUi(self)
        self.setWindowTitle('Конвертер валют')
        self.setWindowIcon(QIcon('tiMtjoTp2BIhVXHXyg24yqgF0vLQABkwhKkthPFVBmU85Cl63iIthIDsB4VKiV6KnrZBA-O1CfM7wHRSgIgeU1r6.jpg'))
        self.ui.btnItog.clicked.connect(self.converter)
    def converter(self):
        int1 = int(self.ui.odin.text())
        int2 = int(self.ui.dva.text())
        int3 = int(self.ui.tri.text())
        output_sum = round(int1 + int2 + int3, 2)
        self.ui.itog.setText(str(output_sum))

app = QtWidgets.QApplication([])
application =  CurrencyConv()
application.show()

sys.exit(app.exec())