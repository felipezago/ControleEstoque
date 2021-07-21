from PyQt5.QtWidgets import QMainWindow


class CadastroFornecedor(QMainWindow):
    def __init__(self, parent=None):
        super(CadastroFornecedor, self).__init__(parent)
        from View.cadastro_fornecedor import Ui_ct_FormFornecedor
        from PyQt5 import QtCore
        from Model.Fornecedor import Fornecedor

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

        # setando novo ID
        self.novo_id = Fornecedor.get_new_fornecedor()
        self.ui.tx_Id.setText(str(self.novo_id))

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
        from Funcoes.funcoes import get_endereco
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
        from Funcoes.configdb import Banco
        import psycopg2
        from Funcoes.funcoes import formatar_cpf_rg


        # campos fornecedor
        nome = self.ui.tx_NomeFantasia.text().upper()
        cnpj = self.ui.tx_cnpj.text().upper()
        telefone = self.ui.tx_Telefone.text().upper()
        email = self.ui.tx_Email.text().lower()

        # campos endereço
        cep = self.ui.tx_Cep.text().upper()
        rua = self.ui.tx_Endereco.text().upper()
        nro = self.ui.tx_Numero.text().upper()
        bairro = self.ui.tx_Bairro.text().upper()
        cidade = self.ui.tx_Cidade.text().upper()
        estado = self.ui.tx_Estado.text().upper()

        conn = None
        try:
            config = Banco()
            params = config.get_params()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute(f"CALL add_fornecedor(\'{rua}\', \'{bairro}\', \'{nro}\', \'{cidade}\', \'{estado}\', "
                        f"\'{cep}\', \'{formatar_cpf_rg(cnpj)}\', \'{nome}\', \'{telefone}\',\'{email}\') ")
            conn.commit()
            cur.close()

        except Exception as error:
            QMessageBox.about(self, "Erro", str(error))
        else:
            QMessageBox.about(self, "Sucesso", "Cadastro efetuado com sucesso!")
            self.fechar()

        conn.close()

    def fechar(self):
        self.close()
