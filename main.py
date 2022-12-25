from PyQt5 import QtWidgets, QtGui, QtCore
from QAMM import Ui_MainWindow
from info import Ui_Form
import sys


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def show_mywindow(self):
        self.ui.pushButton_6.clicked.connect(self.show_mywindow2)

    def show_mywindow2(self):
        self.ui2 = mywindow2()
        self.ui2.show()


class mywindow2(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow2, self).__init__()
        self.ui2 = Ui_Form()
        self.ui2.setupUi(self)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = mywindow()
    w.show()
    w.show_mywindow()
    sys.exit(app.exec_())