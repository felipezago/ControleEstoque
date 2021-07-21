from PyQt5.QtWidgets import QMainWindow
from Model.Venda_Tmp import Venda_Tmp
from Model.Venda_Fin import Venda_Fin
from Model.Finalizadoras import Finalizadoras
from PyQt5 import QtGui, QtCore


class EventFilter(QtCore.QObject):

    def __init__(self, parent=None):
        QtCore.QObject.__init__(self, parent)

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.ActivationChange:
            if self.parent().isActiveWindow():
                if obj.adicionando_fin:
                    obj.preenche_combo()

        return QtCore.QObject.eventFilter(self, obj, event)


class Finalizar(QMainWindow):

    def __init__(self, parent=None):
        super(Finalizar, self).__init__(parent)
        from View.finalizar import Ui_Frame
        from PyQt5.QtCore import Qt

        self.ui = Ui_Frame()
        self.ui.setupUi(self)
        self.dialogs = list()
        self.setFixedSize(self.size())
        self.tela_principal = parent

        self.setWindowModality(Qt.ApplicationModal)
        self.installEventFilter(EventFilter(self))

        self.linha_selecionada = None
        self.fin_selecionada = Venda_Fin()
        self.total = Venda_Tmp.retorna_total()
        self.desconto_total = 0
        self.total_item = 0
        self.adicionando_fin = False
        self.restante = 0

        self.ui.bt_inserir.clicked.connect(self.inserir_fin)
        self.ui.bt_sair.clicked.connect(self.sair)
        self.ui.tx_valor.returnPressed.connect(self.inserir_fin)
        self.ui.tb_fin.cellClicked.connect(self.linha_clicada)
        self.ui.bt_excluir.clicked.connect(self.excluir_finalizacao)
        self.ui.bt_add_finalizadora.clicked.connect(self.add_fin)

        for i in range(0, 3):
            self.ui.tb_fin.horizontalHeaderItem(i).setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.ui.tb_fin.setColumnWidth(0, 30)
        self.ui.tb_fin.setColumnWidth(1, 300)
        self.ui.tb_fin.setColumnWidth(2, 80)

        self.set_lbls()
        self.preenche_tabela()
        self.preenche_combo()

    def add_fin(self):
        from Controller.cadastro_finalizadoras import CadastroFinalizadoras
        from Funcoes.funcoes import exec_app

        self.adicionando_fin = True
        c = CadastroFinalizadoras()
        exec_app(c)
        self.dialogs.append(c)

    def resizeEvent(self, a0: QtGui.QResizeEvent):
        self.setFixedSize(self.size())

    def formatar_texto(self):
        texto = self.ui.tx_valor.text()
        tamanho = len(texto)
        if not texto[tamanho-1:tamanho].isnumeric():
            if texto[tamanho-1:tamanho] != '.':
                self.ui.tx_valor.setText(texto[:tamanho - 1])

            if texto.count(".") > 1 and texto[tamanho-1:tamanho] == '.':
                self.ui.tx_valor.setText(texto[:tamanho - 1])

    def sair(self):
        self.close()

    def preenche_combo(self):
        self.ui.cb_pagamento.clear()
        self.ui.cb_pagamento.addItem("SELECIONE")

        todas_fin = Finalizadoras.get_todas_finalizadoras()

        for contador, fin in enumerate(todas_fin):
            contador += 1
            self.ui.cb_pagamento.addItem(fin[1])
            self.ui.cb_pagamento.setItemData(contador, fin)

    def inserir_fin(self):
        from PyQt5.QtWidgets import QMessageBox

        if self.ui.cb_pagamento.currentIndex() != 0:
            v_fin = Venda_Fin()
            v_fin.finalizadoras = Finalizadoras()
            v_fin.venda = Venda_Tmp()

            indice_fin = self.ui.cb_pagamento.currentIndex()
            fin_id = self.ui.cb_pagamento.itemData(indice_fin)[0]

            v_fin.valor = float(self.ui.tx_valor.text())
            v_fin.finalizadoras.id = fin_id
            v_fin.venda.id = Venda_Tmp.get_cod_venda()[0]

            try:
                v_fin.inserir_fin_venda()
            except Exception as error:
                QMessageBox.about(self, "Erro", str(error))
            else:
                self.preenche_tabela()

                valor_pago = self.tela_principal.venda_fin.valor_pago()
                if valor_pago > self.total:
                    from Model.Vendas import Vendas
                    from Model.Veiculo import Veiculo

                    QMessageBox.about(self, "Venda Finalizada!", f"Valor de troco: {valor_pago - self.total}")

                    v = Venda_Tmp()
                    v.veiculo = Veiculo()
                    indice_veic = self.tela_principal.ui.cb_veiculo.currentIndex()
                    veic_placa = self.tela_principal.ui.cb_veiculo.itemData(indice_veic)[0]
                    v.veiculo.placa = veic_placa
                    v.update_cliente()

                    Vendas.inserir_venda()
                    Venda_Tmp.delete_venda()
                    self.tela_principal.finalizou = True
                    self.close()

                self.set_lbls()
                self.tela_principal.recebeu_pagamento = True
                self.ui.tx_valor.setText("")
                self.ui.cb_pagamento.setCurrentIndex(0)

        else:
            QMessageBox.warning(self, "Erro!", "Favor selecionar uma opção!")

    def excluir_finalizacao(self):
        from PyQt5.QtWidgets import QMessageBox

        if self.fin_selecionada.id:
            reply = QMessageBox.question(self, 'Excluir?', f'Tem certeza que deseja excluir o pagamento?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

            if reply == QMessageBox.Yes:
                try:
                    v_fin = Venda_Fin()
                    v_fin.id = self.fin_selecionada.id
                    v_fin.delete_fin_by_cod()
                    self.tela_principal.recebeu_pagamento = False
                    self.tela_principal.excluiu_pagamento = True
                    self.linha_selecionada = None
                except Exception as error:
                    QMessageBox.warning(self, "Erro", str(error))
                else:
                    self.preenche_tabela()
                    self.set_lbls()
            else:
                return
        else:
            QMessageBox.warning(self, "Atenção!", "Nenhuma linha selecionada!")

    def linha_clicada(self):
        tb = self.ui.tb_fin
        self.linha_selecionada = tb.currentRow()
        self.fin_selecionada.finalizadoras = Finalizadoras()

        self.fin_selecionada.id = tb.item(tb.currentRow(), 0).text()
        self.fin_selecionada.finalizadoras.id = tb.item(tb.currentRow(), 1).text()
        self.fin_selecionada.valor = tb.item(tb.currentRow(), 2).text()

    def preenche_tabela(self):
        from PyQt5.QtWidgets import QTableWidgetItem
        from Model.Finalizadoras import Finalizadoras

        self.ui.tb_fin.clearContents()
        self.ui.tb_fin.setRowCount(0)

        v_fin = Venda_Fin()
        v_fin.venda = Venda_Tmp()
        v_fin.venda.id_venda = Venda_Tmp.get_cod_venda()[0]

        dados = v_fin.get_fins_venda()

        if type(dados) == list:
            for i, linha in enumerate(dados):
                self.ui.tb_fin.insertRow(i)
                self.ui.tb_fin.setItem(i, 2, QTableWidgetItem(str(linha[3])))
                self.ui.tb_fin.setItem(i, 0, QTableWidgetItem(str(linha[0])))

                # finalizadora
                fin = Finalizadoras()
                fin.id = linha[1]
                finalizadora = fin.get_finalizadora_by_id()

                self.ui.tb_fin.setItem(i, 1, QTableWidgetItem(str(finalizadora[1])))

        if self.adicionando_fin:
            self.adicionando_fin = False

    def set_lbls(self):
        self.ui.lb_total.setText(f"{Venda_Tmp.retorna_total():.2f}")
        self.ui.lb_pago.setText(f"{self.tela_principal.venda_fin.valor_pago():.2f}")
        self.restante = Venda_Tmp.retorna_total() - self.tela_principal.venda_fin.valor_pago()
        self.ui.lb_restante.setText(f"{self.restante:.2f}")
