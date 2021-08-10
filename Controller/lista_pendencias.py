from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QPushButton
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt

from Model.Cliente import Cliente
from Model.Pendencias import Pendencias
from Model.Venda_Fin import Venda_Fin


class ListaPendencias(QMainWindow):
    def __init__(self, parent=None):
        super(ListaPendencias, self).__init__(parent)
        from View.pendencias import Ui_Frame

        self.ui = Ui_Frame()
        self.ui.setupUi(self)
        self.dialogs = list()
        self.tamanho_tela = self.size()
        self.setFixedSize(self.tamanho_tela)

        self.setWindowModality(QtCore.Qt.ApplicationModal)

        self.pend_selecionada = Pendencias()
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

        self.ui.tb_pend.setColumnWidth(0, 20)
        self.ui.tb_pend.setColumnWidth(1, 20)
        self.ui.tb_pend.setColumnWidth(2, 250)
        self.ui.tb_pend.setColumnWidth(3, 100)
        self.ui.tb_pend.setColumnWidth(4, 135)
        self.ui.tb_pend.setColumnWidth(5, 100)
        self.ui.tb_pend.setColumnWidth(5, 100)

        for c in range(0, 7):
            self.ui.tb_pend.horizontalHeaderItem(c).setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

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
        self.ui.tb_pend.clearContents()
        self.ui.tb_pend.setRowCount(0)

        dados = Pendencias.todas_pendencias()

        for i, linha in enumerate(dados):

            self.ui.tb_pend.insertRow(i)
            for c in range(0, 3):
                self.ui.tb_pend.setItem(i, c, QTableWidgetItem(str(linha[c])))

            v_fin = Venda_Fin()
            v_fin.venda_id = linha[1]
            valor_pago = v_fin.valor_pago()
            item_valor_pago = QTableWidgetItem(f"{valor_pago:.2f}")
            item_valor_pago.setForeground(QBrush(QColor(103, 194, 0)))

            total = linha[3] + valor_pago
            item_total = QTableWidgetItem(f"{total:.2f}")
            item_total.setForeground(QBrush(QColor(255, 20, 20)))

            restante = total - valor_pago
            item_restante = QTableWidgetItem(f"{restante:.2f}")
            item_restante.setForeground(QBrush(QColor(255, 180, 0)))

            self.ui.tb_pend.setItem(i, 3, item_total)
            self.ui.tb_pend.setItem(i, 4, item_valor_pago)
            self.ui.tb_pend.setItem(i, 5, item_restante)

            btn_abrir = QPushButton(self.ui.tb_pend)
            btn_abrir.setText("ABRIR VENDA")
            btn_abrir.setStyleSheet("""
                                   background-color: #E8DCDC;
                                   color: black;
                                """)

            self.ui.tb_pend.setCellWidget(i, 6, btn_abrir)
            btn_abrir.clicked.connect(self.abrir_venda)

    def buscar(self):
        self.ui.tb_pend.clearContents()
        self.ui.tb_pend.setRowCount(0)

        pendencias = Pendencias()
        pendencias.cliente = Cliente()
        dados = ""

        if self.ui.cb_vendas.currentIndex() == 0:
            pendencias.id = self.ui.tx_busca.text()
            if pendencias.id:
                dados = pendencias.busca_pendencias_by_id()
            else:
                QMessageBox.warning(self, "Atenção!", "Favor informar algum valor!")
                self.dados_tabela()
                return
        elif self.ui.cb_vendas.currentIndex() == 1:
            pendencias.cliente.nome = self.ui.tx_busca.text().upper()
            dados_cliente = pendencias.cliente.get_cliente_by_desc("clie_nome", pendencias.cliente.nome)

            if pendencias.cliente.nome:
                if dados_cliente:
                    if type(dados_cliente) == list:
                        cods = list()
                        for item in dados_cliente:
                            cods.append(item[0])
                        tup = tuple(cods)
                        pendencias.cliente.id = tup
                        dados = pendencias.busca_pendencias_by_cliente("in")
                    else:
                        pendencias.cliente.id = dados_cliente[0]
                        dados = pendencias.busca_pendencias_by_cliente("=")
            else:
                QMessageBox.warning(self, "Atenção!", "Favor informar algum valor!")
                self.dados_tabela()
                return

        if dados:
            self.filtrado = True
            self.ui.bt_refresh.setEnabled(True)

            for i, linha in enumerate(dados):

                self.ui.tb_pend.insertRow(i)
                for c in range(0, 4):
                    self.ui.tb_pend.setItem(i, c, QTableWidgetItem(str(linha[c])))

                v_fin = Venda_Fin()
                v_fin.venda_id = linha[1]
                valor_pago = v_fin.valor_pago()
                self.ui.tb_pend.setItem(i, 4, QTableWidgetItem(str(valor_pago)))

                restante = valor_pago - linha[3]
                self.ui.tb_pend.setItem(i, 5, QTableWidgetItem(str(restante)))

                btn_abrir = QPushButton(self.ui.tb_pend)
                btn_abrir.setText("ABRIR VENDA")
                btn_abrir.setStyleSheet("""
                                       background-color: #E8DCDC;
                                       color: black;
                                    """)

                self.ui.tb_pend.setCellWidget(i, 6, btn_abrir)
                btn_abrir.clicked.connect(self.abrir_venda)
        else:
            QMessageBox.warning(self, "Erro", "Não foi encontrado nenhum registro!")
            self.ui.tx_busca.setText("")
            self.dados_tabela()

        self.ui.tb_pend.selectRow(0)

    def abrir_venda(self):
        id_venda = self.ui.tb_pend.item(self.ui.tb_pend.currentRow(), 1).text()

        from Controller.venda import VendaTemp
        from Funcoes.utils import exec_app

        abrir_venda = VendaTemp(cod_venda=id_venda)
        exec_app(abrir_venda)
        self.dialogs.append(abrir_venda)
        self.close()
