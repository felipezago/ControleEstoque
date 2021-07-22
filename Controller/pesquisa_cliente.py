from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QMainWindow
from PyQt5.QtCore import Qt
from Model.Cliente import Cliente
from PyQt5 import QtGui
from Model.Pessoa import Pessoa
from Funcoes.funcoes import formatar_cpf, formatar_rg
from PyQt5 import QtCore


class EventFilter(QtCore.QObject):

    def __init__(self, parent=None):
        QtCore.QObject.__init__(self, parent)

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.ActivationChange:
            if self.parent().isActiveWindow():
                if obj.adicionando:
                    obj.dados_tabela()

        return QtCore.QObject.eventFilter(self, obj, event)


class PesquisaClientes(QMainWindow):
    def __init__(self, parent=None):
        super(PesquisaClientes, self).__init__(parent)
        from View.pesquisa_clientes import Ui_Frame

        self.ui = Ui_Frame()
        self.ui.setupUi(self)
        self.dialogs = list()
        self.tamanho_tela = self.size()
        self.setFixedSize(self.tamanho_tela)

        self.cliente_selecionado = Cliente()
        self.cliente_selecionado.pessoa = Pessoa()
        self.linha_selecionada = None
        self.filtrado = False
        self.adicionando = False
        self.tela_venda = parent

        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.installEventFilter(EventFilter(self))

        # ação dos botoes
        self.ui.bt_refresh.clicked.connect(self.dados_tabela)
        self.ui.bt_selecionar.clicked.connect(self.sair)
        self.ui.bt_inserir.clicked.connect(self.add)

        # ação da busca
        self.ui.bt_busca.clicked.connect(self.buscar)
        self.ui.tx_busca.returnPressed.connect(self.buscar)

        # signals
        self.ui.tb_clientes.cellClicked.connect(self.linha_clicada)
        self.ui.tb_clientes.cellDoubleClicked.connect(self.linha_clicada)
        self.ui.tx_busca.textChanged.connect(self.formatar_texto)
        self.ui.cb_clientes.currentIndexChanged.connect(self.limpa_campo_busca)

        for i in range(0, 7):
            self.ui.tb_clientes.horizontalHeaderItem(i).setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.ui.tb_clientes.setColumnWidth(0, 30)
        self.ui.tb_clientes.setColumnWidth(1, 150)
        self.ui.tb_clientes.setColumnWidth(2, 250)
        self.ui.tb_clientes.setColumnWidth(3, 150)
        self.ui.tb_clientes.setColumnWidth(4, 250)
        self.ui.tb_clientes.setColumnWidth(5, 150)
        self.ui.tb_clientes.setColumnWidth(6, 175)

        self.preenche_combo()
        self.dados_tabela()

    def add(self):
        from Controller.cadastro_clientes import CadastroClientes
        from Funcoes.funcoes import exec_app

        self.adicionando = True
        c_cli = CadastroClientes()
        exec_app(c_cli)
        self.dialogs.append(c_cli)

    def limpa_campo_busca(self):
        self.ui.tx_busca.setText("")

    def resizeEvent(self, a0):
        self.setFixedSize(self.tamanho_tela)

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

    def closeEvent(self, event: QtGui.QCloseEvent):
        if self.cliente_selecionado.id is not None:
            self.tela_venda.codigo_cliente = self.cliente_selecionado.id
            self.tela_venda.ui.tx_busca_cliente.setText(self.tela_venda.codigo_cliente)
            self.tela_venda.ui.tx_busca_cliente.setFocus()
            self.tela_venda.recebeu_codigo_cliente = True
        else:
            box = QMessageBox()
            box.setIcon(QMessageBox.Question)
            box.setWindowTitle('Sair?')
            box.setText('Tem certeza que deseja sair sem informar o código?')
            box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            button_sim = box.button(QMessageBox.Yes)
            button_sim.setText('Sim')
            button_nao = box.button(QMessageBox.No)
            button_nao.setText('Não')
            box.exec_()

            if box.clickedButton() == button_sim:
                event.accept()
            else:
                event.ignore()

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

        self.ui.tb_clientes.selectRow(0)

    def linha_clicada(self):
        tb = self.ui.tb_clientes
        self.linha_selecionada = tb.currentRow()

        self.cliente_selecionado.id = tb.item(tb.currentRow(), 0).text()
        c = self.cliente_selecionado.get_cliente_by_id()

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

    def dados_tabela(self):
        self.cliente_selecionado.id = None
        self.ui.tx_busca.setText("")
        self.filtrado = False
        self.ui.bt_refresh.setEnabled(False)
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
