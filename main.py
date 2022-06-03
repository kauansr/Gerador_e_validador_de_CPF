from ext.validacpf import valida_cpf
from ext.geradorcpf import geracao_cpf
from ext.design import *
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class Gera_valida_cpf(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.gera_cpf.clicked.connect(self.geracao_cpf)
        self.btn_valida.clicked.connect(self.valida_cpf)

    def geracao_cpf(self):
        self.label_retorno.setText(
            str(geracao_cpf()))

    def valida_cpf(self):
        cpf = self.input_valida_cpf.text()
        self.label_retorno.setText(
            str(valida_cpf(cpf)))


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    geravalida = Gera_valida_cpf()
    geravalida.show()
    qt.exec_()