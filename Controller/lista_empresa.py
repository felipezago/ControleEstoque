import os

from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QMainWindow
from PyQt5.QtCore import Qt
from Model.Empresa import Empresa
from PyQt5 import QtCore, QtGui
from Funcoes.utils import formatar_cnpj, retirar_formatacao
from PyQt5.QtGui import QPixmap


class EventFilter(QtCore.QObject):

    def __init__(self, parent=None):
        QtCore.QObject.__init__(self, parent)

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.ActivationChange:
            if self.parent().isActiveWindow():
                if obj.adicionando:
                    obj.dados_tabela()

        return QtCore.QObject.eventFilter(self, obj, event)


class ListaEmpresa(QMainWindow):
    def __init__(self, parent=None):
        super(ListaEmpresa, self).__init__(parent)
        from View.lista_empresa import Ui_Frame
        from Funcoes.utils import IconeBotaoMenu, resource_path

        if not os.path.isdir('temp'):
            os.makedirs('temp')

        self.ui = Ui_Frame()
        self.ui.setupUi(self)
        self.dialogs = list()
        self.tamanho = self.size()
        self.setFixedSize(self.tamanho)

        self.setWindowIcon(QtGui.QIcon("Imagens/logo_fzr.png"))

        IconeBotaoMenu(self.ui.bt_DelLogo,
                       resource_path('../Imagens/edit-delete.png'))
        IconeBotaoMenu(self.ui.bt_AddLogo,
                       resource_path('../Imagens/edit-add.png'))

        self.setWindowModality(QtCore.Qt.ApplicationModal)
        # removendo opção de maximizar
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

        self.empresa_selecionada = Empresa()
        self.linha_selecionada = None
        self.adicionando = False
        self.filtrado = False
        self.qtd_empresas = Empresa.qtd_emp()
        self.caminho_img = None

        self.installEventFilter(EventFilter(self))

        # ação dos botoes
        self.ui.bt_cancelar.clicked.connect(self.sair)
        self.ui.bt_salvar.clicked.connect(self.editar)
        self.ui.bt_refresh.clicked.connect(self.dados_tabela)
        self.ui.bt_excluir.clicked.connect(self.excluir)
        self.ui.bt_novo.clicked.connect(self.novo)
        self.ui.bt_AddLogo.clicked.connect(self.add_img)
        self.ui.bt_DelLogo.clicked.connect(self.del_img)

        # ação da busca
        self.ui.bt_busca.clicked.connect(self.buscar)
        self.ui.tx_busca.returnPressed.connect(self.buscar)
        self.ui.tx_cep.returnPressed.connect(self.busca_cep)
        self.ui.bt_busca_cep.clicked.connect(self.busca_cep)

        # signals
        self.ui.tb_empresa.cellClicked.connect(self.linha_clicada)
        self.ui.tx_busca.textChanged.connect(self.formatar_texto)
        self.ui.cb_empresa.currentIndexChanged.connect(self.limpa_campo_busca)
        self.ui.tx_cep.textChanged.connect(self.enable_cidade_estado)

        self.set_tx_enabled(False)
        self.ui.tx_cnpj.setEnabled(False)

        for i in range(0, 13):
            self.ui.tb_empresa.horizontalHeaderItem(i).setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.ui.tb_empresa.setColumnWidth(0, 135)
        self.ui.tb_empresa.setColumnWidth(1, 300)
        self.ui.tb_empresa.setColumnWidth(2, 250)
        self.ui.tb_empresa.setColumnWidth(3, 150)
        self.ui.tb_empresa.setColumnWidth(4, 250)
        self.ui.tb_empresa.setColumnWidth(5, 150)
        self.ui.tb_empresa.setColumnWidth(6, 175)
        self.ui.tb_empresa.setColumnWidth(7, 150)
        self.ui.tb_empresa.setColumnWidth(8, 125)
        self.ui.tb_empresa.setColumnWidth(9, 75)
        self.ui.tb_empresa.setColumnWidth(10, 110)
        self.ui.tb_empresa.setColumnWidth(11, 60)
        self.ui.tb_empresa.setColumnWidth(12, 100)

        self.ui.tx_nome_fantasia.setMaxLength(100)
        self.ui.tx_razao_social.setMaxLength(40)
        self.ui.tx_email.setMaxLength(40)
        self.ui.tx_fone.setMaxLength(20)
        self.ui.tx_site.setMaxLength(100)
        self.ui.tx_rua.setMaxLength(60)
        self.ui.tx_numero.setMaxLength(10)
        self.ui.tx_cidade.setMaxLength(50)
        self.ui.tx_estado.setMaxLength(2)
        self.ui.tx_bairro.setMaxLength(60)
        self.ui.tx_cnpj.setMaxLength(16)

        self.preenche_combo()
        self.dados_tabela()
        self.ui.bt_AddLogo.setEnabled(False)

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        self.setFixedSize(self.tamanho)

    def enable_cidade_estado(self):
        if not self.ui.tx_cidade.isEnabled():
            self.ui.tx_cidade.setEnabled(True)
        elif not self.ui.tx_estado.isEnabled():
            self.ui.tx_estado.setEnabled(True)

    def busca_cep(self):
        from Funcoes.APIs import get_endereco
        from PyQt5.QtWidgets import QMessageBox

        self.ui.tx_cidade.setEnabled(True)
        self.ui.tx_estado.setEnabled(True)

        if not self.ui.tx_cep.text() == '-':
            try:
                endereco = get_endereco(self.ui.tx_cep.text())
            except Exception as e:
                QMessageBox.warning(self, "Erro!", f"{e}")
                self.ui.tx_bairro.setText("")
                self.ui.tx_cidade.setText("")
                self.ui.tx_estado.setText("")
                self.ui.tx_rua.setText("")
                self.ui.tx_cep.setText("")
            else:
                self.ui.tx_bairro.setText("")
                self.ui.tx_cidade.setText("")
                self.ui.tx_estado.setText("")
                self.ui.tx_rua.setText("")

                if endereco['bairro'] is not None:
                    self.ui.tx_bairro.setText(endereco['bairro'])
                if endereco['cidade'] is not None:
                    self.ui.tx_cidade.setText(endereco['cidade'])
                    self.ui.tx_cidade.setEnabled(False)
                if endereco['logradouro'] is not None:
                    self.ui.tx_rua.setText(endereco['logradouro'])
                if endereco['uf'] is not None:
                    self.ui.tx_estado.setText(endereco['uf'])
                    self.ui.tx_estado.setEnabled(False)
        else:
            QMessageBox.warning(self, "Erro!", "Favor informar um CEP.")

    def add_img_padrao(self):

        self.ui.lb_LogoEmpresa.setPixmap(QPixmap("temp/select.png").scaledToWidth(
            150, Qt.TransformationMode(Qt.FastTransformation)))

    def add_img(self):
        from PyQt5.QtCore import Qt
        from PyQt5.QtWidgets import QFileDialog

        dialog = QFileDialog()
        dialog.setOption(QFileDialog.DontUseNativeDialog, True)

        fname = dialog.getOpenFileName(
            self, "Selecionar Imagem", "", "Image files (*.jpg *.png)")[0]

        self.ui.lb_LogoEmpresa.setPixmap(QPixmap(fname).scaledToWidth(
            150, Qt.TransformationMode(Qt.FastTransformation)))
        self.ui.bt_AddLogo.setHidden(True)
        self.ui.bt_DelLogo.setVisible(True)

        self.caminho_img = fname

    def del_img(self):
        if self.ui.lb_LogoEmpresa and self.ui.bt_AddLogo.isHidden():
            self.empresa_selecionada.ler_imagem_empresas(self, "temp/")
        else:
            self.ui.lb_LogoEmpresa.clear()

        self.ui.bt_DelLogo.setHidden(True)
        self.ui.bt_AddLogo.setVisible(True)

    def remove_img(self):
        import os

        dir_img = f"temp/{self.empresa_selecionada.nome_fantasia.replace(' ', '').strip()}.png"

        if os.path.isfile(dir_img):
            os.remove(dir_img)

    def novo(self):
        from Controller.cadastro_empresas import CadastroEmpresas
        from Funcoes.utils import exec_app

        self.adicionando = True
        c = CadastroEmpresas()
        exec_app(c)
        self.dialogs.append(c)

    def limpa_campo_busca(self):
        self.ui.tx_busca.setText("")

    def formatar_texto(self):
        texto = self.ui.tx_busca.text()
        tamanho = len(texto)
        if self.ui.cb_empresa.currentIndex() in (0, 3):
            if not texto[tamanho - 1:tamanho].isnumeric():
                self.ui.tx_busca.setText(texto[:tamanho - 1])

    def preenche_combo(self):
        self.ui.cb_empresa.clear()
        self.ui.cb_empresa.addItem("CNPJ")
        self.ui.cb_empresa.addItem("RAZAO SOCIAL")
        self.ui.cb_empresa.addItem("NOME FANTASIA")
        self.ui.cb_empresa.addItem("INSCRIÇÃO ESTADUAL")

    def sair(self):
        self.close()

    def buscar(self):
        self.ui.tb_empresa.clearContents()
        self.ui.tb_empresa.setRowCount(0)
        self.remove_img()

        emp = Empresa()

        if self.ui.cb_empresa.currentIndex() == 1:
            emp.descricao = self.ui.tx_busca.text()
            if emp.descricao:
                dados = Empresa.get_empresas_by_desc("emp_razaosocial", emp.descricao.upper())
            else:
                QMessageBox.warning(self, "Atenção!", "Favor informar algum valor!")
                self.dados_tabela()
                return
        elif self.ui.cb_empresa.currentIndex() == 0:
            if self.ui.tx_busca.text():
                emp.cnpj = self.ui.tx_busca.text()
                dados = emp.get_empresa_by_cnpj()
            else:
                QMessageBox.warning(self, "Atenção!", "Favor informar algum valor!")
                self.dados_tabela()
                return
        elif self.ui.cb_empresa.currentIndex() == 2:
            emp.descricao = self.ui.tx_busca.text()
            if emp.descricao:
                dados = Empresa.get_empresas_by_desc("emp_nomefantasia", emp.descricao.upper())
            else:
                QMessageBox.warning(self, "Atenção!", "Favor informar algum valor!")
                self.dados_tabela()
                return
        else:
            emp.descricao = self.ui.tx_busca.text()
            if emp.descricao:
                dados = Empresa.get_empresas_by_desc("emp_inscricaoestadual", emp.descricao.upper())
            else:
                QMessageBox.warning(self, "Atenção!", "Favor informar algum valor!")
                self.dados_tabela()
                return

        if dados:
            self.filtrado = True
            self.ui.bt_refresh.setEnabled(True)

            for i, linha in enumerate(dados):
                # empresa
                cnpj = QTableWidgetItem(formatar_cnpj(str(linha[0])))
                self.ui.tb_empresa.insertRow(i)
                self.ui.tb_empresa.setItem(i, 0, cnpj)

                for j in range(1, 13):
                    self.ui.tb_empresa.setItem(i, j, QTableWidgetItem(str(linha[j])))
        else:
            QMessageBox.warning(self, "Erro", "Não foi encontrado nenhum registro!")
            self.ui.tx_busca.setText("")
            self.dados_tabela()

        self.limpa_campos()
        self.remove_img()
        self.ui.tb_empresa.selectRow(0)

    def closeEvent(self, a0):
        self.remove_img()

    def linha_clicada(self):
        self.del_img()
        self.remove_img()
        self.ui.bt_AddLogo.setEnabled(True)
        self.ui.lb_LogoEmpresa.clear()
        self.set_tx_enabled(True)

        tb = self.ui.tb_empresa
        self.linha_selecionada = tb.currentRow()

        self.empresa_selecionada.cnpj = tb.item(tb.currentRow(), 0).text()
        self.empresa_selecionada.cnpj = retirar_formatacao(self.empresa_selecionada.cnpj)
        c = self.empresa_selecionada.get_empresa_by_cnpj_all()

        if c is not None:
            self.empresa_selecionada.razao_social = c[1]
            self.empresa_selecionada.nome_fantasia = c[2]
            self.empresa_selecionada.inscricao_estadual = c[3]
            self.empresa_selecionada.email = c[4]
            self.empresa_selecionada.fone = c[5]
            self.empresa_selecionada.site = c[6]
            self.empresa_selecionada.rua = c[7]
            self.empresa_selecionada.bairro = c[8]
            self.empresa_selecionada.numero = c[9]
            self.empresa_selecionada.cidade = c[10]
            self.empresa_selecionada.estado = c[11]
            self.empresa_selecionada.cep = c[12]

            # setando os edits
            self.ui.tx_cnpj.setText(self.empresa_selecionada.cnpj)
            self.ui.tx_razao_social.setText(self.empresa_selecionada.razao_social)
            self.ui.tx_nome_fantasia.setText(self.empresa_selecionada.nome_fantasia)
            self.ui.tx_inscricao.setText(self.empresa_selecionada.inscricao_estadual)
            self.ui.tx_email.setText(self.empresa_selecionada.email)
            self.ui.tx_fone.setText(self.empresa_selecionada.fone)
            self.ui.tx_site.setText(self.empresa_selecionada.site)
            self.ui.tx_rua.setText(self.empresa_selecionada.rua)
            self.ui.tx_bairro.setText(self.empresa_selecionada.bairro)
            self.ui.tx_numero.setText(self.empresa_selecionada.numero)
            self.ui.tx_cidade.setText(self.empresa_selecionada.cidade)
            self.ui.tx_estado.setText(self.empresa_selecionada.estado)
            self.ui.tx_cep.setText(self.empresa_selecionada.cep)

        if not self.empresa_selecionada.ler_imagem_empresas(self, "temp/"):
            self.add_img_padrao()

    def dados_tabela(self):
        self.empresa_selecionada.cnpj = None
        self.ui.tx_busca.setText("")
        self.filtrado = False
        self.ui.bt_refresh.setEnabled(False)
        self.limpa_campos()
        self.ui.tb_empresa.clearContents()
        self.ui.tb_empresa.setRowCount(0)
        self.ui.bt_refresh.setEnabled(False)

        dados = Empresa.get_todas_empresas_tabela()

        if type(dados) == list:
            for i, linha in enumerate(dados):
                # empresa
                cnpj = QTableWidgetItem(formatar_cnpj(str(linha[0])))
                self.ui.tb_empresa.insertRow(i)
                self.ui.tb_empresa.setItem(i, 0, cnpj)

                for j in range(1, 13):
                    self.ui.tb_empresa.setItem(i, j, QTableWidgetItem(str(linha[j])))

        if self.adicionando:
            self.ui.tb_empresa.selectRow(self.ui.tb_empresa.rowCount() - 1)
            self.adicionando = False

    def editar(self):
        if self.empresa_selecionada.cnpj:
            itens = list()

            emp_editar = Empresa()
            emp_editar.cnpj = retirar_formatacao(self.ui.tx_cnpj.text())
            itens.append(emp_editar.cnpj)
            emp_editar.razao_social = self.ui.tx_razao_social.text().upper()
            itens.append(emp_editar.razao_social)
            emp_editar.nome_fantasia = self.ui.tx_nome_fantasia.text().upper()
            itens.append(emp_editar.nome_fantasia)
            emp_editar.inscricao_estadual = self.ui.tx_inscricao.text()
            itens.append(emp_editar.inscricao_estadual)
            emp_editar.email = self.ui.tx_email.text()
            itens.append(emp_editar.email)
            emp_editar.fone = self.ui.tx_fone.text()
            itens.append(emp_editar.fone)
            emp_editar.site = self.ui.tx_site.text()
            itens.append(emp_editar.site)
            emp_editar.rua = self.ui.tx_rua.text().upper()
            itens.append(emp_editar.rua)
            emp_editar.bairro = self.ui.tx_bairro.text().upper()
            itens.append(emp_editar.bairro)
            emp_editar.numero = self.ui.tx_numero.text().upper()
            itens.append(emp_editar.numero)
            emp_editar.cidade = self.ui.tx_cidade.text().upper()
            itens.append(emp_editar.cidade)
            emp_editar.estado = self.ui.tx_estado.text().upper()
            itens.append(emp_editar.estado)
            emp_editar.cep = retirar_formatacao(self.ui.tx_cep.text())
            itens.append(emp_editar.cep)

            try:
                emp_editar.editar()

                if self.caminho_img:
                    if self.empresa_selecionada.check_imagem() is not None:
                        self.empresa_selecionada.atualizar_imagem(self.caminho_img)
                    else:
                        self.empresa_selecionada.gravar_imagem_empresas(self.caminho_img, "png")
                    self.ui.bt_DelLogo.hide()
                    self.ui.bt_AddLogo.show()
            except Exception as error:
                QMessageBox.warning(self, "Erro", str(error))
            else:
                self.ui.tb_empresa.setFocus()

                for i in range(0, 13):
                    self.ui.tb_empresa.setItem(self.linha_selecionada, i, QTableWidgetItem(itens[i]))

                self.ui.tb_empresa.setItem(self.linha_selecionada, 0, QTableWidgetItem(formatar_cnpj(itens[0])))
        else:
            QMessageBox.warning(self, "Atenção!", "Favor selecionar alguma linha!")

    def excluir(self):
        if self.empresa_selecionada.cnpj:
            reply = QMessageBox.question(self, 'Excluir?', f'Tem certeza que deseja excluir a empresa: '
                                                           f'{self.empresa_selecionada.nome_fantasia}?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

            if reply == QMessageBox.Yes:
                try:
                    self.empresa_selecionada.delete_empresa()
                    self.empresa_selecionada.cnpj = None
                    self.del_img()
                except Exception as error:
                    QMessageBox.warning(self, "Erro", str(error))
                else:
                    self.ui.tb_empresa.removeRow(self.linha_selecionada)
                    self.limpa_campos()
            else:
                return
        else:
            QMessageBox.warning(self, "Atenção!", "Favor selecionar alguma linha!")

    def limpa_campos(self):
        self.ui.tx_cnpj.setText("")
        self.ui.tx_fone.setText("")
        self.ui.tx_email.setText("")
        self.ui.tx_cep.setText("")
        self.ui.tx_rua.setText("")
        self.ui.tx_numero.setText("")
        self.ui.tx_bairro.setText("")
        self.ui.tx_cidade.setText("")
        self.ui.tx_estado.setText("")
        self.ui.tx_inscricao.setText("")
        self.ui.tx_nome_fantasia.setText("")
        self.ui.tx_razao_social.setText("")
        self.ui.tx_site.setText("")
        self.del_img()

    def set_tx_enabled(self, boolean):
        self.ui.tx_cnpj.setEnabled(boolean)
        self.ui.tx_fone.setEnabled(boolean)
        self.ui.tx_email.setEnabled(boolean)
        self.ui.tx_cep.setEnabled(boolean)
        self.ui.tx_rua.setEnabled(boolean)
        self.ui.tx_numero.setEnabled(boolean)
        self.ui.tx_bairro.setEnabled(boolean)
        self.ui.tx_cidade.setEnabled(boolean)
        self.ui.tx_estado.setEnabled(boolean)
        self.ui.tx_inscricao.setEnabled(boolean)
        self.ui.tx_nome_fantasia.setEnabled(boolean)
        self.ui.tx_razao_social.setEnabled(boolean)
        self.ui.tx_site.setEnabled(boolean)
