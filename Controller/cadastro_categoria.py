from PyQt5.QtWidgets import QMainWindow


class CadastroCategoria(QMainWindow):
    def __init__(self, parent=None):
        super(CadastroCategoria, self).__init__(parent)
        from View.cadastro_categoria import Ui_ct_FormCategoria
        from PyQt5 import QtCore

        # setando View
        self.ui = Ui_ct_FormCategoria()
        self.ui.setupUi(self)
        self.setFixedSize(285, 161)

        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

        self.ui.bt_SalvarProdutos.clicked.connect(self.inserir)
        self.ui.bt_CancelarProdutos.clicked.connect(self.sair)

        self.ui.tx_desc_cat.setMaxLength(50)

    def inserir(self):
        from Model.Categoria import Categoria
        from PyQt5.QtWidgets import QMessageBox

        cat = Categoria()
        cat.descricao = self.ui.tx_desc_cat.text().upper()

        try:
            cat.inserir_categoria()
        except Exception as error:
            QMessageBox.about(self, "Erro", str(error))
        else:
            QMessageBox.about(self, "Sucesso", "Cadastro efetuado com sucesso!")
            self.ui.tx_desc_cat.setText("")

    def sair(self):
        self.close()
