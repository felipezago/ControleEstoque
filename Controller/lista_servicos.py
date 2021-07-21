from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from Model.Servicos import Servicos
from PyQt5 import QtCore
from PyQt5.QtCore import Qt


class EventFilter(QtCore.QObject):

    def __init__(self, parent=None):
        QtCore.QObject.__init__(self, parent)

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.ActivationChange:
            if self.parent().isActiveWindow():
                if obj.adicionando_serv:
                    obj.dados_tabela()

        return QtCore.QObject.eventFilter(self, obj, event)


class ListaServicos (QMainWindow):
    def __init__(self, parent=None):
        super(ListaServicos, self).__init__(parent)
        from View.lista_servicos import Ui_Frame

        self.ui = Ui_Frame()
        self.ui.setupUi(self)
        self.dialogs = list()
        self.setFixedSize(self.size())

        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

        self.serv_selecionado = Servicos()
        self.linha_selecionada = None
        self.adicionando_serv = False
        self.filtrado = False
        self.qtd_servicos = Servicos.qtd_servicos()

        self.installEventFilter(EventFilter(self))

        # ação dos botoes
        self.ui.bt_cancelar.clicked.connect(self.sair)
        self.ui.bt_refresh.clicked.connect(self.dados_tabela)
        self.ui.bt_excluir.clicked.connect(self.excluir)
        self.ui.bt_novo.clicked.connect(self.novo_servico)
        self.ui.bt_salvar.clicked.connect(self.editar)

        # ação da busca
        self.ui.bt_busca_servicos.clicked.connect(self.buscar)
        self.ui.tx_busca_servicos.returnPressed.connect(self.buscar)

        # signals
        self.ui.tb_servicos.cellClicked.connect(self.linha_clicada)
        self.ui.tx_busca_servicos.textChanged.connect(self.formatar_texto)
        self.ui.cb_servicos.currentIndexChanged.connect(self.limpa_campo_busca)

        self.ui.tx_id.setEnabled(False)
        self.ui.tx_desc_serv.setEnabled(False)
        self.ui.tx_preco.setEnabled(False)

        self.ui.tb_servicos.setColumnWidth(0, 20)
        self.ui.tb_servicos.setColumnWidth(1, 330)
        self.ui.tb_servicos.setColumnWidth(2, 40)

        for c in range(0, 3):
            self.ui.tb_servicos.horizontalHeaderItem(c).setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.preenche_combo()
        self.dados_tabela()

    def novo_servico(self):
        from Controller.cadastro_servicos import CadastroServicos
        from Funcoes.funcoes import exec_app

        self.adicionando_serv = True
        c = CadastroServicos()
        exec_app(c)
        self.dialogs.append(c)

    def limpa_campo_busca(self):
        self.ui.tx_busca_servicos.setText("")

    def formatar_texto(self):
        texto = self.ui.tx_busca_servicos.text()
        tamanho = len(texto)
        if self.ui.cb_servicos.currentIndex() == 0:
            if not texto[tamanho-1:tamanho].isnumeric():
                self.ui.tx_busca_servicos.setText(texto[:tamanho - 1])

        if self.ui.cb_servicos.currentIndex() in (2, 3, 4):
            if not texto[tamanho-1:tamanho].isnumeric():
                if texto[tamanho-1:tamanho] != '.':
                    self.ui.tx_busca_servicos.setText(texto[:tamanho - 1])

                if texto.count(".") > 1 and texto[tamanho-1:tamanho] == '.':
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
                    if texto[indice_ponto+1:indice_ponto+2] == '0':
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

        self.ui.tx_id.setText("")
        self.ui.tx_desc_serv.setText("")
        self.ui.tx_preco.setText("")
        self.ui.tb_servicos.selectRow(0)

    def linha_clicada(self):
        self.ui.tx_desc_serv.setEnabled(True)
        self.ui.tx_preco.setEnabled(True)

        tb = self.ui.tb_servicos
        self.linha_selecionada = tb.currentRow()

        self.serv_selecionado.id = int(tb.item(tb.currentRow(), 0).text())
        c = self.serv_selecionado.get_servico_by_id()
        self.serv_selecionado.descricao = c[1]
        self.serv_selecionado.preco = c[2]

        # setando os edits
        self.ui.tx_desc_serv.setText(self.serv_selecionado.descricao)
        self.ui.tx_id.setText(f'{self.serv_selecionado.id}')
        self.ui.tx_preco.setText(f'{self.serv_selecionado.preco}')

    def dados_tabela(self):
        self.serv_selecionado.id = None
        self.ui.tx_busca_servicos.setText("")

        nova_qtd = Servicos.qtd_servicos()
        if self.adicionando_serv and not self.filtrado and nova_qtd > self.qtd_servicos:
            self.qtd_servicos = nova_qtd

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
            self.adicionando_serv = False
        else:
            self.filtrado = False
            self.ui.bt_refresh.setEnabled(False)
            self.ui.tx_id.setText("")
            self.ui.tx_desc_serv.setText("")
            self.ui.tx_preco.setText("")
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

            if self.adicionando_serv:
                self.ui.tb_servicos.selectRow(self.ui.tb_servicos.rowCount() - 1)
                self.adicionando_serv = False

    def editar(self):
        if self.serv_selecionado.id:
            serv_editar = Servicos()
            serv_editar.id = self.ui.tx_id.text()
            serv_editar.descricao = self.ui.tx_desc_serv.text().upper()
            serv_editar.preco = self.ui.tx_preco.text()

            serv_editar.preco = serv_editar.preco.replace("R$", "")

            try:
                serv_editar.editar_servicos()
            except Exception as error:
                QMessageBox.warning(self, "Erro", str(error))
            else:
                self.ui.tb_servicos.setFocus()
                self.ui.tb_servicos.setItem(self.linha_selecionada, 1, QTableWidgetItem(serv_editar.descricao))
                self.ui.tb_servicos.setItem(self.linha_selecionada, 2, QTableWidgetItem(serv_editar.preco))
        else:
            QMessageBox.warning(self, "Atenção!", "Favor selecionar alguma linha!")

    def excluir(self):
        if self.serv_selecionado.id:
            reply = QMessageBox.question(self, 'Excluir?', f'Tem certeza que deseja excluir o serviço: '
                                                           f'{self.serv_selecionado.descricao}?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

            if reply == QMessageBox.Yes:
                try:
                    self.serv_selecionado.delete_servico_by_id()
                    self.serv_selecionado.id = None
                except Exception as error:
                    QMessageBox.warning(self, "Erro", str(error))
                else:
                    self.ui.tb_servicos.removeRow(self.linha_selecionada)
                    self.ui.tx_id.setText("")
                    self.ui.tx_desc_serv.setText("")
                    self.ui.tx_preco.setText("")
            else:
                return
        else:
            QMessageBox.warning(self, "Atenção!", "Favor selecionar alguma linha!")
