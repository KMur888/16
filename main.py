import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon
from currency_converter import CurrencyConverter
from ui import Ui_MainWindow

class CurrencyConv(QtWidgets.QMainWindow):
    def __init__(self):
        super(CurrencyConv, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Конвертер валют')
        self.setWindowIcon(QIcon('tiMtjoTp2BIhVXHXyg24yqgF0vLQABkwhKkthPFVBmU85Cl63iIthIDsB4VKiV6KnrZBA-O1CfM7wHRSgIgeU1r6.jpg'))
        self.ui.imput_cur.setPlaceholderText('Из валюты')
        self.ui.imput_sum.setPlaceholderText('Сколько')
        self.ui.output_cur.setPlaceholderText('Итого')
        self.ui.output_sum.setPlaceholderText('В валюту')
        self.ui.pushButton.clicked.connect(self.converter)
    def converter(self):
        c = CurrencyConverter()
        input_cur = self.ui.input_cur.text()
        output_cur = self.ui.output_cur.text()
        input_sum = int(self.ui.unput_sum.text())
        output_sum = round(c.convert(input_sum, '%s' % (input_cur), '%s' % (output_cur)), 2)
        self.ui.output_sum.setText(str(output_sum))

app = QtWidgets.QApplication([])
application =  CurrencyConv()
application.show()

sys.exit(app.exec())