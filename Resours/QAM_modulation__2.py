# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QAM_modulation(2).ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from ModulationPy import QAMModem
from scipy import special
import matplotlib.pyplot as plt
import numpy as np


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1108, 628)
        MainWindow.setMinimumSize(QtCore.QSize(1108, 628))
        MainWindow.setMaximumSize(QtCore.QSize(1108, 628))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -20, 1111, 611))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Resours/2.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-46, -40, 1201, 221))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 16777212))
        self.label_2.setSizeIncrement(QtCore.QSize(0, 0))
        self.label_2.setFocusPolicy(QtCore.Qt.TabFocus)
        self.label_2.setStyleSheet("")
        self.label_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label_2.setWordWrap(False)
        self.label_2.setIndent(-1)
        self.label_2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 180, 321, 91))
        self.pushButton.setMinimumSize(QtCore.QSize(321, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 127);")
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(420, 180, 271, 91))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.comboBox.setFont(font)
        self.comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 127);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(408, 150, 171, 31))
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 280, 321, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 127);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 380, 321, 91))
        self.pushButton_3.setMinimumSize(QtCore.QSize(321, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 127);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(420, 320, 281, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(400, 290, 201, 31))
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(420, 380, 281, 31))
        self.lineEdit_3.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(402, 349, 210, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(375, 432, 721, 131))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("Resours/Tract.jpg"))
        self.label_6.setObjectName("label_6")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(748, 319, 321, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 127);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(40, 480, 321, 81))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 127);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(971, 210, 51, 20))
        self.lineEdit_2.setMinimumSize(QtCore.QSize(51, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(722, 209, 251, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(722, 235, 201, 21))
        self.label_8.setObjectName("label_8")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(925, 236, 51, 20))
        self.lineEdit_4.setMinimumSize(QtCore.QSize(51, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(1039, 264, 51, 20))
        self.lineEdit_5.setMinimumSize(QtCore.QSize(51, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(722, 263, 321, 21))
        self.label_9.setObjectName("label_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1108, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.comboBox.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.click)
        self.pushButton_2.clicked.connect(self.click_2)
        self.pushButton_3.clicked.connect(self.click_3)
        self.pushButton_4.clicked.connect(self.click_4)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "КАМ модуляция"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; color:#ffffff;\">Квадратурная амплитудная</span></p><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; color:#ffffff;\">модуляция </span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Сигнальное созвездие"))
        self.comboBox.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.comboBox.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.comboBox.setItemText(0, _translate("MainWindow", "КАМ-4"))
        self.comboBox.setItemText(1, _translate("MainWindow", "КАМ-16"))
        self.comboBox.setItemText(2, _translate("MainWindow", "КАМ-64"))
        self.comboBox.setItemText(3, _translate("MainWindow", "КАМ-256"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Виды модуляции:</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Модуляция"))
        self.pushButton_3.setText(_translate("MainWindow", "Демодуляция"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Входное сообщение:</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Выходное сообщение:</span></p></body></html>"))
        self.pushButton_4.setText(_translate("MainWindow", "Рассчет коэффициентов \n"
" битовых ошибок \n"
" с добавлением АБГШ"))
        self.pushButton_6.setText(_translate("MainWindow", "Информация о \n"
" программе"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Количество символов кадре:</span></p><p><span style=\" font-size:12pt;\"><br/></span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Количество испытаний:</span></p><p><span style=\" font-size:12pt; color:#ffffff;\"><br/></span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Массив отношения сигнал/шум в дБ:</span></p><p><span style=\" font-size:12pt; color:#ffffff;\"><br/></span></p></body></html>"))


    def click(self):
        if self.comboBox.currentText()=="КАМ-4":
            modem = QAMModem(4,
                          gray_map=True,
                          bin_input=False)

            modem.plot_const()
        if self.comboBox.currentText()=="КАМ-16":
            modem = QAMModem(16,
                              gray_map=True,
                              bin_input=False)

            modem.plot_const()
        if self.comboBox.currentText()=="КАМ-64":
            modem = QAMModem(64,
                          gray_map=True,
                          bin_input=False)

            modem.plot_const()
        if self.comboBox.currentText()=="КАМ-256":
            modem = QAMModem(256,
                          gray_map=True,
                          bin_input=False)

            modem.plot_const()
        if self.comboBox.currentText() == "":
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Выберите вид модуляции")
            error.setIcon(QMessageBox.Warning)
            error.exec_()
    def click_2(self):
        count = 0
        if self.comboBox.currentText() == "КАМ-4":
            if self.lineEdit_3.text() == "" or self.lineEdit.text() == "":
                error = QMessageBox()
                error.setWindowTitle("Ошибка")
                error.setText("Введите сообщение")
                error.setIcon(QMessageBox.Warning)
                error.exec_()
            else:
                if len(str(self.lineEdit.text())) < 8:
                    modem = QAMModem(4,
                                     bin_input=False,
                                     soft_decision=False,
                                     bin_output=False)

                    msg = [int(x) for x in str(self.lineEdit.text()).split() if x.isdigit()]
                    print(msg)
                    for item in msg:
                        if item > 3:
                            count += 1
                    if count == 0:
                        modulated = modem.modulate(msg)  # modulation
                        self.lineEdit_3.setText(str(modulated))
                    else:
                        error = QMessageBox()
                        error.setWindowTitle("Ошибка")
                        error.setText("Диапазон значений: [0-4]")
                        error.setIcon(QMessageBox.Warning)
                        error.exec_()
                else:
                    error = QMessageBox()
                    error.setWindowTitle("Ошибка")
                    error.setText("Максимальная длинна сообщения 4 символа!")
                    error.setIcon(QMessageBox.Warning)
                    error.exec_()
        if self.comboBox.currentText() == "КАМ-16":
            if self.lineEdit_3.text() == "" or self.lineEdit.text() == "":
                error = QMessageBox()
                error.setWindowTitle("Ошибка")
                error.setText("Введите сообщение")
                error.setIcon(QMessageBox.Warning)
                error.exec_()
            else:
                if len(str(self.lineEdit.text())) < 32:
                    modem = QAMModem(16,
                                     bin_input=False,
                                     soft_decision=False,
                                     bin_output=False)

                    msg = [int(x) for x in str(self.lineEdit.text()).split() if x.isdigit()]
                    for item in msg:
                        if item > 15:
                            count += 1
                    if count == 0:
                        modulated = modem.modulate(msg)  # modulation
                        self.lineEdit_3.setText(str(modulated))
                    else:
                        error = QMessageBox()
                        error.setWindowTitle("Ошибка")
                        error.setText("Диапазон значений: [0-16]")
                        error.setIcon(QMessageBox.Warning)
                        error.exec_()
                else:
                    error = QMessageBox()
                    error.setWindowTitle("Ошибка")
                    error.setText("Максимальная длинна сообщения 16 символов!")
                    error.setIcon(QMessageBox.Warning)
                    error.exec_()
        if self.comboBox.currentText() == "КАМ-64":
            if self.lineEdit_3.text() == "" or self.lineEdit.text() == "":
                error = QMessageBox()
                error.setWindowTitle("Ошибка")
                error.setText("Введите сообщение")
                error.setIcon(QMessageBox.Warning)
                error.exec_()
            else:
                if len(str(self.lineEdit.text())) < 128:
                    modem = QAMModem(64,
                                     bin_input=False,
                                     soft_decision=False,
                                     bin_output=False)

                    msg = [int(x) for x in str(self.lineEdit.text()).split() if x.isdigit()]
                    for item in msg:
                        if item > 63:
                            count += 1
                    if count == 0:
                        modulated = modem.modulate(msg)  # modulation
                        self.lineEdit_3.setText(str(modulated))
                    else:
                        error = QMessageBox()
                        error.setWindowTitle("Ошибка")
                        error.setText("Диапазон значений: [0-64]")
                        error.setIcon(QMessageBox.Warning)
                        error.exec_()
                else:
                    error = QMessageBox()
                    error.setWindowTitle("Ошибка")
                    error.setText("Максимальная длинна сообщения 64 символа!")
                    error.setIcon(QMessageBox.Warning)
                    error.exec_()
        if self.comboBox.currentText() == "КАМ-256":
            if self.lineEdit_3.text() == "" or self.lineEdit.text() == "":
                error = QMessageBox()
                error.setWindowTitle("Ошибка")
                error.setText("Введите сообщение")
                error.setIcon(QMessageBox.Warning)
                error.exec_()
            else:
                if len(str(self.lineEdit.text())) < 512:
                    modem = QAMModem(256,
                                     bin_input=False,
                                     soft_decision=False,
                                     bin_output=False)

                    msg = [int(x) for x in str(self.lineEdit.text()).split() if x.isdigit()]
                    for item in msg:
                        if item > 255:
                            count += 1
                    if count == 0:
                        modulated = modem.modulate(msg)  # modulation
                        self.lineEdit_3.setText(str(modulated))
                    else:
                        error = QMessageBox()
                        error.setWindowTitle("Ошибка")
                        error.setText("Диапазон значений: [0-256]")
                        error.setIcon(QMessageBox.Warning)
                        error.exec_()
                else:
                    error = QMessageBox()
                    error.setWindowTitle("Ошибка")
                    error.setText("Максимальная длинна сообщения 256 символа!")
                    error.setIcon(QMessageBox.Warning)
                    error.exec_()
        if self.comboBox.currentText() == "":
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Выберите вид модуляции")
            error.setIcon(QMessageBox.Warning)
            error.exec_()
        if self.lineEdit_3.text() == "" or self.lineEdit.text() == "":
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Введите сообщение")
            error.setIcon(QMessageBox.Warning)
            error.exec_()
    #Демодуляция
    def click_3(self):
        count = 0
        if self.comboBox.currentText() == "КАМ-4":
            if self.lineEdit_3.text() == "" or self.lineEdit.text() == "":
                error = QMessageBox()
                error.setWindowTitle("Ошибка")
                error.setText("Введите сообщение")
                error.setIcon(QMessageBox.Warning)
                error.exec_()
            else:
                if len(str(self.lineEdit.text())) < 8:
                    modem = QAMModem(4,
                                     bin_input=False,
                                     soft_decision=False,
                                     bin_output=False)

                    msg = [int(x) for x in str(self.lineEdit.text()).split() if x.isdigit()]
                    for item in msg:
                        if item > 3:
                            count += 1
                    if count == 0:
                        modulated = modem.modulate(msg)  # modulation
                        demodulated = modem.demodulate(modulated)
                        self.lineEdit_3.setText(str(demodulated))
                    else:
                        error = QMessageBox()
                        error.setWindowTitle("Ошибка")
                        error.setText("Диапазон значений: [0-4]")
                        error.setIcon(QMessageBox.Warning)
                        error.exec_()
                else:
                    error = QMessageBox()
                    error.setWindowTitle("Ошибка")
                    error.setText("Максимальная длинна сообщения 4 символа!")
                    error.setIcon(QMessageBox.Warning)
                    error.exec_()
        if self.comboBox.currentText() == "КАМ-16":
            if self.lineEdit_3.text() == "" or self.lineEdit.text() == "":
                error = QMessageBox()
                error.setWindowTitle("Ошибка")
                error.setText("Введите сообщение")
                error.setIcon(QMessageBox.Warning)
                error.exec_()
            else:
                if len(str(self.lineEdit.text())) < 32:
                    modem = QAMModem(16,
                                     bin_input=False,
                                     soft_decision=False,
                                     bin_output=False)

                    msg = [int(x) for x in str(self.lineEdit.text()).split() if x.isdigit()]
                    for item in msg:
                        if item > 15:
                            count += 1
                    if count == 0:
                        modulated = modem.modulate(msg)  # modulation
                        demodulated = modem.demodulate(modulated)
                        self.lineEdit_3.setText(str(demodulated))
                    else:
                        error = QMessageBox()
                        error.setWindowTitle("Ошибка")
                        error.setText("Диапазон значений: [0-16]")
                        error.setIcon(QMessageBox.Warning)
                        error.exec_()
                else:
                    error = QMessageBox()
                    error.setWindowTitle("Ошибка")
                    error.setText("Максимальная длинна сообщения 16 символа!")
                    error.setIcon(QMessageBox.Warning)
                    error.exec_()
        if self.comboBox.currentText() == "КАМ-64":
            if self.lineEdit_3.text() == "" or self.lineEdit.text() == "":
                error = QMessageBox()
                error.setWindowTitle("Ошибка")
                error.setText("Введите сообщение")
                error.setIcon(QMessageBox.Warning)
                error.exec_()
            else:
                if len(str(self.lineEdit.text())) < 128:
                    modem = QAMModem(64,
                                     bin_input=False,
                                     soft_decision=False,
                                     bin_output=False)

                    msg = [int(x) for x in str(self.lineEdit.text()).split() if x.isdigit()]
                    for item in msg:
                        if item > 63:
                            count += 1
                    if count == 0:
                        modulated = modem.modulate(msg)  # modulation
                        demodulated = modem.demodulate(modulated)
                        self.lineEdit_3.setText(str(demodulated))
                    else:
                        error = QMessageBox()
                        error.setWindowTitle("Ошибка")
                        error.setText("Диапазон значений: [0-64]")
                        error.setIcon(QMessageBox.Warning)
                        error.exec_()
                else:
                    error = QMessageBox()
                    error.setWindowTitle("Ошибка")
                    error.setText("Максимальная длинна сообщения 64 символа!")
                    error.setIcon(QMessageBox.Warning)
                    error.exec_()
        if self.comboBox.currentText() == "КАМ-256":
            if self.lineEdit_3.text() == "" or self.lineEdit.text() == "":
                error = QMessageBox()
                error.setWindowTitle("Ошибка")
                error.setText("Введите сообщение")
                error.setIcon(QMessageBox.Warning)
                error.exec_()
            else:
                if len(str(self.lineEdit.text())) < 512:
                    modem = QAMModem(256,
                                     bin_input=False,
                                     soft_decision=False,
                                     bin_output=False)

                    msg = [int(x) for x in str(self.lineEdit.text()).split() if x.isdigit()]
                    for item in msg:
                        if item > 255:
                            count += 1
                    if count == 0:
                        modulated = modem.modulate(msg)  # modulation
                        demodulated = modem.demodulate(modulated)
                        self.lineEdit_3.setText(str(demodulated))
                    else:
                        error = QMessageBox()
                        error.setWindowTitle("Ошибка")
                        error.setText("Диапазон значений: [0-256]")
                        error.setIcon(QMessageBox.Warning)
                        error.exec_()
                else:
                    error = QMessageBox()
                    error.setWindowTitle("Ошибка")
                    error.setText("Максимальная длинна сообщения 256 символа!")
                    error.setIcon(QMessageBox.Warning)
                    error.exec_()
        if self.comboBox.currentText() == "":
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Выберите вид модуляции")
            error.setIcon(QMessageBox.Warning)
            error.exec_()
    def click_4(self):
        def BER_calc(a, b):
            num_ber = np.sum(np.abs(a - b))
            ber = np.mean(np.abs(a - b))
            return int(num_ber), ber

        def BER_qam(M, EbNo):
            EbNo_lin = 10 ** (EbNo / 10)
            Q=self.comboBox.currentText()
            if M > Q:
                P = 2 * np.sqrt((np.sqrt(M) - 1) /
                                (np.sqrt(M) * np.log2(M))) * special.erfc(
                    np.sqrt(EbNo_lin * 3 * np.log2(M) / 2 * (M - 1)))
            else:
                P = 0.5 * special.erfc(np.sqrt(EbNo_lin))
            return P

        EbNos = np.array([i for i in range(int(self.lineEdit_5.text()))])  # массив Eb/No в дБ Eb - энергия сигнала, приходящейся на 1 бит принимаемого сообщения
        # No энергетическая спектральная плотность шума (N0)
        N = int(self.lineEdit_2.text())# колл-во символов в кадре
        N_c = int(self.lineEdit_4.text())  # количество испытаний

        Ms = [4, 16, 64, 256]  # порядок модуляции

        ''' Simulation loops '''

        mean_BER = np.empty((len(EbNos), len(Ms)))
        for idxM, M in enumerate(Ms):
            # print("Modulation order: ", M)
            BER = np.empty((N_c,))
            k = np.log2(M)  # количество бит на символ модуляции

            modem = QAMModem(M,
                             bin_input=True,
                             soft_decision=False,
                             bin_output=True)

            for idxEbNo, EbNo in enumerate(EbNos):
                # print("Eb/No: ", EbNo)
                snrdB = EbNo + 10 * np.log10(k)  # Отношение сигнал/шум (в дБ)
                noiseVar = 10 ** (-snrdB / 10)  # дисперсия шума (мощность)


                for cntr in range(N_c):
                    message_bits = np.random.randint(0, 2, int(N * k))  # message
                    modulated = modem.modulate(message_bits)  # modulation

                    Es = np.mean(np.abs(modulated) ** 2)  # энергия символа
                    No = Es / ((10 ** (EbNo / 10)) * np.log2(M))  # плотность спектра шума

                    noisy = modulated + np.sqrt(No / 2) * \
                            (np.random.randn(modulated.shape[0]) +
                             1j * np.random.randn(modulated.shape[0]))  # АБГШ

                    demodulated = modem.demodulate(noisy, noise_var=noiseVar)
                    NumErr, BER[cntr] = BER_calc(message_bits,
                                                 demodulated)  # коэффициент битовых ошибок
                mean_BER[idxEbNo, idxM] = np.mean(BER, axis=0)  # усредненный коэффициент битовых ошибок

        ''' Theoretical results '''

        BER_theor = np.empty((len(EbNos), len(Ms)))
        for idxM, M in enumerate(Ms):
            BER_theor[:, idxM] = BER_qam(M, EbNos)

        ''' Curves '''

        fig, ax = plt.subplots(figsize=(10, 6), dpi=100)

        plt.semilogy(EbNos, BER_theor[:, 0], 'g-', label='4-QAM (теоретический результат)')
        plt.semilogy(EbNos, BER_theor[:, 1], 'b-', label='16-QAM (теоретический результат)')
        plt.semilogy(EbNos, BER_theor[:, 2], 'k-', label='64-QAM (теоретический результат)')
        plt.semilogy(EbNos, BER_theor[:, 3], 'r-', label='256-QAM (теоретический результат)')

        plt.semilogy(EbNos, mean_BER[:, 0], 'g-o', label='4-QAM (смоделированный релуьтат)')
        plt.semilogy(EbNos, mean_BER[:, 1], 'b-o', label='16-QAM (смоделированный релуьтат)')
        plt.semilogy(EbNos, mean_BER[:, 2], 'k-o', label='64-QAM (смоделированный релуьтат)')
        plt.semilogy(EbNos, mean_BER[:, 3], 'r-o', label='256-QAM (смоделированный релуьтат)')

        ax.set_ylim(1e-7, 2)
        ax.set_xlim(0, 25.1)
        plt.title("M-QAM")
        plt.xlabel('Eb/No (dB)')
        plt.ylabel('BER')
        plt.grid()
        plt.legend(loc='upper right')
        plt.show()

#
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
