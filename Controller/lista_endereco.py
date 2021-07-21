from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from Model.Endereco import Endereco
from PyQt5.QtCore import Qt


class ListaEndereco(QMainWindow):
    def __init__(self, parent=None):
        super(ListaEndereco, self).__init__(parent)
        from View.lista_endereco import Ui_Frame
        from PyQt5 import QtCore

        self.ui = Ui_Frame()
        self.ui.setupUi(self)
        self.dialogs = list()
        self.setFixedSize(self.size())

        self.setWindowModality(QtCore.Qt.ApplicationModal)
        # removendo opção de maximizar
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

        self.end_selecionado = Endereco()
        self.linha_selecionada = None

        # ação dos botoes
        self.ui.bt_cancelar.clicked.connect(self.sair)
        self.ui.bt_salvar.clicked.connect(self.editar)
        self.ui.bt_busca_cep.clicked.connect(self.busca_cep)
        self.ui.tx_cep.returnPressed.connect(self.busca_cep)

        # signals
        self.ui.tb_enderecos.cellClicked.connect(self.linha_clicada)
        self.ui.tx_cep.textChanged.connect(self.enable_cidade_estado)

        self.ui.tx_id.setEnabled(False)
        self.ui.tx_rua.setEnabled(False)
        self.ui.tx_bairro.setEnabled(False)
        self.ui.tx_numero.setEnabled(False)
        self.ui.tx_cep.setEnabled(False)
        self.ui.tx_cidade.setEnabled(False)
        self.ui.tx_estado.setEnabled(False)

        for i in range(0, 7):
            self.ui.tb_enderecos.horizontalHeaderItem(i).setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.ui.tb_enderecos.setColumnWidth(0, 20)
        self.ui.tb_enderecos.setColumnWidth(1, 200)
        self.ui.tb_enderecos.setColumnWidth(2, 200)
        self.ui.tb_enderecos.setColumnWidth(3, 100)
        self.ui.tb_enderecos.setColumnWidth(4, 100)
        self.ui.tb_enderecos.setColumnWidth(5, 30)
        self.ui.tb_enderecos.setColumnWidth(6, 50)

        self.dados_tabela()

    def enable_cidade_estado(self):
        if not self.ui.tx_cidade.isEnabled():
            self.ui.tx_cidade.setEnabled(True)
        elif not self.ui.tx_estado.isEnabled():
            self.ui.tx_estado.setEnabled(True)

    def busca_cep(self):
        from Funcoes.funcoes import get_endereco
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

    def sair(self):
        self.close()

    def linha_clicada(self):
        self.ui.tx_rua.setEnabled(True)
        self.ui.tx_cep.setEnabled(True)
        self.ui.tx_estado.setEnabled(True)
        self.ui.tx_cidade.setEnabled(True)
        self.ui.tx_bairro.setEnabled(True)
        self.ui.tx_estado.setEnabled(True)
        self.ui.tx_numero.setEnabled(True)

        tb = self.ui.tb_enderecos
        self.linha_selecionada = tb.currentRow()

        self.end_selecionado.id = int(tb.item(tb.currentRow(), 0).text())
        c = self.end_selecionado.get_endereco_by_id()
        self.end_selecionado.rua = c[1]
        self.end_selecionado.bairro = c[2]
        self.end_selecionado.numero = c[3]
        self.end_selecionado.cidade = c[4]
        self.end_selecionado.estado = c[5]
        self.end_selecionado.cep = c[6]

        # setando os edits
        self.ui.tx_rua.setText(self.end_selecionado.rua)
        self.ui.tx_bairro.setText(self.end_selecionado.bairro)
        self.ui.tx_numero.setText(self.end_selecionado.numero)
        self.ui.tx_cidade.setText(self.end_selecionado.cidade)
        self.ui.tx_estado.setText(self.end_selecionado.estado)
        self.ui.tx_cep.setText(self.end_selecionado.cep)
        self.ui.tx_id.setText(f'{self.end_selecionado.id}')

    def editar(self):
        if self.end_selecionado.id:
            itens = list()

            end_editar = Endereco()
            end_editar.id = self.ui.tx_id.text()
            itens.append(end_editar.id)
            end_editar.rua = self.ui.tx_rua.text().upper()
            itens.append(end_editar.rua)
            end_editar.bairro = self.ui.tx_bairro.text().upper()
            itens.append(end_editar.bairro)
            end_editar.numero = self.ui.tx_numero.text().upper()
            itens.append(end_editar.numero)
            end_editar.cidade = self.ui.tx_cidade.text().upper()
            itens.append(end_editar.cidade)
            end_editar.estado = self.ui.tx_estado.text().upper()
            itens.append(end_editar.estado)
            end_editar.cep = self.ui.tx_cep.text().upper()
            itens.append(end_editar.cep)



            try:
                end_editar.editar()
            except Exception as error:
                QMessageBox.warning(self, "Erro", str(error))
            else:
                self.ui.tb_enderecos.setFocus()

                for i in range(1, 7):
                    self.ui.tb_enderecos.setItem(self.linha_selecionada, i, QTableWidgetItem(itens[i]))
        else:
            QMessageBox.warning(self, "Atenção!", "Favor selecionar alguma linha!")

    def dados_tabela(self):
        from Model.Operador import Operador
        from Model.Pessoa import Pessoa

        self.ui.tx_id.setText("")
        self.ui.tx_cep.setText("")
        self.ui.tx_rua.setText("")
        self.ui.tx_estado.setText("")
        self.ui.tx_bairro.setText("")
        self.ui.tx_cidade.setText("")
        self.ui.tx_numero.setText("")
        self.ui.tb_enderecos.clearContents()
        self.ui.tb_enderecos.setRowCount(0)

        operador = Operador.get_operador_atual()
        pessoa = Pessoa()
        pessoa.id = operador[0]
        p = pessoa.get_pessoa_usuario_by_id()
        end = Endereco()
        end.id = p[1]
        dados = end.get_endereco_by_id()

        self.ui.tb_enderecos.insertRow(0)

        for c in range(0, 7):
            item_end = str(dados[c])
            self.ui.tb_enderecos.setItem(0, c, QTableWidgetItem(item_end))

