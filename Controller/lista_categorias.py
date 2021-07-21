from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from Model.Categoria import Categoria
from PyQt5 import QtCore
from PyQt5.QtCore import Qt


class EventFilter(QtCore.QObject):

    def __init__(self, parent=None):
        QtCore.QObject.__init__(self, parent)

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.ActivationChange:
            if self.parent().isActiveWindow():
                if obj.adicionando_categoria:
                    obj.dados_tabela()

        return QtCore.QObject.eventFilter(self, obj, event)


class ListaCategorias(QMainWindow):
    def __init__(self, parent=None):
        super(ListaCategorias, self).__init__(parent)
        from View.lista_categorias import Ui_Frame

        self.ui = Ui_Frame()
        self.ui.setupUi(self)
        self.dialogs = list()
        self.setFixedSize(self.size())

        self.setWindowModality(QtCore.Qt.ApplicationModal)
        # removendo opção de maximizar
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

        self.cat_selecionada = Categoria()
        self.linha_selecionada = None
        self.adicionando_categoria = False
        self.qtd_categorias = Categoria.qtd_categorias()
        self.filtrado = False

        self.installEventFilter(EventFilter(self))

        # ação dos botoes
        self.ui.bt_cancelar.clicked.connect(self.sair)
        self.ui.bt_refresh.clicked.connect(self.dados_tabela)
        self.ui.bt_excluir.clicked.connect(self.excluir)
        self.ui.bt_novo.clicked.connect(self.nova_categoria)
        self.ui.bt_salvar.clicked.connect(self.editar)

        # ação da busca
        self.ui.bt_busca_categorias.clicked.connect(self.buscar)
        self.ui.tx_busca_categorias.returnPressed.connect(self.buscar)

        # signals
        self.ui.tb_categorias.cellClicked.connect(self.linha_clicada)
        self.ui.tx_busca_categorias.textChanged.connect(self.formatar_texto)
        self.ui.cb_categoria.currentIndexChanged.connect(self.limpa_campo_busca)

        self.ui.tx_id.setEnabled(False)
        self.ui.tx_desc_cat.setEnabled(False)

        self.ui.tb_categorias.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.ui.tb_categorias.horizontalHeaderItem(1).setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.preenche_combo()
        self.dados_tabela()

    def nova_categoria(self):
        from Controller.cadastro_categoria import CadastroCategoria
        from Funcoes.funcoes import exec_app

        self.adicionando_categoria = True
        c = CadastroCategoria()
        exec_app(c)
        self.dialogs.append(c)

    def limpa_campo_busca(self):
        self.ui.tx_busca_categorias.setText("")

    def formatar_texto(self):
        texto = self.ui.tx_busca_categorias.text()
        tamanho = len(texto)
        if self.ui.cb_categoria.currentIndex() == 1:
            if not texto[tamanho - 1:tamanho].isnumeric():
                self.ui.tx_busca_categorias.setText(texto[:tamanho - 1])

    def preenche_combo(self):
        self.ui.cb_categoria.clear()
        self.ui.cb_categoria.addItem("Descrição")
        self.ui.cb_categoria.addItem("ID")

    def sair(self):
        self.close()

    def buscar(self):
        self.ui.tb_categorias.clearContents()
        self.ui.tb_categorias.setRowCount(0)

        categoria = Categoria()

        if self.ui.cb_categoria.currentIndex() == 0:
            categoria.descricao = self.ui.tx_busca_categorias.text()
            if categoria.descricao:
                dados = Categoria.get_categorias_by_desc(categoria.descricao.upper())
            else:
                QMessageBox.warning(self, "Atenção!", "Favor informar algum valor!")
                self.dados_tabela()
                return
        else:
            if self.ui.tx_busca_categorias.text():
                categoria.id = int(self.ui.tx_busca_categorias.text())
                dados = categoria.get_categoria_by_id()
            else:
                QMessageBox.warning(self, "Atenção!", "Favor informar algum valor!")
                self.dados_tabela()
                return

        if dados:
            self.filtrado = True
            self.ui.bt_refresh.setEnabled(True)

            if type(dados) == list:
                for i, linha in enumerate(dados):
                    self.ui.tb_categorias.insertRow(i)
                    for c in range(0, 2):
                        self.ui.tb_categorias.setItem(i, c, QTableWidgetItem(str(linha[c])))
            else:
                self.ui.tb_categorias.insertRow(0)
                for c in range(0, 2):
                    self.ui.tb_categorias.setItem(0, c, QTableWidgetItem(str(dados[c])))

        else:
            QMessageBox.warning(self, "Erro", "Não foi encontrado nenhum registro!")
            self.ui.tx_busca_categorias.setText("")
            self.dados_tabela()

        self.ui.tx_id.setText("")
        self.ui.tx_desc_cat.setText("")
        self.ui.tb_categorias.selectRow(0)

    def linha_clicada(self):
        self.ui.tx_desc_cat.setEnabled(True)
        tb = self.ui.tb_categorias
        self.linha_selecionada = tb.currentRow()

        self.cat_selecionada.id = int(tb.item(tb.currentRow(), 0).text())
        c = self.cat_selecionada.get_categoria_by_id()
        self.cat_selecionada.descricao = c[1]

        # setando os edits
        self.ui.tx_desc_cat.setText(self.cat_selecionada.descricao)
        self.ui.tx_id.setText(f'{self.cat_selecionada.id}')

    def dados_tabela(self):
        self.cat_selecionada.id = None
        self.ui.tx_busca_categorias.setText("")

        nova_qtd = Categoria.qtd_categorias()
        if self.adicionando_categoria and not self.filtrado and nova_qtd > self.qtd_categorias:
            self.qtd_categorias = nova_qtd
            nova_cat = Categoria()
            novo_id = nova_cat.ultima_categoria()
            nova_cat.id = novo_id[0]
            nova_cat.descricao = nova_cat.get_categoria_by_id()[1]

            item_id = QTableWidgetItem(str(nova_cat.id))
            item_id.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

            item_desc = QTableWidgetItem(nova_cat.descricao)
            item_desc.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

            self.ui.tb_categorias.insertRow(self.ui.tb_categorias.rowCount())
            self.ui.tb_categorias.setItem(self.ui.tb_categorias.rowCount() - 1, 0, item_id)
            self.ui.tb_categorias.setItem(self.ui.tb_categorias.rowCount() - 1, 1, item_desc)

            self.ui.tb_categorias.selectRow(self.ui.tb_categorias.rowCount() - 1)
            self.adicionando_categoria = False
        else:
            self.filtrado = False
            self.ui.bt_refresh.setEnabled(False)
            self.ui.tx_id.setText("")
            self.ui.tx_desc_cat.setText("")
            self.ui.tb_categorias.clearContents()
            self.ui.tb_categorias.setRowCount(0)

            dados = Categoria.get_todas_categorias()

            for i, linha in enumerate(dados):
                item_id = QTableWidgetItem(str(linha[0]))
                item_id.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

                item_desc = QTableWidgetItem(linha[1])
                item_desc.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

                self.ui.tb_categorias.insertRow(i)
                self.ui.tb_categorias.setItem(i, 0, item_id)
                self.ui.tb_categorias.setItem(i, 1, item_desc)

            if self.adicionando_categoria:
                self.ui.tb_categorias.selectRow(self.ui.tb_categorias.rowCount() - 1)
                self.adicionando_categoria = False

    def editar(self):
        if self.cat_selecionada.id:
            cat_editar = Categoria()
            cat_editar.id = self.ui.tx_id.text()
            cat_editar.descricao = self.ui.tx_desc_cat.text().upper()

            try:
                cat_editar.editar_categorias()
            except Exception as error:
                QMessageBox.warning(self, "Erro", str(error))
            else:
                self.ui.tb_categorias.setFocus()
                self.ui.tb_categorias.setItem(self.linha_selecionada, 1, QTableWidgetItem(cat_editar.descricao))
        else:
            QMessageBox.warning(self, "Atenção!", "Favor selecionar alguma linha!")

    def excluir(self):
        if self.cat_selecionada.id:
            reply = QMessageBox.question(self, 'Excluir?', f'Tem certeza que deseja excluir a categoria: '
                                                           f'{self.cat_selecionada.descricao}?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

            if reply == QMessageBox.Yes:
                try:
                    self.cat_selecionada.delete_categoria_by_id()
                    self.cat_selecionada.id = None
                except Exception as error:
                    QMessageBox.warning(self, "Erro", str(error))
                else:
                    self.ui.tb_categorias.removeRow(self.linha_selecionada)
                    self.ui.tx_id.setText("")
                    self.ui.tx_desc_cat.setText("")
            else:
                return
        else:
            QMessageBox.warning(self, "Atenção!", "Favor selecionar alguma linha!")
