from PyQt5 import QtCore
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QMainWindow

from Model.Usuario import Usuario
from Model.Veiculo import Veiculo
from Model.Venda_Itens import Vendas
from Model.Venda_Tmp import Venda_Tmp
from PyQt5 import QtGui
from Funcoes.utils import exec_app
from Model.Cliente import Cliente
from Model.Pessoa import Pessoa
from Model.Servicos import Servicos
from Model.Produtos import Produtos
from Model.Venda_Fin import Venda_Fin
from Model.Vendas_Header import Vendas_Header


class EventFilter(QtCore.QObject):

    def __init__(self, parent=None):
        QtCore.QObject.__init__(self, parent)

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.ActivationChange:
            if self.parent().isActiveWindow():
                if obj.recebeu_codigo_cliente:
                    obj.buscar_cliente()
                elif obj.recebeu_codigo_item:
                    obj.buscar_item()
                elif obj.adicionando_veic:
                    if obj.cliente_selecionado:
                        obj.preenche_combo_veiculos()
                elif obj.excluiu_descontos or obj.recebeu_desconto:
                    obj.atualiza_tabela()
                elif obj.recebeu_pagamento or obj.excluiu_pagamento:
                    obj.set_valores_lbl()

                if obj.finalizou:
                    obj.limpa_tela()

        return QtCore.QObject.eventFilter(self, obj, event)


