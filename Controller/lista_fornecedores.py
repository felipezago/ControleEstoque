from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QMainWindow
from PyQt5.QtCore import Qt
from Model.Fornecedor import Fornecedor
from PyQt5 import QtCore
from Funcoes.funcoes import formatar_cnpj, retirar_formatacao


class EventFilter(QtCore.QObject):

    def __init__(self, parent=None):
        QtCore.QObject.__init__(self, parent)

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.ActivationChange:
            if self.parent().isActiveWindow():
                if obj.adicionando:
                    obj.dados_tabela()

        return QtCore.QObject.eventFilter(self, obj, event)


class ListaFornecedor(QMainWindow):
    def __init__(self, parent=None):
        super(ListaFornecedor, self).__init__(parent)
        from View.lista_fornecedores import Ui_Frame

        self.ui = Ui_Frame()
        self.ui.setupUi(self)
        self.dialogs = list()
        self.setFixedSize(self.size())

        self.setWindowModality(QtCore.Qt.ApplicationModal)

        # removendo opção de maximizar
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

        self.fornecedor_selecionado = Fornecedor()
        self.linha_selecionada = None
        self.adicionando = False
        self.filtrado = False
        self.qtd_Fornecedors = Fornecedor.qtd_forn()
        self.caminho_img = None

        self.installEventFilter(EventFilter(self))

        # ação dos botoes
        self.ui.bt_cancelar.clicked.connect(self.sair)
        self.ui.bt_salvar.clicked.connect(self.editar)
        self.ui.bt_refresh.clicked.connect(self.dados_tabela)
        self.ui.bt_excluir.clicked.connect(self.excluir)
        self.ui.bt_novo.clicked.connect(self.novo)

        # ação da busca
        self.ui.bt_busca.clicked.connect(self.buscar)
        self.ui.tx_busca.returnPressed.connect(self.buscar)
        self.ui.tx_cep.returnPressed.connect(self.busca_cep)
        self.ui.bt_busca_cep.clicked.connect(self.busca_cep)

        # signals
        self.ui.tb_fornecedores.cellClicked.connect(self.linha_clicada)
        self.ui.tx_busca.textChanged.connect(self.formatar_texto)
        self.ui.cb_fornecedores.currentIndexChanged.connect(self.limpa_campo_busca)
        self.ui.tx_cep.textChanged.connect(self.enable_cidade_estado)

        self.set_tx_enabled(False)
        self.ui.tx_id.setEnabled(False)

        for i in range(0, 11):
            self.ui.tb_fornecedores.horizontalHeaderItem(i).setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.ui.tb_fornecedores.setColumnWidth(0, 30)
        self.ui.tb_fornecedores.setColumnWidth(1, 300)
        self.ui.tb_fornecedores.setColumnWidth(2, 150)
        self.ui.tb_fornecedores.setColumnWidth(3, 220)
        self.ui.tb_fornecedores.setColumnWidth(4, 150)
        self.ui.tb_fornecedores.setColumnWidth(5, 150)
        self.ui.tb_fornecedores.setColumnWidth(6, 175)
        self.ui.tb_fornecedores.setColumnWidth(7, 150)
        self.ui.tb_fornecedores.setColumnWidth(8, 125)
        self.ui.tb_fornecedores.setColumnWidth(9, 75)
        self.ui.tb_fornecedores.setColumnWidth(10, 110)

        self.ui.tx_nome_fantasia.setMaxLength(50)
        self.ui.tx_email.setMaxLength(40)
        self.ui.tx_fone.setMaxLength(20)
        self.ui.tx_cnpj.setMaxLength(20)
        self.ui.tx_rua.setMaxLength(60)
        self.ui.tx_numero.setMaxLength(10)
        self.ui.tx_cidade.setMaxLength(50)
        self.ui.tx_estado.setMaxLength(2)
        self.ui.tx_bairro.setMaxLength(60)
        self.ui.tx_cnpj.setMaxLength(16)

        self.preenche_combo()
        self.dados_tabela()

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

    def novo(self):
        from Controller.cadastro_fornecedor import CadastroFornecedor
        from Funcoes.funcoes import exec_app

        self.adicionando = True
        c = CadastroFornecedor()
        exec_app(c)
        self.dialogs.append(c)

    def limpa_campo_busca(self):
        self.ui.tx_busca.setText("")

    def formatar_texto(self):
        texto = self.ui.tx_busca.text()
        tamanho = len(texto)
        if self.ui.cb_fornecedores.currentIndex() in (0, 3):
            if not texto[tamanho-1:tamanho].isnumeric():
                self.ui.tx_busca.setText(texto[:tamanho - 1])

    def preenche_combo(self):
        self.ui.cb_fornecedores.clear()
        self.ui.cb_fornecedores.addItem("ID")
        self.ui.cb_fornecedores.addItem("CNPJ")
        self.ui.cb_fornecedores.addItem("NOME FANTASIA")

    def sair(self):
        self.close()

    def buscar(self):
        self.ui.tb_fornecedores.clearContents()
        self.ui.tb_fornecedores.setRowCount(0)

        forn = Fornecedor()

        if self.ui.cb_fornecedores.currentIndex() == 1:
            forn.cnpj = self.ui.tx_busca.text()
            if forn.cnpj:
                dados = Fornecedor.get_fornecedores_by_desc("forn_cnpj", forn.cnpj)
            else:
                QMessageBox.warning(self, "Atenção!", "Favor informar algum valor!")
                self.dados_tabela()
                return
        elif self.ui.cb_fornecedores.currentIndex() == 0:
            if self.ui.tx_busca.text():
                forn.id = int(self.ui.tx_busca.text())
                dados = forn.get_fornecedor_by_id()
            else:
                QMessageBox.warning(self, "Atenção!", "Favor informar algum valor!")
                self.dados_tabela()
                return
        else:
            forn.nome = self.ui.tx_busca.text()
            if forn.nome:
                dados = Fornecedor.get_fornecedores_by_desc("forn_nome", forn.nome.upper())
            else:
                QMessageBox.warning(self, "Atenção!", "Favor informar algum valor!")
                self.dados_tabela()
                return

        if dados:
            self.filtrado = True
            self.ui.bt_refresh.setEnabled(True)

            if isinstance(dados, list):
                for i, linha in enumerate(dados):
                    self.ui.tb_fornecedores.insertRow(i)
                    id_fornecedor = QTableWidgetItem(str(linha[0]))
                    self.ui.tb_fornecedores.setItem(i, 0, id_fornecedor)

                    for j in range(0, 11):
                        if j == 2:
                            self.ui.tb_fornecedores.setItem(i, j, QTableWidgetItem(formatar_cnpj(str(linha[j]))))
                        else:
                            self.ui.tb_fornecedores.setItem(i, j, QTableWidgetItem(str(linha[j])))
            else:
                self.ui.tb_fornecedores.insertRow(0)
                id_fornecedor = QTableWidgetItem(str(dados[0]))
                self.ui.tb_fornecedores.setItem(0, 0, id_fornecedor)

                for j in range(0, 11):
                    if j == 2:
                        self.ui.tb_fornecedores.setItem(0, j, QTableWidgetItem(formatar_cnpj(str(dados[j]))))
                    else:
                        self.ui.tb_fornecedores.setItem(0, j, QTableWidgetItem(str(dados[j])))
        else:
            QMessageBox.warning(self, "Erro", "Não foi encontrado nenhum registro!")
            self.ui.tx_busca.setText("")
            self.dados_tabela()

        self.limpa_campos()
        self.ui.tb_fornecedores.selectRow(0)

    def linha_clicada(self):
        self.set_tx_enabled(True)

        tb = self.ui.tb_fornecedores
        self.linha_selecionada = tb.currentRow()

        self.fornecedor_selecionado.id = tb.item(tb.currentRow(), 0).text()
        c = self.fornecedor_selecionado.get_fornecedor_by_id()

        if c is not None:
            self.fornecedor_selecionado.nome = c[1]
            self.fornecedor_selecionado.cnpj = c[2]
            self.fornecedor_selecionado.email = c[3]
            self.fornecedor_selecionado.fone = c[4]
            self.fornecedor_selecionado.rua = c[5]
            self.fornecedor_selecionado.bairro = c[6]
            self.fornecedor_selecionado.numero = c[7]
            self.fornecedor_selecionado.cidade = c[8]
            self.fornecedor_selecionado.estado = c[9]
            self.fornecedor_selecionado.cep = c[10]

            # setando os edits
            self.ui.tx_cnpj.setText(self.fornecedor_selecionado.cnpj)
            self.ui.tx_nome_fantasia.setText(self.fornecedor_selecionado.nome)
            self.ui.tx_email.setText(self.fornecedor_selecionado.email)
            self.ui.tx_fone.setText(self.fornecedor_selecionado.fone)
            self.ui.tx_id.setText(self.fornecedor_selecionado.id)
            self.ui.tx_rua.setText(self.fornecedor_selecionado.rua)
            self.ui.tx_bairro.setText(self.fornecedor_selecionado.bairro)
            self.ui.tx_numero.setText(self.fornecedor_selecionado.numero)
            self.ui.tx_cidade.setText(self.fornecedor_selecionado.cidade)
            self.ui.tx_estado.setText(self.fornecedor_selecionado.estado)
            self.ui.tx_cep.setText(self.fornecedor_selecionado.cep)

    def dados_tabela(self):
        self.fornecedor_selecionado.id = None
        self.ui.tx_busca.setText("")
        self.filtrado = False
        self.ui.bt_refresh.setEnabled(False)
        self.limpa_campos()
        self.ui.tb_fornecedores.clearContents()
        self.ui.tb_fornecedores.setRowCount(0)
        self.ui.bt_refresh.setEnabled(False)

        dados = Fornecedor.get_todos_fornecedores_tabela()

        for i, linha in enumerate(dados):
            self.ui.tb_fornecedores.insertRow(i)
            for j in range(0, 11):
                if j == 2:
                    self.ui.tb_fornecedores.setItem(i, j, QTableWidgetItem(formatar_cnpj(str(linha[j]))))
                else:
                    self.ui.tb_fornecedores.setItem(i, j, QTableWidgetItem(str(linha[j])))

    def editar(self):
        if self.fornecedor_selecionado.cnpj:
            itens = list()

            forn_editar = Fornecedor()
            forn_editar.id = self.ui.tx_id.text()
            itens.append(forn_editar.id)
            forn_editar.nome = self.ui.tx_nome_fantasia.text().upper()
            itens.append(forn_editar.nome)
            forn_editar.cnpj = retirar_formatacao(self.ui.tx_cnpj.text())
            itens.append(forn_editar.cnpj)
            forn_editar.email = self.ui.tx_email.text()
            itens.append(forn_editar.email)
            forn_editar.fone = self.ui.tx_fone.text()
            itens.append(forn_editar.fone)
            forn_editar.rua = self.ui.tx_rua.text().upper()
            itens.append(forn_editar.rua)
            forn_editar.bairro = self.ui.tx_bairro.text().upper()
            itens.append(forn_editar.bairro)
            forn_editar.numero = self.ui.tx_numero.text().upper()
            itens.append(forn_editar.numero)
            forn_editar.cidade = self.ui.tx_cidade.text().upper()
            itens.append(forn_editar.cidade)
            forn_editar.estado = self.ui.tx_estado.text().upper()
            itens.append(forn_editar.estado)
            forn_editar.cep = retirar_formatacao(self.ui.tx_cep.text())
            itens.append(forn_editar.cep)

            try:
                forn_editar.editar()
            except Exception as error:
                QMessageBox.warning(self, "Erro", str(error))
            else:
                self.ui.tb_fornecedores.setFocus()
                for i in range(0, 11):
                    if i == 2:
                        self.ui.tb_fornecedores.setItem(self.linha_selecionada, 2,
                                                        QTableWidgetItem(formatar_cnpj(itens[2])))
                    else:
                        self.ui.tb_fornecedores.setItem(self.linha_selecionada, i, QTableWidgetItem(itens[i]))

        else:
            QMessageBox.warning(self, "Atenção!", "Favor selecionar alguma linha!")

    def excluir(self):
        if self.fornecedor_selecionado.id:
            reply = QMessageBox.question(self, 'Excluir?', f'Tem certeza que deseja excluir o Fornecedor: '
                                                           f'{self.fornecedor_selecionado.nome}?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

            if reply == QMessageBox.Yes:
                try:
                    self.fornecedor_selecionado.delete_fornecedor_by_id()
                    self.fornecedor_selecionado.id = None
                except Exception as error:
                    QMessageBox.warning(self, "Erro", str(error))
                else:
                    self.ui.tb_fornecedores.removeRow(self.linha_selecionada)
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
        self.ui.tx_id.setText("")
        self.ui.tx_nome_fantasia.setText("")
        self.ui.tx_cnpj.setText("")

    def set_tx_enabled(self, boolean):
        self.ui.tx_fone.setEnabled(boolean)
        self.ui.tx_email.setEnabled(boolean)
        self.ui.tx_cep.setEnabled(boolean)
        self.ui.tx_rua.setEnabled(boolean)
        self.ui.tx_numero.setEnabled(boolean)
        self.ui.tx_bairro.setEnabled(boolean)
        self.ui.tx_cidade.setEnabled(boolean)
        self.ui.tx_estado.setEnabled(boolean)
        self.ui.tx_nome_fantasia.setEnabled(boolean)
        self.ui.tx_cnpj.setEnabled(boolean)
