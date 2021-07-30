from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QMainWindow
from Model.Usuario import Usuario
from Model.Pessoa import Pessoa
from PyQt5.QtCore import Qt


class ListaUsuario(QMainWindow):
    def __init__(self, parent=None):
        super(ListaUsuario, self).__init__(parent)
        from View.lista_usuario import Ui_Frame
        from PyQt5 import QtCore

        self.ui = Ui_Frame()
        self.ui.setupUi(self)
        self.dialogs = list()
        self.setFixedSize(self.size())

        self.setWindowModality(QtCore.Qt.ApplicationModal)
        # removendo opção de maximizar
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

        self.usuario_selecionado = Usuario()
        self.linha_selecionada = None

        # ação dos botoes
        self.ui.bt_cancelar.clicked.connect(self.sair)
        self.ui.bt_salvar.clicked.connect(self.validar_campos)

        # signals
        self.ui.tb_usuario.cellClicked.connect(self.linha_clicada)

        self.ui.tx_id.setEnabled(False)
        self.ui.tx_rg.setEnabled(False)
        self.ui.tx_cpf.setEnabled(False)
        self.ui.tx_fone.setEnabled(False)
        self.ui.tx_nome.setEnabled(False)
        self.ui.tx_celular.setEnabled(False)
        self.ui.tx_email.setEnabled(False)

        for c in range(0, 8):
            self.ui.tb_usuario.horizontalHeaderItem(c).setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.ui.tb_usuario.setColumnWidth(0, 20)
        self.ui.tb_usuario.setColumnWidth(1, 100)
        self.ui.tb_usuario.setColumnWidth(2, 200)
        self.ui.tb_usuario.setColumnWidth(3, 150)
        self.ui.tb_usuario.setColumnWidth(4, 200)
        self.ui.tb_usuario.setColumnWidth(5, 100)
        self.ui.tb_usuario.setColumnWidth(6, 150)
        self.ui.tb_usuario.setColumnWidth(7, 100)

        self.dados_tabela()

    def sair(self):
        self.close()

    def linha_clicada(self):
        self.ui.tx_rg.setEnabled(True)
        self.ui.tx_cpf.setEnabled(True)
        self.ui.tx_fone.setEnabled(True)
        self.ui.tx_nome.setEnabled(True)
        self.ui.tx_celular.setEnabled(True)
        self.ui.tx_email.setEnabled(True)

        tb = self.ui.tb_usuario
        self.linha_selecionada = tb.currentRow()

        self.usuario_selecionado.id = int(tb.item(tb.currentRow(), 0).text())
        usu = self.usuario_selecionado.get_usuario_by_id()

        if usu is not None:
            self.usuario_selecionado.cpf = usu[1]
            self.usuario_selecionado.nome = usu[2]
            self.usuario_selecionado.fone = usu[3]
            self.usuario_selecionado.email = usu[4]
            self.usuario_selecionado.rg = usu[5]
            self.usuario_selecionado.celular = usu[6]
            self.usuario_selecionado.login = usu[7]

            # setando os edits
            self.ui.tx_id.setText(str(self.usuario_selecionado.id))
            self.ui.tx_cpf.setText(self.usuario_selecionado.cpf)
            self.ui.tx_nome.setText(self.usuario_selecionado.nome)
            self.ui.tx_fone.setText(self.usuario_selecionado.fone)
            self.ui.tx_email.setText(self.usuario_selecionado.email)
            self.ui.tx_rg.setText(self.usuario_selecionado.rg)
            self.ui.tx_celular.setText(self.usuario_selecionado.celular)
            self.ui.tx_login.setText(self.usuario_selecionado.nome)

    def editar(self):
        from Funcoes.utils import verificar_criptografia

        if self.usuario_selecionado.id:
            itens = list()

            usu_editar = Usuario()
            usu_editar.id = self.ui.tx_id.text()
            itens.append(usu_editar.id)
            usu_editar.cpf = self.ui.tx_cpf.text().upper()
            itens.append(usu_editar.cpf)
            usu_editar.nome = self.ui.tx_nome.text().upper()
            itens.append(usu_editar.nome)
            usu_editar.fone = self.ui.tx_fone.text().upper()
            itens.append(usu_editar.fone)
            usu_editar.email = self.ui.tx_email.text().upper()
            itens.append(usu_editar.email)
            usu_editar.rg = self.ui.tx_rg.text().upper()
            itens.append(usu_editar.rg)
            usu_editar.celular = self.ui.tx_celular.text().upper()
            itens.append(usu_editar.celular)
            usu_editar.nome = self.ui.tx_login.text()
            itens.append(usu_editar.nome)

            if self.ui.tx_senha_antiga:
                senha = str(usu_editar.get_senha_criptografada()[0]).encode()

                if verificar_criptografia(self.ui.tx_senha_antiga.text().encode(), senha):
                    if self.validar_senhas():
                        if self.ui.tx_nova_senha.text() == self.ui.tx_nova_senha_2.text():
                            usu_editar.senha = self.ui.tx_nova_senha.text()
                else:
                    self.ui.tx_senha_antiga.clear()
                    self.ui.tx_senha_antiga.setPlaceholderText("A senha antiga não confere")

            try:
                usu_editar.editar()
            except Exception as error:
                QMessageBox.warning(self, "Erro", str(error))
            else:
                self.ui.tb_usuario.setFocus()
                for c in range(0, 8):
                    self.ui.tb_usuario.setItem(self.linha_selecionada, c, QTableWidgetItem(itens[c]))
        else:
            QMessageBox.warning(self, "Atenção!", "Favor selecionar alguma linha!")

    def dados_tabela(self):
        from Model.Operador import Operador

        self.ui.tx_id.setText("")
        self.ui.tx_rg.setText("")
        self.ui.tx_cpf.setText("")
        self.ui.tx_nome.setText("")
        self.ui.tx_fone.setText("")
        self.ui.tx_nova_senha.setText("")
        self.ui.tx_nova_senha_2.setText("")
        self.ui.tx_senha_antiga.setText("")
        self.ui.tx_login.setText("")
        self.ui.tx_celular.setText("")
        self.ui.tx_email.setText("")

        self.ui.tb_usuario.clearContents()
        self.ui.tb_usuario.setRowCount(0)

        operador = Operador.get_operador_atual()
        usu = Usuario()
        usu.id = operador[0]

        dados_usuario = usu.get_usuario_by_id()

        self.ui.tb_usuario.insertRow(0)

        for i in range(0, 8):
            self.ui.tb_usuario.setItem(0, i, QTableWidgetItem(str(dados_usuario[i])))

    def validar_campos(self):
        if not self.ui.tx_nome.text():
            self.ui.tx_nome.setFocus()
        elif not self.ui.tx_id.text():
            self.ui.tx_id.setFocus()
        elif not self.ui.tx_rg.text():
            self.ui.tx_rg.setFocus()
        elif not self.ui.tx_cpf.text():
            self.ui.tx_cpf.setFocus()
        elif not self.ui.tx_fone.text():
            self.ui.tx_fone.setFocus()
        elif not self.ui.tx_email.text():
            self.ui.tx_email.setFocus()
        elif not self.ui.tx_celular.text():
            self.ui.tx_celular.setFocus()
        elif not self.ui.tx_login.text():
            self.ui.tx_login.setFocus()
        else:
            self.editar()

    def validar_senhas(self):
        if not self.ui.tx_senha_antiga.text():
            self.ui.tx_senha_antiga.setFocus()
            return False
        elif not self.ui.tx_nova_senha.text():
            self.ui.tx_nova_senha.setFocus()
            return False
        elif self.ui.tx_nova_senha_2.text() != self.ui.tx_nova_senha.text():
            self.ui.tx_nova_senha_2.clear()
            self.ui.tx_nova_senha_2.setPlaceholderText("As senhas não conferem")
            self.ui.tx_nova_senha_2.setFocus()
            return False
        return True

