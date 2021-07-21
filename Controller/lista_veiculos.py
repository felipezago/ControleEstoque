from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QMainWindow
from PyQt5.QtCore import Qt
from Model.Veiculo import Veiculo
from PyQt5 import QtCore
from Model.Cliente import Cliente
from Model.Pessoa import Pessoa


class EventFilter(QtCore.QObject):

    def __init__(self, parent=None):
        QtCore.QObject.__init__(self, parent)

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.ActivationChange:
            if self.parent().isActiveWindow():
                if obj.adicionando:
                    obj.dados_tabela()

        return QtCore.QObject.eventFilter(self, obj, event)


class ListaVeiculos(QMainWindow):
    def __init__(self, parent=None):
        super(ListaVeiculos, self).__init__(parent)
        from View.lista_veiculos import Ui_Frame

        self.ui = Ui_Frame()
        self.ui.setupUi(self)
        self.dialogs = list()
        self.setFixedSize(self.size())

        self.setWindowModality(QtCore.Qt.ApplicationModal)
        # removendo opção de maximizar
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

        self.veiculo_selecionado = Veiculo()
        self.veiculo_selecionado.pessoa = Pessoa()
        self.linha_selecionada = None
        self.adicionando = False
        self.filtrado = False
        self.qtd_veic = Veiculo.qtd_cli()

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

        # signals
        self.ui.tb_veiculos.cellClicked.connect(self.linha_clicada)
        self.ui.cb_veiculos.currentIndexChanged.connect(self.limpa_campo_busca)

        self.set_tx_enabled(False)

        for i in range(0, 4):
            self.ui.tb_veiculos.horizontalHeaderItem(i).setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.ui.tb_veiculos.setColumnWidth(0, 100)
        self.ui.tb_veiculos.setColumnWidth(1, 150)
        self.ui.tb_veiculos.setColumnWidth(2, 150)
        self.ui.tb_veiculos.setColumnWidth(3, 150)

        self.ui.tx_placa.setMaxLength(15)
        self.ui.tx_marca.setMaxLength(50)
        self.ui.tx_modelo.setMaxLength(60)

        self.preenche_combo()
        self.dados_tabela()

    def novo(self):
        from Controller.cadastro_veiculos import CadastroVeiculos
        from Funcoes.funcoes import exec_app

        self.adicionando = True
        c = CadastroVeiculos()
        exec_app(c)
        self.dialogs.append(c)

    def limpa_campo_busca(self):
        self.ui.tx_busca.setText("")

    def preenche_combo(self):
        self.ui.cb_veiculos.clear()
        self.ui.cb_veiculos.addItem("PLACA")
        self.ui.cb_veiculos.addItem("MARCA")
        self.ui.cb_veiculos.addItem("MODELO")
        self.ui.cb_veiculos.addItem("CLIENTE")

    def sair(self):
        self.close()

    def buscar(self):
        self.ui.cb_cliente.clear()
        self.ui.tb_veiculos.clearContents()
        self.ui.tb_veiculos.setRowCount(0)
        
        veic = Veiculo()
        veic.cliente = Cliente()
        veic.cliente.pessoa = Pessoa()
        dados = ""

        if self.ui.cb_veiculos.currentIndex() == 3:
            veic.cliente.pessoa.nome = self.ui.tx_busca.text().upper()
            if veic.cliente.pessoa.nome:
                dados_pessoa = veic.cliente.pessoa.get_pessoa_by_desc("pess_nome", veic.cliente.pessoa.nome.upper(),
                                                                      'CLIENTE')
                for item in dados_pessoa:
                    veic.cliente.pessoa.id = item[0]
                    cli = veic.cliente.get_cliente_by_pessoa()
                    veic.cliente.id = cli[0]
                    dados = veic.get_veic_by_pessoa()
            else:
                QMessageBox.warning(self, "Atenção!", "Favor informar algum valor!")
                self.dados_tabela()
                return
        elif self.ui.cb_veiculos.currentIndex() == 0:
            veic.placa = self.ui.tx_busca.text().upper()
            if veic.placa:
                dados = veic.get_veic_by_desc("veic_placa", veic.placa)
            else:
                QMessageBox.warning(self, "Atenção!", "Favor informar algum valor!")
                self.dados_tabela()
                return
        elif self.ui.cb_veiculos.currentIndex() == 1:
            veic.marca = self.ui.tx_busca.text().upper()
            if veic.marca:
                dados = veic.get_veic_by_desc("veic_marca", veic.marca)
            else:
                QMessageBox.warning(self, "Atenção!", "Favor informar algum valor!")
                self.dados_tabela()
                return
        else:
            veic.modelo = self.ui.tx_busca.text().upper()
            if veic.modelo:
                dados = veic.get_veic_by_desc("veic_modelo", veic.modelo)
            else:
                QMessageBox.warning(self, "Atenção!", "Favor informar algum valor!")
                self.dados_tabela()
                return

        if dados:
            self.filtrado = True
            self.ui.bt_refresh.setEnabled(True)

            v = Veiculo()
            v.cliente = Cliente()
            v.cliente.pessoa = Pessoa()

            if type(dados) == list:
                for i, linha in enumerate(dados):
                    # clientes
                    v.placa = linha[0]
                    v.cliente.id = linha[1]
                    cliente = v.cliente.get_cliente_by_id()
                    v.cliente.pessoa.id = cliente[1]
                    dados_cliente = v.cliente.pessoa.get_pessoa_cliente_by_id()

                    self.ui.tb_veiculos.insertRow(i)
                    self.ui.tb_veiculos.setItem(i, 0, QTableWidgetItem(str(linha[0])))

                    for j in range(2, 4):
                        item = linha[j]
                        self.ui.tb_veiculos.setItem(i, j - 1, QTableWidgetItem(str(item)))

                    try:
                        clie_nome = QTableWidgetItem(str(dados_cliente[3]))
                    except TypeError:
                        QMessageBox.warning(self, "Erro", "Não foi encontrado nenhum registro!")
                        self.ui.tx_busca.setText("")
                        self.dados_tabela()
                    else:
                        self.ui.tb_veiculos.setItem(i, 3, clie_nome)
            else:
                v.id = dados[0]
                v.cliente.id = dados[1]
                cliente = v.cliente.get_cliente_by_id()
                v.cliente.pessoa.id = cliente[1]
                dados_cliente = v.cliente.pessoa.get_pessoa_cliente_by_id()
                self.ui.tb_veiculos.insertRow(0)

                self.ui.tb_veiculos.setItem(0, 0, QTableWidgetItem(str(dados[0])))

                for j in range(2, 4):
                    item = dados[j]
                    self.ui.tb_veiculos.setItem(0, j - 1, QTableWidgetItem(str(item)))

                try:
                    clie_nome = QTableWidgetItem(str(dados_cliente[3]))
                except TypeError:
                    QMessageBox.warning(self, "Erro", "Não foi encontrado nenhum registro!")
                    self.ui.tx_busca.setText("")
                    self.dados_tabela()
                else:
                    self.ui.tb_veiculos.setItem(0, 3, clie_nome)
        else:
            QMessageBox.warning(self, "Erro", "Não foi encontrado nenhum registro!")
            self.ui.tx_busca.setText("")
            self.dados_tabela()

        self.limpa_campos()
        self.ui.tb_veiculos.selectRow(0)

    def preenche_combo_clientes(self):
        self.ui.cb_cliente.clear()
        todos_clientes = Cliente.get_todos_clientes()

        pessoa = Pessoa()

        for contador, v in enumerate(todos_clientes):
            contador += 1
            pessoa.id = v[1]
            nome_pessoa = pessoa.get_pessoa_cliente_by_id()[3]

            # Descrição da CB
            self.ui.cb_cliente.addItem(nome_pessoa)
            self.ui.cb_cliente.setItemData(contador - 1, v)

    def linha_clicada(self):
        self.set_tx_enabled(True)
        self.preenche_combo_clientes()

        tb = self.ui.tb_veiculos
        self.linha_selecionada = tb.currentRow()

        self.veiculo_selecionado.placa = tb.item(tb.currentRow(), 0).text()
        v = self.veiculo_selecionado.get_veic_by_placa()

        # pessoa
        if v is not None:
            self.veiculo_selecionado.cliente = Cliente()
            self.veiculo_selecionado.cliente.pessoa = Pessoa()
            self.veiculo_selecionado.cliente.id = v[1]
            cli = self.veiculo_selecionado.cliente.get_cliente_by_id()
            self.veiculo_selecionado.cliente.pessoa.id = cli[1]
            pessoa = self.veiculo_selecionado.cliente.pessoa.get_pessoa_cliente_by_id()
            self.veiculo_selecionado.cliente.pessoa.nome = pessoa[3]
            self.veiculo_selecionado.placa = v[0]
            self.veiculo_selecionado.marca = v[2]
            self.veiculo_selecionado.modelo = v[3]

            # setando os edits
            self.ui.tx_placa.setText(self.veiculo_selecionado.placa)
            self.ui.tx_marca.setText(self.veiculo_selecionado.marca)
            self.ui.tx_modelo.setText(self.veiculo_selecionado.modelo)
            indice = self.ui.cb_cliente.findText(self.veiculo_selecionado.cliente.pessoa.nome)
            self.ui.cb_cliente.setCurrentIndex(indice)

    def dados_tabela(self):
        self.ui.cb_cliente.clear()
        self.veiculo_selecionado.placa = None
        self.ui.tx_busca.setText("")
        self.filtrado = False

        self.ui.bt_refresh.setEnabled(False)
        self.limpa_campos()
        self.ui.tb_veiculos.clearContents()
        self.ui.tb_veiculos.setRowCount(0)

        dados = Veiculo.get_todos_veiculos()

        self.ui.bt_refresh.setEnabled(False)

        v = Veiculo()
        v.cliente = Cliente()
        v.cliente.pessoa = Pessoa()

        if type(dados) == list:
            for i, linha in enumerate(dados):
                # clientes
                v.id = linha[0]
                v.cliente.id = linha[1]
                cliente = v.cliente.get_cliente_by_id()
                v.cliente.pessoa.id = cliente[1]
                dados_cliente = v.cliente.pessoa.get_pessoa_cliente_by_id()

                self.ui.tb_veiculos.insertRow(i)
                self.ui.tb_veiculos.setItem(i, 0, QTableWidgetItem(str(linha[0])))

                for j in range(2, 4):
                    item = linha[j]
                    self.ui.tb_veiculos.setItem(i, j - 1, QTableWidgetItem(str(item)))

                try:
                    clie_nome = QTableWidgetItem(str(dados_cliente[3]))
                except TypeError:
                    QMessageBox.warning(self, "Erro", "Não foi encontrado nenhum registro!")
                    self.ui.tx_busca.setText("")
                    self.dados_tabela()
                else:
                    self.ui.tb_veiculos.setItem(i, 3, clie_nome)
        else:
            v.id = dados[0]
            v.cliente.id = dados[1]
            cliente = v.cliente.get_cliente_by_id()
            v.cliente.pessoa.id = cliente[1]
            dados_cliente = v.cliente.pessoa.get_pessoa_cliente_by_id()

            self.ui.tb_veiculos.insertRow(0)
            self.ui.tb_veiculos.setItem(0, 0, QTableWidgetItem(str(dados[0])))

            for j in range(2, 4):
                item = dados[j]
                self.ui.tb_veiculos.setItem(0, j - 1, QTableWidgetItem(str(item)))

            try:
                clie_nome = QTableWidgetItem(str(dados_cliente[3]))
            except TypeError:
                QMessageBox.warning(self, "Erro", "Não foi encontrado nenhum registro!")
                self.ui.tx_busca.setText("")
                self.dados_tabela()
            else:
                self.ui.tb_veiculos.setItem(0, 3, clie_nome)

    def editar(self):
        if self.veiculo_selecionado.placa:
            itens = list()

            veic_editar = Veiculo()
            veic_editar.placa = self.ui.tx_placa.text().upper()
            itens.append(veic_editar.placa)

            veic_editar.marca = self.ui.tx_marca.text().upper()
            itens.append(veic_editar.marca)
            veic_editar.modelo = self.ui.tx_modelo.text().upper()
            itens.append(veic_editar.modelo)

            veic_editar.cliente = Cliente()
            veic_editar.cliente.pessoa = Pessoa()
            indice = self.ui.cb_cliente.currentIndex()
            veic_editar.cliente.id = self.ui.cb_cliente.itemData(indice)[0]
            veic_editar.cliente.pessoa.id = self.ui.cb_cliente.itemData(indice)[1]
            pess_editar = veic_editar.cliente.pessoa.get_pessoa_cliente_by_id()
            clie_nome = pess_editar[3]
            itens.append(clie_nome)

            try:
                veic_editar.editar(self.veiculo_selecionado.placa)
            except Exception as error:
                QMessageBox.warning(self, "Erro", str(error))
            else:
                self.ui.tb_veiculos.setFocus()

                for i in range(0, 4):
                    self.ui.tb_veiculos.setItem(self.linha_selecionada, i, QTableWidgetItem(str(itens[i])))
        else:
            QMessageBox.warning(self, "Atenção!", "Favor selecionar alguma linha!")

    def excluir(self):
        if self.veiculo_selecionado.placa:
            reply = QMessageBox.question(self, 'Excluir?', f'Tem certeza que deseja excluir o veículo '
                                                           f'{self.veiculo_selecionado.modelo} do cliente '
                                                           f'{self.veiculo_selecionado.cliente.pessoa.nome}?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

            if reply == QMessageBox.Yes:
                try:
                    self.veiculo_selecionado.delete_veiculos_by_id()
                    self.veiculo_selecionado.id = None
                    self.ui.cb_cliente.clear()
                except Exception as error:
                    QMessageBox.warning(self, "Erro", str(error))
                else:
                    self.ui.tb_veiculos.removeRow(self.linha_selecionada)
                    self.limpa_campos()
            else:
                return
        else:
            QMessageBox.warning(self, "Atenção!", "Favor selecionar alguma linha!")

    def limpa_campos(self):
        self.ui.tx_placa.setText("")
        self.ui.tx_marca.setText("")
        self.ui.tx_modelo.setText("")
        self.ui.cb_cliente.setCurrentIndex(0)

    def set_tx_enabled(self, boolean):
        self.ui.tx_placa.setEnabled(boolean)
        self.ui.tx_marca.setEnabled(boolean)
        self.ui.tx_modelo.setEnabled(boolean)
        self.ui.cb_cliente.setEnabled(boolean)
