from PyQt5.QtGui import QColor, QBrush
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QPushButton
from Model.Cliente import Cliente
from Model.Venda_Fin import Venda_Fin
from Model.Venda_Itens import Vendas
from Model.Vendas_Header import Vendas_Header
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt


class ListaVendas(QMainWindow):
    def __init__(self, parent=None):
        super(ListaVendas, self).__init__(parent)
        from View.lista_vendas import Ui_Frame

        self.ui = Ui_Frame()
        self.ui.setupUi(self)
        self.dialogs = list()
        self.tamanho_tela = self.size()
        self.setFixedSize(self.tamanho_tela)

        self.setWindowModality(QtCore.Qt.ApplicationModal)

        self.venda_selecionada = Vendas_Header()
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

        if self.tela:
            self.ui.cb_vendas.setCurrentIndex(2)
            self.ui.bt_refresh.setEnabled(False)
            self.ui.cb_vendas.setEnabled(False)

    def resizeEvent(self, a0: QtGui.QResizeEvent):
        self.resize(self.tamanho_tela)

    def limpa_campo_busca(self):
        self.ui.tx_busca.setText("")
        if self.ui.cb_vendas.currentIndex() in (2, 3):
            self.ui.tx_busca.setEnabled(False)
            self.ui.bt_busca.setEnabled(False)
            self.ui.bt_refresh.setEnabled(False)
            self.buscar()
        else:
            self.ui.tx_busca.setEnabled(True)
            self.ui.bt_busca.setEnabled(True)

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
        self.ui.tb_vendas.clearContents()
        self.ui.tb_vendas.setRowCount(0)

        dados = Vendas_Header.get_vendas()

        for i, linha in enumerate(dados):

            self.ui.tb_vendas.insertRow(i)
            for c in range(0, 7):
                if c == 6:
                    item = QTableWidgetItem(str(linha[6]))
                    if linha[6] == "PENDENTE":
                        fin = Venda_Fin()
                        fin.venda_id = linha[0]
                        pago = fin.valor_pago()

                        total = linha[5] - pago
                        self.ui.tb_vendas.setItem(i, 5, QTableWidgetItem(str(total)))

                        btn_editar = QPushButton(self.ui.tb_vendas)
                        btn_editar.setText("ABRIR VENDA")
                        btn_editar.setStyleSheet("""
                                background-color: #E8DCDC;
                                color: black;
                        """)

                        self.ui.tb_vendas.setCellWidget(i, 7, btn_editar)
                        btn_editar.clicked.connect(self.abrir_venda)

                        item.setForeground(QBrush(QColor(255, 0, 0)))
                        self.ui.tb_vendas.setItem(i, 6, item)
                    else:
                        btn_exc = QPushButton(self.ui.tb_vendas)
                        btn_exc.setText("DETALHES")
                        btn_exc.setStyleSheet("""
                            background-color: #E8DCDC;
                            color: black;
                        """)

                        self.ui.tb_vendas.setCellWidget(i, 7, btn_exc)
                        btn_exc.clicked.connect(self.detalhes_venda)

                        item.setForeground(QBrush(QColor(103, 194, 0)))
                        self.ui.tb_vendas.setItem(i, 6, item)
                elif c == 2:
                    if linha[2] is None:
                        self.ui.tb_vendas.setItem(i, 2, QTableWidgetItem("SEM VEICULO"))
                    else:
                        self.ui.tb_vendas.setItem(i, 2, QTableWidgetItem(str(linha[c])))
                else:
                    self.ui.tb_vendas.setItem(i, c, QTableWidgetItem(str(linha[c])))

    def buscar(self):
        self.ui.tb_vendas.clearContents()
        self.ui.tb_vendas.setRowCount(0)

        venda = Vendas_Header()
        venda.cliente = Cliente()
        dados = ""

        if self.ui.cb_vendas.currentIndex() == 0:
            venda.id = self.ui.tx_busca.text()
            if venda.id:
                dados = venda.busca_vendas_by_id()
            else:
                QMessageBox.warning(self, "Atenção!", "Favor informar algum valor!")
                self.dados_tabela()
                return
        elif self.ui.cb_vendas.currentIndex() == 1:
            venda.cliente.nome = self.ui.tx_busca.text().upper()
            if venda.cliente.nome:
                dados_cliente = venda.cliente.get_cliente_by_desc("clie_nome", venda.cliente.nome)

                if dados_cliente:
                    if len(dados_cliente) > 1:
                        cods = list()
                        for item in dados_cliente:
                            cods.append(item[0])
                        tup = tuple(cods)
                        venda.cliente.id = tup
                        dados = venda.busca_vendas_by_cliente("in")
                    else:
                        venda.cliente.id = dados_cliente[0][0]
                        dados = venda.busca_vendas_by_cliente("=")
            else:
                QMessageBox.warning(self, "Atenção!", "Favor informar algum valor!")
                self.dados_tabela()
                return
        elif self.ui.cb_vendas.currentIndex() == 2:
            venda.status = "PENDENTE"
            dados = venda.busca_vendas_by_status()
        else:
            venda.status = "FINALIZADO"
            dados = venda.busca_vendas_by_status()

        if dados:
            self.filtrado = True
            self.ui.bt_refresh.setEnabled(True)

            for i, linha in enumerate(dados):
                self.ui.tb_vendas.insertRow(i)
                for c in range(0, 7):
                    if c == 6:
                        item = QTableWidgetItem(str(linha[6]))
                        if linha[6] == "PENDENTE":
                            fin = Venda_Fin()
                            fin.venda_id = linha[0]
                            pago = fin.valor_pago()

                            total = linha[5] - pago
                            self.ui.tb_vendas.setItem(i, 5, QTableWidgetItem(str(total)))

                            btn_editar = QPushButton(self.ui.tb_vendas)
                            btn_editar.setText("ABRIR VENDA")
                            btn_editar.setStyleSheet("""
                                    background-color: #E8DCDC;
                                    color: black;
                            """)

                            self.ui.tb_vendas.setCellWidget(i, 7, btn_editar)
                            btn_editar.clicked.connect(self.abrir_venda)

                            item.setForeground(QBrush(QColor(255, 0, 0)))
                            self.ui.tb_vendas.setItem(i, 6, item)
                        else:
                            btn_exc = QPushButton(self.ui.tb_vendas)
                            btn_exc.setText("DETALHES")
                            btn_exc.setStyleSheet("""
                                background-color: #E8DCDC;
                                color: black;
                            """)

                            self.ui.tb_vendas.setCellWidget(i, 7, btn_exc)
                            btn_exc.clicked.connect(self.detalhes_venda)

                            item.setForeground(QBrush(QColor(103, 194, 0)))
                            self.ui.tb_vendas.setItem(i, 6, item)
                    elif c == 2:
                        if linha[2] is None:
                            self.ui.tb_vendas.setItem(i, 2, QTableWidgetItem("SEM VEICULO"))
                        else:
                            self.ui.tb_vendas.setItem(i, 2, QTableWidgetItem(str(linha[c])))
                    else:
                        self.ui.tb_vendas.setItem(i, c, QTableWidgetItem(str(linha[c])))
        else:
            QMessageBox.warning(self, "Erro", "Não foi encontrado nenhum registro!")
            self.ui.tx_busca.setText("")
            self.dados_tabela()

        self.ui.tb_vendas.selectRow(0)

    def abrir_venda(self):
        id_venda = self.ui.tb_vendas.item(self.ui.tb_vendas.currentRow(), 0).text()

        from Controller.venda import VendaTemp
        from Funcoes.utils import exec_app

        abrir_venda = VendaTemp(cod_venda=id_venda)
        exec_app(abrir_venda)
        self.dialogs.append(abrir_venda)
        self.close()

    def detalhes_venda(self):
        id_venda = self.ui.tb_vendas.item(self.ui.tb_vendas.currentRow(), 0).text()

        from Controller.detalhes_venda import DetalhesVenda
        from Funcoes.utils import exec_app

        det_venda = DetalhesVenda(cod_venda=id_venda)
        exec_app(det_venda)
        self.dialogs.append(det_venda)
        self.close()

