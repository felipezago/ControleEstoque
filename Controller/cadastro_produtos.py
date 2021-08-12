from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui


class EventFilter(QtCore.QObject):

    def __init__(self, parent=None):
        QtCore.QObject.__init__(self, parent)

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.ActivationChange:
            if self.parent().isActiveWindow():
                # Reseta CB Categorias
                if obj.adicionando_forn:
                    obj.adicionando_forn = False
                    obj.preenche_combo_fornecedores()
                    obj.ui.cb_forn.setCurrentIndex(obj.indice_forn)

                if obj.adicionando_cat:
                    obj.adicionando_cat = False
                    obj.preenche_combo_categorias()
                    obj.ui.cb_CategoriaProduto.setCurrentIndex(obj.indice_cat)

        return QtCore.QObject.eventFilter(self, obj, event)


class CadastroProdutos(QMainWindow):
    def __init__(self, parent=None):
        super(CadastroProdutos, self).__init__(parent)
        from View.cadastro_produtos import Ui_ct_FormProdutos
        from Funcoes.utils import IconeBotaoMenu, resource_path
        from PyQt5.QtGui import QIntValidator, QDoubleValidator
        from Model.Produtos import Produtos

        # setando View
        self.ui = Ui_ct_FormProdutos()
        self.ui.setupUi(self)
        self.dialogs = list()
        self.tamanho = self.size()
        self.setFixedSize(self.tamanho)

        self.setWindowIcon(QtGui.QIcon("Imagens/logo_fzr.png"))

        self.caminho_img = None
        self.adicionando_forn = False
        self.adicionando_cat = False
        self.indice_forn = 0
        self.indice_cat = 0

        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

        # adicionando icones aos botoes
        IconeBotaoMenu(self.ui.bt_DelImagem,
                       resource_path('../Imagens/edit-delete.png'))
        IconeBotaoMenu(self.ui.bt_AddImagem,
                       resource_path('../Imagens/edit-add.png'))
        IconeBotaoMenu(self.ui.bt_AddCategoriaProduto,
                       resource_path('../Imagens/edit-add.png'))
        IconeBotaoMenu(self.ui.bt_addForn,
                       resource_path('../Imagens/edit-add.png'))

        # definindo ações dos botões
        self.ui.bt_AddCategoriaProduto.clicked.connect(self.add_categoria)
        self.ui.bt_AddImagem.clicked.connect(self.upload_imagem)
        self.ui.bt_DelImagem.clicked.connect(self.del_img)
        self.ui.bt_CancelarProdutos.clicked.connect(self.fechar)
        self.ui.bt_addForn.clicked.connect(self.add_forn)
        self.ui.bt_SalvarProdutos.clicked.connect(self.validar_campos)

        # instalando filtro de eventos
        self.installEventFilter(EventFilter(self))

        # definindo novo ID
        self.novo_id = Produtos.get_new_produto()
        self.ui.tx_idProduto.setText(str(self.novo_id))

        # preenchendo combos
        self.preenche_combo_categorias()
        self.preenche_combo_fornecedores()

        # setando validadores
        validator_int = QIntValidator(-9999, 9999, self)
        validator_double = QDoubleValidator(0, 9999, 4)
        self.ui.tx_EstoqueMaximoProduto.setValidator(validator_int)
        self.ui.tx_ValorUnitarioProduto.setValidator(validator_double)

        # prevenindo erros
        self.ui.tx_DescricaoProduto.setMaxLength(50)
        self.ui.tx_marca.setMaxLength(60)
        self.ui.tx_codbarras.setMaxLength(15)

        self.ui.tx_ValorUnitarioProduto.textChanged.connect(self.converter_virgula)

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        self.setFixedSize(self.tamanho)

    def converter_virgula(self):
        valor = str(self.ui.tx_ValorUnitarioProduto.text())
        virgula = valor.find(',')
        if virgula > 0:
            self.ui.tx_ValorUnitarioProduto.setText(valor.replace(",", "."))

    def add_forn(self):
        from Controller.cadastro_fornecedor import CadastroFornecedor
        from Funcoes.utils import exec_app

        cad_forn = CadastroFornecedor()
        exec_app(cad_forn)
        self.dialogs.append(cad_forn)
        self.adicionando_forn = True
        self.indice_forn = self.ui.cb_forn.currentIndex()

    def add_categoria(self):
        from Controller.cadastro_categoria import CadastroCategoria
        from Funcoes.utils import exec_app

        cad_cat = CadastroCategoria()
        exec_app(cad_cat)
        self.dialogs.append(cad_cat)

        self.adicionando_cat = True
        self.indice_cat = self.ui.cb_CategoriaProduto.currentIndex()

    def upload_imagem(self):
        from PyQt5.QtCore import Qt
        from PyQt5.QtWidgets import QFileDialog
        from PyQt5.QtGui import QPixmap

        dialog = QFileDialog()
        dialog.setOption(QFileDialog.DontUseNativeDialog, True)

        fname = dialog.getOpenFileName(
            self, "Selecionar Imagem", "", "Image files (*.jpg *.png)")[0]

        self.ui.lb_FotoProduto.setPixmap(QPixmap(fname).scaledToWidth(
            150, Qt.TransformationMode(Qt.FastTransformation)))
        # self.lb_FotoProduto.setScaledContents(True)
        self.ui.bt_AddImagem.setHidden(True)
        self.ui.bt_DelImagem.setVisible(True)

        self.caminho_img = fname

    def del_img(self):
        self.ui.lb_FotoProduto.clear()
        self.ui.bt_DelImagem.setHidden(True)
        self.ui.bt_AddImagem.setVisible(True)

    def preenche_combo_categorias(self):
        from Model.Categoria import Categoria

        self.ui.cb_CategoriaProduto.clear()
        self.ui.cb_CategoriaProduto.addItem("SELECIONE")
        todas_categorias = Categoria.get_todas_categorias()

        for contador, cat in enumerate(todas_categorias):
            contador += 1
            self.ui.cb_CategoriaProduto.addItem(cat[1])
            self.ui.cb_CategoriaProduto.setItemData(contador, cat)

    def preenche_combo_fornecedores(self):
        from Model.Fornecedor import Fornecedor

        self.ui.cb_forn.clear()
        self.ui.cb_forn.addItem("SELECIONE")
        todos_fornecedores = Fornecedor.get_todos_fornecedores()

        for contador, f in enumerate(todos_fornecedores):
            contador += 1
            self.ui.cb_forn.addItem(f[1])
            self.ui.cb_forn.setItemData(contador, f)

    def validar_campos(self):
        if not self.ui.tx_DescricaoProduto.text():
            self.ui.tx_DescricaoProduto.setFocus()
        if not self.ui.tx_codbarras.text():
            self.ui.tx_codbarras.setFocus()
        elif self.ui.cb_forn.currentIndex() == 0:
            self.ui.cb_forn.setFocus()
        elif self.ui.cb_CategoriaProduto.currentIndex() == 0:
            self.ui.cb_CategoriaProduto.setFocus()
        elif not self.ui.tx_marca.text():
            self.ui.tx_marca.setFocus()
        elif not self.ui.tx_EstoqueMaximoProduto.text():
            self.ui.tx_EstoqueMaximoProduto.setFocus()
        elif not self.ui.tx_ValorUnitarioProduto.text():
            self.ui.tx_ValorUnitarioProduto.setFocus()
        else:
            self.salvar()

    def salvar(self):
        from PyQt5.QtWidgets import QMessageBox
        from Funcoes.configdb import Banco
        from Model.Produtos import Produtos

        import psycopg2

        # campos fornecedor
        descricao = self.ui.tx_DescricaoProduto.text().upper()
        codbarras = self.ui.tx_codbarras.text().upper()
        marca = self.ui.tx_marca.text().upper()
        estoque = self.ui.tx_EstoqueMaximoProduto.text()
        preco = float(self.ui.tx_ValorUnitarioProduto.text())

        # combo box
        indice_forn = self.ui.cb_forn.currentIndex()
        indice_cat = self.ui.cb_CategoriaProduto.currentIndex()
        fornecedor_id = self.ui.cb_forn.itemData(indice_forn)[0]
        categoria_id = self.ui.cb_CategoriaProduto.itemData(indice_cat)[0]

        conn = None
        try:
            config = Banco()
            params = config.get_params()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()

            cur.execute(f"SELECT add_prod(\'{descricao}\', \'{codbarras}\', \'{marca}\', {estoque}, {preco}, "
                        f"{fornecedor_id}, {categoria_id});")

            new_id = cur.fetchone()
            conn.commit()
            cur.close()

            if self.caminho_img:
                prod_img = Produtos()
                prod_img.id = new_id[0]
                prod_img.gravar_imagem_produtos(self.caminho_img, "png")

        except Exception as error:
            print(error)
            QMessageBox.about(self, "Erro", str(error))
        else:
            QMessageBox.about(self, "Sucesso", "Cadastro efetuado com sucesso!")

        conn.close()
        self.limpa_campos()

    def fechar(self):
        self.close()

    def limpa_campos(self):
        self.del_img()
        self.ui.tx_marca.setText("")
        self.ui.tx_codbarras.setText("")
        self.ui.tx_DescricaoProduto.setText("")
        self.ui.tx_EstoqueMaximoProduto.setText("")
        self.ui.tx_ValorUnitarioProduto.setText("")
        self.ui.tx_PorcentagemVarejo.setText("")
        self.ui.cb_forn.setCurrentIndex(0)
        self.ui.cb_CategoriaProduto.setCurrentIndex(0)
