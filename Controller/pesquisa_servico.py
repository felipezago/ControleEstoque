from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QMainWindow
from PyQt5.QtCore import Qt
from Model.Servicos import Servicos
from PyQt5 import QtGui
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


class PesquisaServico(QMainWindow):
    def __init__(self, parent=None):
        super(PesquisaServico, self).__init__(parent)
        from View.pesquisa_servicos import Ui_Frame

        self.ui = Ui_Frame()
        self.ui.setupUi(self)
        self.dialogs = list()
        self.tamanho_tela = self.size()
        self.setFixedSize(self.tamanho_tela)

        self.servico_selecionado = Servicos()
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
        self.ui.bt_busca_servicos.clicked.connect(self.buscar)
        self.ui.tx_busca_servicos.returnPressed.connect(self.buscar)

        # signals
        self.ui.tb_servicos.cellClicked.connect(self.linha_clicada)
        self.ui.tb_servicos.cellDoubleClicked.connect(self.linha_clicada)
        self.ui.tx_busca_servicos.textChanged.connect(self.formatar_texto)
        self.ui.cb_servicos.currentIndexChanged.connect(self.limpa_campo_busca)

        for i in range(0, 3):
            self.ui.tb_servicos.horizontalHeaderItem(i).setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.ui.tb_servicos.setColumnWidth(0, 30)
        self.ui.tb_servicos.setColumnWidth(1, 250)
        self.ui.tb_servicos.setColumnWidth(2, 100)

        self.preenche_combo()
        self.dados_tabela()

    def add(self):
        from Controller.cadastro_servicos import CadastroServicos
        from Funcoes.funcoes import exec_app

        self.adicionando = True
        c_serv = CadastroServicos()
        exec_app(c_serv)
        self.dialogs.append(c_serv)

    def limpa_campo_busca(self):
        self.ui.tx_busca_servicos.setText("")

    def resizeEvent(self, a0):
        self.setFixedSize(self.tamanho_tela)

    def formatar_texto(self):
        texto = self.ui.tx_busca_servicos.text()
        tamanho = len(texto)
        if self.ui.cb_servicos.currentIndex() == 0:
            if not texto[tamanho - 1:tamanho].isnumeric():
                self.ui.tx_busca_servicos.setText(texto[:tamanho - 1])

        if self.ui.cb_servicos.currentIndex() in (2, 3, 4):
            if not texto[tamanho - 1:tamanho].isnumeric():
                if texto[tamanho - 1:tamanho] != '.':
                    self.ui.tx_busca_servicos.setText(texto[:tamanho - 1])

                if texto.count(".") > 1 and texto[tamanho - 1:tamanho] == '.':
                    self.ui.tx_busca_servicos.setText(texto[:tamanho - 1])

    def preenche_combo(self):
        self.ui.cb_servicos.clear()
        self.ui.cb_servicos.addItem("ID")
        self.ui.cb_servicos.addItem("DESCRIÇÃO")
        self.ui.cb_servicos.addItem("PREÇO >")
        self.ui.cb_servicos.addItem("PREÇO <")
        self.ui.cb_servicos.addItem("PREÇO =")

    def sair(self):
        self.close()

    def closeEvent(self, event: QtGui.QCloseEvent):
        if self.servico_selecionado.id is not None:
            self.tela_venda.codigo_item = self.servico_selecionado.id
            self.tela_venda.ui.tx_busca_item.setText(f"{self.tela_venda.codigo_item}")
            self.tela_venda.ui.tx_busca_item.setFocus()
            self.tela_venda.recebeu_codigo_item = True
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
        self.ui.tb_servicos.clearContents()
        self.ui.tb_servicos.setRowCount(0)

        serv = Servicos()

        dados = ""

        if self.ui.cb_servicos.currentIndex() == 1:
            serv.descricao = self.ui.tx_busca_servicos.text()
            if serv.descricao:
                dados = Servicos.get_servicos_by_desc(serv.descricao.upper())
            else:
                QMessageBox.warning(self, "Atenção!", "Favor informar algum valor!")
                self.dados_tabela()
                return
        elif self.ui.cb_servicos.currentIndex() == 0:
            if self.ui.tx_busca_servicos.text():
                serv.id = int(self.ui.tx_busca_servicos.text())
                dados = serv.get_servico_by_id()
            else:
                QMessageBox.warning(self, "Atenção!", "Favor informar algum valor!")
                self.dados_tabela()
                return
        else:
            texto = self.ui.tx_busca_servicos.text()
            if texto:
                if texto.count('.') >= 1:
                    indice_ponto = texto.find('.')
                    if texto[indice_ponto + 1:indice_ponto + 2] == '0':
                        self.ui.tx_busca_servicos.setText(texto[:indice_ponto])

                serv.preco = float(self.ui.tx_busca_servicos.text())

                if self.ui.cb_servicos.currentIndex() == 2:
                    dados = serv.get_servico_by_preco(">=")
                elif self.ui.cb_servicos.currentIndex() == 3:
                    dados = serv.get_servico_by_preco("<=")
                elif self.ui.cb_servicos.currentIndex() == 4:
                    dados = serv.get_servico_by_preco("=")
            else:
                QMessageBox.warning(self, "Atenção!", "Favor informar algum valor!")
                self.dados_tabela()
                return

        if dados:
            self.filtrado = True
            self.ui.bt_refresh.setEnabled(True)

            if type(dados) == list:
                for i, linha in enumerate(dados):
                    item_id = QTableWidgetItem(str(linha[0]))
                    item_id.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

                    item_desc = QTableWidgetItem(linha[1])
                    item_desc.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

                    item_preco = QTableWidgetItem(str(linha[2]))
                    item_preco.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

                    self.ui.tb_servicos.insertRow(i)

                    for c in range(0, 3):
                        item = str(linha[c])
                        self.ui.tb_servicos.setItem(i, c, QTableWidgetItem(item))
            else:
                self.ui.tb_servicos.insertRow(0)
                for c in range(0, 3):
                    item = str(dados[c])
                    self.ui.tb_servicos.setItem(0, c, QTableWidgetItem(item))

        else:
            QMessageBox.warning(self, "Erro", "Não foi encontrado nenhum registro!")
            self.ui.tx_busca_servicos.setText("")
            self.dados_tabela()

        self.ui.tb_servicos.selectRow(0)

    def linha_clicada(self):
        tb = self.ui.tb_servicos
        self.linha_selecionada = tb.currentRow()

        self.servico_selecionado.id = int(tb.item(tb.currentRow(), 0).text())
        c = self.servico_selecionado.get_servico_by_id()
        self.servico_selecionado.descricao = c[1]
        self.servico_selecionado.preco = c[2]

    def dados_tabela(self):
        self.servico_selecionado.id = None
        self.ui.tx_busca_servicos.setText("")

        if self.adicionando and not self.filtrado:
            novo_serv = Servicos()
            novo_id = novo_serv.ultimo_servico()
            novo_serv.id = novo_id[0][0]
            novo_serv.get_servico_by_id()
            novo_serv.descricao = novo_serv.get_servico_by_id()[1]
            novo_serv.preco = novo_serv.get_servico_by_id()[2]

            item_id = QTableWidgetItem(str(novo_serv.id))
            item_id.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

            item_desc = QTableWidgetItem(novo_serv.descricao)
            item_desc.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

            item_preco = QTableWidgetItem(str(novo_serv.preco))
            item_preco.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

            self.ui.tb_servicos.insertRow(self.ui.tb_servicos.rowCount())
            self.ui.tb_servicos.setItem(self.ui.tb_servicos.rowCount() - 1, 0, item_id)
            self.ui.tb_servicos.setItem(self.ui.tb_servicos.rowCount() - 1, 1, item_desc)
            self.ui.tb_servicos.setItem(self.ui.tb_servicos.rowCount() - 1, 2, item_preco)

            self.ui.tb_servicos.selectRow(self.ui.tb_servicos.rowCount() - 1)
            self.adicionando = False
        else:
            self.filtrado = False
            self.ui.bt_refresh.setEnabled(False)
            self.ui.tb_servicos.clearContents()
            self.ui.tb_servicos.setRowCount(0)

            dados = Servicos.get_todos_servicos()

            for i, linha in enumerate(dados):
                item_id = QTableWidgetItem(str(linha[0]))
                item_id.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

                item_desc = QTableWidgetItem(str(linha[1]))
                item_desc.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

                item_preco = QTableWidgetItem(str(linha[2]))
                item_preco.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

                self.ui.tb_servicos.insertRow(i)
                for c in range(0, 3):
                    item = str(linha[c])
                    self.ui.tb_servicos.setItem(i, c, QTableWidgetItem(item))

            if self.adicionando:
                self.ui.tb_servicos.selectRow(self.ui.tb_servicos.rowCount() - 1)
                self.adicionando = False
