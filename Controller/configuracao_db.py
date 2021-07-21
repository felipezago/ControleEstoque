import sys
import configparser
from PyQt5.QtWidgets import *
from Model.Operador import Operador


class DBConfig(QMainWindow):
    def __init__(self, parent=None):
        super(DBConfig, self).__init__(parent)
        from View import mainDB
        import os
        from PyQt5 import QtCore

        # setar ui
        self.ui = mainDB.Ui_ct_dbConf()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())

        self.setWindowModality(QtCore.Qt.ApplicationModal)

        # Botao Teste banco de Dados
        self.ui.bt_TestarConexao.clicked.connect(self.testar)
        # Botao Salvando Conexao Banco de Dados
        self.ui.bt_SalvarConfigDB.clicked.connect(self.salvar)

        # Inserindo Dados Conexao Banco de Dados Caso exista
        config = configparser.ConfigParser()
        if not config.has_section("POSTGRESQL"):
            config.add_section("POSTGRESQL")
        config.sections()

        self.caminho = os.path.abspath(os.path.dirname(sys.argv[0]))

        if config.read(os.path.join(self.caminho, 'database.ini')):
            try:
                self.ui.tx_IpServer.setText(config['POSTGRESQL']['host'])
            except KeyError:
                config['POSTGRESQL']['host'] = ""
            try:
                self.ui.tx_DbName.setText(config['POSTGRESQL']['database'])
            except KeyError:
                config['POSTGRESQL']['database'] = ""
            try:
                self.ui.tx_DbUser.setText(config['POSTGRESQL']['user'])
            except KeyError:
                config['POSTGRESQL']['user'] = ""
            try:
                self.ui.tx_DbPass.setText(config['POSTGRESQL']['password'])
            except KeyError:
                config['POSTGRESQL']['password'] = ""

        self.dialogs = list()

        self.ui.tx_IpServer.textChanged.connect(self.desabilita_bt)
        self.ui.tx_DbUser.textChanged.connect(self.desabilita_bt)
        self.ui.tx_DbName.textChanged.connect(self.desabilita_bt)
        self.ui.tx_DbPass.textChanged.connect(self.desabilita_bt)

    def desabilita_bt(self):
        self.ui.bt_SalvarConfigDB.setEnabled(False)
        self.ui.lb_StatusTesteDb.clear()
        self.ui.lb_status_db.clear()
        self.ui.lb_status_user.clear()
        self.ui.lb_status_senha.clear()

    def salvar(self):
        import os
        from Funcoes.criar_tabelas import create_tables

        db_host = str(self.ui.tx_IpServer.text())
        db_name = str(self.ui.tx_DbName.text())
        db_user = str(self.ui.tx_DbUser.text())
        db_pass = str(self.ui.tx_DbPass.text())
        config = configparser.ConfigParser()
        config['POSTGRESQL'] = {'host': db_host,
                                'database': db_name,
                                'user': db_user,
                                'password': db_pass}
        path = os.path.abspath(os.path.dirname(sys.argv[0]))
        with open(os.path.join(path, 'database.ini'), 'w') as configfile:
            config.write(configfile)

        if create_tables():

            if Operador.verifica_operador_ativo():
                reply = QMessageBox.question(self, 'Sair?', 'Para que as alterações tenham efeito, deve ser '
                                                            'reiniciado o Sistema. Deseja sair?',
                                                QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

                if reply == QMessageBox.Yes:
                    self.close()
                else:
                    pass
            else:
                from Controller.login import Login
                from Funcoes.funcoes import exec_app

                login = Login()
                exec_app(login)
                self.dialogs.append(login)
                self.close()

    def testar(self):
        from PyQt5.QtGui import QPixmap
        from Funcoes.configdb import ConexaoTeste
        from Funcoes.funcoes import resource_path

        conecta = ConexaoTeste()

        conecta.DbHost = str(self.ui.tx_IpServer.text())
        conecta.DbName = str(self.ui.tx_DbName.text())
        conecta.DbUser = str(self.ui.tx_DbUser.text())
        conecta.DbPassword = str(self.ui.tx_DbPass.text())

        self.ui.lb_status_db.clear()
        self.ui.lb_status_senha.clear()
        self.ui.lb_status_user.clear()

        conecta.conectar()

        if conecta.sucesso:

            self.ui.bt_SalvarConfigDB.setEnabled(True)
            self.ui.lb_StatusTesteDb.setPixmap(
                QPixmap(resource_path('../Imagens/Sucesso.png')))
            self.ui.lb_status_db.setPixmap(
                QPixmap(resource_path('../Imagens/Sucesso.png')))
            self.ui.lb_status_user.setPixmap(
                QPixmap(resource_path('../Imagens/Sucesso.png')))
            self.ui.lb_status_senha.setPixmap(
                QPixmap(resource_path('../Imagens/Sucesso.png')))
            self.ui.lb_StatusTesteDb.setScaledContents(True)
            self.ui.bt_SalvarConfigDB.setEnabled(True)
        else:
            self.ui.bt_SalvarConfigDB.setEnabled(False)
            self.ui.lb_StatusTesteDb.setPixmap(
                QPixmap(resource_path('../Imagens/Fail.png')))
            self.ui.lb_status_db.setPixmap(
                QPixmap(resource_path('../Imagens/Fail.png')))
            self.ui.lb_status_user.setPixmap(
                QPixmap(resource_path('../Imagens/Fail.png')))
            self.ui.lb_status_senha.setPixmap(
                QPixmap(resource_path('../Imagens/Fail.png')))


def exec_conf_db():
    from Funcoes.funcoes import centralizar
    app = QApplication(sys.argv)
    form = DBConfig()
    form.show()
    centralizar(form)
    app.exec_()
