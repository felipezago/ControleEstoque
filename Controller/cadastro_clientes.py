from PyQt5.QtWidgets import QMainWindow


class CadastroClientes(QMainWindow):
    def __init__(self, parent=None):
        super(CadastroClientes, self).__init__(parent)
        from View.cadastro_cliente import Ui_ct_FormClientes
        from PyQt5 import QtCore
        from Model.Cliente import Cliente

        self.ui = Ui_ct_FormClientes()
        self.ui.setupUi(self)
        self.dialogs = list()
        self.setFixedSize(669, 440)

        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

        self.novo_id = Cliente.get_new_cliente()
        self.ui.tx_Id.setText(str(self.novo_id))

        self.ui.tx_nome.setMaxLength(60)
        self.ui.tx_Email.setMaxLength(50)
        self.ui.tx_Endereco.setMaxLength(60)
        self.ui.tx_Numero.setMaxLength(10)
        self.ui.tx_Cidade.setMaxLength(50)
        self.ui.tx_Estado.setMaxLength(2)
        self.ui.tx_Bairro.setMaxLength(60)

        self.ui.bt_Voltar.clicked.connect(self.sair)
        self.ui.bt_Salvar.clicked.connect(self.validar_campos)
        self.ui.tx_Cep.returnPressed.connect(self.busca_cep)
        self.ui.bt_busca_cep.clicked.connect(self.busca_cep)
        self.ui.tx_Cep.textChanged.connect(self.enable_cidade_estado)

    def enable_cidade_estado(self):
        if not self.ui.tx_Cidade.isEnabled():
            self.ui.tx_Cidade.setEnabled(True)
        elif not self.ui.tx_Estado.isEnabled():
            self.ui.tx_Estado.setEnabled(True)

    def busca_cep(self):
        from Funcoes.funcoes import get_endereco
        from PyQt5.QtWidgets import QMessageBox

        self.ui.tx_Cidade.setEnabled(True)
        self.ui.tx_Estado.setEnabled(True)

        if not self.ui.tx_Cep.text() == '-':
            try:
                endereco = get_endereco(self.ui.tx_Cep.text())
            except Exception as e:
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

    def sair(self):
        self.close()

    def validar_campos(self):
        if not self.ui.tx_nome.text():
            self.ui.tx_nome.setFocus()
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
        import psycopg2
        from PyQt5.QtWidgets import QMessageBox
        from Funcoes.configdb import Banco
        from Funcoes.funcoes import formatar_cpf_rg

        # campos usuário
        nome = self.ui.tx_nome.text().upper()
        cpf = self.ui.tx_cpf.text().upper()
        rg = self.ui.tx_rg.text().upper()
        telefone = self.ui.tx_Telefone.text().upper()
        email = self.ui.tx_Email.text().lower()
        celular = self.ui.tx_Celular.text().upper()

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
            cur.execute(f"CALL add_clientes(\'{rua}\', \'{bairro}\', \'{nro}\', \'{cidade}\', \'{estado}\', "
                        f"\'{cep}\', \'{formatar_cpf_rg(cpf)}\', \'{nome}\', \'{telefone}\',\'{email}\', "
                        f"\'{formatar_cpf_rg(rg)}\', \'{celular}\', 'CLIENTE')")
            conn.commit()
            cur.close()

        except Exception as error:
            QMessageBox.about(self, "Erro", str(error))
        else:
            QMessageBox.about(self, "Sucesso", "Cadastro efetuado com sucesso!")

        conn.close()
