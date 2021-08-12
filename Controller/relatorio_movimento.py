from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QColor, QBrush
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox

from Model.Compra_Header import Compras_Header
from Model.Vendas_Header import Vendas_Header


class RelatorioMovimento(QMainWindow):
    def __init__(self, parent=None):
        super(RelatorioMovimento, self).__init__(parent)
        from View.relatorio_movimento import Ui_Frame
        from PyQt5.QtCore import Qt
        from datetime import date

        self.ui = Ui_Frame()
        self.ui.setupUi(self)
        self.dialogs = list()
        self.tamanho = self.size()
        self.setFixedSize(self.tamanho)

        self.setWindowIcon(QtGui.QIcon("Imagens/logo_fzr.png"))

        self.setWindowModality(QtCore.Qt.ApplicationModal)
        # removendo opção de maximizar
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

        # ação dos botoes
        self.ui.bt_sair.clicked.connect(self.sair)
        self.ui.bt_buscar.clicked.connect(self.buscar)

        for c in range(0, 5):
            self.ui.tb_rel.horizontalHeaderItem(c).setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.ui.tb_rel.setColumnWidth(0, 130)
        self.ui.tb_rel.setColumnWidth(1, 130)
        self.ui.tb_rel.setColumnWidth(2, 130)
        self.ui.tb_rel.setColumnWidth(3, 130)
        self.ui.tb_rel.setColumnWidth(4, 130)

        self.ui.tx_datainicial.setDate(date.today())
        self.ui.tx_datafinal.setDate(date.today())
        self.buscar()

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        self.setFixedSize(self.tamanho)

    def sair(self):
        self.close()

    def buscar(self):
        self.ui.tb_rel.clearContents()
        self.ui.tb_rel.setRowCount(0)

        if self.ui.tx_datainicial.date() and self.ui.tx_datafinal.date():
            if self.ui.tx_datafinal.date().getDate() >= self.ui.tx_datainicial.date().getDate():
                # FORMATO (YYYY, mm, dd)
                inicial = self.ui.tx_datainicial.date().getDate()
                final = self.ui.tx_datafinal.date().getDate()

                dados_venda = Vendas_Header.relatorio_movimento(f"{inicial[2]}/{inicial[1]}/{inicial[0]}",
                                                                f"{final[2]}/{final[1]}/{final[0]}")
                dados_compra = Compras_Header.relatorio_movimento(f"{inicial[2]}/{inicial[1]}/{inicial[0]}",
                                                                  f"{final[2]}/{final[1]}/{final[0]}")

                total_liq = 0
                self.ui.tb_rel.insertRow(0)

                if dados_compra is not None and dados_venda is not None:

                    if dados_venda is not None:
                        for i in range(0, 3):
                            self.ui.tb_rel.setItem(0, i, QTableWidgetItem(f"R$ {dados_venda[i]}"))
                            total_liq = dados_venda[2]
                    else:
                        for i in range(0, 3):
                            self.ui.tb_rel.setItem(0, i, QTableWidgetItem("R$ 0.00"))

                    tot_compras = 0
                    if dados_compra is not None:
                        self.ui.tb_rel.setItem(0, 3, QTableWidgetItem(f"R$ {dados_compra[0]}"))
                        tot_compras = dados_compra[0]
                    else:
                        self.ui.tb_rel.setItem(0, 3, QTableWidgetItem("R$ 0.00"))

                    res = total_liq - tot_compras

                    self.ui.tb_rel.setItem(0, 4, QTableWidgetItem(f"R$ {res}"))
                    item = self.ui.tb_rel.item(0, 4)

                    if res > 0:
                        self.ui.tb_rel.setHorizontalHeaderLabels(["VENDAS", "DESCONTOS", "VENDAS LIQ.", "COMPRAS", "LUCRO"])
                        item.setForeground(QBrush(QColor(103, 194, 0)))
                    else:
                        self.ui.tb_rel.setHorizontalHeaderLabels(
                            ["VENDAS", "DESCONTOS", "VENDAS LIQ.", "COMPRAS", "PREJUÍZO"])
                        item.setForeground(QBrush(QColor(255, 0, 0)))

                    compra = self.ui.tb_rel.item(0, 3)
                    compra.setForeground(QBrush(QColor(255, 0, 0)))

                    liq = self.ui.tb_rel.item(0, 2)
                    liq.setForeground(QBrush(QColor(103, 194, 0)))
                else:
                    QMessageBox.warning(self, "Aviso!", "Nenhum dado encontrado para filtro selecionado.")
                    self.ui.tb_rel.setRowCount(0)

            else:
                QMessageBox.warning(self, "Aviso!", "Data inicial não pode ser maior que a data final.")
                self.ui.tb_rel.setRowCount(0)
