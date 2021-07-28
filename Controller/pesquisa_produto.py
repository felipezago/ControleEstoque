from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QMainWindow
from PyQt5.QtCore import Qt
from Model.Produtos import Produtos
from Model.Categoria import Categoria
from Model.Fornecedor import Fornecedor
from PyQt5 import QtCore
from PyQt5 import QtGui


class EventFilter(QtCore.QObject):

    def __init__(self, parent=None):
        QtCore.QObject.__init__(self, parent)

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.ActivationChange:
            if self.parent().isActiveWindow():
                if obj.adicionando:
                    obj.dados_tabela()

        return QtCore.QObject.eventFilter(self, obj, event)


class PesquisaProdutos(QMainWindow):
    def __init__(self, parent=None):
        super(PesquisaProdutos, self).__init__(parent)
        from View.pesquisa_produtos import Ui_Frame

        self.ui = Ui_Frame()
        self.ui.setupUi(self)
        self.dialogs = list()
        self.tamanho_tela = self.size()
        self.setFixedSize(self.tamanho_tela)

        self.produto_selecionado = Produtos()
        self.linha_selecionada = None
        self.adicionando = False
        self.filtrado = False
        self.tela_venda = parent

        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.installEventFilter(EventFilter(self))

        # ação dos botoes
        self.ui.bt_refresh.clicked.connect(self.dados_tabela)
        self.ui.bt_inserir.clicked.connect(self.novo)
        self.ui.bt_selecionar.clicked.connect(self.sair)

        # ação da busca
        self.ui.bt_busca.clicked.connect(self.buscar)
        self.ui.tx_busca.returnPressed.connect(self.buscar)

        # signals
        self.ui.tb_produtos.cellClicked.connect(self.linha_clicada)
        self.ui.tb_produtos.cellDoubleClicked.connect(self.sair)
        self.ui.tx_busca.textChanged.connect(self.formatar_texto)
        self.ui.cb_produtos.currentIndexChanged.connect(self.limpa_campo_busca)

        for i in range(0, 8):
            self.ui.tb_produtos.horizontalHeaderItem(i).setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.ui.tb_produtos.setColumnWidth(0, 30)
        self.ui.tb_produtos.setColumnWidth(1, 150)
        self.ui.tb_produtos.setColumnWidth(2, 80)
        self.ui.tb_produtos.setColumnWidth(3, 230)
        self.ui.tb_produtos.setColumnWidth(4, 200)
        self.ui.tb_produtos.setColumnWidth(5, 150)
        self.ui.tb_produtos.setColumnWidth(6, 200)
        self.ui.tb_produtos.setColumnWidth(7, 200)

        self.preenche_combo()
        self.dados_tabela()

    def novo(self):
        from Controller.cadastro_produtos import CadastroProdutos
        from Funcoes.funcoes import exec_app

        self.adicionando = True
        c = CadastroProdutos()
        exec_app(c)
        self.dialogs.append(c)

    def limpa_campo_busca(self):
        self.ui.tx_busca.setText("")

    def formatar_texto(self):
        texto = self.ui.tx_busca.text()
        tamanho = len(texto)
        if self.ui.cb_produtos.currentIndex() in (0, 1):
            if not texto[tamanho-1:tamanho].isnumeric():
                self.ui.tx_busca.setText(texto[:tamanho - 1])

    def preenche_combo(self):
        self.ui.cb_produtos.clear()
        self.ui.cb_produtos.addItem("ID")
        self.ui.cb_produtos.addItem("CODIGO DE BARRAS")
        self.ui.cb_produtos.addItem("DESCRIÇÃO")
        self.ui.cb_produtos.addItem("MARCA")
        self.ui.cb_produtos.addItem("FORNECEDOR")
        self.ui.cb_produtos.addItem("CATEGORIA")

    def sair(self):
        self.close()

    def closeEvent(self, event: QtGui.QCloseEvent):
        if self.produto_selecionado.id is not None:
            self.tela_venda.codigo_item = self.produto_selecionado.id
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
        self.ui.tb_produtos.clearContents()
        self.ui.tb_produtos.setRowCount(0)

        prod = Produtos()
        prod.categoria = Categoria()
        prod.fornecedor = Fornecedor()
        dados = ""

        if self.ui.tx_busca.text():
            if self.ui.cb_produtos.currentIndex() == 0:
                prod.id = self.ui.tx_busca.text()
                dados = prod.get_produto_by_id_tb()
            elif self.ui.cb_produtos.currentIndex() == 1:
                prod.codbarras = self.ui.tx_busca.text()
                dados = prod.get_produtos_by_desc("prod_codbarras", prod.codbarras)
            elif self.ui.cb_produtos.currentIndex() == 2:
                prod.descricao = self.ui.tx_busca.text().upper()
                dados = prod.get_produtos_by_desc("prod_desc", prod.descricao)
            elif self.ui.cb_produtos.currentIndex() == 3:
                prod.marca = self.ui.tx_busca.text().upper()
                dados = prod.get_produtos_by_desc("prod_marca", prod.marca)
            elif self.ui.cb_produtos.currentIndex() == 4:
                prod.fornecedor.nome = self.ui.tx_busca.text().upper()
                dados_fornecedor = prod.fornecedor.get_fornecedores_by_desc("forn_nome", prod.fornecedor.nome)

                if dados_fornecedor:
                    if type(dados_fornecedor) == list:
                        cods = list()
                        for item in dados_fornecedor:
                            cods.append(item[0])
                        tup = tuple(cods)
                        prod.fornecedor.id = tup
                        dados = prod.get_produto_by_fornecedor("in")
                    else:
                        prod.fornecedor.id = dados_fornecedor[0]
                        dados = prod.get_produto_by_fornecedor("=")
            else:
                prod.categoria.descricao = self.ui.tx_busca.text().upper()
                dados_cat = prod.categoria.get_categorias_by_desc(prod.categoria.descricao)

                if dados_cat:
                    if type(dados_cat) == list:
                        cods = list()
                        for item in dados_cat:
                            cods.append(item[0])
                        tup = tuple(cods)
                        prod.categoria.id = tup
                        dados = prod.get_produto_by_categoria("in")
                    else:
                        prod.categoria.id = dados_cat[0]
                        dados = prod.get_produto_by_categoria("=")
        else:
            QMessageBox.warning(self, "Atenção!", "Favor informar algum valor!")
            self.dados_tabela()
            return

        if dados:
            self.filtrado = True
            self.ui.bt_refresh.setEnabled(True)

            for i, linha in enumerate(dados):
                # Produtos
                self.ui.tb_produtos.insertRow(i)
                for j in range(0, 8):
                    self.ui.tb_produtos.setItem(i, j, QTableWidgetItem(str(linha[j])))
        else:
            QMessageBox.warning(self, "Erro", "Não foi encontrado nenhum registro!")
            self.ui.tx_busca.setText("")
            self.dados_tabela()

        self.ui.tb_produtos.selectRow(0)

    def linha_clicada(self):
        tb = self.ui.tb_produtos
        self.linha_selecionada = tb.currentRow()

        self.produto_selecionado.id = tb.item(tb.currentRow(), 0).text()
        p = self.produto_selecionado.get_produto_by_id()

        if p is not None:
            self.produto_selecionado.estoque = p[3]
            self.produto_selecionado.codbarras = p[4]
            self.produto_selecionado.descricao = p[5]
            self.produto_selecionado.marca = p[6]
            self.produto_selecionado.preco = p[7]

        # fornecedor
        self.produto_selecionado.fornecedor = Fornecedor()
        self.produto_selecionado.fornecedor.id = p[1]
        forn_selecionado = self.produto_selecionado.fornecedor.get_fornecedor_by_id()
        self.produto_selecionado.fornecedor.nome = forn_selecionado[1]

        # categoria
        self.produto_selecionado.categoria = Categoria()
        self.produto_selecionado.categoria.id = p[2]
        cat_selecionada = self.produto_selecionado.categoria.get_categoria_by_id()
        self.produto_selecionado.categoria.descricao = cat_selecionada[1]

    def dados_tabela(self):
        self.produto_selecionado.id = None
        self.ui.tx_busca.setText("")
        self.filtrado = False
        self.ui.bt_refresh.setEnabled(False)
        self.ui.tb_produtos.clearContents()
        self.ui.tb_produtos.setRowCount(0)
        self.ui.bt_refresh.setEnabled(False)

        dados = Produtos.get_todos_produtos()

        for i, linha in enumerate(dados):
            self.ui.tb_produtos.insertRow(i)

            for j in range(0, 8):
                self.ui.tb_produtos.setItem(i, j, QTableWidgetItem(str(linha[j])))

        if self.adicionando:
            self.ui.tb_produtos.selectRow(self.ui.tb_produtos.rowCount() - 1)
            self.adicionando = False
