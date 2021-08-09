from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from Model.Fornecedor import Fornecedor
from Funcoes.utils import formatar_cnpj
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


class PesquisaForn(QMainWindow):
    def __init__(self, parent=None):
        super(PesquisaForn, self).__init__(parent)
        from View.pesquisa_fornecedores import Ui_Frame

        self.ui = Ui_Frame()
        self.ui.setupUi(self)
        self.dialogs = list()
        self.tamanho_tela = self.size()
        self.setFixedSize(self.tamanho_tela)

        self.forn_selecionado = Fornecedor()
        self.linha_selecionada = None
        self.filtrado = False
        self.adicionando = False
        self.tela_venda = parent

        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.installEventFilter(EventFilter(self))

        # ação dos botoes
        self.ui.bt_refresh.clicked.connect(self.dados_tabela)
        self.ui.bt_selecionar.clicked.connect(self.sair)
        self.ui.bt_novo.clicked.connect(self.add)

        # ação da busca
        self.ui.bt_busca.clicked.connect(self.buscar)
        self.ui.tx_busca.returnPressed.connect(self.buscar)

        # signals
        self.ui.tb_fornecedores.cellClicked.connect(self.linha_clicada)
        self.ui.tb_fornecedores.cellDoubleClicked.connect(self.linha_clicada)
        self.ui.tx_busca.textChanged.connect(self.formatar_texto)
        self.ui.cb_fornecedores.currentIndexChanged.connect(self.limpa_campo_busca)

        for i in range(0, 5):
            self.ui.tb_fornecedores.horizontalHeaderItem(i).setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.ui.tb_fornecedores.setColumnWidth(0, 30)
        self.ui.tb_fornecedores.setColumnWidth(1, 250)
        self.ui.tb_fornecedores.setColumnWidth(2, 150)
        self.ui.tb_fornecedores.setColumnWidth(3, 150)
        self.ui.tb_fornecedores.setColumnWidth(4, 150)

        self.preenche_combo()
        self.dados_tabela()

    def add(self):
        from Controller.cadastro_fornecedor import CadastroFornecedor
        from Funcoes.utils import exec_app

        self.adicionando = True
        c_forn = CadastroFornecedor()
        exec_app(c_forn)
        self.dialogs.append(c_forn)

    def limpa_campo_busca(self):
        self.ui.tx_busca.setText("")

    def resizeEvent(self, a0):
        self.setFixedSize(self.tamanho_tela)

    def formatar_texto(self):
        texto = self.ui.tx_busca.text()
        tamanho = len(texto)
        if self.ui.cb_fornecedores.currentIndex() in (0, 3):
            if not texto[tamanho-1:tamanho].isnumeric():
                self.ui.tx_busca.setText(texto[:tamanho - 1])

    def preenche_combo(self):
        self.ui.cb_fornecedores.clear()
        self.ui.cb_fornecedores.addItem("ID")
        self.ui.cb_fornecedores.addItem("CNPJ")
        self.ui.cb_fornecedores.addItem("NOME FANTASIA")

    def sair(self):
        self.close()

    def closeEvent(self, event: QtGui.QCloseEvent):
        if self.forn_selecionado.id is not None:
            self.tela_venda.codigo_forn = self.forn_selecionado.id
            self.tela_venda.ui.tx_busca_forn.setText(self.tela_venda.codigo_forn)
            self.tela_venda.ui.tx_busca_forn.setFocus()
            self.tela_venda.recebeu_codigo_forn = True
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
        self.ui.tb_fornecedores.clearContents()
        self.ui.tb_fornecedores.setRowCount(0)

        forn = Fornecedor()

        if self.ui.cb_fornecedores.currentIndex() == 1:
            forn.cnpj = self.ui.tx_busca.text()
            if forn.cnpj:
                dados = Fornecedor.get_fornecedores_by_desc("forn_cnpj", forn.cnpj)
            else:
                QMessageBox.warning(self, "Atenção!", "Favor informar algum valor!")
                self.dados_tabela()
                return
        elif self.ui.cb_fornecedores.currentIndex() == 0:
            if self.ui.tx_busca.text():
                forn.id = int(self.ui.tx_busca.text())
                dados = forn.get_fornecedor_by_id()
            else:
                QMessageBox.warning(self, "Atenção!", "Favor informar algum valor!")
                self.dados_tabela()
                return
        else:
            forn.nome = self.ui.tx_busca.text()
            if forn.nome:
                dados = Fornecedor.get_fornecedores_by_desc("forn_nome", forn.nome.upper())
            else:
                QMessageBox.warning(self, "Atenção!", "Favor informar algum valor!")
                self.dados_tabela()
                return

        if dados:
            self.filtrado = True
            self.ui.bt_refresh.setEnabled(True)

            if isinstance(dados, list):
                for i, linha in enumerate(dados):
                    self.ui.tb_fornecedores.insertRow(i)
                    id_fornecedor = QTableWidgetItem(str(linha[0]))
                    self.ui.tb_fornecedores.setItem(i, 0, id_fornecedor)

                    for j in range(0, 5):
                        if j == 2:
                            self.ui.tb_fornecedores.setItem(i, j, QTableWidgetItem(formatar_cnpj(str(linha[j]))))
                        else:
                            self.ui.tb_fornecedores.setItem(i, j, QTableWidgetItem(str(linha[j])))
            else:
                self.ui.tb_fornecedores.insertRow(0)
                id_fornecedor = QTableWidgetItem(str(dados[0]))
                self.ui.tb_fornecedores.setItem(0, 0, id_fornecedor)

                for j in range(0, 11):
                    if j == 2:
                        self.ui.tb_fornecedores.setItem(0, j, QTableWidgetItem(formatar_cnpj(str(dados[j]))))
                    else:
                        self.ui.tb_fornecedores.setItem(0, j, QTableWidgetItem(str(dados[j])))
        else:
            QMessageBox.warning(self, "Erro", "Não foi encontrado nenhum registro!")
            self.ui.tx_busca.setText("")
            self.dados_tabela()

        self.ui.tb_fornecedores.selectRow(0)

    def linha_clicada(self):
        tb = self.ui.tb_fornecedores
        self.linha_selecionada = tb.currentRow()
        self.forn_selecionado.id = tb.item(tb.currentRow(), 0).text()
        c = self.forn_selecionado.get_fornecedor_by_id()

        if c is not None:
            self.forn_selecionado.cpf = c[1]
            self.forn_selecionado.nome = c[2]
            self.forn_selecionado.fone = c[3]
            self.forn_selecionado.email = c[4]
            self.forn_selecionado.rg = c[5]
            self.forn_selecionado.celular = c[6]

    def dados_tabela(self):
        self.forn_selecionado.id = None
        self.ui.tx_busca.setText("")
        self.filtrado = False
        self.ui.bt_refresh.setEnabled(False)
        self.ui.tb_fornecedores.clearContents()
        self.ui.tb_fornecedores.setRowCount(0)
        self.ui.bt_refresh.setEnabled(False)

        dados = Fornecedor.get_todos_fornecedores_tabela()

        for i, linha in enumerate(dados):
            self.ui.tb_fornecedores.insertRow(i)
            for j in range(0, 5):
                if j == 2:
                    self.ui.tb_fornecedores.setItem(i, j, QTableWidgetItem(formatar_cnpj(str(linha[j]))))
                else:
                    self.ui.tb_fornecedores.setItem(i, j, QTableWidgetItem(str(linha[j])))

        if self.adicionando:
            self.ui.tb_fornecedores.selectRow(self.ui.tb_fornecedores.rowCount() - 1)
            self.adicionando = False