class VendaTemp(QMainWindow):
    def __init__(self, parent=None, cod_venda=""):
        super(VendaTemp, self).__init__(parent)
        from View.venda import Ui_Frame
        from PyQt5.QtGui import QIntValidator
        from PyQt5.QtCore import Qt
        from Model.Venda_Itens import Vendas

        self.ui = Ui_Frame()
        self.ui.setupUi(self)
        self.dialogs = list()
        self.setFixedSize(self.size())

        self.installEventFilter(EventFilter(self))

        self.item_selecionado = None
        self.cliente_selecionado = Cliente()
        self.cliente_selecionado.pessoa = Pessoa()
        self.venda_selecionada = Venda_Tmp()

        self.venda_fin = Venda_Fin()

        self.linha_selecionada = None
        self.codigo_cliente = None
        self.codigo_item = None
        self.codigo_venda = None

        # flags
        self.adicionando = False
        self.recebeu_codigo_cliente = False
        self.recebeu_codigo_item = False
        self.recebeu_desconto = False
        self.recebeu_desconto_subtotal = False
        self.adicionando_veic = False
        self.excluiu_descontos = False
        self.recebeu_pagamento = False
        self.excluiu_pagamento = False
        self.finalizou = False

        self.ui.lb_valor_total.setText("0,00")
        self.ui.lb_valor_parcial.setText("0,00")
        self.ui.lb_descontos.setText("0,00")
        self.ui.lb_valor_pago.setText("0,00")
        self.ui.bt_add_veiculo.setEnabled(False)

        self.setWindowModality(QtCore.Qt.ApplicationModal)

        # ação dos botoes
        self.ui.bt_cancelar.clicked.connect(self.sair)
        self.ui.bt_aberto.clicked.connect(self.deixar_aberto)
        self.ui.bt_excluir.clicked.connect(self.excluir)
        self.ui.bt_inserir.clicked.connect(self.valida_campos)
        self.ui.bt_add_veiculo.clicked.connect(self.add_veic)
        self.ui.tx_qtd.returnPressed.connect(self.valida_campos)
        self.ui.bt_alterar_cliente.clicked.connect(self.libera_campos_cliente)
        self.ui.bt_descontos.clicked.connect(self.tela_descontos)
        self.ui.bt_finalizar.clicked.connect(self.tela_fin)

        # ação da busca
        self.ui.bt_busca_cliente.clicked.connect(self.enter_cliente)
        self.ui.tx_busca_cliente.returnPressed.connect(self.enter_cliente)

        self.ui.bt_busca_item.clicked.connect(self.enter_item)
        self.ui.tx_busca_item.returnPressed.connect(self.enter_item)

        # signals
        self.ui.tb_venda.cellClicked.connect(self.linha_clicada)
        self.ui.tx_busca_cliente.textChanged.connect(lambda: self.formatar_texto("cliente"))
        self.ui.tx_busca_item.textChanged.connect(lambda: self.formatar_texto("item"))
        self.ui.tx_qtd.textChanged.connect(self.alterar_valor_total)

        for i in range(0, 7):
            self.ui.tb_venda.horizontalHeaderItem(i).setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.ui.tb_venda.setColumnWidth(0, 30)
        self.ui.tb_venda.setColumnWidth(1, 220)
        self.ui.tb_venda.setColumnWidth(2, 100)
        self.ui.tb_venda.setColumnWidth(3, 80)
        self.ui.tb_venda.setColumnWidth(4, 100)
        self.ui.tb_venda.setColumnWidth(5, 100)
        self.ui.tb_venda.setColumnWidth(6, 100)

        validator_int = QIntValidator(0, 9999, self)
        self.ui.tx_qtd.setValidator(validator_int)

        self.ui.tx_qtd.setEnabled(False)
        self.ui.tx_valor.setEnabled(False)
        self.ui.tx_total.setEnabled(False)
        self.ui.tx_nome_cliente.setEnabled(False)
        self.ui.tx_descricao_prod.setEnabled(False)
        self.ui.bt_alterar_cliente.setHidden(True)
        self.ui.bt_descontos.setEnabled(False)

        self.preenche_combo_selecao()

        if cod_venda:
            self.codigo_venda = cod_venda
            self.vendas_itens = Vendas()
            vendas_header = Vendas_Header()
            self.venda_tmp = Venda_Tmp()
            self.ui.bt_descontos.setEnabled(True)

            self.venda_tmp.id_venda = cod_venda
            self.vendas_itens.id_venda = cod_venda
            vendas_header.id = cod_venda
            self.venda_fin.venda_id = cod_venda

            self.venda_tmp.inserir_from_itens()
            header = vendas_header.get_vendas_by_id()
            self.ui.tx_busca_cliente.setText(str(header[1]))
            self.buscar_cliente()

            vendas_header.veiculo = Veiculo()
            vendas_header.veiculo.placa = header[2]
            veic = vendas_header.veiculo.get_veic_by_placa()

            if vendas_header.veiculo.placa != 'null':
                idx = self.ui.cb_veiculo.findText(veic[1] + " - " + veic[2])
                self.ui.cb_veiculo.setCurrentIndex(idx)
                self.ui.tx_busca_cliente.setEnabled(False)
                self.ui.tx_nome_cliente.setEnabled(False)
                self.ui.cb_veiculo.setEnabled(False)
                self.ui.bt_add_veiculo.setEnabled(False)
                self.ui.bt_alterar_cliente.setVisible(True)

            self.atualiza_tabela()

    def resizeEvent(self, a0: QtGui.QResizeEvent):
        self.setFixedSize(self.size())

    def libera_campos_cliente(self):
        self.ui.tx_busca_cliente.setEnabled(True)
        self.ui.bt_busca_cliente.setEnabled(True)
        self.ui.tx_nome_cliente.setEnabled(True)
        self.ui.cb_veiculo.setEnabled(True)
        self.ui.bt_add_veiculo.setEnabled(True)
        self.ui.bt_alterar_cliente.setHidden(True)

    def tela_descontos(self):
        from Controller.descontos import Descontos

        if Venda_Tmp.check_registros():
            if self.venda_fin.valor_pago() > 0:
                QMessageBox.warning(self, "Aviso!", "Não é possível aplicar descontos após ter realizar um pagamento.")
            else:
                desc = Descontos(self)
                exec_app(desc)
                self.dialogs.append(desc)
        else:
            QMessageBox.warning(self, "Aviso!", "Não é possível aplicar descontos sem nenhum item registrado.")

    def tela_fin(self):
        from Controller.finalizar import Finalizar

        if Venda_Tmp.check_registros():
            fin = Finalizar(self)
            exec_app(fin)
            self.dialogs.append(fin)
        else:
            QMessageBox.warning(self, "Erro!", "Não é possível efetuar pagamento sem venda.")

    def alterar_valor_total(self):
        if self.ui.tx_qtd.text():
            self.calcula_preco()
        else:
            self.ui.tx_total.setText(self.ui.tx_valor.text())

    def add_veic(self):
        from Controller.cadastro_veiculos import CadastroVeiculos

        c_veic = CadastroVeiculos(self)
        exec_app(c_veic)
        self.dialogs.append(c_veic)
        self.adicionando_veic = True

    def enter_cliente(self):
        if self.ui.tx_busca_cliente.text():
            self.buscar_cliente()
        else:
            self.pesquisar_cliente()

    def enter_item(self):
        if self.ui.tx_busca_item.text():
            self.buscar_item()
        else:
            self.pesquisar_item()

    def formatar_texto(self, tipo):
        if tipo == "cliente":
            texto = self.ui.tx_busca_cliente.text()
            tamanho = len(texto)
            if not texto[tamanho - 1:tamanho].isnumeric():
                self.ui.tx_busca_cliente.setText(texto[:tamanho - 1])
        elif tipo == "item":
            texto = self.ui.tx_busca_item.text()
            tamanho = len(texto)
            if not texto[tamanho - 1:tamanho].isnumeric():
                self.ui.tx_busca_item.setText(texto[:tamanho - 1])

    def preenche_combo_selecao(self):
        self.ui.cb_selec.clear()
        self.ui.cb_selec.addItem("PRODUTO")
        self.ui.cb_selec.addItem("SERVIÇO")

    def sair(self):
        self.close()

    def closeEvent(self, event: QtGui.QCloseEvent):
        if not Venda_Tmp.check_registros() or Vendas_Header.check_vendas(Venda_Tmp.get_cod_venda()):
            Venda_Tmp.delete_venda()
            event.accept()
        else:
            box = QMessageBox()
            box.setIcon(QMessageBox.Question)
            box.setWindowTitle('Sair?')
            box.setText('Tem certeza que deseja sair sem finalizar a venda? Todos os dados serão perdidos.')
            box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            button_sim = box.button(QMessageBox.Yes)
            button_sim.setText('Sim')
            button_nao = box.button(QMessageBox.No)
            button_nao.setText('Não')
            box.exec_()

            if box.clickedButton() == button_sim:
                self.delete_fins()
                Venda_Tmp.delete_venda()
                event.accept()
            else:
                event.ignore()

    def deixar_aberto(self):
        if Venda_Tmp.check_registros():
            from Model.Vendas_Header import Vendas_Header
            from Model.Veiculo import Veiculo
            from Model.Pendencias import Pendencias
            from Funcoes.utils import data_hora_atual

            itens = Vendas()

            fin = Venda_Fin()
            fin.venda_id = Venda_Tmp.get_cod_venda()

            header = Vendas_Header()
            header.cliente = Cliente()
            header.veiculo = Veiculo()
            header.cliente.id = self.cliente_selecionado.id
            header.id = Venda_Tmp.get_cod_venda()
            header.status = "PENDENTE"
            header.qtd_itens = Venda_Tmp.qtd_itens()
            header.total_descontos = Venda_Tmp.soma_descontos()
            header.valor_total = Venda_Tmp.retorna_total()
            header.datahora = data_hora_atual()

            pend = Pendencias()
            pend.venda = header
            pend.veiculo = header.veiculo
            pend.cliente = self.cliente_selecionado
            pend.datahora = data_hora_atual()
            pend.valor = header.valor_total - fin.valor_pago()

            if self.ui.cb_veiculo.currentIndex() != 0:
                indice_veic = self.ui.cb_veiculo.currentIndex()
                header.veiculo.placa = self.ui.cb_veiculo.itemData(indice_veic)[0]
                pend.veiculo = header.veiculo

            if self.codigo_venda:
                header.update()
                pend.update()
                v = Vendas()
                v.id_venda = self.codigo_venda
                v.delete_venda_by_id()
                v.inserir_venda()

                itens.id_venda = self.codigo_venda
                itens_venda = itens.select_produtos_venda()

                for linha in itens_venda:
                    produtos = Produtos()
                    produtos.id = linha[1]
                    qtd = linha[3]
                    produtos.alterar_estoque("-", qtd)
            else:
                header.inserir()
                pend.inserir()
                Vendas.inserir_venda()

                itens.id_venda = Venda_Tmp.get_cod_venda()
                itens_venda = itens.select_produtos_venda()

                for linha in itens_venda:
                    produtos = Produtos()
                    produtos.id = linha[1]
                    qtd = linha[3]
                    produtos.alterar_estoque("-", qtd)

            reply = QMessageBox.question(self, 'Imprimir?', f'Deseja imprimir o relatório da venda?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

            if reply == QMessageBox.Yes:
                from Funcoes.utils import print_dialog
                from Funcoes.PDF.pdf_venda import gerar_pdf
                from Model.Operador import Operador

                usuario_operador = Usuario()
                usuario_operador.id = Operador.get_operador_atual()[0]
                usu = usuario_operador.get_usuario_by_id()
                cnpj = usu[10]

                gerar_pdf(header.id, cnpj, self.cliente_selecionado.id)
                print_dialog(self, "venda.pdf")

            Venda_Tmp.delete_venda()
            self.limpa_tela()
        else:
            QMessageBox.warning(self, "Aviso!", "Não é possível finalizar sem nenhum item registrado.")

    def valida_campos(self):
        if not self.ui.tx_busca_cliente.text() and not self.ui.tx_nome_cliente.text():
            self.ui.tx_busca_cliente.setFocus()
        elif not self.ui.tx_busca_item.text() and not self.ui.tx_descricao_prod.text():
            self.ui.tx_busca_item.setFocus()
        else:
            self.inserir()

    def inserir(self):
        venda = Venda_Tmp()
        self.set_clientes_enabled(False)

        if self.ui.tx_qtd.text():
            qtd = int(self.ui.tx_qtd.text())
        else:
            qtd = 1

        if type(self.item_selecionado) == Servicos:
            tipo = "SERVIÇO"
            if Venda_Tmp.existe_servico_venda(self.item_selecionado.id):
                venda.id_prod_serv = self.item_selecionado.id
                venda.qtd = qtd
                venda.tipo = tipo
                self.venda_fin.venda_id = Venda_Tmp.get_cod_venda()
                venda.add_qtd_item()
                self.limpa_campos_item()
                self.atualiza_tabela()
                return
        else:
            tipo = "PRODUTO"
            if Venda_Tmp.existe_produto_venda(self.item_selecionado.id):
                venda.id_prod_serv = self.item_selecionado.id
                venda.qtd = qtd
                venda.tipo = tipo
                self.venda_fin.venda_id = Venda_Tmp.get_cod_venda()
                venda.add_qtd_item()
                self.limpa_campos_item()
                self.atualiza_tabela()
                return

        from Funcoes.utils import data_hora_atual

        status = "EM ANDAMENTO"

        venda.id_prod_serv = self.item_selecionado.id
        venda.valor = float(self.ui.tx_valor.text())
        venda.desconto = 0
        venda.data_hora = data_hora_atual()
        venda.tipo = tipo
        venda.qtd = qtd
        venda.status = status

        maximo = venda.select_max()

        if self.codigo_venda:
            venda.inserir_venda(self.codigo_venda)
        else:
            if maximo == 0:
                venda.inserir_venda(1)
            else:
                venda.inserir_venda(maximo + 1)

        self.venda_fin.venda_id = Venda_Tmp.get_cod_venda()

        self.limpa_campos_item()
        self.atualiza_tabela()
        self.ui.bt_descontos.setEnabled(True)

    def atualiza_tabela(self):
        self.ui.tb_venda.clearContents()
        self.ui.tb_venda.setRowCount(0)
        self.recebeu_desconto = False

        dados = Venda_Tmp.get_venda_atual()

        for i, linha in enumerate(dados):
            total = int(linha[6]) * float(linha[7])

            self.ui.tb_venda.insertRow(i)
            self.ui.tb_venda.setItem(i, 0, QTableWidgetItem(str(linha[0])))
            self.ui.tb_venda.setItem(i, 3, QTableWidgetItem(str(linha[6])))
            self.ui.tb_venda.setItem(i, 4, QTableWidgetItem(f"{total:.2f}"))
            self.ui.tb_venda.setItem(i, 5, QTableWidgetItem(f"{linha[8]:.2f}"))
            self.ui.tb_venda.setItem(i, 6, QTableWidgetItem(str(linha[5])))

            # item
            if linha[5] == "SERVIÇO":
                serv = Servicos()
                serv.id = linha[4]
                servico = serv.get_servico_by_id()
                self.ui.tb_venda.setItem(i, 1, QTableWidgetItem(str(servico[1])))
                self.ui.tb_venda.setItem(i, 2, QTableWidgetItem(str(servico[2])))
            else:
                p = Produtos()
                p.id = linha[4]
                produto = p.get_produto_by_id()
                self.ui.tb_venda.setItem(i, 1, QTableWidgetItem(str(produto[5])))
                self.ui.tb_venda.setItem(i, 2, QTableWidgetItem(str(produto[7])))

        self.set_valores_lbl()
        self.ui.tb_venda.selectRow(self.ui.tb_venda.rowCount() - 1)

    def pesquisar_cliente(self):
        from Controller.pesquisa_cliente import PesquisaClientes

        busca_cli = PesquisaClientes(self)
        exec_app(busca_cli)
        self.dialogs.append(busca_cli)

    def buscar_cliente(self):
        self.recebeu_codigo_cliente = False
        if self.ui.tx_busca_cliente.text():
            cli = Cliente()
            cli.id = int(self.ui.tx_busca_cliente.text())
            cliente = cli.get_cliente_by_id()

            try:
                self.cliente_selecionado.id = cliente[0]
                self.cliente_selecionado.nome = cliente[2]
            except TypeError:
                QMessageBox.warning(self, "Erro!", "Cliente não encontrado.")
                self.limpar_selecao_cliente()
                return
            else:
                self.ui.tx_nome_cliente.setText(self.cliente_selecionado.nome)
                self.preenche_combo_veiculos()
                self.ui.cb_veiculo.showPopup()
                self.ui.bt_add_veiculo.setEnabled(True)
        else:
            QMessageBox.warning(self, "Erro!", "Favor informar um código.")
            self.limpar_selecao_cliente()

    def pesquisar_item(self):
        from Controller.pesquisa_servico import PesquisaServico
        from Controller.pesquisa_produto import PesquisaProdutos

        if self.ui.cb_selec.currentIndex() == 0:
            busca_prod = PesquisaProdutos(self)
            exec_app(busca_prod)
            self.dialogs.append(busca_prod)
        else:
            busca_serv = PesquisaServico(self)
            exec_app(busca_serv)
            self.dialogs.append(busca_serv)

    def buscar_item(self):
        self.recebeu_codigo_item = False
        if self.ui.cb_selec.currentIndex() == 1:
            if self.ui.tx_busca_item.text():
                serv = Servicos()
                serv.id = int(self.ui.tx_busca_item.text())
                servico = serv.get_servico_by_id()

                self.item_selecionado = Servicos()

                try:
                    self.item_selecionado.id = servico[0]
                    self.item_selecionado.descricao = servico[1]
                    self.item_selecionado.preco = servico[2]
                except TypeError:
                    QMessageBox.warning(self, "Erro!", "Serviço não encontrado.")
                    self.limpar_selecao_item()
                    return
                else:
                    self.ui.tx_descricao_prod.setText(self.item_selecionado.descricao)
                    self.ui.tx_valor.setText(str(self.item_selecionado.preco))
                    self.ui.tx_qtd.setEnabled(True)
                    self.ui.tx_qtd.setFocus()
                    self.calcula_preco()
            else:
                QMessageBox.warning(self, "Erro!", "Favor informar um código.")
                self.limpar_selecao_item()
        else:
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
                    self.ui.tx_valor.setText(str(self.item_selecionado.preco))
                    self.ui.tx_qtd.setEnabled(True)
                    self.ui.tx_qtd.setFocus()
                    self.calcula_preco()

            else:
                QMessageBox.warning(self, "Erro!", "Favor informar um produto.")
                self.limpar_selecao_item()

    def linha_clicada(self):
        tb = self.ui.tb_venda
        self.linha_selecionada = tb.currentRow()
        self.venda_selecionada.cod_interno = tb.item(self.linha_selecionada, 0).text()

    def preenche_combo_veiculos(self):
        from Model.Veiculo import Veiculo

        self.ui.cb_veiculo.clear()
        self.ui.cb_veiculo.addItem("SELECIONE")

        v = Veiculo()
        v.cliente = Cliente()
        v.cliente.id = self.cliente_selecionado.id

        todos_veiculos = v.get_veic_by_cliente("=")

        for contador, veic in enumerate(todos_veiculos):
            contador += 1
            self.ui.cb_veiculo.addItem(f"{veic[1]} - {veic[2]}")
            self.ui.cb_veiculo.setItemData(contador, veic)

        self.ui.cb_veiculo.setFocus()

    def limpar_selecao_cliente(self):
        self.cliente_selecionado.id = None
        self.cliente_selecionado.nome = ""
        self.ui.bt_add_veiculo.setEnabled(False)
        self.ui.tx_nome_cliente.setText("")
        self.ui.tx_busca_cliente.setText("")
        self.ui.cb_veiculo.clear()
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
        if Venda_Tmp.check_registros():
            if not self.venda_fin.valor_pago() > 0:
                if self.venda_selecionada.cod_interno:
                    reply = QMessageBox.question(self, 'Excluir?', f'Tem certeza que deseja excluir o item: '
                                                                   f'{self.venda_selecionada.cod_interno}?',
                                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                    if reply == QMessageBox.Yes:
                        try:
                            if Venda_Tmp.qtd_itens() == 1:
                                self.limpar_selecao_cliente()
                                self.set_clientes_enabled(True)
                                self.ui.bt_descontos.setEnabled(False)
                                self.recebeu_desconto_subtotal = False
                                self.ui.bt_add_veiculo.setEnabled(False)
                            self.venda_selecionada.delete_item_venda()
                            self.venda_selecionada.cod_interno = None

                        except Exception as error:
                            QMessageBox.warning(self, "Erro", str(error))
                        else:
                            self.ui.tb_venda.removeRow(self.linha_selecionada)
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
        self.ui.lb_valor_parcial.setText(f"{Venda_Tmp.retorna_total() + Venda_Tmp.soma_descontos():.2f}")
        self.ui.lb_descontos.setText(f"{Venda_Tmp.soma_descontos():.2f}")
        self.ui.lb_valor_total.setText(f"{Venda_Tmp.retorna_total() - self.venda_fin.valor_pago():.2f}")
        self.ui.lb_valor_pago.setText(f"{self.venda_fin.valor_pago():.2f}")

    def set_clientes_enabled(self, boolean):
        self.ui.bt_alterar_cliente.setHidden(boolean)
        self.ui.tx_busca_cliente.setEnabled(boolean)
        self.ui.cb_veiculo.setEnabled(boolean)
        self.ui.bt_add_veiculo.setEnabled(boolean)
        self.ui.bt_busca_cliente.setEnabled(boolean)
        self.ui.bt_add_veiculo.setEnabled(boolean)

    def limpa_campos_item(self):
        self.ui.tx_busca_item.setText("")
        self.ui.tx_descricao_prod.setText("")
        self.ui.tx_qtd.setText("")
        self.ui.tx_valor.setText("")
        self.ui.tx_total.setText("")
        self.ui.tx_busca_item.setFocus()

    @staticmethod
    def delete_fins():
        v_fin = Venda_Fin()
        v_fin.venda_id = Venda_Tmp.get_cod_venda()
        v_fin.delete_fin_by_venda()

    def limpa_tela(self):
        self.ui.lb_valor_total.setText("0,00")
        self.ui.lb_descontos.setText("0,00")
        self.ui.lb_valor_pago.setText("0,00")
        self.ui.lb_valor_parcial.setText("0,00")

        self.ui.tx_busca_cliente.setEnabled(True)
        self.ui.bt_busca_cliente.setEnabled(True)
        self.ui.tx_busca_cliente.setText("")
        self.ui.tx_nome_cliente.setText("")
        self.ui.cb_veiculo.setCurrentIndex(0)
        self.ui.cb_veiculo.setEnabled(True)
        self.ui.cb_veiculo.clear()
        self.ui.bt_alterar_cliente.setHidden(True)

        self.ui.tb_venda.clearContents()
        self.ui.tb_venda.setRowCount(0)
        self.ui.tx_busca_cliente.setFocus()

        self.recebeu_pagamento = False
        self.finalizou = False
