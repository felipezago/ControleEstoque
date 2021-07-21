from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QMainWindow
from PyQt5.QtCore import Qt
from Model.Cliente import Cliente
from PyQt5 import QtCore
from Model.Endereco import Endereco
from Model.Pessoa import Pessoa
from Funcoes.funcoes import formatar_cpf, formatar_rg
from Funcoes.funcoes import formatar_cpf, formatar_rg


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
        self.setFixedSize(self.size())

        self.setWindowModality(QtCore.Qt.ApplicationModal)
        # removendo opção de maximizar
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

        self.cliente_selecionado = Cliente()
        self.cliente_selecionado.pessoa = Pessoa()
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

    def enable_cidade_estado(self):
        if not self.ui.tx_cidade.isEnabled():
            self.ui.tx_cidade.setEnabled(True)
        elif not self.ui.tx_estado.isEnabled():
            self.ui.tx_estado.setEnabled(True)

    def busca_cep(self):
        from Funcoes.funcoes import get_endereco
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
        from Funcoes.funcoes import exec_app

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
        self.ui.cb_clientes.addItem("CPF")
        self.ui.cb_clientes.addItem("RG")

    def sair(self):
        self.close()

    def buscar(self):
        self.ui.tb_clientes.clearContents()
        self.ui.tb_clientes.setRowCount(0)

        cli = Cliente()
        cli.pessoa = Pessoa()

        if self.ui.cb_clientes.currentIndex() == 1:
            cli.pessoa.nome = self.ui.tx_busca.text()
            if cli.pessoa.nome:
                dados = cli.pessoa.get_pessoa_by_desc_tabela("pess_nome", cli.pessoa.nome.upper(), 'CLIENTE')
            else:
                QMessageBox.warning(self, "Atenção!", "Favor informar algum valor!")
                self.dados_tabela()
                return
        elif self.ui.cb_clientes.currentIndex() == 0:
            if self.ui.tx_busca.text():
                cli.id = self.ui.tx_busca.text()
                dados = cli.get_cliente_by_id_tabela()
            else:
                QMessageBox.warning(self, "Atenção!", "Favor informar algum valor!")
                self.dados_tabela()
                return
        elif self.ui.cb_clientes.currentIndex() == 2:
            cli.pessoa.cpf = self.ui.tx_busca.text()
            if cli.pessoa.cpf:
                dados = cli.pessoa.get_pessoa_by_desc_tabela("pess_cpf", cli.pessoa.cpf, 'CLIENTE')
            else:
                QMessageBox.warning(self, "Atenção!", "Favor informar algum valor!")
                self.dados_tabela()
                return
        else:
            cli.pessoa.rg = self.ui.tx_busca.text()
            if cli.pessoa.rg:
                dados = cli.pessoa.get_pessoa_by_desc_tabela("pess_rg", cli.pessoa.rg, 'CLIENTE')
            else:
                QMessageBox.warning(self, "Atenção!", "Favor informar algum valor!")
                self.dados_tabela()
                return

        if dados:
            self.filtrado = True
            self.ui.bt_refresh.setEnabled(True)

            for i, linha in enumerate(dados):
                self.ui.tb_clientes.insertRow(i)
                for j in range(0, 13):
                    self.ui.tb_clientes.setItem(i, j, QTableWidgetItem(str(linha[j])))
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

        # pessoa
        if c is not None:
            # pessoa
            if c is not None:
                self.cliente_selecionado.pessoa = Pessoa()
                self.cliente_selecionado.pessoa.id = c[1]
                p = self.cliente_selecionado.pessoa.get_pessoa_cliente_by_id()
                self.cliente_selecionado.pessoa.cpf = p[2]
                self.cliente_selecionado.pessoa.nome = p[3]
                self.cliente_selecionado.pessoa.fone = p[4]
                self.cliente_selecionado.pessoa.email = p[5]
                self.cliente_selecionado.pessoa.rg = p[6]
                self.cliente_selecionado.pessoa.celular = p[7]

                # endereço
                self.cliente_selecionado.pessoa.endereco = Endereco()
                self.cliente_selecionado.pessoa.endereco.id = p[1]
                end_selecionado = self.cliente_selecionado.pessoa.endereco.get_endereco_by_id()
                self.cliente_selecionado.pessoa.endereco.rua = end_selecionado[1]
                self.cliente_selecionado.pessoa.endereco.bairro = end_selecionado[2]
                self.cliente_selecionado.pessoa.endereco.numero = end_selecionado[3]
                self.cliente_selecionado.pessoa.endereco.cidade = end_selecionado[4]
                self.cliente_selecionado.pessoa.endereco.estado = end_selecionado[5]
                self.cliente_selecionado.pessoa.endereco.cep = end_selecionado[6]

                # setando os edits
                self.ui.tx_id.setText(self.cliente_selecionado.id)
                self.ui.tx_cpf.setText(self.cliente_selecionado.pessoa.cpf)
                self.ui.tx_nome.setText(self.cliente_selecionado.pessoa.nome)
                self.ui.tx_fone.setText(self.cliente_selecionado.pessoa.fone)
                self.ui.tx_email.setText(self.cliente_selecionado.pessoa.email)
                self.ui.tx_rg.setText(self.cliente_selecionado.pessoa.rg)
                self.ui.tx_celular.setText(self.cliente_selecionado.pessoa.celular)

                self.ui.tx_rua.setText(self.cliente_selecionado.pessoa.endereco.rua)
                self.ui.tx_bairro.setText(self.cliente_selecionado.pessoa.endereco.bairro)
                self.ui.tx_numero.setText(self.cliente_selecionado.pessoa.endereco.numero)
                self.ui.tx_cidade.setText(self.cliente_selecionado.pessoa.endereco.cidade)
                self.ui.tx_estado.setText(self.cliente_selecionado.pessoa.endereco.estado)
                self.ui.tx_cep.setText(self.cliente_selecionado.pessoa.endereco.cep)

    def dados_tabela(self):
        self.cliente_selecionado.id = None
        self.ui.tx_busca.setText("")
        self.filtrado = False
        self.ui.bt_refresh.setEnabled(False)
        self.limpa_campos()
        self.ui.tb_clientes.clearContents()
        self.ui.tb_clientes.setRowCount(0)
        self.ui.bt_refresh.setEnabled(False)

        dados = Cliente.get_todos_clientes_tabela()

        for i, linha in enumerate(dados):
            self.ui.tb_clientes.insertRow(i)
            for j in range(0, 13):
                if j == 5:
                    self.ui.tb_clientes.setItem(i, 5, QTableWidgetItem(formatar_rg((linha[5]))))
                elif j == 1:
                    self.ui.tb_clientes.setItem(i, 1, QTableWidgetItem(formatar_cpf((linha[1]))))
                else:
                    self.ui.tb_clientes.setItem(i, j, QTableWidgetItem(str(linha[j])))

        if self.adicionando:
            self.ui.tb_clientes.selectRow(self.ui.tb_clientes.rowCount() - 1)
            self.adicionando = False

    def editar(self):
        from Funcoes.funcoes import formatar_cpf_rg

        if self.cliente_selecionado.id:
            itens = list()

            cli_editar = Cliente()
            cli_editar.id = self.ui.tx_id.text()
            itens.append(cli_editar.id)

            cli_editar.pessoa = Pessoa()
            cli_editar.pessoa.id = self.cliente_selecionado.pessoa.id
            cli_editar.pessoa.cpf = formatar_cpf_rg(self.ui.tx_cpf.text())
            itens.append(cli_editar.pessoa.cpf)
            cli_editar.pessoa.nome = self.ui.tx_nome.text()
            itens.append(cli_editar.pessoa.nome)
            cli_editar.pessoa.fone = self.ui.tx_fone.text()
            itens.append(cli_editar.pessoa.fone)
            cli_editar.pessoa.email = self.ui.tx_email.text()
            itens.append(cli_editar.pessoa.email)
            cli_editar.pessoa.rg = formatar_cpf_rg(self.ui.tx_rg.text())
            itens.append(cli_editar.pessoa.rg)
            cli_editar.pessoa.celular = self.ui.tx_celular.text()
            itens.append(cli_editar.pessoa.celular)

            cli_editar.pessoa.endereco = Endereco()
            cli_editar.pessoa.endereco.id = self.cliente_selecionado.pessoa.endereco.id
            cli_editar.pessoa.endereco.rua = self.ui.tx_rua.text().upper()
            itens.append(cli_editar.pessoa.endereco.rua)
            cli_editar.pessoa.endereco.bairro = self.ui.tx_bairro.text().upper()
            itens.append(cli_editar.pessoa.endereco.bairro)
            cli_editar.pessoa.endereco.numero = self.ui.tx_numero.text().upper()
            itens.append(cli_editar.pessoa.endereco.numero)
            cli_editar.pessoa.endereco.cidade = self.ui.tx_cidade.text().upper()
            itens.append(cli_editar.pessoa.endereco.cidade)
            cli_editar.pessoa.endereco.estado = self.ui.tx_estado.text().upper()
            itens.append(cli_editar.pessoa.endereco.estado)
            cli_editar.pessoa.endereco.cep = formatar_cpf_rg(self.ui.tx_cep.text())
            itens.append(cli_editar.pessoa.endereco.cep)

            try:
                cli_editar.pessoa.editar()
                cli_editar.pessoa.endereco.editar()
            except Exception as error:
                QMessageBox.warning(self, "Erro", str(error))
            else:
                self.ui.tb_clientes.setFocus()

                for i in range(0, 13):
                    self.ui.tb_clientes.setItem(self.linha_selecionada, i, QTableWidgetItem(itens[i]))

                self.ui.tb_clientes.setItem(self.linha_selecionada, 1, QTableWidgetItem(formatar_cpf((itens[1]))))
                self.ui.tb_clientes.setItem(self.linha_selecionada, 5, QTableWidgetItem(formatar_rg((itens[5]))))
        else:
            QMessageBox.warning(self, "Atenção!", "Favor selecionar alguma linha!")

    def excluir(self):
        if self.cliente_selecionado.id:
            reply = QMessageBox.question(self, 'Excluir?', f'Tem certeza que deseja excluir o cliente: '
                                                           f'{self.cliente_selecionado.pessoa.nome}?',
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
