from PyQt5.QtWidgets import QMainWindow


class CadastroUsuario(QMainWindow):
    def __init__(self, parent=None):
        super(CadastroUsuario, self).__init__(parent)
        from View.cadastro_usuario import Ui_ct_FormUsuario
        from PyQt5 import QtCore

        # setando View
        self.ui = Ui_ct_FormUsuario()
        self.ui.setupUi(self)
        self.dialogs = list()
        self.setFixedSize(1000, 443)

        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

        # eventos
        self.ui.bt_Voltar.clicked.connect(self.fechar)
        self.ui.bt_salvarUsuario.clicked.connect(self.valida_campos)
        self.ui.tx_cep.textChanged.connect(self.enable_cidade_estado)
        self.ui.bt_busca_cep.clicked.connect(self.busca_cep)
        self.ui.tx_cep.returnPressed.connect(self.busca_cep)
        self.ui.bt_add_emp.clicked.connect(self.add_emp)

        self.ui.tx_nome.setMaxLength(60)
        self.ui.tx_Email.setMaxLength(50)
        self.ui.tx_Endereco.setMaxLength(60)
        self.ui.tx_Num.setMaxLength(10)
        self.ui.tx_Cidade.setMaxLength(50)
        self.ui.tx_Estado.setMaxLength(2)
        self.ui.tx_Bairro.setMaxLength(60)

        self.preenche_combo_empresas()

    def add_emp(self):
        from Controller.cadastro_empresas import CadastroEmpresas
        from Funcoes.funcoes import exec_app

        c_emp = CadastroEmpresas()
        exec_app(c_emp)
        self.dialogs.append(c_emp)

    def preenche_combo_empresas(self):
        from Model.Empresa import Empresa

        self.ui.cb_empresa.clear()
        self.ui.cb_empresa.addItem("SELECIONE")
        todos_fornecedores = Empresa.get_todas_empresas()

        for contador, f in enumerate(todos_fornecedores):
            contador += 1
            self.ui.cb_empresa.addItem(f[4])
            self.ui.cb_empresa.setItemData(contador, f)

    def enable_cidade_estado(self):
        if not self.ui.tx_Cidade.isEnabled():
            self.ui.tx_Cidade.setEnabled(True)
        elif not self.ui.tx_Estado.isEnabled():
            self.ui.tx_Estado.setEnabled(True)

    def busca_cep(self):
        from Funcoes.APIs import get_endereco
        from PyQt5.QtWidgets import QMessageBox

        if not self.ui.tx_cep.text() == '-':
            try:
                endereco = get_endereco(self.ui.tx_cep.text())
            except BaseException as e:
                QMessageBox.warning(self, "Erro!", f"{e}")
                self.ui.tx_Bairro.setText("")
                self.ui.tx_Cidade.setText("")
                self.ui.tx_Estado.setText("")
                self.ui.tx_Endereco.setText("")
                self.ui.tx_cep.setText("")
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
        elif self.ui.cb_empresa.currentIndex() == 0:
            self.ui.cb_empresa.setFocus()
        elif self.ui.cb_nivel.currentIndex() == 0:
            self.ui.cb_nivel.setFocus()
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
        nivel = self.ui.cb_nivel.itemText(self.ui.cb_nivel.currentIndex())
        index_emp = self.ui.cb_empresa.currentIndex()
        empresa_cnpj = self.ui.cb_empresa.itemData(index_emp)[0]

        conn = None
        try:
            config = Banco()
            params = config.get_params()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute(f"CALL add_usuario(\'{rua}\', \'{bairro}\', \'{nro}\', \'{cidade}\', \'{estado}\', "
                        f"\'{cep}\', \'{formatar_cpf_rg(cpf)}\', \'{nome}\', \'{telefone}\',\'{email}\', "
                        f"\'{formatar_cpf_rg(rg)}\', \'{celular}\', 'USUÁRIO', \'{usuario}\', "
                        f"\'{criptografar_senha(senha)}\', \'{empresa_cnpj}\', \'{nivel}\')")
            conn.commit()
            cur.close()

        except Exception as error:
            QMessageBox.about(self, "Erro", str(error))
        else:
            QMessageBox.about(self, "Sucesso", "Cadastro efetuado com sucesso!")
            self.fechar()

        conn.close()
