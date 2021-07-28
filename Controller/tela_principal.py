from PyQt5.QtWidgets import QApplication, QMainWindow, QShortcut, QLabel
from PyQt5 import QtCore
from Model.Operador import Operador
from Funcoes.funcoes import exec_app
import sys

app = QApplication(sys.argv)


class Label(QLabel):
    clicked = QtCore.pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()


class TelaPrincipal(QMainWindow):
    kill_thread = False
    saida_operador = False

    def __init__(self, parent=None):
        super(TelaPrincipal, self).__init__(parent)
        from Funcoes.funcoes import resource_path, retorna_ip
        from Funcoes.configdb import Banco
        from View.tela_principal import Ui_MainWindow
        from Model.Pessoa import Pessoa
        from Model.Usuario import Usuario
        from PyQt5 import QtGui

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.dialogs = list()

        self.usuario_operador = Usuario()
        self.pessoa_operador = Pessoa()

        palete = QtGui.QPalette()
        image = QtGui.QPixmap(resource_path('../Imagens/background_1920x1080.png'))
        brush = QtGui.QBrush(image)
        palete.setBrush(QtGui.QPalette.Background, brush)
        self.setPalette(palete)

        # atalhos
        self.ui.lbl_atalho_venda.clicked.connect(self.nova_venda)
        self.ui.lbl_atalho_venda_txt.clicked.connect(self.nova_venda)
        self.atalho_venda = QShortcut(QtGui.QKeySequence("F5"), self)
        self.atalho_venda.activated.connect(self.nova_venda)

        # redimensionando
        self.resolucao = app.desktop().screenGeometry()
        self.width, self.height = self.resolucao.width(), self.resolucao.height()
        self.resize(self.width, self.height)
        self.ui.frame.move(self.width - 350, self.height - 360)
        self.ui.frame_atalhos.resize(self.width, 61)

        # setando variaveis
        self.ui.lbl_ip.setText("IP: " + retorna_ip())
        self.ui.lbl_bd.setText("Base de dados: " + Banco().get_params()['database'])
        self.usuario_operador.id = Operador.get_operador_atual()[0]

        nome = str(self.usuario_operador.get_usuario_by_id()[2]).title()
        nivel = self.usuario_operador.get_usuario_by_id()[8]
        self.ui.lbl_usuario.setText("Usuário: " + nome)

        if nivel == "VENDEDOR":
            self.ui.actionCadastroEmpresas.setVisible(False)
            self.ui.actionCadastroUsuarios.setVisible(False)
            self.ui.actionVisualizaEmpresas.setVisible(False)
            self.ui.menuConfigura_o.menuAction().setVisible(False)
            self.ui.actionVisualizaUsuarios.triggered.connect(self.visualiza_usuario)
        else:
            self.ui.actionVisualizaUsuarios.triggered.connect(self.visualiza_usuarios)
            self.ui.actionVisualizaUsuarios.setText("Usuarios")

        # actions cadastro
        self.ui.actionCadastroUsuarios.triggered.connect(self.cadastro_usuarios)
        self.ui.actionCadastroProdutos.triggered.connect(self.cadastro_produtos)
        self.ui.actionCadastroCategorias.triggered.connect(self.cadastro_categoria)
        self.ui.actionCadastroFornecedores.triggered.connect(self.cadastro_fornecedor)
        self.ui.actionCadastroServicos.triggered.connect(self.cadastro_servicos)
        self.ui.actionCadastroEmpresas.triggered.connect(self.cadastro_empresa)
        self.ui.actionCadastroClientes.triggered.connect(self.cadastro_clientes)
        self.ui.actionCadastroVeiculos.triggered.connect(self.cadastro_veiculos)
        self.ui.actionCadastroFinalizadoras.triggered.connect(self.cadastro_finalizadoras)

        # actions visualizar
        self.ui.actionVisualizaCategorias.triggered.connect(self.visualiza_categorias)
        self.ui.actionVisualizaServicos.triggered.connect(self.visualiza_servicos)
        self.ui.actionVisualizaEndereco.setVisible(False)
        self.ui.actionVisualizaEmpresas.triggered.connect(self.visualiza_empresas)
        self.ui.actionVisualizaClientes.triggered.connect(self.visualiza_clientes)
        self.ui.actionVisualizaVeiculos.triggered.connect(self.visualiza_veiculos)
        self.ui.actionVisualizaFornecedores.triggered.connect(self.visualiza_fornecedores)
        self.ui.actionVisualizaProdutos.triggered.connect(self.visualiza_produtos)
        self.ui.actionVisualizaFinalizadoras.triggered.connect(self.visualiza_finalizadoras)

        # actions venda
        self.ui.actionNova_Venda.triggered.connect(self.nova_venda)

        # actions conf
        self.ui.actionBanco_de_Dados.triggered.connect(self.configurar_db)

        # actions sair
        self.ui.actionSaidaOperador.triggered.connect(self.sair_operador)
        self.ui.actionSair_do_Sistema.triggered.connect(self.sair_sistema)

        import threading
        x = threading.Thread(target=self.thread_func)
        x.start()

    def visualiza_finalizadoras(self):
        from Controller.lista_finalizadoras import ListaFinalizadoras

        l_fin = ListaFinalizadoras()
        exec_app(l_fin)
        self.dialogs.append(l_fin)

    def cadastro_finalizadoras(self):
        from Controller.cadastro_finalizadoras import CadastroFinalizadoras

        c_fin = CadastroFinalizadoras()
        exec_app(c_fin)
        self.dialogs.append(c_fin)

    def nova_venda(self):
        from Controller.venda import VendaTemp

        nova_venda = VendaTemp()
        exec_app(nova_venda)
        self.dialogs.append(nova_venda)

    def visualiza_produtos(self):
        from Controller.lista_produtos import ListaProdutos

        l_prod = ListaProdutos()
        exec_app(l_prod)
        self.dialogs.append(l_prod)

    def visualiza_fornecedores(self):
        from Controller.lista_fornecedores import ListaFornecedor

        l_forn = ListaFornecedor()
        exec_app(l_forn)
        self.dialogs.append(l_forn)

    def visualiza_veiculos(self):
        from Controller.lista_veiculos import ListaVeiculos

        l_veic = ListaVeiculos()
        exec_app(l_veic)
        self.dialogs.append(l_veic)

    def visualiza_clientes(self):
        from Controller.lista_clientes import ListaClientes

        l_cli = ListaClientes()
        exec_app(l_cli)
        self.dialogs.append(l_cli)

    def visualiza_empresas(self):
        from Controller.lista_empresa import ListaEmpresa

        l_usu = ListaEmpresa()
        exec_app(l_usu)
        self.dialogs.append(l_usu)

    def visualiza_usuario(self):
        from Controller.lista_usuario import ListaUsuario

        l_usu = ListaUsuario()
        exec_app(l_usu)
        self.dialogs.append(l_usu)

    def visualiza_usuarios(self):
        from Controller.lista_usuarios import ListaUsuario

        l_usus = ListaUsuario()
        exec_app(l_usus)
        self.dialogs.append(l_usus)

    def visualiza_endereco(self):
        from Controller.lista_endereco import ListaEndereco

        l_end = ListaEndereco()
        exec_app(l_end)
        self.dialogs.append(l_end)

    def visualiza_categorias(self):
        from Controller.lista_categorias import ListaCategorias
        l_cat = ListaCategorias()
        exec_app(l_cat)
        self.dialogs.append(l_cat)

    def visualiza_servicos(self):
        from Controller.lista_servicos import ListaServicos
        l_serv = ListaServicos()
        exec_app(l_serv)
        self.dialogs.append(l_serv)

    def cadastro_veiculos(self):
        from Controller.cadastro_veiculos import CadastroVeiculos
        veic = CadastroVeiculos()
        exec_app(veic)
        self.dialogs.append(veic)

    def cadastro_clientes(self):
        from Controller.cadastro_clientes import CadastroClientes
        clie = CadastroClientes()
        exec_app(clie)
        self.dialogs.append(clie)

    def cadastro_usuarios(self):
        from Controller.cadastro_usuario import CadastroUsuario
        usu = CadastroUsuario()
        exec_app(usu)
        self.dialogs.append(usu)

    def cadastro_empresa(self):
        from Controller.cadastro_empresas import CadastroEmpresas
        emp = CadastroEmpresas()
        exec_app(emp)
        self.dialogs.append(emp)

    def cadastro_produtos(self):
        from Controller.cadastro_produtos import CadastroProdutos
        prod = CadastroProdutos()
        exec_app(prod)
        self.dialogs.append(prod)

    def cadastro_fornecedor(self):
        from Controller.cadastro_fornecedor import CadastroFornecedor
        cad_forn = CadastroFornecedor()
        exec_app(cad_forn)
        self.dialogs.append(cad_forn)

    def cadastro_categoria(self):
        from Controller.cadastro_categoria import CadastroCategoria
        cat = CadastroCategoria()
        exec_app(cat)
        self.dialogs.append(cat)

    def cadastro_servicos(self):
        from Controller.cadastro_servicos import CadastroServicos
        serv = CadastroServicos()
        exec_app(serv)
        self.dialogs.append(serv)

    def sair_operador(self):
        self.saida_operador = True
        self.close()

    def sair_sistema(self):
        self.close()

    def configurar_db(self):
        import Controller.configuracao_db
        conf = Controller.configuracao_db.DBConfig()
        exec_app(conf)
        self.dialogs.append(conf)

    def closeEvent(self, event):
        from PyQt5.QtWidgets import QMessageBox

        box = QMessageBox()
        box.setIcon(QMessageBox.Question)
        box.setWindowTitle('Sair?')
        box.setText('Tem certeza que deseja sair?')
        box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        button_sim = box.button(QMessageBox.Yes)
        button_sim.setText('Sim')
        button_nao = box.button(QMessageBox.No)
        button_nao.setText('Não')
        box.exec_()

        if box.clickedButton() == button_sim:
            from Model.Venda_Tmp import Venda_Tmp

            event.accept()

            Venda_Tmp.delete_venda()

            self.kill_thread = True

            if self.saida_operador:
                self.saida_operador = False
                from Controller.login import Login

                Operador.sair_operador()
                logins = Login()
                exec_app(logins)
                self.dialogs.append(logins)
            else:
                sys.exit(1)
        else:
            if self.saida_operador:
                self.saida_operador = False
            event.ignore()

    def resizeEvent(self, event):
        self.resize(self.width, self.height)
        self.ui.frame.move(self.width - 350, self.height - 360)

    def thread_func(self):
        from datetime import datetime
        import time

        while not self.kill_thread:
            data_e_hora_atuais = datetime.now()
            data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M:%S')
            self.ui.lbl_data.setText(data_e_hora_em_texto)
            time.sleep(1)


def exec_main():
    from PyQt5 import QtCore

    translator = QtCore.QTranslator(app)
    locale = QtCore.QLocale.system().name()
    path = QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.TranslationsPath)
    translator.load("qt_%s" % locale, path)
    app.installTranslator(translator)
    form = TelaPrincipal()
    form.showMaximized()
    sys.exit(app.exec_())
