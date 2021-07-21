from PyQt5.QtWidgets import QMainWindow


class CadastroUsuario(QMainWindow):
    def __init__(self, parent=None):
        super(CadastroUsuario, self).__init__(parent)
        from View.cadastro_usuario import Ui_ct_FormUsuario
        from PyQt5 import QtCore

        # setando View
        self.ui = Ui_ct_FormUsuario()
        self.ui.setupUi(self)
        self.setFixedSize(1000, 443)

        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

        # eventos
        self.ui.bt_Voltar.clicked.connect(self.fechar)
        self.ui.bt_salvarUsuario.clicked.connect(self.valida_campos)

        self.ui.tx_nome.setMaxLength(60)
        self.ui.tx_Email.setMaxLength(50)
        self.ui.tx_Endereco.setMaxLength(60)
        self.ui.tx_Num.setMaxLength(10)
        self.ui.tx_Cidade.setMaxLength(50)
        self.ui.tx_Estado.setMaxLength(2)
        self.ui.tx_Bairro.setMaxLength(60)

    def fechar(self):
        self.close()

    def valida_campos(self):

        if not self.ui.tx_nome.text():
            self.ui.tx_nome.setFocus()
        elif not self.ui.tx_Email.text():
            self.ui.tx_Email.setFocus()
        elif not self.ui.tx_usuario.text():
            self.ui.tx_usuario.setFocus()
        elif not self.ui.tx_Estado.text():
            self.ui.tx_Estado.setFocus()
        elif not self.ui.tx_Cidade.text():
            self.ui.tx_Cidade.setFocus()
        elif not self.ui.tx_Bairro.text():
            self.ui.tx_Bairro.setFocus()
        elif not self.ui.tx_Num.text():
            self.ui.tx_Num.setFocus()
        elif not self.ui.tx_Endereco.text():
            self.ui.tx_Endereco.setFocus()
        elif not self.ui.tx_senha.text():
            self.ui.tx_senha.setFocus()
        elif not self.ui.tx_senha2.text():
            self.ui.tx_senha2.setFocus()
        elif self.ui.tx_senha2.text() != self.ui.tx_senha.text():
            self.ui.tx_senha2.clear()
            self.ui.tx_senha2.setPlaceholderText("As senhas não conferem")
            self.ui.tx_senha2.setFocus()
        else:
            self.cadastrar()

    def cadastrar(self):
        import psycopg2
        from PyQt5.QtWidgets import QMessageBox
        from Funcoes.configdb import Banco
        from Funcoes.funcoes import criptografar_senha, formatar_cpf_rg

        # campos usuário
        nome = self.ui.tx_nome.text().upper()
        cpf = self.ui.tx_cpf.text().upper()
        rg = self.ui.tx_rg.text().upper()
        telefone = self.ui.tx_Telefone.text().upper()
        email = self.ui.tx_Email.text().lower()
        celular = self.ui.tx_Celular.text().upper()

        # campos endereço
        cep = self.ui.tx_cep.text().upper()
        rua = self.ui.tx_Endereco.text().upper()
        nro = self.ui.tx_Num.text().upper()
        bairro = self.ui.tx_Bairro.text().upper()
        cidade = self.ui.tx_Cidade.text().upper()
        estado = self.ui.tx_Estado.text().upper()

        # campos login
        usuario = self.ui.tx_usuario.text().lower()
        senha = self.ui.tx_senha.text()

        conn = None
        try:
            config = Banco()
            params = config.get_params()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute(f"CALL add_usuario(\'{rua}\', \'{bairro}\', \'{nro}\', \'{cidade}\', \'{estado}\', "
                            f"\'{cep}\', \'{formatar_cpf_rg(cpf)}\', \'{nome}\', \'{telefone}\',\'{email}\', "
                            f"\'{formatar_cpf_rg(rg)}\', \'{celular}\', 'USUÁRIO', \'{usuario}\', "
                            f"\'{criptografar_senha(senha)}\')")
            conn.commit()
            cur.close()

        except Exception as error:
            QMessageBox.about(self, "Erro", str(error))
        else:
            QMessageBox.about(self, "Sucesso", "Cadastro efetuado com sucesso!")
            self.fechar()

        conn.close()
