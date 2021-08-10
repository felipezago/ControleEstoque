from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem

from Model.Compra_Fin import Compra_Fin
from Model.Compra_Header import Compras_Header
from Model.Compra_Itens import Compra_Itens
from Model.Fornecedor import Fornecedor
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt


class DetalhesCompra(QMainWindow):
    def __init__(self, parent=None, cod_compra=""):
        super(DetalhesCompra, self).__init__(parent)
        from View.detalhes_compra import Ui_Frame

        self.ui = Ui_Frame()
        self.ui.setupUi(self)
        self.dialogs = list()
        self.tamanho_tela = self.size()
        self.setFixedSize(self.tamanho_tela)

        self.setWindowModality(QtCore.Qt.ApplicationModal)

        self.compra_selecionada = Compras_Header()
        self.compra_selecionada.id = cod_compra
        self.compra_selecionada.fornecedor = Fornecedor()

        cod_forn = self.compra_selecionada.retorna_cod_forn()

        self.compra_selecionada.fornecedor.id = cod_forn
        forn = self.compra_selecionada.fornecedor.get_fornecedor_by_id()
        self.compra_selecionada.fornecedor.nome = forn[1]

        datahora = self.compra_selecionada.retorna_hora()
        data_e_hora_em_texto = datahora.strftime('%d/%m/%Y %H:%M:%S')
        self.compra_selecionada.datahora = data_e_hora_em_texto

        self.tela = parent

        self.ui.bt_cancelar.clicked.connect(self.sair)
        self.ui.bt_excluir.clicked.connect(self.excluir)

        self.ui.tb_itens.setColumnWidth(0, 20)
        self.ui.tb_itens.setColumnWidth(1, 400)
        self.ui.tb_itens.setColumnWidth(2, 50)
        self.ui.tb_itens.setColumnWidth(3, 100)
        self.ui.tb_itens.setColumnWidth(4, 135)

        self.ui.tb_fin.setColumnWidth(0, 200)
        self.ui.tb_fin.setColumnWidth(1, 110)

        for c in range(0, 5):
            self.ui.tb_itens.horizontalHeaderItem(c).setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        for c in range(0, 2):
            self.ui.tb_fin.horizontalHeaderItem(c).setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.dados_tabela_itens()
        self.dados_tabela_fin()
        self.set_lbl()

    def set_lbl(self):
        self.ui.lb_compra.setText(f"Compra - Código {self.compra_selecionada.id}")
        self.ui.lb_hora.setText(f"{self.compra_selecionada.datahora}")
        self.ui.lb_cliente.setText(f"{self.compra_selecionada.fornecedor.nome}")

        c = Compra_Itens()
        c.id_compra = self.compra_selecionada.id
        self.ui.lb_total_itens.setText(f"R$ {c.retorna_total()}")

    def resizeEvent(self, a0: QtGui.QResizeEvent):
        self.resize(self.tamanho_tela)

    def sair(self):
        self.close()

    def dados_tabela_itens(self):
        self.ui.tb_itens.clearContents()
        self.ui.tb_itens.setRowCount(0)

        itens = Compra_Itens()
        itens.id_compra = self.compra_selecionada.id
        dados = itens.detalhes_compra()

        for i, linha in enumerate(dados):

            self.ui.tb_itens.insertRow(i)
            for c in range(0, 5):
                self.ui.tb_itens.setItem(i, c, QTableWidgetItem(str(linha[c])))

    def dados_tabela_fin(self):
        self.ui.tb_fin.clearContents()
        self.ui.tb_fin.setRowCount(0)

        c_fin = Compra_Fin()
        c_fin.compra_id = self.compra_selecionada.id

        dados = c_fin.get_fins_compra_pdf()

        for i, linha in enumerate(dados):

            self.ui.tb_fin.insertRow(i)
            for c in range(0, 2):
                self.ui.tb_fin.setItem(i, c, QTableWidgetItem(str(linha[c])))

    def excluir(self):

        reply = QMessageBox.question(self, 'Excluir?', f'Tem certeza que deseja excluir a compra: '
                                                       f'{self.compra_selecionada.id}?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

        if reply == QMessageBox.Yes:
            try:
                self.compra_selecionada.delete_compra()
                self.compra_selecionada.id = None
            except Exception as error:
                QMessageBox.warning(self, "Erro", str(error))
            else:
                QMessageBox.information(self, "Sucesso!", "Compra excluída com sucesso!")
                from Controller.lista_compras import ListaCompras
                from Funcoes.utils import exec_app

                lista_c = ListaCompras()
                exec_app(lista_c)
                self.dialogs.append(lista_c)

                self.close()
        else:
            return
