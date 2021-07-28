from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore


class EventFilter(QtCore.QObject):

    def __init__(self, parent=None):
        QtCore.QObject.__init__(self, parent)

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.ActivationChange:
            if self.parent().isActiveWindow():
                if obj.ui.cb_cliente.currentIndex() == 0:
                    obj.preenche_combo()

        return QtCore.QObject.eventFilter(self, obj, event)


class CadastroVeiculos(QMainWindow):
    def __init__(self, parent=None):
        super(CadastroVeiculos, self).__init__(parent)
        from View.cadastro_veiculo import Ui_ct_FormVeiculos
        from Funcoes.funcoes import IconeBotaoMenu, resource_path

        self.ui = Ui_ct_FormVeiculos()
        self.ui.setupUi(self)
        self.dialogs = list()
        self.setFixedSize(562, 283)

        self.tela = parent

        IconeBotaoMenu(self.ui.bt_add_cliente,
                       resource_path('../Imagens/edit-add.png'))

        self.ui.tx_placa.setMaxLength(15)
        self.ui.tx_marca.setMaxLength(50)
        self.ui.tx_modelo.setMaxLength(60)

        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.installEventFilter(EventFilter(self))

        self.ui.bt_salvar.clicked.connect(self.validar_campos)
        self.ui.bt_cancelar.clicked.connect(self.fechar)
        self.ui.bt_add_cliente.clicked.connect(self.cadastro_cliente)

        self.preenche_combo()

    def cadastro_cliente(self):
        from Funcoes.funcoes import exec_app
        from Controller.cadastro_clientes import CadastroClientes

        clie = CadastroClientes()
        exec_app(clie)
        self.dialogs.append(clie)

    def fechar(self):
        self.close()

    def preenche_combo(self):
        from Model.Cliente import Cliente
        from Model.Pessoa import Pessoa

        self.ui.cb_cliente.clear()
        self.ui.cb_cliente.addItem("SELECIONE")
        todos_clientes = Cliente.get_todos_clientes()

        pessoa = Pessoa()

        for contador, v in enumerate(todos_clientes):
            contador += 1
            pessoa.id = v[1]
            nome_pessoa = pessoa.get_pessoa_cliente_by_id()[3]
            # Descrição da CB
            self.ui.cb_cliente.addItem(nome_pessoa)
            self.ui.cb_cliente.setItemData(contador, v)

        if self.tela:
            indice = self.ui.cb_cliente.findText(self.tela.cliente_selecionado.pessoa.nome)
            self.ui.cb_cliente.setCurrentIndex(indice)

    def validar_campos(self):
        if not self.ui.tx_marca.text():
            self.ui.tx_marca.setFocus()
        elif not self.ui.tx_placa.text():
            self.ui.tx_placa.setFocus()
        elif not self.ui.tx_modelo.text():
            self.ui.tx_modelo.setFocus()
        elif self.ui.cb_cliente.currentIndex() == 0:
            self.ui.cb_cliente.setFocus()
        else:
            self.salvar()

    def salvar(self):
        from Model.Veiculo import Veiculo
        from Model.Pessoa import Pessoa
        from PyQt5.QtWidgets import QMessageBox
        from Funcoes.funcoes import retirar_formatacao
        v = Veiculo()
        v.cliente = Pessoa()

        v.placa = retirar_formatacao(self.ui.tx_placa.text().upper())
        v.marca = self.ui.tx_marca.text().upper()
        v.modelo = self.ui.tx_modelo.text().upper()

        indice_cliente = self.ui.cb_cliente.currentIndex()
        v.cliente.id = self.ui.cb_cliente.itemData(indice_cliente)[0]

        try:
            v.inserir_veiculo()

        except Exception as error:
            print(error)
            QMessageBox.about(self, "Erro", str(error))
        else:
            QMessageBox.about(self, "Sucesso", "Cadastro efetuado com sucesso!")
