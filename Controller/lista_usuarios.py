from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QMainWindow

from Model.Empresa import Empresa
from Model.Usuario import Usuario
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui
from Funcoes.utils import formatar_cpf, formatar_rg


class EventFilter(QtCore.QObject):

    def __init__(self, parent=None):
        QtCore.QObject.__init__(self, parent)

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.ActivationChange:
            if self.parent().isActiveWindow():
                if obj.adicionando:
                    obj.dados_tabela()

        return QtCore.QObject.eventFilter(self, obj, event)


class ListaUsuario(QMainWindow):
    def __init__(self, parent=None):
        super(ListaUsuario, self).__init__(parent)
        from View.lista_usuarios import Ui_Frame
        from PyQt5 import QtCore

        self.ui = Ui_Frame()
        self.ui.setupUi(self)
        self.dialogs = list()
        self.tamanho = self.size()
        self.setFixedSize(self.tamanho)

        self.setWindowIcon(QtGui.QIcon("Imagens/logo_fzr.png"))

        self.setWindowModality(QtCore.Qt.ApplicationModal)
        # removendo opção de maximizar
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

        self.usuario_selecionado = Usuario()
        self.linha_selecionada = None
        self.adicionando = False
        self.filtrado = False
        self.qtd_usu = Usuario.qtd_usu()

        self.installEventFilter(EventFilter(self))

        self.ui.bt_cancelar.clicked.connect(self.sair)
        self.ui.bt_salvar.clicked.connect(self.editar)
        self.ui.bt_refresh.clicked.connect(self.dados_tabela)
        self.ui.bt_excluir.clicked.connect(self.excluir)
        self.ui.bt_novo.clicked.connect(self.novo)

        # ação da busca
        self.ui.bt_busca.clicked.connect(self.buscar)
        self.ui.tx_busca.returnPressed.connect(self.buscar)

        # signals
        self.ui.tb_usuario.cellClicked.connect(self.linha_clicada)
        self.ui.tx_busca.textChanged.connect(self.formatar_texto)
        self.ui.cb_opc.currentIndexChanged.connect(self.limpa_campo_busca)

        self.ui.tx_id.setEnabled(False)
        self.ui.tx_rg.setEnabled(False)
        self.ui.tx_cpf.setEnabled(False)
        self.ui.tx_fone.setEnabled(False)
        self.ui.tx_nome.setEnabled(False)
        self.ui.tx_celular.setEnabled(False)
        self.ui.tx_email.setEnabled(False)

        for c in range(0, 10):
            self.ui.tb_usuario.horizontalHeaderItem(c).setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.ui.tb_usuario.setColumnWidth(0, 20)
        self.ui.tb_usuario.setColumnWidth(1, 110)
        self.ui.tb_usuario.setColumnWidth(2, 200)
        self.ui.tb_usuario.setColumnWidth(3, 150)
        self.ui.tb_usuario.setColumnWidth(4, 200)
        self.ui.tb_usuario.setColumnWidth(5, 100)
        self.ui.tb_usuario.setColumnWidth(6, 150)
        self.ui.tb_usuario.setColumnWidth(7, 130)
        self.ui.tb_usuario.setColumnWidth(8, 100)
        self.ui.tb_usuario.setColumnWidth(9, 150)

        self.preenche_combo()
        self.dados_tabela()

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        self.setFixedSize(self.tamanho)

    def novo(self):
        from Controller.cadastro_usuario import CadastroUsuario
        from Funcoes.utils import exec_app

        self.adicionando = True
        c = CadastroUsuario()
        exec_app(c)
        self.dialogs.append(c)

    def limpa_campo_busca(self):
        self.ui.tx_busca.setText("")

    def formatar_texto(self):
        texto = self.ui.tx_busca.text()
        tamanho = len(texto)
        if self.ui.cb_opc.currentIndex() != 1:
            if not texto[tamanho-1:tamanho].isnumeric():
                self.ui.tx_busca.setText(texto[:tamanho - 1])

    def preenche_combo(self):
        self.ui.cb_opc.clear()
        self.ui.cb_opc.addItem("ID")
        self.ui.cb_opc.addItem("NOME")
        self.ui.cb_opc.addItem("CPF")
        self.ui.cb_opc.addItem("RG")

        self.ui.cb_nivel.clear()
        self.ui.cb_nivel.addItem("VENDEDOR")
        self.ui.cb_nivel.addItem("GERENTE")

    def sair(self):
        self.close()

    def preenche_combo_empresas(self):
        self.ui.cb_empresa.clear()
        todas_empresas = Empresa.get_todas_empresas()

        for contador, e in enumerate(todas_empresas):
            self.ui.cb_empresa.addItem(e[2])
            self.ui.cb_empresa.setItemData(contador, e)

    def linha_clicada(self):
        self.ui.tx_rg.setEnabled(True)
        self.ui.tx_cpf.setEnabled(True)
        self.ui.tx_fone.setEnabled(True)
        self.ui.tx_nome.setEnabled(True)
        self.ui.tx_celular.setEnabled(True)
        self.ui.tx_email.setEnabled(True)
        self.preenche_combo_empresas()

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
            self.usuario_selecionado.nivel = usu[8]

            self.usuario_selecionado.empresa = Empresa()
            self.usuario_selecionado.empresa.cnpj = usu[10]
            emp = self.usuario_selecionado.empresa.get_empresa_by_cnpj()

            self.usuario_selecionado.empresa.nome_fantasia = emp[0][2]

            # setando os edits
            self.ui.tx_id.setText(str(self.usuario_selecionado.id))
            self.ui.tx_cpf.setText(self.usuario_selecionado.cpf)
            self.ui.tx_nome.setText(self.usuario_selecionado.nome)
            self.ui.tx_fone.setText(self.usuario_selecionado.fone)
            self.ui.tx_email.setText(self.usuario_selecionado.email)
            self.ui.tx_rg.setText(self.usuario_selecionado.rg)
            self.ui.tx_celular.setText(self.usuario_selecionado.celular)
            self.ui.tx_login.setText(self.usuario_selecionado.login.lower())

            indice_emp = self.ui.cb_empresa.findText(self.usuario_selecionado.empresa.nome_fantasia)
            self.ui.cb_empresa.setCurrentIndex(indice_emp)

            indice_nivel = self.ui.cb_nivel.findText(self.usuario_selecionado.nivel)
            self.ui.cb_nivel.setCurrentIndex(indice_nivel)

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
            usu_editar.email = self.ui.tx_email.text()
            itens.append(usu_editar.email)
            usu_editar.rg = self.ui.tx_rg.text().upper()
            itens.append(usu_editar.rg)
            usu_editar.celular = self.ui.tx_celular.text()
            itens.append(usu_editar.celular)
            usu_editar.login = self.ui.tx_login.text()
            itens.append(usu_editar.login)
            usu_editar.nivel = self.ui.cb_nivel.itemText(self.ui.cb_nivel.currentIndex())
            itens.append(usu_editar.nivel)
            usu_editar.empresa = Empresa()
            index_emp = self.ui.cb_empresa.currentIndex()
            usu_editar.empresa.cnpj = self.ui.cb_empresa.itemData(index_emp)[0]
            usu_editar.empresa.nome_fantasia = self.ui.cb_empresa.itemData(index_emp)[2]
            itens.append(usu_editar.empresa.nome_fantasia)

            if self.ui.tx_senha_antiga:
                senha = str(usu_editar.get_senha_criptografada()[0]).encode()

                if verificar_criptografia(self.ui.tx_senha_antiga.text().encode(), senha):
                    if self.validar_senhas():
                        if self.ui.tx_nova_senha.text() == self.ui.tx_nova_senha_2.text():
                            usu_editar.senha = self.ui.tx_nova_senha.text()
                            self.ui.tx_senha_antiga.setText("")
                            self.ui.tx_nova_senha.setText("")
                            self.ui.tx_nova_senha_2.setText("")
                else:
                    self.ui.tx_senha_antiga.clear()
                    self.ui.tx_senha_antiga.setPlaceholderText("A senha antiga não confere")

            try:
                usu_editar.editar()
            except Exception as error:
                QMessageBox.warning(self, "Erro", str(error))
            else:
                self.ui.tb_usuario.setFocus()
                for c in range(0, 10):
                    if c == 1:
                        self.ui.tb_usuario.setItem(self.linha_selecionada, c,
                                                   QTableWidgetItem(formatar_cpf(str(itens[c]))))
                    elif c == 5:
                        self.ui.tb_usuario.setItem(self.linha_selecionada, c,
                                                   QTableWidgetItem(formatar_rg(str(itens[c]))))
                    else:
                        self.ui.tb_usuario.setItem(self.linha_selecionada, c, QTableWidgetItem(itens[c]))
        else:
            QMessageBox.warning(self, "Atenção!", "Favor selecionar alguma linha!")

    def buscar(self):
        self.ui.tb_usuario.clearContents()
        self.ui.tb_usuario.setRowCount(0)

        usu = Usuario()

        if self.ui.cb_opc.currentIndex() == 1:
            usu.nome = self.ui.tx_busca.text()
            if usu.nome:
                dados = usu.get_usu_by_desc("usu_nome", usu.nome.upper())
            else:
                QMessageBox.warning(self, "Atenção!", "Favor informar algum valor!")
                self.dados_tabela()
                return
        elif self.ui.cb_opc.currentIndex() == 0:
            if self.ui.tx_busca.text():
                usu.id = self.ui.tx_busca.text()
                dados = usu.get_usuario_by_id()
            else:
                QMessageBox.warning(self, "Atenção!", "Favor informar algum valor!")
                self.dados_tabela()
                return
        elif self.ui.cb_opc.currentIndex() == 2:
            usu.cpf = self.ui.tx_busca.text()
            if usu.cpf:
                dados = usu.get_usu_by_desc("usu_cpf", usu.cpf)
            else:
                QMessageBox.warning(self, "Atenção!", "Favor informar algum valor!")
                self.dados_tabela()
                return
        else:
            usu.rg = self.ui.tx_busca.text()
            if usu.rg:
                dados = usu.get_usu_by_desc("usu_rg", usu.rg)
            else:
                QMessageBox.warning(self, "Atenção!", "Favor informar algum valor!")
                self.dados_tabela()
                return

        if dados:
            self.filtrado = True
            self.ui.bt_refresh.setEnabled(True)

            if isinstance(dados, list):
                for i, linha in enumerate(dados):
                    self.ui.tb_usuario.insertRow(i)
                    for j in range(0, 10):
                        if j == 1:
                            self.ui.tb_usuario.setItem(i, j, QTableWidgetItem(formatar_cpf(str(linha[j]))))
                        elif j == 5:
                            self.ui.tb_usuario.setItem(i, j, QTableWidgetItem(formatar_rg(str(linha[j]))))
                        else:
                            self.ui.tb_usuario.setItem(i, j, QTableWidgetItem(str(linha[j])))
            else:
                self.ui.tb_usuario.insertRow(0)
                for j in range(0, 10):
                    if j == 1:
                        self.ui.tb_usuario.setItem(0, j, QTableWidgetItem(formatar_cpf(str(dados[j]))))
                    elif j == 5:
                        self.ui.tb_usuario.setItem(0, j, QTableWidgetItem(formatar_rg(str(dados[j]))))
                    else:
                        self.ui.tb_usuario.setItem(0, j, QTableWidgetItem(str(dados[j])))
        else:
            QMessageBox.warning(self, "Erro", "Não foi encontrado nenhum registro!")
            self.ui.tx_busca.setText("")
            self.dados_tabela()

        self.limpa_campos()
        self.ui.tb_usuario.selectRow(0)

    def dados_tabela(self):
        self.usuario_selecionado.id = None
        self.ui.tx_busca.setText("")
        self.filtrado = False
        self.ui.bt_refresh.setEnabled(False)
        self.limpa_campos()
        self.ui.tb_usuario.clearContents()
        self.ui.tb_usuario.setRowCount(0)
        self.ui.bt_refresh.setEnabled(False)

        dados = Usuario.get_todos_usuarios()

        for i, linha in enumerate(dados):
            self.ui.tb_usuario.insertRow(i)
            for j in range(0, 10):
                if j == 5:
                    self.ui.tb_usuario.setItem(i, 5, QTableWidgetItem(formatar_rg((linha[5]))))
                elif j == 1:
                    self.ui.tb_usuario.setItem(i, j, QTableWidgetItem(formatar_cpf(str(linha[j]))))
                else:
                    self.ui.tb_usuario.setItem(i, j, QTableWidgetItem(str(linha[j])))

        if self.adicionando:
            self.ui.tb_usuario.selectRow(self.ui.tb_usuario.rowCount() - 1)
            self.adicionando = False

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

    def excluir(self):
        if self.usuario_selecionado.id:
            reply = QMessageBox.question(self, 'Excluir?', f'Tem certeza que deseja excluir o usuario: '
                                                           f'{self.usuario_selecionado.nome}?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

            if reply == QMessageBox.Yes:
                try:
                    self.usuario_selecionado.delete_usuario_by_id()
                    self.usuario_selecionado.id = None
                except Exception as error:
                    QMessageBox.warning(self, "Erro", str(error))
                else:
                    self.ui.tb_usuario.removeRow(self.linha_selecionada)
                    self.limpa_campos()
            else:
                return
        else:
            QMessageBox.warning(self, "Atenção!", "Favor selecionar alguma linha!")

    def limpa_campos(self):
        self.ui.tx_id.setText("")
        self.ui.tx_fone.setText("")
        self.ui.tx_email.setText("")
        self.ui.tx_senha_antiga.setText("")
        self.ui.tx_nova_senha.setText("")
        self.ui.tx_nova_senha_2.setText("")
        self.ui.tx_rg.setText("")
        self.ui.tx_cpf.setText("")
        self.ui.tx_nome.setText("")
        self.ui.tx_celular.setText("")
        self.ui.tx_login.setText("")
