import os
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QMainWindow
from Model.Compra_Itens import Compra_Itens
from Model.Produtos import Produtos
from Model.Categoria import Categoria
from Model.Fornecedor import Fornecedor
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QPixmap


class EventFilter(QtCore.QObject):

    def __init__(self, parent=None):
        QtCore.QObject.__init__(self, parent)

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.ActivationChange:
            if self.parent().isActiveWindow():
                if obj.adicionando:
                    obj.dados_tabela()

        return QtCore.QObject.eventFilter(self, obj, event)


class ListaProdutos(QMainWindow):
    def __init__(self, parent=None):
        super(ListaProdutos, self).__init__(parent)
        from View.lista_produtos import Ui_Frame
        from Funcoes.utils import icone_botao_menu
        from PyQt5.QtGui import QDoubleValidator
        from PyQt5.QtCore import Qt

        if not os.path.isdir('temp'):
            os.makedirs('temp')

        self.ui = Ui_Frame()
        self.ui.setupUi(self)
        self.dialogs = list()
        self.tamanho = self.size()
        self.setFixedSize(self.tamanho)

        self.setWindowIcon(QtGui.QIcon("Imagens/logo_fzr.png"))

        icone_botao_menu(self.ui.bt_DelLogo, QtGui.QPixmap('Imagens/edit-delete.png'))
        icone_botao_menu(self.ui.bt_AddLogo, QtGui.QPixmap('Imagens/edit-add.png'))

        # removendo opção de maximizar
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

        self.produto_selecionado = Produtos()
        self.linha_selecionada = None
        self.adicionando = False
        self.filtrado = False
        self.qtd_produtos = Produtos.qtd_prod()
        self.caminho_img = None

        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.installEventFilter(EventFilter(self))

        # ação dos botoes
        self.ui.bt_cancelar.clicked.connect(self.sair)
        self.ui.bt_salvar.clicked.connect(self.editar)
        self.ui.bt_refresh.clicked.connect(self.dados_tabela)
        self.ui.bt_excluir.clicked.connect(self.excluir)
        self.ui.bt_novo.clicked.connect(self.novo)
        self.ui.bt_AddLogo.clicked.connect(self.add_img)
        self.ui.bt_DelLogo.clicked.connect(self.del_img)

        # ação da busca
        self.ui.bt_busca.clicked.connect(self.buscar)
        self.ui.tx_busca.returnPressed.connect(self.buscar)

        # signals
        self.ui.tb_produtos.cellClicked.connect(self.linha_clicada)
        self.ui.tx_busca.textChanged.connect(self.formatar_texto)
        self.ui.tx_preco.textChanged.connect(self.calcula_lucro)
        self.ui.tx_preco_compra.textChanged.connect(self.calcula_lucro)
        self.ui.cb_produtos.currentIndexChanged.connect(self.limpa_campo_busca)

        self.set_tx_enabled(False)
        self.ui.tx_id.setEnabled(False)

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

        validator_double = QDoubleValidator(0, 9999, 4)
        self.ui.tx_preco.setValidator(validator_double)

        # prevenindo erros
        self.ui.tx_descricao.setMaxLength(50)
        self.ui.tx_marca.setMaxLength(60)
        self.ui.tx_codbarras.setMaxLength(15)

        self.preenche_combo()
        self.dados_tabela()
        self.ui.cb_fornecedor.clear()
        self.ui.cb_categoria.clear()

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        self.setFixedSize(self.tamanho)

    def add_img(self):
        from PyQt5.QtCore import Qt
        from PyQt5.QtWidgets import QFileDialog

        dialog = QFileDialog()
        dialog.setOption(QFileDialog.DontUseNativeDialog, True)

        fname = dialog.getOpenFileName(
            self, "Selecionar Imagem", "", "Image files (*.jpg *.png)")[0]

        self.ui.lb_foto_prod.setPixmap(QPixmap(fname).scaledToWidth(
            150, Qt.TransformationMode(Qt.FastTransformation)))
        self.ui.bt_AddLogo.setHidden(True)
        self.ui.bt_DelLogo.setVisible(True)

        self.caminho_img = fname

    def del_img(self):
        if self.ui.lb_foto_prod and self.ui.bt_AddLogo.isHidden():
            self.empresa_selecionada.ler_imagem_empresas(self, "temp/")
        else:
            self.ui.lb_foto_prod.clear()

        self.ui.bt_DelLogo.setHidden(True)
        self.ui.bt_AddLogo.setVisible(True)

    def remove_img(self):
        import os

        dir_img = f"temp/{self.produto_selecionado.descricao}.png"

        if os.path.isfile(dir_img):
            os.remove(dir_img)

    def novo(self):
        from Controller.cadastro_produtos import CadastroProdutos
        from Funcoes.utils import exec_app

        self.adicionando = True
        c = CadastroProdutos()
        exec_app(c)
        self.dialogs.append(c)

    def preenche_combo_categorias(self):
        self.ui.cb_categoria.clear()
        todas_categorias = Categoria.get_todas_categorias()

        for contador, cat in enumerate(todas_categorias):
            contador += 1
            self.ui.cb_categoria.addItem(cat[1])
            self.ui.cb_categoria.setItemData(contador - 1, cat)

    def preenche_combo_fornecedores(self):
        self.ui.cb_fornecedor.clear()
        todos_fornecedores = Fornecedor.get_todos_fornecedores()

        for contador, f in enumerate(todos_fornecedores):
            contador += 1
            self.ui.cb_fornecedor.addItem(f[1])
            self.ui.cb_fornecedor.setItemData(contador - 1, f)

    def limpa_campo_busca(self):
        self.ui.tx_busca.setText("")

        if self.ui.cb_produtos.currentIndex() in (6, 7):
            self.buscar()
            self.ui.tx_busca.setEnabled(False)
            self.ui.bt_busca.setEnabled(False)
        else:
            self.ui.tx_busca.setEnabled(True)
            self.ui.bt_busca.setEnabled(True)

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
        self.ui.cb_produtos.addItem("MAIOR ESTOQUE")
        self.ui.cb_produtos.addItem("MENOR ESTOQUE")

    def sair(self):
        self.close()

    def buscar(self):
        self.ui.cb_fornecedor.clear()
        self.ui.cb_categoria.clear()
        self.ui.tb_produtos.clearContents()
        self.limpa_campos()
        self.ui.tb_produtos.setRowCount(0)

        prod = Produtos()
        prod.categoria = Categoria()
        prod.fornecedor = Fornecedor()
        dados = ""

        if self.ui.cb_produtos.currentIndex() == 6:
            dados = prod.order_by_estoque("desc")
        elif self.ui.cb_produtos.currentIndex() == 7:
            dados = prod.order_by_estoque("asc")
        else:
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

        self.limpa_campos()
        self.ui.tb_produtos.selectRow(0)

    def closeEvent(self, a0):
        self.remove_img()

    def linha_clicada(self):
        self.del_img()
        self.remove_img()
        self.ui.lb_foto_prod.clear()
        self.set_tx_enabled(True)
        self.preenche_combo_categorias()
        self.preenche_combo_fornecedores()
        self.ui.tx_PorcentagemVarejo.setText("")

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

        # setando os edits
        self.ui.tx_id.setText(self.produto_selecionado.id)
        self.ui.tx_codbarras.setText(self.produto_selecionado.codbarras)
        self.ui.tx_descricao.setText(self.produto_selecionado.descricao)
        self.ui.tx_marca.setText(self.produto_selecionado.marca)
        self.ui.tx_preco.setText(str(self.produto_selecionado.preco))

        indice_forn = self.ui.cb_fornecedor.findText(self.produto_selecionado.fornecedor.nome)
        self.ui.cb_fornecedor.setCurrentIndex(indice_forn)
        indice_cat = self.ui.cb_categoria.findText(self.produto_selecionado.categoria.descricao)
        self.ui.cb_categoria.setCurrentIndex(indice_cat)

        compra_itens = Compra_Itens()
        compra_itens.id_prod = self.produto_selecionado
        preco = compra_itens.retorna_ultimo_preco()
        if preco != 0:
            self.ui.tx_preco_compra.setText(str(compra_itens.retorna_ultimo_preco()))
            self.calcula_lucro()
        else:
            self.ui.tx_preco_compra.setText("")

        self.produto_selecionado.ler_imagem_produtos(self, "temp/")

    def calcula_lucro(self):
        if self.ui.tx_preco_compra.text() and self.ui.tx_preco.text():
            if float(self.ui.tx_preco.text()) > 0:
                preco_compra = float(self.ui.tx_preco_compra.text())
                preco_venda = float(self.ui.tx_preco.text())
                lucro = preco_venda - preco_compra
                lucro = lucro / preco_compra * 100
                if preco_compra > preco_venda:
                    self.ui.tx_PorcentagemVarejo.setText("")
                else:
                    self.ui.tx_PorcentagemVarejo.setText(f"{lucro:.2f}")
            else:
                self.ui.tx_PorcentagemVarejo.setText("")
        else:
            self.ui.tx_PorcentagemVarejo.setText("")

    def dados_tabela(self):
        self.ui.cb_fornecedor.clear()
        self.ui.cb_categoria.clear()
        self.produto_selecionado.id = None
        self.ui.tx_busca.setText("")
        self.filtrado = False
        self.del_img()
        self.ui.bt_refresh.setEnabled(False)
        self.limpa_campos()
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

    def editar(self):
        if self.produto_selecionado.id:
            itens = list()

            prod_editar = Produtos()
            prod_editar.id = self.ui.tx_id.text()
            itens.append(prod_editar.id)
            prod_editar.codbarras = self.ui.tx_codbarras.text().upper()
            itens.append(prod_editar.codbarras)
            prod_editar.estoque = self.ui.tb_produtos.item(self.ui.tb_produtos.currentRow(), 2).text()
            itens.append(prod_editar.estoque)
            prod_editar.descricao = self.ui.tx_descricao.text().upper()
            itens.append(prod_editar.descricao)
            prod_editar.marca = self.ui.tx_marca.text().upper()
            itens.append(prod_editar.marca)
            prod_editar.preco = float(self.ui.tx_preco.text().upper())
            itens.append(prod_editar.preco)

            prod_editar.fornecedor = Fornecedor()
            indice_forn = self.ui.cb_fornecedor.currentIndex()
            prod_editar.fornecedor.id = self.ui.cb_fornecedor.itemData(indice_forn)[0]
            forn_editar = prod_editar.fornecedor.get_fornecedor_by_id()
            nome_forn = forn_editar[1]
            itens.append(nome_forn)

            prod_editar.categoria = Categoria()
            indice_cat = self.ui.cb_categoria.currentIndex()
            prod_editar.categoria.id = self.ui.cb_categoria.itemData(indice_cat)[0]
            cat_editar = prod_editar.categoria.get_categoria_by_id()
            nome_cat = cat_editar[1]
            itens.append(nome_cat)

            try:
                prod_editar.editar()

                if self.caminho_img:
                    if self.produto_selecionado.check_imagem() is not None:
                        self.produto_selecionado.atualizar_imagem(self.caminho_img)
                    else:
                        self.produto_selecionado.gravar_imagem_produtos(self.caminho_img, "png")
                    self.ui.bt_DelLogo.hide()
                    self.ui.bt_AddLogo.show()
            except Exception as error:
                QMessageBox.warning(self, "Erro", str(error))
            else:
                self.ui.tb_produtos.setFocus()

                for i in range(0, 7):
                    self.ui.tb_produtos.setItem(self.linha_selecionada, i, QTableWidgetItem(str(itens[i])))
        else:
            QMessageBox.warning(self, "Atenção!", "Favor selecionar alguma linha!")

    def excluir(self):
        if self.produto_selecionado.id:
            reply = QMessageBox.question(self, 'Excluir?', f'Tem certeza que deseja excluir o Produto: '
                                                           f'{self.produto_selecionado.descricao}?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

            if reply == QMessageBox.Yes:
                try:
                    self.produto_selecionado.delete()
                    self.produto_selecionado.id = None
                    self.del_img()
                    self.ui.cb_categoria.clear()
                    self.ui.cb_fornecedor.clear()
                except Exception as error:
                    QMessageBox.warning(self, "Erro", str(error))
                else:
                    self.ui.tb_produtos.removeRow(self.linha_selecionada)
                    self.limpa_campos()
            else:
                return
        else:
            QMessageBox.warning(self, "Atenção!", "Favor selecionar alguma linha!")

    def limpa_campos(self):
        self.ui.tx_id.setText("")
        self.ui.tx_marca.setText("")
        self.ui.tx_codbarras.setText("")
        self.ui.tx_preco.setText("")
        self.ui.tx_descricao.setText("")
        self.ui.tx_preco_compra.setText("")
        self.del_img()

    def set_tx_enabled(self, boolean):
        self.ui.tx_marca.setEnabled(boolean)
        self.ui.tx_codbarras.setEnabled(boolean)
        self.ui.tx_preco.setEnabled(boolean)
        self.ui.tx_descricao.setEnabled(boolean)
