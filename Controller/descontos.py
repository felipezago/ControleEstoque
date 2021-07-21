from PyQt5.QtWidgets import QMainWindow
from Model.Venda_Tmp import Venda_Tmp
from PyQt5 import QtGui


class Descontos(QMainWindow):

    def __init__(self, parent=None):
        super(Descontos, self).__init__(parent)
        from View.descontos import Ui_Frame
        from PyQt5.QtCore import Qt

        self.ui = Ui_Frame()
        self.ui.setupUi(self)
        self.dialogs = list()
        self.setFixedSize(self.size())
        self.tela_principal = parent

        self.setWindowModality(Qt.ApplicationModal)

        self.linha_selecionada = None
        self.item_selecionado = Venda_Tmp()
        self.total = Venda_Tmp.retorna_total()
        self.desconto_total = 0
        self.total_item = 0

        self.ui.bt_inserir.clicked.connect(self.aplicar_desconto)
        self.ui.bt_sair.clicked.connect(self.sair)
        self.ui.tx_valor.returnPressed.connect(self.aplicar_desconto)
        self.ui.tb_itens_venda.cellClicked.connect(self.linha_clicada)
        self.ui.tx_valor.textChanged.connect(self.formatar_texto)
        self.ui.bt_excluir.clicked.connect(self.excluir_descontos)

        for i in range(0, 6):
            self.ui.tb_itens_venda.horizontalHeaderItem(i).setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.ui.tb_itens_venda.setColumnWidth(0, 30)
        self.ui.tb_itens_venda.setColumnWidth(1, 300)
        self.ui.tb_itens_venda.setColumnWidth(2, 100)
        self.ui.tb_itens_venda.setColumnWidth(3, 80)
        self.ui.tb_itens_venda.setColumnWidth(4, 100)
        self.ui.tb_itens_venda.setColumnWidth(5, 100)

        self.ui.lb_descontos.setText(f"{Venda_Tmp.soma_descontos():.2f}")
        self.ui.lb_total.setText(f"{Venda_Tmp.retorna_total():.2f}")

        self.preenche_tabela()

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

    def aplicar_desconto(self):
        from PyQt5.QtWidgets import QMessageBox

        indice = self.ui.cb_tipo_desconto.currentIndex()
        valor = float(self.ui.tx_valor.text())
        restante = 0

        if valor:
            porcentagem = valor / 100
            if indice in (1, 2):
                if not self.tela_principal.recebeu_desconto_subtotal:
                    if valor <= 99.9:
                        if indice == 1:
                            self.desconto_total += self.total * porcentagem
                            desconto_itens = self.desconto_total / Venda_Tmp.qtd_itens()
                            dados = Venda_Tmp.get_venda_atual()

                            for item in dados:
                                item_venda = Venda_Tmp()
                                item_venda.cod_interno = item[0]
                                item_venda.desconto = item[7]
                                item_venda.valor = item[6]
                                item_venda.qtd = item[5]
                                total_item = item_venda.valor * item_venda.qtd

                                desconto_total = item_venda.desconto + desconto_itens

                                if desconto_total >= total_item:
                                    if item_venda.desconto == 0:
                                        novo_desconto = total_item - 0.01
                                    else:
                                        novo_desconto = (desconto_total - total_item) + 0.01

                                    restante += desconto_itens - novo_desconto
                                    item_venda.desconto = novo_desconto
                                else:
                                    item_venda.desconto += desconto_itens
                                item_venda.inserir_desconto_item()

                            self.tela_principal.recebeu_desconto = True
                            self.tela_principal.recebeu_desconto_subtotal = True
                            self.tela_principal.excluiu_descontos = False
                            self.preenche_tabela()
                        else:
                            if self.item_selecionado.cod_interno:
                                self.desconto_total += self.total_item * porcentagem
                                desconto_item = self.desconto_total

                                item_venda = Venda_Tmp()
                                item_venda.cod_interno = self.item_selecionado.cod_interno
                                item_venda.desconto = desconto_item
                                item_venda.inserir_desconto_item()

                                self.tela_principal.recebeu_desconto = True
                                self.tela_principal.recebeu_desconto_subtotal = True
                                self.tela_principal.excluiu_descontos = False
                                self.preenche_tabela()
                            else:
                                QMessageBox.warning(self, "Erro!", "Selecione um item.")
                    else:
                        QMessageBox.warning(self, "Erro!", "Item não pode receber mais que 99.9% de desconto.")
                else:
                    QMessageBox.warning(self, "Erro!", "Item já recebeu desconto em percentual")
            elif indice in (3, 4):
                if indice == 3:
                    if valor < self.total:
                        self.desconto_total = valor
                        desconto_itens = self.desconto_total / Venda_Tmp.qtd_itens()
                        dados = Venda_Tmp.get_venda_atual()

                        for item in dados:
                            item_venda = Venda_Tmp()
                            item_venda.cod_interno = item[0]
                            item_venda.desconto = item[7]
                            item_venda.valor = item[6]
                            item_venda.qtd = item[5]
                            total_item = item_venda.valor * item_venda.qtd

                            desconto_total = item_venda.desconto + desconto_itens

                            if desconto_total >= total_item:
                                if item_venda.desconto == 0:
                                    novo_desconto = total_item - 0.01
                                else:
                                    novo_desconto = (desconto_total - total_item) + 0.01
                                restante += desconto_itens - novo_desconto
                                item_venda.desconto = novo_desconto
                            else:
                                item_venda.desconto += desconto_itens
                            item_venda.inserir_desconto_item()

                        self.tela_principal.recebeu_desconto = True
                        self.tela_principal.excluiu_descontos = False
                        self.preenche_tabela()
                    else:
                        QMessageBox.warning(self, "Erro!", "Valor do desconto não pode ser maior que o valor total.")
                else:
                    if self.item_selecionado.cod_interno:
                        if valor < self.total_item:
                            self.desconto_total = valor

                            item_venda = Venda_Tmp()
                            item_venda.cod_interno = self.item_selecionado.cod_interno
                            item_venda.desconto = self.desconto_total
                            item_venda.inserir_desconto_item()

                            self.tela_principal.recebeu_desconto = True
                            self.tela_principal.excluiu_descontos = False
                            self.preenche_tabela()
                        else:
                            QMessageBox.warning(self, "Erro!", "Valor do desconto não pode ser maior que o valor total "
                                                               "do item.")
                    else:
                        QMessageBox.warning(self, "Erro!", "Selecione um item.")
            else:
                QMessageBox.warning(self, "Erro!", "Favor selecionar uma opção!")
        else:
            QMessageBox.warning(self, "Erro!", "Favor informar um valor.")

        if restante > 0:
            dados = Venda_Tmp.get_venda_atual()

            for item in dados:
                item_venda = Venda_Tmp()
                item_venda.cod_interno = item[0]
                item_venda.desconto = item[7]
                item_venda.valor = item[6]
                item_venda.qtd = item[5]
                total_item = item_venda.valor * item_venda.qtd

                if not item_venda.desconto == (total_item - 0.01):
                    sobra = total_item - item_venda.desconto
                    if sobra >= restante:
                        item_venda.desconto += restante
                        restante = 0
                    else:
                        novo_desconto = item_venda.desconto + (sobra - 0.01)
                        restante -= (sobra - 0.01)
                        item_venda.desconto = novo_desconto
                    item_venda.inserir_desconto_item()
                    self.preenche_tabela()

        self.ui.tx_valor.setText("")
        self.set_lbls()

    def sair(self):
        self.close()

    def excluir_descontos(self):
        from PyQt5.QtWidgets import QMessageBox

        if Venda_Tmp.soma_descontos() > 0:
            reply = QMessageBox.question(self, 'Excluir?', f'Tem certeza que deseja excluir todos os descontos?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

            if reply == QMessageBox.Yes:
                try:
                    Venda_Tmp.delete_descontos()
                    self.tela_principal.recebeu_desconto_subtotal = False
                    self.tela_principal.recebeu_desconto = False
                    self.tela_principal.excluiu_descontos = True
                    self.desconto_total = 0
                    self.total_item = 0
                    self.linha_selecionada = None
                except Exception as error:
                    QMessageBox.warning(self, "Erro", str(error))
                else:
                    self.preenche_tabela()
                    self.set_lbls()
            else:
                return
        else:
            QMessageBox.warning(self, "Atenção!", "Não há nenhum desconto aplicado!")

    def linha_clicada(self):
        tb = self.ui.tb_itens_venda
        self.linha_selecionada = tb.currentRow()

        self.item_selecionado.cod_interno = tb.item(tb.currentRow(), 0).text()
        self.item_selecionado.valor = tb.item(tb.currentRow(), 2).text()
        self.item_selecionado.qtd = tb.item(tb.currentRow(), 3).text()
        self.total_item = float(tb.item(tb.currentRow(), 4).text())

    def preenche_tabela(self):
        from Model.Servicos import Servicos
        from Model.Produtos import Produtos
        from PyQt5.QtWidgets import QTableWidgetItem

        self.ui.tb_itens_venda.clearContents()
        self.ui.tb_itens_venda.setRowCount(0)

        dados = Venda_Tmp.get_venda_atual()

        if type(dados) == list:
            for i, linha in enumerate(dados):
                total = int(linha[5]) * float(linha[6])

                self.ui.tb_itens_venda.insertRow(i)
                self.ui.tb_itens_venda.setItem(i, 0, QTableWidgetItem(str(linha[0])))
                self.ui.tb_itens_venda.setItem(i, 3, QTableWidgetItem(str(linha[5])))
                self.ui.tb_itens_venda.setItem(i, 4, QTableWidgetItem(f"{total:.2f}"))
                self.ui.tb_itens_venda.setItem(i, 5, QTableWidgetItem(f"{linha[7]:.2f}"))

                # item
                if linha[5] == "SERVIÇO":
                    serv = Servicos()
                    serv.id = linha[4]
                    servico = serv.get_servico_by_id()
                    self.ui.tb_itens_venda.setItem(i, 1, QTableWidgetItem(str(servico[1])))
                    self.ui.tb_itens_venda.setItem(i, 2, QTableWidgetItem(str(servico[2])))
                else:
                    p = Produtos()
                    p.id = linha[3]
                    produto = p.get_produto_by_id()
                    self.ui.tb_itens_venda.setItem(i, 1, QTableWidgetItem(str(produto[5])))
                    self.ui.tb_itens_venda.setItem(i, 2, QTableWidgetItem(str(produto[7])))

    def set_lbls(self):
        self.ui.lb_descontos.setText(f"{Venda_Tmp.soma_descontos():.2f}")
        self.ui.lb_total.setText(f"{Venda_Tmp.retorna_total():.2f}")
