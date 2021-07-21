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
                dados = prod.get_produto_by_id()
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
                if type(dados_fornecedor) == list:
                    for item in dados_fornecedor:
                        prod.fornecedor.id = dados_fornecedor[0]
                        dados = prod.get_produto_by_fornecedor()
                else:
                    prod.fornecedor.id = dados_fornecedor[0]
                    dados = prod.get_produto_by_fornecedor()
            else:
                prod.categoria.descricao = self.ui.tx_busca.text().upper()
                dados_cat = prod.categoria.get_categorias_by_desc(prod.categoria.descricao)
                prod.categoria.id = dados_cat[0]
                dados = prod.get_produto_by_categoria()
        else:
            QMessageBox.warning(self, "Atenção!", "Favor informar algum valor!")
            self.dados_tabela()
            return

        if dados:

            self.filtrado = True
            self.ui.bt_refresh.setEnabled(True)

            if type(dados) == list:
                for i, linha in enumerate(dados):
                    # Produtos
                    prod_id = QTableWidgetItem(str(linha[0]))
                    self.ui.tb_produtos.insertRow(i)
                    self.ui.tb_produtos.setItem(i, 0, prod_id)

                    # fornecedor
                    f = Fornecedor()
                    f.id = int(linha[1])
                    forn_prod = f.get_fornecedor_by_id()
                    f.nome = forn_prod[2]

                    # categoria
                    c = Categoria()
                    c.id = int(linha[2])
                    cat_prod = c.get_categoria_by_id()
                    c.descricao = cat_prod[1]

                    self.ui.tb_produtos.setItem(i, 1, QTableWidgetItem(str(linha[4])))
                    self.ui.tb_produtos.setItem(i, 2, QTableWidgetItem(str(linha[3])))
                    self.ui.tb_produtos.setItem(i, 3, QTableWidgetItem(str(linha[5])))
                    self.ui.tb_produtos.setItem(i, 4, QTableWidgetItem(str(linha[6])))
                    self.ui.tb_produtos.setItem(i, 5, QTableWidgetItem(str(linha[7])))
                    self.ui.tb_produtos.setItem(i, 6, QTableWidgetItem(str(f.nome)))
                    self.ui.tb_produtos.setItem(i, 7, QTableWidgetItem(str(c.descricao)))
            else:
                prod_id = QTableWidgetItem(str(dados[0]))
                self.ui.tb_produtos.insertRow(0)
                self.ui.tb_produtos.setItem(0, 0, prod_id)

                for j in range(1, 6):
                    # estoque no lugar do codigo de barras
                    if j == 1:
                        item_prod = dados[j + 3]
                    # codbarras no lugar do estoque
                    elif j == 2:
                        item_prod = dados[j + 1]
                    # demais campos
                    else:
                        item_prod = dados[j + 2]
                    self.ui.tb_produtos.setItem(0, j, QTableWidgetItem(str(item_prod)))

                # fornecedor
                f = Fornecedor()
                f.id = int(dados[1])
                forn_prod = f.get_fornecedor_by_id()
                f.nome = forn_prod[2]
                self.ui.tb_produtos.setItem(0, 6, QTableWidgetItem(str(f.nome)))

                # categoria
                c = Categoria()
                c.id = int(dados[2])
                cat_prod = c.get_categoria_by_id()
                c.descricao = cat_prod[1]
                self.ui.tb_produtos.setItem(0, 7, QTableWidgetItem(str(c.descricao)))
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
        self.produto_selecionado.fornecedor.nome = forn_selecionado[2]

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

        dados = Produtos.get_todos_produtos()

        self.ui.bt_refresh.setEnabled(False)

        if type(dados) == list:
            for i, linha in enumerate(dados):
                # Produtos
                prod_id = QTableWidgetItem(str(linha[0]))
                self.ui.tb_produtos.insertRow(i)
                self.ui.tb_produtos.setItem(i, 0, prod_id)

                for j in range(1, 6):
                    # estoque no lugar do codigo de barras
                    if j == 1:
                        item_prod = linha[j + 3]
                    # codbarras no lugar do estoque
                    elif j == 2:
                        item_prod = linha[j + 1]
                    # demais campos
                    else:
                        item_prod = linha[j + 2]
                    self.ui.tb_produtos.setItem(i, j, QTableWidgetItem(str(item_prod)))

                # fornecedor
                f = Fornecedor()
                f.id = int(linha[1])
                forn_prod = f.get_fornecedor_by_id()
                f.nome = forn_prod[2]
                self.ui.tb_produtos.setItem(i, 6, QTableWidgetItem(str(f.nome)))

                # categoria
                c = Categoria()
                c.id = int(linha[2])
                cat_prod = c.get_categoria_by_id()
                c.descricao = cat_prod[1]
                self.ui.tb_produtos.setItem(i, 7, QTableWidgetItem(str(c.descricao)))
        else:
            prod_id = QTableWidgetItem(str(dados[0]))
            self.ui.tb_produtos.insertRow(0)
            self.ui.tb_produtos.setItem(0, 0, prod_id)

            for j in range(1, 6):
                # estoque no lugar do codigo de barras
                if j == 1:
                    item_prod = dados[j + 3]
                # codbarras no lugar do estoque
                elif j == 2:
                    item_prod = dados[j + 1]
                # demais campos
                else:
                    item_prod = dados[j + 2]
                self.ui.tb_produtos.setItem(0, j, QTableWidgetItem(str(item_prod)))

            # fornecedor
            f = Fornecedor()
            f.id = int(dados[1])
            forn_prod = f.get_fornecedor_by_id()
            f.nome = forn_prod[2]
            self.ui.tb_produtos.setItem(0, 6, QTableWidgetItem(str(f.nome)))

            # categoria
            c = Categoria()
            c.id = int(dados[1])
            cat_prod = c.get_categoria_by_id()
            c.descricao = cat_prod[1]
            self.ui.tb_produtos.setItem(0, 7, QTableWidgetItem(str(c.descricao)))

        if self.adicionando:
            self.ui.tb_produtos.selectRow(self.ui.tb_produtos.rowCount() - 1)
            self.adicionando = False
