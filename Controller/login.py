from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication
from Funcoes.utils import centralizar


class Login(QMainWindow):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        from View import login
        from Model.Usuario import Usuario
        from Funcoes.utils import resource_path
        from PyQt5 import QtGui
        from PyQt5.QtCore import Qt

        # background images
        palete = QtGui.QPalette()
        image = QtGui.QPixmap((QtGui.QPixmap('Imagens/login_bg.png')))
        brush = QtGui.QBrush(image)
        palete.setBrush(QtGui.QPalette.Background, brush)
        self.setPalette(palete)

        # setando View
        self.ui = login.Ui_ct_login()
        self.ui.setupUi(self)
        self.dialogs = list()
        self.tamanho = self.size()
        self.setFixedSize(self.tamanho)

        self.setWindowIcon(QtGui.QIcon("Imagens/logo_fzr.png"))

        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)

        # eventos
        self.ui.bt_login.clicked.connect(self.validar_login)
        self.ui.tx_user.returnPressed.connect(self.ui.tx_senha.setFocus)
        self.ui.tx_senha.returnPressed.connect(self.validar_login)

        self.usuarios = Usuario.get_todos_usuarios()

        if self.usuarios:
            self.ui.bt_cadastrar.hide()
        else:
            self.ui.bt_cadastrar.setHidden(False)
            self.ui.bt_cadastrar.clicked.connect(self.cadastrar)

        self.operador = None

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        self.setFixedSize(self.size())

    def validar_login(self):
        from Funcoes.configdb import Banco
        import psycopg2
        from Funcoes.utils import verificar_criptografia, exec_app
        from Model.Operador import Operador

        self.usuarios = self.ui.tx_user.text().lower()
        senha = self.ui.tx_senha.text()
        config = Banco()
        conn = None
        try:

            params = config.get_params()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute(f'SELECT * FROM usuarios WHERE usu_login = LOWER(\'{self.usuarios}\')')
            linha = cur.fetchone()

            # se encontrar o usu??rio
            if linha is not None:
                # pega a senha e codifica
                passwd = linha[3].encode()
                # se a senha criptografada bater
                if verificar_criptografia(senha.encode(), passwd):
                    if not Operador.verifica_operador_ativo():
                        Operador.inserir_operador(linha[0])
                        self.operador = Operador.get_operador_atual()

                    from Controller.tela_principal import TelaPrincipal
                    princ = TelaPrincipal()
                    princ.showMaximized()
                    centralizar(princ)
                    self.dialogs.append(princ)
                    self.close()

                else:
                    self.ui.lb_alert.setText("Senha Inv??lida")
            else:
                self.ui.lb_alert.setText("Usu??rio n??o encontrado")

            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print('Database connection closed.')

    def cadastrar(self):
        from Funcoes.utils import exec_app
        from Controller.cadastro_usuario import CadastroUsuario

        cadastro = CadastroUsuario()
        exec_app(cadastro)
        self.dialogs.append(cadastro)


def exec_login():
    import sys

    app = QApplication(sys.argv)
    form = Login()
    form.show()
    centralizar(form)
    app.exec_()
