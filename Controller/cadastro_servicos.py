from PyQt5.QtWidgets import QMainWindow


class CadastroServicos(QMainWindow):
    def __init__(self, parent=None):
        super(CadastroServicos, self).__init__(parent)
        from View.cadastro_servicos import Ui_ct_FormServicos
        from PyQt5 import QtCore
        from PyQt5.QtGui import QDoubleValidator

        # setando View
        self.ui = Ui_ct_FormServicos()
        self.ui.setupUi(self)
        self.dialogs = list()
        self.setFixedSize(562, 261)

        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

        validator_double = QDoubleValidator(0, 9999, 4)
        self.ui.tx_ValorUnitarioProduto.setValidator(validator_double)

        self.ui.tx_DescricaoServico.setMaxLength(60)

        self.ui.tx_ValorUnitarioProduto.textChanged.connect(self.converter_virgula)
        self.ui.bt_cancelar.clicked.connect(self.sair)
        self.ui.bt_salvar.clicked.connect(self.salvar)

    def sair(self):
        self.close()

    def valida_campos(self):

        if not self.ui.tx_DescricaoServico.text():
            self.ui.tx_DescricaoServico.setFocus()
        elif not self.ui.tx_ValorUnitarioProduto.text():
            self.ui.tx_ValorUnitarioProduto.setFocus()
        else:
            self.salvar()

    def salvar(self):
        from Model.Servicos import Servicos
        from PyQt5.QtWidgets import QMessageBox

        descricao = self.ui.tx_DescricaoServico.text().upper()
        preco = float(self.ui.tx_ValorUnitarioProduto.text())

        novo_servico = Servicos()
        novo_servico.descricao = descricao
        novo_servico.preco = preco

        try:
            novo_servico.inserir_servico()

        except Exception as error:
            QMessageBox.about(self, "Erro", str(error))
        else:
            QMessageBox.about(self, "Sucesso", "Cadastro efetuado com sucesso!")

        self.limpa_campos()

    def converter_virgula(self):
        valor = str(self.ui.tx_ValorUnitarioProduto.text())
        virgula = valor.find(',')
        if virgula > 0:
            self.ui.tx_ValorUnitarioProduto.setText(valor.replace(",", "."))

    def limpa_campos(self):
        self.ui.tx_ValorUnitarioProduto.setText("")
        self.ui.tx_DescricaoServico.setText("")
