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
            veic.cliente.nome = self.ui.tx_busca.text().upper()
            if veic.cliente.nome:
                dados_pessoa = veic.cliente.get_cliente_by_desc("clie_nome", veic.cliente.nome.upper())

                if dados_pessoa:
                    if len(dados_pessoa) > 1:
                        cods = list()
                        for item in dados_pessoa:
                            cods.append(item[0])
                        tup = tuple(cods)
                        veic.cliente.id = tup
                        dados = veic.get_veic_by_cliente("in")
                    else:
                        veic.cliente.id = dados_pessoa[0][0]
                        dados = veic.get_veic_by_cliente("=")
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
            print(dados)

            self.filtrado = True
            self.ui.bt_refresh.setEnabled(True)

            for i, linha in enumerate(dados):
                self.ui.tb_veiculos.insertRow(i)

                for j in range(0, len(linha)):
                    self.ui.tb_veiculos.setItem(i, j, QTableWidgetItem(str(linha[j])))
        else:
            QMessageBox.warning(self, "Erro", "Não foi encontrado nenhum registro!")
            self.ui.tx_busca.setText("")
            self.dados_tabela()

        self.limpa_campos()
        self.ui.tb_veiculos.selectRow(0)

    def preenche_combo_clientes(self):
        from Model.Cliente import Cliente

        self.ui.cb_cliente.clear()
        self.ui.cb_cliente.addItem("SELECIONE")

        todos_clientes = Cliente.get_todos_clientes()

        for contador, v in enumerate(todos_clientes):
            contador += 1
            self.ui.cb_cliente.addItem(v[2])
            self.ui.cb_cliente.setItemData(contador, v)

    def linha_clicada(self):
        self.set_tx_enabled(True)
        self.preenche_combo_clientes()

        tb = self.ui.tb_veiculos
        self.linha_selecionada = tb.currentRow()

        self.veiculo_selecionado.placa = tb.item(tb.currentRow(), 0).text()
        v = self.veiculo_selecionado.get_veic_by_placa()

        if v is not None:
            self.veiculo_selecionado.placa = v[0]
            self.veiculo_selecionado.marca = v[1]
            self.veiculo_selecionado.modelo = v[2]
            self.veiculo_selecionado.cliente = Cliente()
            self.veiculo_selecionado.cliente.nome = v[3]

            # setando os edits
            self.ui.tx_placa.setText(self.veiculo_selecionado.placa)
            self.ui.tx_marca.setText(self.veiculo_selecionado.marca)
            self.ui.tx_modelo.setText(self.veiculo_selecionado.modelo)
            indice = self.ui.cb_cliente.findText(self.veiculo_selecionado.cliente.nome)
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
        self.ui.bt_refresh.setEnabled(False)

        dados = Veiculo.get_todos_veiculos()

        if dados:
            for i, linha in enumerate(dados):
                self.ui.tb_veiculos.insertRow(i)

                for j in range(0, len(linha)):
                    self.ui.tb_veiculos.setItem(i, j, QTableWidgetItem(str(linha[j])))
        else:
            QMessageBox.warning(self, "Erro", "Não foi encontrado nenhum registro!")
            self.ui.tx_busca.setText("")
            self.dados_tabela()

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
            indice = self.ui.cb_cliente.currentIndex()
            veic_editar.cliente.id = self.ui.cb_cliente.itemData(indice)[0]
            cli = veic_editar.cliente.get_cliente_by_id()
            veic_editar.cliente.nome = cli[2]
            itens.append(veic_editar.cliente.nome)

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
                                                           f'{self.veiculo_selecionado.cliente.nome}?',
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
