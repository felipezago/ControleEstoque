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
        self.usuario_selecionado.nome = usu[2]
        self.usuario_selecionado.pessoa = Pessoa()
        self.usuario_selecionado.pessoa.id = usu[1]

        pess = self.usuario_selecionado.pessoa.get_pessoa_usuario_by_id()
        self.usuario_selecionado.pessoa.cpf = pess[2]
        self.usuario_selecionado.pessoa.nome = pess[3]
        self.usuario_selecionado.pessoa.fone = pess[4]
        self.usuario_selecionado.pessoa.email = pess[5]
        self.usuario_selecionado.pessoa.rg = pess[6]
        self.usuario_selecionado.pessoa.celular = pess[7]

        # setando os edits
        self.ui.tx_id.setText(str(self.usuario_selecionado.id))
        self.ui.tx_cpf.setText(self.usuario_selecionado.pessoa.cpf)
        self.ui.tx_nome.setText(self.usuario_selecionado.pessoa.nome)
        self.ui.tx_fone.setText(self.usuario_selecionado.pessoa.fone)
        self.ui.tx_email.setText(self.usuario_selecionado.pessoa.email)
        self.ui.tx_rg.setText(self.usuario_selecionado.pessoa.rg)
        self.ui.tx_celular.setText(self.usuario_selecionado.pessoa.celular)
        self.ui.tx_login.setText(self.usuario_selecionado.nome)

    def editar(self):
        from Funcoes.funcoes import verificar_criptografia

        if self.usuario_selecionado.id:
            itens = list()

            usu_editar = Usuario()
            usu_editar.id = self.ui.tx_id.text()
            itens.append(usu_editar.id)
            usu_editar.pessoa = Pessoa()
            usu_editar.pessoa.id = self.usuario_selecionado.get_usuario_by_id()[1]
            usu_editar.pessoa.cpf = self.ui.tx_cpf.text().upper()
            itens.append(usu_editar.pessoa.cpf)
            usu_editar.pessoa.nome = self.ui.tx_nome.text().upper()
            itens.append(usu_editar.pessoa.nome)
            usu_editar.pessoa.fone = self.ui.tx_fone.text().upper()
            itens.append(usu_editar.pessoa.fone)
            usu_editar.pessoa.email = self.ui.tx_email.text().upper()
            itens.append(usu_editar.pessoa.email)
            usu_editar.pessoa.rg = self.ui.tx_rg.text().upper()
            itens.append(usu_editar.pessoa.rg)
            usu_editar.pessoa.celular = self.ui.tx_celular.text().upper()
            itens.append(usu_editar.pessoa.celular)
            usu_editar.nome = self.ui.tx_login.text()
            itens.append(usu_editar.pessoa.nome)

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
                usu_editar.pessoa.editar()
            except Exception as error:
                QMessageBox.warning(self, "Erro", str(error))
            else:
                self.ui.tb_usuario.setFocus()
                for c in range(1, 8):
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
        usu.pessoa = Pessoa()
        usu.pessoa.id = operador[0]

        dados_pessoa = usu.pessoa.get_pessoa_usuario_by_id()
        dados_usuario = usu.get_usuario_by_pessoa()

        self.ui.tb_usuario.insertRow(0)

        # dados usuario
        id_usu = QTableWidgetItem(str(dados_usuario[0]))
        id_usu.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.ui.tb_usuario.setItem(0, 0, id_usu)
        login = QTableWidgetItem(str(dados_usuario[2]))
        login.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.ui.tb_usuario.setItem(0, 7, login)

        # dados  pessoa
        cpf = QTableWidgetItem(dados_pessoa[2])
        cpf.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        nome = QTableWidgetItem(dados_pessoa[3])
        nome.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        fone = QTableWidgetItem(dados_pessoa[4])
        fone.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        email = QTableWidgetItem(dados_pessoa[5])
        email.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        rg = QTableWidgetItem(dados_pessoa[6])
        rg.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        celular = QTableWidgetItem(dados_pessoa[7])
        celular.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        item = list()
        for c in range(2, 8):
            item.append(dados_pessoa[c])

        for i in range(1, 7):
            self.ui.tb_usuario.setItem(0, i, QTableWidgetItem(item[i - 1]))

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

