from PyQt5.QtWidgets import QMainWindow

from Controller.venda import VendaTemp
from Funcoes.utils import data_hora_atual
from Model.Compra_Itens import Compra_Itens
from Model.Compra_Fin import Compra_Fin
from Model.Compra_Header import Compras_Header
from Model.Compra_Tmp import Compra_Tmp
from Model.Fornecedor import Fornecedor
from Model.Pendencias import Pendencias
from Model.Produtos import Produtos
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
        self.tamanho = self.size()
        self.setFixedSize(self.tamanho)

        self.setWindowIcon(QtGui.QIcon("Imagens/logo_fzr.png"))

        self.tela_principal = parent

        self.setWindowModality(Qt.ApplicationModal)
        self.installEventFilter(EventFilter(self))

        self.linha_selecionada = None

        if isinstance(self.tela_principal, VendaTemp):
            self.fin_selecionada = Venda_Fin()
            self.total = Venda_Tmp.retorna_total()
        else:
            self.fin_selecionada = Compra_Fin()
            self.total = Compra_Tmp.retorna_total()

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
        from Funcoes.utils import exec_app

        self.adicionando_fin = True
        c = CadastroFinalizadoras()
        exec_app(c)
        self.dialogs.append(c)

    def resizeEvent(self, a0: QtGui.QResizeEvent):
        self.setFixedSize(self.tamanho)

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
            if isinstance(self.tela_principal, VendaTemp):
                v_fin = Venda_Fin()
                v_fin.venda_id = Venda_Tmp.get_cod_venda()
            else:
                v_fin = Compra_Fin()
                v_fin.compra_id = Compra_Tmp.get_cod_compra()

            v_fin.finalizadoras = Finalizadoras()
            indice_fin = self.ui.cb_pagamento.currentIndex()
            fin_id = self.ui.cb_pagamento.itemData(indice_fin)[0]

            v_fin.valor = float(self.ui.tx_valor.text())
            v_fin.finalizadoras.id = fin_id

            try:
                if isinstance(self.tela_principal, VendaTemp):
                    if v_fin.check_fin(fin_id):
                        v_fin.update_fin_venda(fin_id)
                    else:
                        v_fin.inserir_fin_venda()
                    valor_pago = self.tela_principal.venda_fin.valor_pago()
                else:
                    if v_fin.check_fin(fin_id):
                        v_fin.update_fin_compra(fin_id)
                    else:
                        v_fin.inserir_fin_compra()
                    valor_pago = self.tela_principal.compra_fin.valor_pago()
            except Exception as error:
                QMessageBox.about(self, "Erro", str(error))
            else:
                self.preenche_tabela()

                if valor_pago >= self.total:
                    from Model.Venda_Itens import Vendas
                    from Model.Veiculo import Veiculo
                    from Model.Vendas_Header import Vendas_Header
                    from Model.Usuario import Usuario
                    from Model.Operador import Operador
                    from Model.Cliente import Cliente

                    self.tela_principal.finalizou = True

                    if (valor_pago - self.total) > 0:
                        QMessageBox.about(self, "Venda Finalizada!", f"Valor de troco: {valor_pago - self.total:.2f}")

                    if isinstance(self.tela_principal, VendaTemp):
                        v = Venda_Tmp()
                        v.veiculo = Veiculo()

                        header = Vendas_Header()
                        header.veiculo = Veiculo()
                        header.cliente = Cliente()
                        header.id = Venda_Tmp.get_cod_venda()

                        indice_veic = self.tela_principal.ui.cb_veiculo.currentIndex()
                        if indice_veic != 0:
                            v.veiculo = Veiculo()
                            veic_placa = self.tela_principal.ui.cb_veiculo.itemData(indice_veic)[0]
                            v.veiculo.placa = veic_placa
                            header.veiculo.placa = veic_placa

                        v.cliente = Cliente()
                        v.cliente.id = self.tela_principal.cliente_selecionado.id
                        header.cliente.id = self.tela_principal.cliente_selecionado.id
                        v.update_cliente()

                        header.qtd_itens = Venda_Tmp.qtd_itens()
                        header.total_descontos = Venda_Tmp.soma_descontos()
                        header.valor_total = Venda_Tmp.retorna_total()
                        header.status = "FINALIZADO"
                        header.datahora = data_hora_atual()

                        if self.tela_principal.codigo_venda:
                            header.update()
                            venda = Vendas()
                            venda.id_venda = self.tela_principal.codigo_venda
                            venda.delete_venda_by_id()
                            Vendas.inserir_venda()

                            p = Pendencias()
                            p.venda = Vendas_Header()
                            p.venda.id = self.tela_principal.codigo_venda
                            p.delete()
                        else:
                            header.inserir()
                            Vendas.inserir_venda()

                            itens = Vendas()
                            itens.id_venda = Venda_Tmp.get_cod_venda()
                            itens_venda = itens.select_produtos_venda()

                            for linha in itens_venda:
                                produtos = Produtos()
                                produtos.id = linha[1]
                                qtd = linha[3]
                                produtos.alterar_estoque("-", qtd)

                        Venda_Tmp.delete_venda()

                        reply = QMessageBox.question(self, 'Imprimir?', f'Deseja imprimir o relatório da venda?',
                                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

                        if reply == QMessageBox.Yes:
                            from Funcoes.utils import print_dialog
                            from Funcoes.PDF.pdf_venda import gerar_pdf

                            usuario_operador = Usuario()
                            usuario_operador.id = Operador.get_operador_atual()[0]
                            usu = usuario_operador.get_usuario_by_id()
                            cnpj = usu[10]

                            gerar_pdf(header.id, cnpj, v.cliente.id)
                            print_dialog(self, f"venda_{self.tela_principal.codigo_venda}.pdf")

                        self.close()
                    else:
                        c = Compra_Tmp()

                        header = Compras_Header()
                        header.fornecedor = Fornecedor()
                        header.id = Compra_Tmp.get_cod_compra()

                        c.fornecedor = Fornecedor()
                        c.fornecedor.id = self.tela_principal.forn_selecionado.id
                        header.fornecedor.id = self.tela_principal.forn_selecionado.id
                        c.update_forn()

                        header.qtd_itens = Compra_Tmp.qtd_itens()
                        header.valor_total = Compra_Tmp.retorna_total()
                        header.status = "FINALIZADO"
                        header.datahora = data_hora_atual()

                        header.inserir()
                        Compra_Itens.inserir_compra()

                        itens = Compra_Itens()
                        itens.id_compra = Compra_Tmp.get_cod_compra()
                        itens_compra = itens.select_produtos_compra()

                        for linha in itens_compra:
                            produtos = Produtos()
                            produtos.id = linha[1]
                            qtd = linha[2]
                            produtos.alterar_estoque("+", qtd)

                        Compra_Tmp.delete_compra()

                        self.close()

                self.set_lbls()
                self.ui.tx_valor.setText("")
                self.tela_principal.recebeu_pagamento = True
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
                    if isinstance(self.tela_principal, VendaTemp):
                        v_fin = Venda_Fin()
                        v_fin.id = self.fin_selecionada.id
                        v_fin.delete_fin_by_cod()
                    else:
                        c_fin = Compra_Fin()
                        c_fin.id = self.fin_selecionada.id
                        c_fin.delete_fin_by_cod()

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

        if isinstance(self.tela_principal, VendaTemp):
            v_fin = Venda_Fin()
            v_fin.venda_id = Venda_Tmp.get_cod_venda()
            dados = v_fin.get_fins_venda()
        else:
            v_fin = Compra_Fin()
            v_fin.compra_id = Compra_Tmp.get_cod_compra()
            dados = v_fin.get_fins_compra()

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
        if isinstance(self.tela_principal, VendaTemp):
            self.ui.lb_total.setText(f"{Venda_Tmp.retorna_total():.2f}")
            self.restante = Venda_Tmp.retorna_total() - self.tela_principal.venda_fin.valor_pago()
            self.ui.lb_pago.setText(f"{self.tela_principal.venda_fin.valor_pago():.2f}")
        else:
            self.ui.lb_total.setText(f"{Compra_Tmp.retorna_total():.2f}")
            self.restante = Compra_Tmp.retorna_total() - self.tela_principal.compra_fin.valor_pago()
            self.ui.lb_pago.setText(f"{self.tela_principal.compra_fin.valor_pago():.2f}")

        self.ui.lb_restante.setText(f"{self.restante:.2f}")
