from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QPushButton
from Model.Vendas_Header import Vendas_Header
from PyQt5 import QtCore
from PyQt5.QtCore import Qt


class ListaVendas(QMainWindow):
    def __init__(self, parent=None):
        super(ListaVendas, self).__init__(parent)
        from View.lista_vendas import Ui_Frame

        self.ui = Ui_Frame()
        self.ui.setupUi(self)
        self.dialogs = list()
        self.setFixedSize(self.size())

        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

        self.venda_selecionada = Vendas_Header()
        self.linha_selecionada = None
        self.filtrado = False

        # ação dos botoes
        self.ui.bt_refresh.clicked.connect(self.dados_tabela)

        # signals
        self.ui.tx_busca.textChanged.connect(self.formatar_texto)
        self.ui.cb_vendas.currentIndexChanged.connect(self.limpa_campo_busca)

        self.ui.tb_vendas.setColumnWidth(0, 20)
        self.ui.tb_vendas.setColumnWidth(1, 200)
        self.ui.tb_vendas.setColumnWidth(2, 150)
        self.ui.tb_vendas.setColumnWidth(3, 100)
        self.ui.tb_vendas.setColumnWidth(4, 135)
        self.ui.tb_vendas.setColumnWidth(5, 100)
        self.ui.tb_vendas.setColumnWidth(6, 100)
        self.ui.tb_vendas.setColumnWidth(7, 110)

        for c in range(0, 8):
            self.ui.tb_vendas.horizontalHeaderItem(c).setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.dados_tabela()

    def limpa_campo_busca(self):
        self.ui.tx_busca.setText("")

    def formatar_texto(self):
        texto = self.ui.tx_busca.text()
        tamanho = len(texto)
        if self.ui.cb_vendas.currentIndex() == 0:
            if not texto[tamanho-1:tamanho].isnumeric():
                self.ui.tx_busca.setText(texto[:tamanho - 1])

    def sair(self):
        self.close()

    def dados_tabela(self):
        self.ui.tx_busca.setText("")
        self.filtrado = False
        self.ui.bt_refresh.setEnabled(False)
        self.ui.tb_vendas.clearContents()
        self.ui.tb_vendas.setRowCount(0)

        dados = Vendas_Header.get_vendas()

        for i, linha in enumerate(dados):

            self.ui.tb_vendas.insertRow(i)
            for c in range(0, 7):
                self.ui.tb_vendas.setItem(i, c, QTableWidgetItem(str(linha[c])))

            if linha[6] == "PENDENTE":
                btn_editar = QPushButton(self.ui.tb_vendas)
                btn_editar.setText("ABRIR VENDA")
                self.ui.tb_vendas.setCellWidget(i, 7, btn_editar)
                btn_editar.clicked.connect(self.abrir_venda)

    def abrir_venda(self):
        id_venda = self.ui.tb_vendas.item(self.ui.tb_vendas.currentRow(), 0).text()

        from Controller.venda import VendaTemp
        from Funcoes.utils import exec_app

        abrir_venda = VendaTemp(cod_venda=id_venda)
        exec_app(abrir_venda)
        self.dialogs.append(abrir_venda)

    def excluir(self):
        if self.venda_selecionada.id:
            reply = QMessageBox.question(self, 'Excluir?', f'Tem certeza que deseja excluir a venda: '
                                                           f'{self.venda_selecionada.id}?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

            if reply == QMessageBox.Yes:
                try:
                    self.venda_selecionada.delete()
                    self.venda_selecionada.id = None
                except Exception as error:
                    QMessageBox.warning(self, "Erro", str(error))
                else:
                    self.ui.tb_vendas.removeRow(self.linha_selecionada)
            else:
                return
        else:
            QMessageBox.warning(self, "Atenção!", "Favor selecionar alguma linha!")
