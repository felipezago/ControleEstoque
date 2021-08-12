from PyQt5 import QtCore
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QMainWindow
from Model.Compra_Header import Compras_Header
from Model.Compra_Tmp import Compra_Tmp
from Model.Fornecedor import Fornecedor
from PyQt5 import QtGui
from Funcoes.utils import exec_app
from Model.Produtos import Produtos
from Model.Compra_Fin import Compra_Fin


class EventFilter(QtCore.QObject):

    def __init__(self, parent=None):
        QtCore.QObject.__init__(self, parent)

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.ActivationChange:
            if self.parent().isActiveWindow():
                if obj.recebeu_codigo_forn:
                    obj.buscar_forn()
                elif obj.recebeu_codigo_item:
                    obj.buscar_item()
                elif obj.recebeu_pagamento or obj.excluiu_pagamento:
                    obj.set_valores_lbl()
                if obj.finalizou:
                    obj.limpa_tela()
                    QMessageBox.information(obj, "Sucesso!", "Compra finalizada!")

        return QtCore.QObject.eventFilter(self, obj, event)


class Compra(QMainWindow):
    def __init__(self, parent=None):
        super(Compra, self).__init__(parent)
        from View.compra import Ui_Frame
        from PyQt5.QtGui import QIntValidator
        from PyQt5.QtCore import Qt

        self.ui = Ui_Frame()
        self.ui.setupUi(self)
        self.dialogs = list()
        self.size = self.size()
        self.setFixedSize(self.size)

        self.setWindowIcon(QtGui.QIcon("Imagens/logo_fzr.png"))

        self.installEventFilter(EventFilter(self))

        self.item_selecionado = None
        self.forn_selecionado = Fornecedor()
        self.compra_selecionada = Compra_Tmp()
        self.compra_fin = Compra_Fin()

        self.linha_selecionada = None
        self.codigo_forn = None
        self.codigo_item = None
        self.codigo_compra = None

        # flags
        self.adicionando = False
        self.recebeu_codigo_forn = False
        self.recebeu_codigo_item = False
        self.recebeu_pagamento = False
        self.excluiu_pagamento = False
        self.finalizou = False

        self.ui.lb_valor_total.setText("0,00")
        self.ui.lb_valor_parcial.setText("0,00")
        self.ui.lb_valor_pago.setText("0,00")

        self.setWindowModality(QtCore.Qt.ApplicationModal)

        # ação dos botoes
        self.ui.bt_cancelar.clicked.connect(self.sair)
        self.ui.bt_excluir.clicked.connect(self.excluir)
        self.ui.bt_inserir.clicked.connect(self.valida_campos)
        self.ui.tx_qtd.returnPressed.connect(self.valida_campos)
        self.ui.tx_valor.returnPressed.connect(self.ui.tx_qtd.setFocus)
        self.ui.bt_alterar_cliente.clicked.connect(self.libera_campos_forn)
        self.ui.bt_finalizar.clicked.connect(self.tela_fin)

        # ação da busca
        self.ui.bt_busca_cliente.clicked.connect(self.enter_forn)
        self.ui.tx_busca_forn.returnPressed.connect(self.enter_forn)

        self.ui.bt_busca_item.clicked.connect(self.enter_item)
        self.ui.tx_busca_item.returnPressed.connect(self.enter_item)

        # signals
        self.ui.tb_compra.cellClicked.connect(self.linha_clicada)
        self.ui.tx_busca_forn.textChanged.connect(lambda: self.formatar_texto("fornecedor"))
        self.ui.tx_busca_item.textChanged.connect(lambda: self.formatar_texto("item"))
        self.ui.tx_qtd.textChanged.connect(self.alterar_valor_total)
        self.ui.tx_valor.textChanged.connect(self.alterar_valor_total)

        for i in range(0, 5):
            self.ui.tb_compra.horizontalHeaderItem(i).setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.ui.tb_compra.setColumnWidth(0, 30)
        self.ui.tb_compra.setColumnWidth(1, 350)
        self.ui.tb_compra.setColumnWidth(2, 100)
        self.ui.tb_compra.setColumnWidth(3, 100)
        self.ui.tb_compra.setColumnWidth(4, 100)

        validator_int = QIntValidator(0, 9999, self)
        self.ui.tx_qtd.setValidator(validator_int)

        self.ui.tx_qtd.setEnabled(False)
        self.ui.tx_valor.setEnabled(False)
        self.ui.tx_total.setEnabled(False)
        self.ui.tx_nome_forn.setEnabled(False)
        self.ui.tx_descricao_prod.setEnabled(False)
        self.ui.bt_alterar_cliente.setHidden(True)

    def resizeEvent(self, a0: QtGui.QResizeEvent):
        self.setFixedSize(self.size)

    def libera_campos_forn(self):
        self.ui.tx_busca_forn.setEnabled(True)
        self.ui.bt_busca_cliente.setEnabled(True)
        self.ui.tx_nome_forn.setEnabled(True)
        self.ui.bt_alterar_cliente.setHidden(True)

    def tela_fin(self):
        from Controller.finalizar import Finalizar

        if Compra_Tmp.check_registros():
            fin = Finalizar(self)
            exec_app(fin)
            self.dialogs.append(fin)
        else:
            QMessageBox.warning(self, "Erro!", "Não é possível efetuar pagamento sem venda.")

    def alterar_valor_total(self):
        if self.ui.tx_qtd.text() and self.ui.tx_valor.text():
            self.calcula_preco()
        else:
            self.ui.tx_total.setText(self.ui.tx_valor.text())

    def enter_forn(self):
        if self.ui.tx_busca_forn.text():
            self.buscar_forn()
        else:
            self.pesquisar_forn()

    def enter_item(self):
        if self.ui.tx_busca_item.text():
            self.buscar_item()
        else:
            self.pesquisar_item()

    def formatar_texto(self, tipo):
        if tipo == "fornecedor":
            texto = self.ui.tx_busca_forn.text()
            tamanho = len(texto)
            if not texto[tamanho - 1:tamanho].isnumeric():
                self.ui.tx_busca_forn.setText(texto[:tamanho - 1])
        elif tipo == "item":
            texto = self.ui.tx_busca_item.text()
            tamanho = len(texto)
            if not texto[tamanho - 1:tamanho].isnumeric():
                self.ui.tx_busca_item.setText(texto[:tamanho - 1])

    def sair(self):
        self.close()

    def closeEvent(self, event: QtGui.QCloseEvent):
        if not Compra_Tmp.check_registros() or Compras_Header.check_compras(Compra_Tmp.get_cod_compra()):
            Compra_Tmp.delete_compra()
            event.accept()
        else:
            box = QMessageBox()
            box.setIcon(QMessageBox.Question)
            box.setWindowTitle('Sair?')
            box.setText('Tem certeza que deseja sair sem finalizar a compra? Todos os dados serão perdidos.')
            box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            button_sim = box.button(QMessageBox.Yes)
            button_sim.setText('Sim')
            button_nao = box.button(QMessageBox.No)
            button_nao.setText('Não')
            box.exec_()

            if box.clickedButton() == button_sim:
                self.delete_fins()
                Compra_Tmp.delete_compra()
                event.accept()
            else:
                event.ignore()

    def valida_campos(self):
        if not self.ui.tx_busca_forn.text() and not self.ui.tx_nome_forn.text():
            self.ui.tx_busca_forn.setFocus()
        elif not self.ui.tx_busca_item.text() and not self.ui.tx_descricao_prod.text():
            self.ui.tx_busca_item.setFocus()
        elif not self.ui.tx_valor.text():
            self.ui.tx_valor.setFocus()
        elif not self.ui.tx_qtd.text():
            self.ui.tx_qtd\
                .setFocus()
        else:
            self.inserir()

    def inserir(self):
        compra = Compra_Tmp()
        self.set_forn_enabled(False)

        if self.ui.tx_qtd.text():
            qtd = int(self.ui.tx_qtd.text())
        else:
            qtd = 1

        if Compra_Tmp.existe_produto_compra(self.item_selecionado.id):
            compra.id_prod = self.item_selecionado.id
            compra.qtd = qtd
            compra.add_qtd_item()
            self.compra_fin.compra_id = Compra_Tmp.get_cod_compra()
            self.limpa_campos_item()
            self.atualiza_tabela()
            return

        from Funcoes.utils import data_hora_atual

        status = "EM ANDAMENTO"

        compra.id_prod = self.item_selecionado.id
        compra.valor = float(self.ui.tx_valor.text())
        compra.data_hora = data_hora_atual()
        compra.qtd = qtd
        compra.status = status

        maximo = compra.select_max()

        if maximo == 0:
            compra.inserir_compra(1)
        else:
            compra.inserir_compra(maximo + 1)

        self.compra_fin.compra_id = Compra_Tmp.get_cod_compra()

        self.limpa_campos_item()
        self.atualiza_tabela()

    def atualiza_tabela(self):
        self.ui.tb_compra.clearContents()
        self.ui.tb_compra.setRowCount(0)

        dados = Compra_Tmp.get_compra_atual()

        for i, linha in enumerate(dados):
            self.ui.tb_compra.insertRow(i)
            for j in range(0, 5):
                self.ui.tb_compra.setItem(i, j, QTableWidgetItem(str(linha[j])))

        self.set_valores_lbl()
        self.ui.tb_compra.selectRow(self.ui.tb_compra.rowCount() - 1)

    def pesquisar_forn(self):
        from Controller.pesquisa_forn import PesquisaForn

        busca_forn = PesquisaForn(self)
        exec_app(busca_forn)
        self.dialogs.append(busca_forn)

    def buscar_forn(self):
        self.recebeu_codigo_forn = False
        if self.ui.tx_busca_forn.text():
            forn = Fornecedor()
            forn.id = int(self.ui.tx_busca_forn.text())
            fornecedor = forn.get_fornecedor_by_id()

            try:
                self.forn_selecionado.id = fornecedor[0]
                self.forn_selecionado.nome = fornecedor[1]
            except TypeError:
                QMessageBox.warning(self, "Erro!", "Fornecedor não encontrado.")
                self.limpar_selecao_forn()
                return
            else:
                self.ui.tx_nome_forn.setText(self.forn_selecionado.nome)
                self.ui.tx_busca_item.setFocus()
        else:
            QMessageBox.warning(self, "Erro!", "Favor informar um código.")
            self.limpar_selecao_forn()

    def pesquisar_item(self):
        from Controller.pesquisa_produto import PesquisaProdutos

        busca_prod = PesquisaProdutos(self)
        exec_app(busca_prod)
        self.dialogs.append(busca_prod)

    def buscar_item(self):
        self.recebeu_codigo_item = False

        if self.ui.tx_busca_item.text():
            prod = Produtos()
            prod.id = int(self.ui.tx_busca_item.text())
            produto = prod.get_produto_by_id()

            self.item_selecionado = Produtos()

            try:
                self.item_selecionado.id = produto[0]
                self.item_selecionado.descricao = produto[5]
                self.item_selecionado.preco = produto[7]
            except TypeError:
                QMessageBox.warning(self, "Erro!", "Produto não encontrado.")
                self.limpar_selecao_item()
                return
            else:
                self.ui.tx_descricao_prod.setText(self.item_selecionado.descricao)
                self.ui.tx_valor.setEnabled(True)
                self.ui.tx_qtd.setEnabled(True)
                self.ui.tx_valor.setFocus()
        else:
            QMessageBox.warning(self, "Erro!", "Favor informar um produto.")
            self.limpar_selecao_item()

    def linha_clicada(self):
        tb = self.ui.tb_compra
        self.linha_selecionada = tb.currentRow()
        self.compra_selecionada.cod_interno = tb.item(self.linha_selecionada, 0).text()

    def limpar_selecao_forn(self):
        self.forn_selecionado.id = None
        self.forn_selecionado.nome = ""
        self.ui.tx_nome_forn.setText("")
        self.ui.tx_busca_forn.setText("")
        self.ui.bt_alterar_cliente.setHidden(True)

    def limpar_selecao_item(self):
        self.item_selecionado.id = None
        self.ui.tx_busca_item.setText("")
        self.ui.tx_descricao_prod.setText("")
        self.ui.tx_valor.setText("")
        self.ui.tx_qtd.setText("")
        self.ui.tx_total.setText("")

    def calcula_preco(self):
        if self.ui.tx_qtd.text():
            qtd = int(self.ui.tx_qtd.text())
        else:
            qtd = 1
        total = qtd * float(self.ui.tx_valor.text())
        self.ui.tx_total.setText(f"{total:.2f}")
        return total

    def excluir(self):
        if Compra_Tmp.check_registros():
            if not self.compra_fin.valor_pago() > 0:
                if self.compra_selecionada.cod_interno:
                    reply = QMessageBox.question(self, 'Excluir?', f'Tem certeza que deseja excluir o item: '
                                                                   f'{self.compra_selecionada.cod_interno}?',
                                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                    if reply == QMessageBox.Yes:
                        try:
                            if Compra_Tmp.qtd_itens() == 1:
                                self.limpar_selecao_forn()
                                self.set_forn_enabled(True)
                            self.compra_selecionada.delete_item_compra()
                            self.compra_selecionada.cod_interno = None

                        except Exception as error:
                            QMessageBox.warning(self, "Erro", str(error))
                        else:
                            self.ui.tb_compra.removeRow(self.linha_selecionada)
                            self.set_valores_lbl()
                    else:
                        return
                else:
                    QMessageBox.warning(self, "Atenção!", "Favor selecionar alguma linha!")
            else:
                QMessageBox.warning(self, "Atenção!", "Não é possível excluir um item após ter efetuado um pagamento.")
        else:
            QMessageBox.warning(self, "Aviso!", "Não é possível excluir itens, se não há itens registrados.")

    def set_valores_lbl(self):
        self.ui.lb_valor_parcial.setText(f"{Compra_Tmp.retorna_total()}")
        self.ui.lb_valor_total.setText(f"{Compra_Tmp.retorna_total() - self.compra_fin.valor_pago():.2f}")
        self.ui.lb_valor_pago.setText(f"{self.compra_fin.valor_pago():.2f}")

    def set_forn_enabled(self, boolean):
        self.ui.bt_alterar_cliente.setHidden(boolean)
        self.ui.tx_busca_forn.setEnabled(boolean)
        self.ui.bt_busca_cliente.setEnabled(boolean)

    def limpa_campos_item(self):
        self.ui.tx_busca_item.setText("")
        self.ui.tx_descricao_prod.setText("")
        self.ui.tx_qtd.setText("")
        self.ui.tx_valor.setText("")
        self.ui.tx_total.setText("")
        self.ui.tx_busca_item.setFocus()

    @staticmethod
    def delete_fins():
        c_fin = Compra_Fin()
        c_fin.compra_id = Compra_Tmp.get_cod_compra()
        c_fin.delete_fin_by_compra()

    def limpa_tela(self):
        self.ui.lb_valor_total.setText("0,00")
        self.ui.lb_valor_pago.setText("0,00")
        self.ui.lb_valor_parcial.setText("0,00")

        self.ui.tx_busca_forn.setEnabled(True)
        self.ui.bt_busca_cliente.setEnabled(True)
        self.ui.tx_busca_forn.setText("")
        self.ui.tx_nome_forn.setText("")
        self.ui.bt_alterar_cliente.setHidden(True)

        self.ui.tb_compra.clearContents()
        self.ui.tb_compra.setRowCount(0)
        self.ui.tx_busca_forn.setFocus()

        self.recebeu_pagamento = False
        self.finalizou = False
