from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QPushButton
from Model.Compra_Header import Compras_Header
from Model.Fornecedor import Fornecedor
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt


class ListaCompras(QMainWindow):
    def __init__(self, parent=None):
        super(ListaCompras, self).__init__(parent)
        from View.lista_compras import Ui_Frame

        self.ui = Ui_Frame()
        self.ui.setupUi(self)
        self.dialogs = list()
        self.tamanho_tela = self.size()
        self.setFixedSize(self.tamanho_tela)

        self.setWindowIcon(QtGui.QIcon("Imagens/logo_fzr.png"))

        self.setWindowModality(QtCore.Qt.ApplicationModal)

        self.compra_selecionada = Compras_Header()
        self.linha_selecionada = None
        self.filtrado = False
        self.tela = parent

        # ação da busca
        self.ui.bt_busca.clicked.connect(self.buscar)
        self.ui.tx_busca.returnPressed.connect(self.buscar)

        # ação dos botoes
        self.ui.bt_refresh.clicked.connect(self.dados_tabela)

        # signals
        self.ui.tx_busca.textChanged.connect(self.formatar_texto)
        self.ui.cb_vendas.currentIndexChanged.connect(self.limpa_campo_busca)

        self.ui.tb_compras.setColumnWidth(0, 20)
        self.ui.tb_compras.setColumnWidth(1, 350)
        self.ui.tb_compras.setColumnWidth(2, 150)
        self.ui.tb_compras.setColumnWidth(3, 100)
        self.ui.tb_compras.setColumnWidth(4, 135)
        self.ui.tb_compras.setColumnWidth(5, 100)

        for c in range(0, 5):
            self.ui.tb_compras.horizontalHeaderItem(c).setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.dados_tabela()

    def resizeEvent(self, a0: QtGui.QResizeEvent):
        self.resize(self.tamanho_tela)

    def limpa_campo_busca(self):
        self.ui.tx_busca.setText("")

    def formatar_texto(self):
        texto = self.ui.tx_busca.text()
        tamanho = len(texto)
        if self.ui.cb_vendas.currentIndex() == 0:
            if not texto[tamanho - 1:tamanho].isnumeric():
                self.ui.tx_busca.setText(texto[:tamanho - 1])

    def sair(self):
        self.close()

    def dados_tabela(self):
        self.ui.tx_busca.setText("")
        self.filtrado = False
        self.ui.bt_refresh.setEnabled(False)
        self.ui.tb_compras.clearContents()
        self.ui.tb_compras.setRowCount(0)

        dados = Compras_Header.get_compras()

        for i, linha in enumerate(dados):

            self.ui.tb_compras.insertRow(i)
            for c in range(0, 5):
                if c == 4:
                    btn_detalhes = QPushButton(self.ui.tb_compras)
                    btn_detalhes.setText("DETALHES")
                    btn_detalhes.setStyleSheet("""
                                                    background-color: #E8DCDC;
                                                    color: black;
                                                """)

                    self.ui.tb_compras.setCellWidget(i, c, btn_detalhes)
                    btn_detalhes.clicked.connect(self.detalhes_compra)
                else:
                    self.ui.tb_compras.setItem(i, c, QTableWidgetItem(str(linha[c])))

    def buscar(self):
        self.ui.tb_compras.clearContents()
        self.ui.tb_compras.setRowCount(0)

        compra = Compras_Header()
        compra.fornecedor = Fornecedor()
        dados = ""

        if self.ui.cb_vendas.currentIndex() == 0:
            compra.id = self.ui.tx_busca.text()
            if compra.id:
                dados = compra.busca_compras_by_id()
            else:
                QMessageBox.warning(self, "Atenção!", "Favor informar algum valor!")
                self.dados_tabela()
                return
        elif self.ui.cb_vendas.currentIndex() == 1:
            compra.fornecedor.nome = self.ui.tx_busca.text().upper()
            dados_fornecedor = compra.fornecedor.get_fornecedores_by_desc("forn_nome", compra.fornecedor.nome)

            if compra.fornecedor.nome:
                if dados_fornecedor:
                    if type(dados_fornecedor) == list:
                        cods = list()
                        for item in dados_fornecedor:
                            cods.append(item[0])
                        tup = tuple(cods)
                        compra.fornecedor.id = tup
                        dados = compra.busca_compras_by_forn("in")
                    else:
                        compra.fornecedor.id = dados_fornecedor[0]
                        dados = compra.busca_compras_by_forn("=")
            else:
                QMessageBox.warning(self, "Atenção!", "Favor informar algum valor!")
                self.dados_tabela()
                return

        if dados:
            self.filtrado = True
            self.ui.bt_refresh.setEnabled(True)

            for i, linha in enumerate(dados):

                self.ui.tb_compras.insertRow(i)
                for c in range(0, 5):
                    if c == 4:
                        btn_detalhes = QPushButton(self.ui.tb_compras)
                        btn_detalhes.setText("DETALHES")
                        btn_detalhes.setStyleSheet("""
                                                        background-color: #E8DCDC;
                                                        color: black;
                                                    """)

                        self.ui.tb_compras.setCellWidget(i, c, btn_detalhes)
                        btn_detalhes.clicked.connect(self.detalhes_compra)
                    else:
                        self.ui.tb_compras.setItem(i, c, QTableWidgetItem(str(linha[c])))
        else:
            QMessageBox.warning(self, "Erro", "Não foi encontrado nenhum registro!")
            self.ui.tx_busca.setText("")
            self.dados_tabela()

        self.ui.tb_compras.selectRow(0)

    def detalhes_compra(self):
        id_compra = self.ui.tb_compras.item(self.ui.tb_compras.currentRow(), 0).text()

        from Controller.detalhes_compra import DetalhesCompra
        from Funcoes.utils import exec_app

        det_compra = DetalhesCompra(cod_compra=id_compra)
        exec_app(det_compra)
        self.dialogs.append(det_compra)
        self.close()
