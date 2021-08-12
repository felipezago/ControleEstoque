from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from Funcoes.utils import exec_app
from Model.Vendas_Header import Vendas_Header


class AbrirVenda(QMainWindow):
    def __init__(self, parent=None):
        super(AbrirVenda, self).__init__(parent)
        from View.abrir_venda import Ui_Frame

        self.ui = Ui_Frame()
        self.ui.setupUi(self)
        self.dialogs = list()
        self.tamanho = self.size()
        self.setFixedSize(self.tamanho)

        self.setWindowIcon(QtGui.QIcon("Imagens/logo_fzr.png"))

        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

        self.ui.bt_busca.clicked.connect(self.pesquisar)
        self.ui.tx_codigo.returnPressed.connect(self.pesquisar)

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        self.setFixedSize(self.tamanho)

    def pesquisar(self):
        if self.ui.tx_codigo.text():
            header = Vendas_Header()
            header.id = self.ui.tx_codigo.text()
            v = header.get_venda_pendente_by_id()

            if v is not None:
                self.abrir_venda()
                self.close()
            else:
                QMessageBox.information(self, "Aviso!", "Não há venda pendente com esse código.")
                self.ui.tx_codigo.setText("")
        else:
            self.pesquisar_venda()

    def abrir_venda(self):
        from Controller.venda import VendaTemp

        nova_venda = VendaTemp(cod_venda=self.ui.tx_codigo.text())
        exec_app(nova_venda)
        self.dialogs.append(nova_venda)

    def pesquisar_venda(self):
        from Controller.lista_vendas import ListaVendas

        if Vendas_Header.check_pendentes() != 0:
            l_vendas = ListaVendas(self)
            exec_app(l_vendas)
            self.dialogs.append(l_vendas)
            self.close()
        else:
            QMessageBox.information(self, "Aviso!", "Não existem vendas pendentes.")
            self.ui.tx_codigo.setText("")
