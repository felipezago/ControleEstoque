from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore


class EventFilter(QtCore.QObject):

    def __init__(self, parent=None):
        QtCore.QObject.__init__(self, parent)

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.ActivationChange:
            if self.parent().isActiveWindow():
                # Reseta CB Categorias
                if obj.ui.cb_empresa.currentIndex() == 0:
                    obj.preenche_combo_empresas()

        return QtCore.QObject.eventFilter(self, obj, event)


class CadastroUsuario(QMainWindow):
    def __init__(self, parent=None):
        super(CadastroUsuario, self).__init__(parent)
        from View.cadastro_usuario import Ui_ct_FormUsuario
        from PyQt5 import QtCore

        # setando View
        self.ui = Ui_ct_FormUsuario()
        self.ui.setupUi(self)
        self.dialogs = list()
        self.setFixedSize(self.size())

        self.installEventFilter(EventFilter(self))

        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

        # eventos
        self.ui.bt_Voltar.clicked.connect(self.fechar)
        self.ui.bt_salvarUsuario.clicked.connect(self.valida_campos)
        self.ui.bt_add_emp.clicked.connect(self.add_emp)

        self.ui.tx_nome.setMaxLength(60)
        self.ui.tx_Email.setMaxLength(50)

        self.preenche_combo_empresas()

    def add_emp(self):
        from Controller.cadastro_empresas import CadastroEmpresas
        from Funcoes.utils import exec_app

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
            self.ui.cb_empresa.addItem(f[2])
            self.ui.cb_empresa.setItemData(contador, f)

    def fechar(self):
        self.close()

    def valida_campos(self):
        if not self.ui.tx_nome.text():
            self.ui.tx_nome.setFocus()
        elif not self.ui.tx_Email.text():
            self.ui.tx_Email.setFocus()
        elif not self.ui.tx_usuario.text():
            self.ui.tx_usuario.setFocus()
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
        from PyQt5.QtWidgets import QMessageBox
        from Model.Usuario import Usuario
        from Model.Empresa import Empresa

        usu_inserir = Usuario()
        usu_inserir.empresa = Empresa()

        usu_inserir.nome = self.ui.tx_nome.text().upper()
        usu_inserir.cpf = self.ui.tx_cpf.text().upper()
        usu_inserir.rg = self.ui.tx_rg.text().upper()
        usu_inserir.fone = self.ui.tx_Telefone.text().upper()
        usu_inserir.email = self.ui.tx_Email.text().lower()
        usu_inserir.celular = self.ui.tx_Celular.text().upper()
        usu_inserir.login = self.ui.tx_usuario.text().lower()
        usu_inserir.senha = self.ui.tx_senha.text()
        usu_inserir.nivel = self.ui.cb_nivel.itemText(self.ui.cb_nivel.currentIndex())
        index_emp = self.ui.cb_empresa.currentIndex()
        usu_inserir.empresa.cnpj = self.ui.cb_empresa.itemData(index_emp)[0]

        try:
            usu_inserir.inserir()
        except Exception as error:
            QMessageBox.about(self, "Erro", str(error))
        else:
            QMessageBox.about(self, "Sucesso", "Cadastro efetuado com sucesso!")
            self.fechar()
