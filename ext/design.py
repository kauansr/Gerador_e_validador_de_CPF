from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(756, 265)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(490, 59, 61, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 61, 31))
        self.label_2.setObjectName("label_2")
        self.input_valida_cpf = QtWidgets.QLineEdit(self.centralwidget)
        self.input_valida_cpf.setGeometry(QtCore.QRect(80, 10, 461, 31))
        self.input_valida_cpf.setObjectName("input_valida_cpf")
        self.btn_valida = QtWidgets.QPushButton(self.centralwidget)
        self.btn_valida.setGeometry(QtCore.QRect(550, 10, 200, 31))
        self.btn_valida.setMinimumSize(QtCore.QSize(200, 0))
        self.btn_valida.setObjectName("btn_valida")
        self.gera_cpf = QtWidgets.QPushButton(self.centralwidget)
        self.gera_cpf.setGeometry(QtCore.QRect(550, 60, 201, 31))
        self.gera_cpf.setObjectName("gera_cpf")
        self.label_retorno = QtWidgets.QLineEdit(self.centralwidget)
        self.label_retorno.setGeometry(QtCore.QRect(22, 200, 721, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_retorno.setFont(font)
        self.label_retorno.setStyleSheet("color: green;")
        self.label_retorno.setAlignment(QtCore.Qt.AlignCenter)
        self.label_retorno.setObjectName("label_retorno")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gerador e Validador de CPF"))
        self.label.setText(_translate("MainWindow", "Gerar CPF:"))
        self.label_2.setText(_translate("MainWindow", "Validar CPF:"))
        self.btn_valida.setText(_translate("MainWindow", "VALIDAR"))
        self.gera_cpf.setText(_translate("MainWindow", "GERAR"))
