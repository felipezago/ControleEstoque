from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from Model.Cliente import Cliente
from Model.Operador import Operador
from Model.Usuario import Usuario
from Model.Veiculo import Veiculo
from Model.Venda_Fin import Venda_Fin
from Model.Venda_Itens import Vendas
from Model.Vendas_Header import Vendas_Header
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt


class DetalhesVenda(QMainWindow):
    def __init__(self, parent=None, cod_venda=""):
        super(DetalhesVenda, self).__init__(parent)
        from View.detalhes_venda import Ui_Frame

        self.ui = Ui_Frame()
        self.ui.setupUi(self)
        self.dialogs = list()
        self.tamanho_tela = self.size()
        self.setFixedSize(self.tamanho_tela)

        self.setWindowIcon(QtGui.QIcon("Imagens/logo_fzr.png"))

        self.setWindowModality(QtCore.Qt.ApplicationModal)

        self.venda_selecionada = Vendas_Header()
        self.venda_selecionada.id = cod_venda
        self.venda_selecionada.veiculo = Veiculo()
        self.venda_selecionada.cliente = Cliente()

        placa = self.venda_selecionada.retorna_placa_veiculo()
        cod_cli = self.venda_selecionada.retorna_cod_cliente()

        if placa != 0:
            self.venda_selecionada.veiculo.placa = placa
            veic = self.venda_selecionada.veiculo.get_veic_by_placa()
            self.venda_selecionada.veiculo.marca = veic[1]
            self.venda_selecionada.veiculo.modelo = veic[2]

        self.venda_selecionada.cliente.id = cod_cli
        cli = self.venda_selecionada.cliente.get_cliente_by_id()
        self.venda_selecionada.cliente.nome = cli[2]

        datahora = self.venda_selecionada.retorna_hora()
        data_e_hora_em_texto = datahora.strftime('%d/%m/%Y %H:%M:%S')
        self.venda_selecionada.datahora = data_e_hora_em_texto

        self.tela = parent

        self.ui.bt_cancelar.clicked.connect(self.sair)
        self.ui.bt_excluir.clicked.connect(self.excluir)
        self.ui.bt_imprimir.clicked.connect(self.imprimir)

        self.ui.tb_itens.setColumnWidth(0, 20)
        self.ui.tb_itens.setColumnWidth(1, 200)
        self.ui.tb_itens.setColumnWidth(2, 50)
        self.ui.tb_itens.setColumnWidth(3, 100)
        self.ui.tb_itens.setColumnWidth(4, 135)
        self.ui.tb_itens.setColumnWidth(5, 100)

        self.ui.tb_fin.setColumnWidth(0, 200)
        self.ui.tb_fin.setColumnWidth(1, 110)

        for c in range(0, 6):
            self.ui.tb_itens.horizontalHeaderItem(c).setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        for c in range(0, 2):
            self.ui.tb_fin.horizontalHeaderItem(c).setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.dados_tabela_itens()
        self.dados_tabela_fin()
        self.set_lbl()

    def imprimir(self):
        reply = QMessageBox.question(self, 'Imprimir?', f'Deseja imprimir o relatório da venda?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

        if reply == QMessageBox.Yes:
            from Funcoes.utils import print_dialog
            from Funcoes.PDF.pdf_venda import gerar_pdf

            usuario_operador = Usuario()
            usuario_operador.id = Operador.get_operador_atual()[0]
            usu = usuario_operador.get_usuario_by_id()
            cnpj = usu[10]

            gerar_pdf(self.venda_selecionada.id, cnpj, self.venda_selecionada.cliente.id)
            print_dialog(self, f"venda.pdf")

        self.close()

    def set_lbl(self):
        self.ui.lb_venda.setText(f"Venda - Código {self.venda_selecionada.id}")
        self.ui.lb_hora.setText(f"{self.venda_selecionada.datahora}")
        if self.venda_selecionada.veiculo.placa:
            self.ui.lb_veiculo.setText(f"{self.venda_selecionada.veiculo.marca} - "
                                       f"{self.venda_selecionada.veiculo.modelo}")
        else:
            self.ui.lb_veiculo.setText(f"SEM VEÍCULO")
        self.ui.lb_cliente.setText(f"{self.venda_selecionada.cliente.nome}")
        v = Vendas()
        v.id_venda = self.venda_selecionada.id
        self.ui.lb_total_itens.setText(f"R$ {v.retorna_total()}")
        self.ui.lb_total_descontos.setText(f"R$ {v.retorna_total_descontos()}")
        self.ui.lb_total_liquido.setText(f"R$ {v.retorna_total() - v.retorna_total_descontos()}")

    def resizeEvent(self, a0: QtGui.QResizeEvent):
        self.resize(self.tamanho_tela)

    def sair(self):
        self.close()

    def dados_tabela_itens(self):
        self.ui.tb_itens.clearContents()
        self.ui.tb_itens.setRowCount(0)

        itens = Vendas()
        itens.id_venda = self.venda_selecionada.id
        dados = itens.detalhes_venda()

        for i, linha in enumerate(dados):

            self.ui.tb_itens.insertRow(i)
            for c in range(0, 6):
                self.ui.tb_itens.setItem(i, c, QTableWidgetItem(str(linha[c])))

    def dados_tabela_fin(self):
        self.ui.tb_fin.clearContents()
        self.ui.tb_fin.setRowCount(0)

        v_fin = Venda_Fin()
        v_fin.venda_id = self.venda_selecionada.id

        dados = v_fin.get_fins_venda_pdf()

        for i, linha in enumerate(dados):

            self.ui.tb_fin.insertRow(i)
            for c in range(0, 2):
                self.ui.tb_fin.setItem(i, c, QTableWidgetItem(str(linha[c])))

    def excluir(self):

        reply = QMessageBox.question(self, 'Excluir?', f'Tem certeza que deseja excluir a venda: '
                                                       f'{self.venda_selecionada.id}?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

        if reply == QMessageBox.Yes:
            try:
                self.venda_selecionada.delete_venda()
                self.venda_selecionada.id = None
            except Exception as error:
                QMessageBox.warning(self, "Erro", str(error))
            else:
                QMessageBox.information(self, "Sucesso!", "Venda excluída com sucesso!")
                from Controller.lista_vendas import ListaVendas
                from Funcoes.utils import exec_app

                lista_v = ListaVendas()
                exec_app(lista_v)
                self.dialogs.append(lista_v)

                self.close()
        else:
            return
