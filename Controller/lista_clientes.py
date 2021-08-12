from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QMainWindow
from PyQt5.QtCore import Qt
from Model.Cliente import Cliente
from PyQt5 import QtCore, QtGui
from Funcoes.utils import formatar_cpf, formatar_rg, formatar_cnpj


class EventFilter(QtCore.QObject):

    def __init__(self, parent=None):
        QtCore.QObject.__init__(self, parent)

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.ActivationChange:
            if self.parent().isActiveWindow():
                if obj.adicionando:
                    obj.dados_tabela()

        return QtCore.QObject.eventFilter(self, obj, event)


class ListaClientes(QMainWindow):
    def __init__(self, parent=None):
        super(ListaClientes, self).__init__(parent)
        from View.lista_clientes import Ui_Frame

        self.ui = Ui_Frame()
        self.ui.setupUi(self)
        self.dialogs = list()
        self.tamanho = self.size()
        self.setFixedSize(self.tamanho)

        self.setWindowIcon(QtGui.QIcon("Imagens/logo_fzr.png"))

        self.setWindowModality(QtCore.Qt.ApplicationModal)
        # removendo opção de maximizar
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

        self.cliente_selecionado = Cliente()
        self.linha_selecionada = None
        self.adicionando = False
        self.filtrado = False
        self.qtd_cli = Cliente.qtd_cli()

        self.installEventFilter(EventFilter(self))

        # ação dos botoes
        self.ui.bt_cancelar.clicked.connect(self.sair)
        self.ui.bt_salvar.clicked.connect(self.editar)
        self.ui.bt_refresh.clicked.connect(self.dados_tabela)
        self.ui.bt_excluir.clicked.connect(self.excluir)
        self.ui.bt_novo.clicked.connect(self.novo)

        # ação da busca
        self.ui.bt_busca.clicked.connect(self.buscar)
        self.ui.tx_busca.returnPressed.connect(self.buscar)
        self.ui.tx_cep.returnPressed.connect(self.busca_cep)
        self.ui.bt_busca_cep.clicked.connect(self.busca_cep)

        # signals
        self.ui.tb_clientes.cellClicked.connect(self.linha_clicada)
        self.ui.tx_busca.textChanged.connect(self.formatar_texto)
        self.ui.cb_clientes.currentIndexChanged.connect(self.limpa_campo_busca)
        self.ui.tx_cep.textChanged.connect(self.enable_cidade_estado)

        self.set_tx_enabled(False)
        self.ui.tx_id.setEnabled(False)

        for i in range(0, 13):
            self.ui.tb_clientes.horizontalHeaderItem(i).setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.ui.tb_clientes.setColumnWidth(0, 30)
        self.ui.tb_clientes.setColumnWidth(1, 150)
        self.ui.tb_clientes.setColumnWidth(2, 250)
        self.ui.tb_clientes.setColumnWidth(3, 150)
        self.ui.tb_clientes.setColumnWidth(4, 250)
        self.ui.tb_clientes.setColumnWidth(5, 150)
        self.ui.tb_clientes.setColumnWidth(6, 175)
        self.ui.tb_clientes.setColumnWidth(7, 150)
        self.ui.tb_clientes.setColumnWidth(8, 125)
        self.ui.tb_clientes.setColumnWidth(9, 75)
        self.ui.tb_clientes.setColumnWidth(10, 110)
        self.ui.tb_clientes.setColumnWidth(11, 60)
        self.ui.tb_clientes.setColumnWidth(12, 100)

        self.ui.tx_nome.setMaxLength(60)
        self.ui.tx_email.setMaxLength(50)
        self.ui.tx_rua.setMaxLength(60)
        self.ui.tx_numero.setMaxLength(10)
        self.ui.tx_cidade.setMaxLength(50)
        self.ui.tx_estado.setMaxLength(2)
        self.ui.tx_bairro.setMaxLength(60)

        self.preenche_combo()
        self.dados_tabela()

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        self.setFixedSize(self.tamanho)

    def enable_cidade_estado(self):
        if not self.ui.tx_cidade.isEnabled():
            self.ui.tx_cidade.setEnabled(True)
        elif not self.ui.tx_estado.isEnabled():
            self.ui.tx_estado.setEnabled(True)

    def busca_cep(self):
        from Funcoes.APIs import get_endereco
        from PyQt5.QtWidgets import QMessageBox

        self.ui.tx_cidade.setEnabled(True)
        self.ui.tx_estado.setEnabled(True)

        if not self.ui.tx_cep.text() == '-':
            try:
                endereco = get_endereco(self.ui.tx_cep.text())
            except Exception as e:
                QMessageBox.warning(self, "Erro!", f"{e}")
                self.ui.tx_bairro.setText("")
                self.ui.tx_cidade.setText("")
                self.ui.tx_estado.setText("")
                self.ui.tx_rua.setText("")
                self.ui.tx_cep.setText("")
            else:
                self.ui.tx_bairro.setText("")
                self.ui.tx_cidade.setText("")
                self.ui.tx_estado.setText("")
                self.ui.tx_rua.setText("")

                if endereco['bairro'] is not None:
                    self.ui.tx_bairro.setText(endereco['bairro'])
                if endereco['cidade'] is not None:
                    self.ui.tx_cidade.setText(endereco['cidade'])
                    self.ui.tx_cidade.setEnabled(False)
                if endereco['logradouro'] is not None:
                    self.ui.tx_rua.setText(endereco['logradouro'])
                if endereco['uf'] is not None:
                    self.ui.tx_estado.setText(endereco['uf'])
                    self.ui.tx_estado.setEnabled(False)
        else:
            QMessageBox.warning(self, "Erro!", "Favor informar um CEP.")

    def novo(self):
        from Controller.cadastro_clientes import CadastroClientes
        from Funcoes.utils import exec_app

        self.adicionando = True
        c = CadastroClientes()
        exec_app(c)
        self.dialogs.append(c)

    def limpa_campo_busca(self):
        self.ui.tx_busca.setText("")

    def formatar_texto(self):
        texto = self.ui.tx_busca.text()
        tamanho = len(texto)
        if self.ui.cb_clientes.currentIndex() != 1:
            if not texto[tamanho-1:tamanho].isnumeric():
                self.ui.tx_busca.setText(texto[:tamanho - 1])

    def preenche_combo(self):
        self.ui.cb_clientes.clear()
        self.ui.cb_clientes.addItem("ID")
        self.ui.cb_clientes.addItem("NOME")
        self.ui.cb_clientes.addItem("CPF/CNPJ")
        self.ui.cb_clientes.addItem("RG")

    def sair(self):
        self.close()

    def buscar(self):
        self.ui.tb_clientes.clearContents()
        self.ui.tb_clientes.setRowCount(0)

        cli = Cliente()

        if self.ui.cb_clientes.currentIndex() == 1:
            cli.nome = self.ui.tx_busca.text()
            if cli.nome:
                dados = cli.get_cliente_by_desc("clie_nome", cli.nome.upper())
            else:
                QMessageBox.warning(self, "Atenção!", "Favor informar algum valor!")
                self.dados_tabela()
                return
        elif self.ui.cb_clientes.currentIndex() == 0:
            if self.ui.tx_busca.text():
                cli.id = self.ui.tx_busca.text()
                dados = cli.get_cliente_by_id()
            else:
                QMessageBox.warning(self, "Atenção!", "Favor informar algum valor!")
                self.dados_tabela()
                return
        elif self.ui.cb_clientes.currentIndex() == 2:
            cli.cpf = self.ui.tx_busca.text()
            if cli.cpf:
                dados = cli.get_cliente_by_desc("clie_cpf_cnpj", cli.cpf)
            else:
                QMessageBox.warning(self, "Atenção!", "Favor informar algum valor!")
                self.dados_tabela()
                return
        else:
            cli.rg = self.ui.tx_busca.text()
            if cli.rg:
                dados = cli.get_cliente_by_desc("clie_rg", cli.rg)
            else:
                QMessageBox.warning(self, "Atenção!", "Favor informar algum valor!")
                self.dados_tabela()
                return

        if dados:
            self.filtrado = True
            self.ui.bt_refresh.setEnabled(True)

            if isinstance(dados, list):
                for i, linha in enumerate(dados):
                    self.ui.tb_clientes.insertRow(i)
                    for j in range(0, 13):
                        if j == 1:
                            if len(linha[j]) >= 14:
                                self.ui.tb_clientes.setItem(i, j, QTableWidgetItem(formatar_cnpj(str(linha[j]))))
                            else:
                                self.ui.tb_clientes.setItem(i, j, QTableWidgetItem(formatar_cpf(str(linha[j]))))
                        elif j == 5:
                            self.ui.tb_clientes.setItem(i, j, QTableWidgetItem(formatar_rg(str(linha[j]))))
                        else:
                            self.ui.tb_clientes.setItem(i, j, QTableWidgetItem(str(linha[j])))
            else:
                self.ui.tb_clientes.insertRow(0)
                for j in range(0, 13):
                    if j == 1:
                        if len(dados[j]) >= 14:
                            self.ui.tb_clientes.setItem(0, j, QTableWidgetItem(formatar_cnpj(str(dados[j]))))
                        else:
                            self.ui.tb_clientes.setItem(0, j, QTableWidgetItem(formatar_cpf(str(dados[j]))))
                    elif j == 5:
                        self.ui.tb_clientes.setItem(0, j, QTableWidgetItem(formatar_rg(str(dados[j]))))
                    else:
                        self.ui.tb_clientes.setItem(0, j, QTableWidgetItem(str(dados[j])))
        else:
            QMessageBox.warning(self, "Erro", "Não foi encontrado nenhum registro!")
            self.ui.tx_busca.setText("")
            self.dados_tabela()

        self.limpa_campos()
        self.ui.tb_clientes.selectRow(0)

    def linha_clicada(self):
        self.set_tx_enabled(True)

        tb = self.ui.tb_clientes
        self.linha_selecionada = tb.currentRow()
        self.cliente_selecionado.id = tb.item(tb.currentRow(), 0).text()
        c = self.cliente_selecionado.get_cliente_by_id()

        if c is not None:
            self.cliente_selecionado.cpf = c[1]
            self.cliente_selecionado.nome = c[2]
            self.cliente_selecionado.fone = c[3]
            self.cliente_selecionado.email = c[4]
            self.cliente_selecionado.rg = c[5]
            self.cliente_selecionado.celular = c[6]
            self.cliente_selecionado.rua = c[7]
            self.cliente_selecionado.bairro = c[8]
            self.cliente_selecionado.numero = c[9]
            self.cliente_selecionado.cidade = c[10]
            self.cliente_selecionado.estado = c[11]
            self.cliente_selecionado.cep = c[12]

            # setando os edits
            self.ui.tx_id.setText(self.cliente_selecionado.id)
            if len(self.cliente_selecionado.cpf) >= 14:
                self.ui.tx_cpf.setInputMask("##.###.###/####-##")
                self.ui.tx_rg.setEnabled(False)
                self.ui.tx_celular.setEnabled(False)
                self.ui.tx_celular.setInputMask("")
                self.ui.tx_rg.setInputMask("")
                self.ui.tx_celular.setText("ISENTO")
                self.ui.tx_celular.setText("ISENTO")
            else:
                self.ui.tx_cpf.setInputMask("###.###.###-##")
                self.ui.tx_rg.setEnabled(True)
                self.ui.tx_celular.setEnabled(True)
                self.ui.tx_celular.setInputMask("(##) #####-####")
                self.ui.tx_rg.setInputMask("##.###.###-#")
            self.ui.tx_cpf.setText(self.cliente_selecionado.cpf)
            self.ui.tx_nome.setText(self.cliente_selecionado.nome)
            self.ui.tx_fone.setText(self.cliente_selecionado.fone)
            self.ui.tx_email.setText(self.cliente_selecionado.email)
            self.ui.tx_rg.setText(self.cliente_selecionado.rg)
            self.ui.tx_celular.setText(self.cliente_selecionado.celular)

            self.ui.tx_rua.setText(self.cliente_selecionado.rua)
            self.ui.tx_bairro.setText(self.cliente_selecionado.bairro)
            self.ui.tx_numero.setText(self.cliente_selecionado.numero)
            self.ui.tx_cidade.setText(self.cliente_selecionado.cidade)
            self.ui.tx_estado.setText(self.cliente_selecionado.estado)
            self.ui.tx_cep.setText(self.cliente_selecionado.cep)

    def dados_tabela(self):
        self.cliente_selecionado.id = None
        self.ui.tx_busca.setText("")
        self.filtrado = False
        self.ui.bt_refresh.setEnabled(False)
        self.limpa_campos()
        self.ui.tb_clientes.clearContents()
        self.ui.tb_clientes.setRowCount(0)
        self.ui.bt_refresh.setEnabled(False)

        dados = Cliente.get_todos_clientes()

        for i, linha in enumerate(dados):
            self.ui.tb_clientes.insertRow(i)
            for j in range(0, 13):
                if j == 5:
                    if linha[5] != "ISENTO":
                        self.ui.tb_clientes.setItem(i, 5, QTableWidgetItem(formatar_rg((linha[5]))))
                    else:
                        self.ui.tb_clientes.setItem(i, 5, QTableWidgetItem(linha[5]))
                elif j == 1:
                    if len(linha[j]) >= 14:
                        self.ui.tb_clientes.setItem(i, j, QTableWidgetItem(formatar_cnpj(str(linha[j]))))
                    else:
                        self.ui.tb_clientes.setItem(i, j, QTableWidgetItem(formatar_cpf(str(linha[j]))))
                else:
                    self.ui.tb_clientes.setItem(i, j, QTableWidgetItem(str(linha[j])))

        if self.adicionando:
            self.ui.tb_clientes.selectRow(self.ui.tb_clientes.rowCount() - 1)
            self.adicionando = False

    def editar(self):
        from Funcoes.utils import retirar_formatacao

        if self.cliente_selecionado.id:
            itens = list()

            cli_editar = Cliente()
            cli_editar.id = self.ui.tx_id.text()
            itens.append(cli_editar.id)
            cli_editar.cpf = retirar_formatacao(self.ui.tx_cpf.text())
            itens.append(cli_editar.cpf)
            cli_editar.nome = self.ui.tx_nome.text()
            itens.append(cli_editar.nome)
            cli_editar.fone = self.ui.tx_fone.text()
            itens.append(cli_editar.fone)
            cli_editar.email = self.ui.tx_email.text()
            itens.append(cli_editar.email)
            cli_editar.rg = retirar_formatacao(self.ui.tx_rg.text())
            itens.append(cli_editar.rg)
            cli_editar.celular = self.ui.tx_celular.text()
            itens.append(cli_editar.celular)
            cli_editar.rua = self.ui.tx_rua.text().upper()
            itens.append(cli_editar.rua)
            cli_editar.bairro = self.ui.tx_bairro.text().upper()
            itens.append(cli_editar.bairro)
            cli_editar.numero = self.ui.tx_numero.text().upper()
            itens.append(cli_editar.numero)
            cli_editar.cidade = self.ui.tx_cidade.text().upper()
            itens.append(cli_editar.cidade)
            cli_editar.estado = self.ui.tx_estado.text().upper()
            itens.append(cli_editar.estado)
            cli_editar.cep = retirar_formatacao(self.ui.tx_cep.text())
            itens.append(cli_editar.cep)

            try:
                cli_editar.editar()
            except Exception as error:
                QMessageBox.warning(self, "Erro", str(error))
            else:
                self.ui.tb_clientes.setFocus()

                for i in range(0, 13):
                    if i == 1:
                        if len(itens[i]) >= 14:
                            self.ui.tb_clientes.setItem(self.linha_selecionada, i,
                                                        QTableWidgetItem(formatar_cnpj(str(itens[i]))))
                        else:
                            self.ui.tb_clientes.setItem(self.linha_selecionada, i,
                                                        QTableWidgetItem(formatar_cpf(str(itens[i]))))
                    elif i == 5:
                        if itens[5] != "ISENTO":
                            self.ui.tb_clientes.setItem(self.linha_selecionada, 5,
                                                    QTableWidgetItem(formatar_rg((itens[5]))))
                        else:
                            self.ui.tb_clientes.setItem(self.linha_selecionada, 5,
                                                        QTableWidgetItem(itens[5]))
                    else:
                        self.ui.tb_clientes.setItem(self.linha_selecionada, i, QTableWidgetItem(itens[i]))
        else:
            QMessageBox.warning(self, "Atenção!", "Favor selecionar alguma linha!")

    def excluir(self):
        if self.cliente_selecionado.id:
            reply = QMessageBox.question(self, 'Excluir?', f'Tem certeza que deseja excluir o cliente: '
                                                           f'{self.cliente_selecionado.nome}?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

            if reply == QMessageBox.Yes:
                try:
                    self.cliente_selecionado.delete_cliente_by_id()
                    self.cliente_selecionado.id = None
                except Exception as error:
                    QMessageBox.warning(self, "Erro", str(error))
                else:
                    self.ui.tb_clientes.removeRow(self.linha_selecionada)
                    self.limpa_campos()
            else:
                return
        else:
            QMessageBox.warning(self, "Atenção!", "Favor selecionar alguma linha!")

    def limpa_campos(self):
        self.ui.tx_id.setText("")
        self.ui.tx_fone.setText("")
        self.ui.tx_email.setText("")
        self.ui.tx_cep.setText("")
        self.ui.tx_rua.setText("")
        self.ui.tx_numero.setText("")
        self.ui.tx_bairro.setText("")
        self.ui.tx_cidade.setText("")
        self.ui.tx_estado.setText("")
        self.ui.tx_rg.setText("")
        self.ui.tx_cpf.setText("")
        self.ui.tx_nome.setText("")
        self.ui.tx_celular.setText("")

    def set_tx_enabled(self, boolean):
        self.ui.tx_fone.setEnabled(boolean)
        self.ui.tx_email.setEnabled(boolean)
        self.ui.tx_cep.setEnabled(boolean)
        self.ui.tx_rua.setEnabled(boolean)
        self.ui.tx_numero.setEnabled(boolean)
        self.ui.tx_bairro.setEnabled(boolean)
        self.ui.tx_cidade.setEnabled(boolean)
        self.ui.tx_estado.setEnabled(boolean)
        self.ui.tx_rg.setEnabled(boolean)
        self.ui.tx_nome.setEnabled(boolean)
        self.ui.tx_celular.setEnabled(boolean)
        self.ui.tx_cpf.setEnabled(boolean)
