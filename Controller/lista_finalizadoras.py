from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from Model.Finalizadoras import Finalizadoras
from PyQt5 import QtCore
from PyQt5.QtCore import Qt


class EventFilter(QtCore.QObject):

    def __init__(self, parent=None):
        QtCore.QObject.__init__(self, parent)

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.ActivationChange:
            if self.parent().isActiveWindow():
                if obj.adicionando_fin:
                    obj.dados_tabela()

        return QtCore.QObject.eventFilter(self, obj, event)


class ListaFinalizadoras(QMainWindow):
    def __init__(self, parent=None):
        super(ListaFinalizadoras, self).__init__(parent)
        from View.lista_finalizadoras import Ui_Frame

        self.ui = Ui_Frame()
        self.ui.setupUi(self)
        self.dialogs = list()
        self.setFixedSize(self.size())

        self.setWindowModality(QtCore.Qt.ApplicationModal)

        # removendo opção de maximizar
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

        self.fin_selecionada = Finalizadoras()
        self.linha_selecionada = None
        self.adicionando_fin = False
        self.qtd_fin = Finalizadoras.qtd_fin()
        self.filtrado = False

        self.installEventFilter(EventFilter(self))

        # ação dos botoes
        self.ui.bt_cancelar.clicked.connect(self.sair)
        self.ui.bt_refresh.clicked.connect(self.dados_tabela)
        self.ui.bt_excluir.clicked.connect(self.excluir)
        self.ui.bt_novo.clicked.connect(self.nova_fin)
        self.ui.bt_salvar.clicked.connect(self.editar)

        # ação da busca
        self.ui.bt_busca.clicked.connect(self.buscar)
        self.ui.tx_busca.returnPressed.connect(self.buscar)

        # signals
        self.ui.tb_finalizadoras.cellClicked.connect(self.linha_clicada)
        self.ui.tx_busca.textChanged.connect(self.formatar_texto)
        self.ui.cb_fin.currentIndexChanged.connect(self.limpa_campo_busca)

        self.ui.tx_id.setEnabled(False)
        self.ui.tx_desc.setEnabled(False)

        self.ui.tb_finalizadoras.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.ui.tb_finalizadoras.horizontalHeaderItem(1).setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.preenche_combo()
        self.dados_tabela()

    def nova_fin(self):
        from Controller.cadastro_finalizadoras import CadastroFinalizadoras
        from Funcoes.utils import exec_app

        self.adicionando_fin = True
        c = CadastroFinalizadoras()
        exec_app(c)
        self.dialogs.append(c)

    def limpa_campo_busca(self):
        self.ui.tx_busca.setText("")

    def formatar_texto(self):
        texto = self.ui.tx_busca.text()
        tamanho = len(texto)
        if self.ui.cb_fin.currentIndex() == 1:
            if not texto[tamanho - 1:tamanho].isnumeric():
                self.ui.tx_busca.setText(texto[:tamanho - 1])

    def preenche_combo(self):
        self.ui.cb_fin.clear()
        self.ui.cb_fin.addItem("Descrição")
        self.ui.cb_fin.addItem("ID")

    def sair(self):
        self.close()

    def buscar(self):
        self.ui.tb_finalizadoras.clearContents()
        self.ui.tb_finalizadoras.setRowCount(0)

        finalizadora = Finalizadoras()

        if self.ui.cb_fin.currentIndex() == 0:
            finalizadora.descricao = self.ui.tx_busca.text()
            if finalizadora.descricao:
                dados = finalizadora.get_fin_by_desc(finalizadora.descricao.upper())
            else:
                QMessageBox.warning(self, "Atenção!", "Favor informar algum valor!")
                self.dados_tabela()
                return
        else:
            if self.ui.tx_busca.text():
                finalizadora.id = int(self.ui.tx_busca.text())
                dados = finalizadora.get_finalizadora_by_id()
            else:
                QMessageBox.warning(self, "Atenção!", "Favor informar algum valor!")
                self.dados_tabela()
                return

        if dados:
            self.filtrado = True
            self.ui.bt_refresh.setEnabled(True)

            if type(dados) == list:
                for i, linha in enumerate(dados):
                    self.ui.tb_finalizadoras.insertRow(i)
                    for c in range(0, 2):
                        self.ui.tb_finalizadoras.setItem(i, c, QTableWidgetItem(str(linha[c])))
            else:
                self.ui.tb_finalizadoras.insertRow(0)
                for c in range(0, 2):
                    self.ui.tb_finalizadoras.setItem(0, c, QTableWidgetItem(str(dados[c])))

        else:
            QMessageBox.warning(self, "Erro", "Não foi encontrado nenhum registro!")
            self.ui.tx_busca.setText("")
            self.dados_tabela()

        self.ui.tx_id.setText("")
        self.ui.tx_desc.setText("")
        self.ui.tb_finalizadoras.selectRow(0)

    def linha_clicada(self):
        self.ui.tx_desc.setEnabled(True)
        tb = self.ui.tb_finalizadoras
        self.linha_selecionada = tb.currentRow()

        self.fin_selecionada.id = int(tb.item(tb.currentRow(), 0).text())
        c = self.fin_selecionada.get_finalizadora_by_id()
        self.fin_selecionada.descricao = c[1]

        # setando os edits
        self.ui.tx_desc.setText(self.fin_selecionada.descricao)
        self.ui.tx_id.setText(f'{self.fin_selecionada.id}')

    def dados_tabela(self):
        self.fin_selecionada.id = None
        self.ui.tx_busca.setText("")

        nova_qtd = Finalizadoras.qtd_fin()
        if self.adicionando_fin and not self.filtrado and nova_qtd > self.qtd_fin:
            self.qtd_fin = nova_qtd
            nova_fin = Finalizadoras()
            novo_id = nova_fin.ultima_fin()
            nova_fin.id = novo_id[0]
            nova_fin.descricao = nova_fin.get_finalizadora_by_id()[1]

            item_id = QTableWidgetItem(str(nova_fin.id))
            item_id.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

            item_desc = QTableWidgetItem(nova_fin.descricao)
            item_desc.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

            self.ui.tb_finalizadoras.insertRow(self.ui.tb_finalizadoras.rowCount())
            self.ui.tb_finalizadoras.setItem(self.ui.tb_finalizadoras.rowCount() - 1, 0, item_id)
            self.ui.tb_finalizadoras.setItem(self.ui.tb_finalizadoras.rowCount() - 1, 1, item_desc)

            self.ui.tb_finalizadoras.selectRow(self.ui.tb_finalizadoras.rowCount() - 1)
            self.adicionando_fin = False
        else:
            self.filtrado = False
            self.ui.bt_refresh.setEnabled(False)
            self.ui.tx_id.setText("")
            self.ui.tx_desc.setText("")
            self.ui.tb_finalizadoras.clearContents()
            self.ui.tb_finalizadoras.setRowCount(0)

            dados = Finalizadoras.get_todas_finalizadoras()

            for i, linha in enumerate(dados):
                item_id = QTableWidgetItem(str(linha[0]))
                item_id.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

                item_desc = QTableWidgetItem(linha[1])
                item_desc.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

                self.ui.tb_finalizadoras.insertRow(i)
                self.ui.tb_finalizadoras.setItem(i, 0, item_id)
                self.ui.tb_finalizadoras.setItem(i, 1, item_desc)

            if self.adicionando_fin:
                self.ui.tb_finalizadoras.selectRow(self.ui.tb_finalizadoras.rowCount() - 1)
                self.adicionando_fin = False

    def editar(self):
        if self.fin_selecionada.id:
            fin_editar = Finalizadoras()
            fin_editar.id = self.ui.tx_id.text()
            fin_editar.descricao = self.ui.tx_desc.text().upper()

            try:
                fin_editar.editar_finalizadoras()
            except Exception as error:
                QMessageBox.warning(self, "Erro", str(error))
            else:
                self.ui.tb_finalizadoras.setFocus()
                self.ui.tb_finalizadoras.setItem(self.linha_selecionada, 1, QTableWidgetItem(fin_editar.descricao))
        else:
            QMessageBox.warning(self, "Atenção!", "Favor selecionar alguma linha!")

    def excluir(self):
        if self.fin_selecionada.id:
            reply = QMessageBox.question(self, 'Excluir?', f'Tem certeza que deseja excluir a finalizadora: '
                                                           f'{self.fin_selecionada.descricao}?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

            if reply == QMessageBox.Yes:
                try:
                    self.fin_selecionada.delete_fin_by_id()
                    self.fin_selecionada.id = None
                except Exception as error:
                    QMessageBox.warning(self, "Erro", str(error))
                else:
                    self.ui.tb_finalizadoras.removeRow(self.linha_selecionada)
                    self.ui.tx_id.setText("")
                    self.ui.tx_desc.setText("")
            else:
                return
        else:
            QMessageBox.warning(self, "Atenção!", "Favor selecionar alguma linha!")
