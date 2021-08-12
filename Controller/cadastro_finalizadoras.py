from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow


class CadastroFinalizadoras(QMainWindow):
    def __init__(self, parent=None):
        super(CadastroFinalizadoras, self).__init__(parent)
        from View.cadastro_finalizadoras import Ui_ct_FormProdutos
        from PyQt5 import QtCore

        # setando View
        self.ui = Ui_ct_FormProdutos()
        self.ui.setupUi(self)
        self.dialogs = list()
        self.tamanho = self.size()
        self.setFixedSize(self.tamanho)

        self.setWindowIcon(QtGui.QIcon("Imagens/logo_fzr.png"))

        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

        self.ui.tx_desc.setMaxLength(60)

        self.ui.bt_cancelar.clicked.connect(self.sair)
        self.ui.bt_salvar.clicked.connect(self.salvar)
        self.ui.tx_desc.returnPressed.connect(self.salvar)

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        self.setFixedSize(self.tamanho)

    def sair(self):
        self.close()

    def valida_campos(self):

        if not self.ui.tx_desc.text():
            self.ui.tx_desc.setFocus()
        else:
            self.salvar()

    def salvar(self):
        from Model.Finalizadoras import Finalizadoras
        from PyQt5.QtWidgets import QMessageBox

        descricao = self.ui.tx_desc.text().upper()

        nova_fin = Finalizadoras()
        nova_fin.descricao = descricao

        try:
            nova_fin.inserir_finalizadora()

        except Exception as error:
            QMessageBox.about(self, "Erro", str(error))
        else:
            QMessageBox.about(self, "Sucesso", "Cadastro efetuado com sucesso!")
            self.ui.tx_desc.setText("")
