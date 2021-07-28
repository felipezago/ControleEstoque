from PyQt5.QtWidgets import QMainWindow
from Model.Fornecedor import Fornecedor


class CadastroFornecedor(QMainWindow):
    def __init__(self, parent=None):
        super(CadastroFornecedor, self).__init__(parent)
        from View.cadastro_fornecedor import Ui_ct_FormFornecedor
        from PyQt5 import QtCore

        # setando View
        self.ui = Ui_ct_FormFornecedor()
        self.ui.setupUi(self)
        self.setFixedSize(653, 371)

        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

        # ação dos botões
        self.ui.bt_Salvar.clicked.connect(self.valida_campos)
        self.ui.bt_Voltar.clicked.connect(self.fechar)
        self.ui.bt_busca_cep.clicked.connect(self.busca_cep)
        self.ui.tx_Cep.returnPressed.connect(self.busca_cep)
        self.ui.tx_Cep.textChanged.connect(self.enable_cidade_estado)

        self.ui.tx_NomeFantasia.setMaxLength(50)
        self.ui.tx_Email.setMaxLength(60)
        self.ui.tx_Endereco.setMaxLength(60)
        self.ui.tx_Numero.setMaxLength(10)
        self.ui.tx_Cidade.setMaxLength(50)
        self.ui.tx_Estado.setMaxLength(2)
        self.ui.tx_Bairro.setMaxLength(60)

    def enable_cidade_estado(self):
        if not self.ui.tx_Cidade.isEnabled():
            self.ui.tx_Cidade.setEnabled(True)
        elif not self.ui.tx_Estado.isEnabled():
            self.ui.tx_Estado.setEnabled(True)

    def busca_cep(self):
        from Funcoes.APIs import get_endereco
        from PyQt5.QtWidgets import QMessageBox

        if not self.ui.tx_Cep.text() == '-':
            try:
                endereco = get_endereco(self.ui.tx_Cep.text())
            except BaseException as e:
                QMessageBox.warning(self, "Erro!", f"{e}")
                self.ui.tx_Bairro.setText("")
                self.ui.tx_Cidade.setText("")
                self.ui.tx_Estado.setText("")
                self.ui.tx_Endereco.setText("")
                self.ui.tx_Cep.setText("")
            else:
                self.ui.tx_Bairro.setText("")
                self.ui.tx_Cidade.setText("")
                self.ui.tx_Estado.setText("")
                self.ui.tx_Endereco.setText("")

                if endereco['bairro'] is not None:
                    self.ui.tx_Bairro.setText(endereco['bairro'])
                if endereco['cidade'] is not None:
                    self.ui.tx_Cidade.setText(endereco['cidade'])
                    self.ui.tx_Cidade.setEnabled(False)
                if endereco['logradouro'] is not None:
                    self.ui.tx_Endereco.setText(endereco['logradouro'])
                if endereco['uf'] is not None:
                    self.ui.tx_Estado.setText(endereco['uf'])
                    self.ui.tx_Estado.setEnabled(False)
        else:
            QMessageBox.warning(self, "Erro!", "Favor informar um CEP.")

    def valida_campos(self):
        if not self.ui.tx_NomeFantasia.text():
            self.ui.tx_NomeFantasia.setFocus()
        elif not self.ui.tx_cnpj.text() or self.ui.tx_cnpj.text() == "../----":
            self.ui.tx_cnpj.setFocus()
        elif not self.ui.tx_Email.text():
            self.ui.tx_Email.setFocus()
        elif not self.ui.tx_Estado.text():
            self.ui.tx_Estado.setFocus()
        elif not self.ui.tx_Cidade.text():
            self.ui.tx_Cidade.setFocus()
        elif not self.ui.tx_Bairro.text():
            self.ui.tx_Bairro.setFocus()
        elif not self.ui.tx_Numero.text():
            self.ui.tx_Numero.setFocus()
        elif not self.ui.tx_Endereco.text():
            self.ui.tx_Endereco.setFocus()
        else:
            self.salvar()

    def salvar(self):
        from PyQt5.QtWidgets import QMessageBox

        forn_inserir = Fornecedor()

        forn_inserir.nome = self.ui.tx_NomeFantasia.text().upper()
        forn_inserir.cnpj = self.ui.tx_cnpj.text().upper()
        forn_inserir.telefone = self.ui.tx_Telefone.text().upper()
        forn_inserir.email = self.ui.tx_Email.text().lower()
        forn_inserir.cep = self.ui.tx_Cep.text().upper()
        forn_inserir.rua = self.ui.tx_Endereco.text().upper()
        forn_inserir.nro = self.ui.tx_Numero.text().upper()
        forn_inserir.bairro = self.ui.tx_Bairro.text().upper()
        forn_inserir.cidade = self.ui.tx_Cidade.text().upper()
        forn_inserir.estado = self.ui.tx_Estado.text().upper()

        try:
            forn_inserir.editar()
        except Exception as error:
            QMessageBox.about(self, "Erro", str(error))
        else:
            QMessageBox.about(self, "Sucesso", "Cadastro efetuado com sucesso!")
            self.fechar()

    def fechar(self):
        self.close()
