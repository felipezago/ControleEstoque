from PyQt5.QtWidgets import QMainWindow, QInputDialog, QLineEdit, QMessageBox
from psycopg2.extensions import JSON
from Funcoes.APIs import get_empresa_from_cnpj
from Funcoes.funcoes import retirar_formatacao


class CadastroClientes(QMainWindow):
    def __init__(self, parent=None):
        super(CadastroClientes, self).__init__(parent)
        from View.cadastro_cliente import Ui_ct_FormClientes
        from PyQt5 import QtCore

        self.ui = Ui_ct_FormClientes()
        self.ui.setupUi(self)
        self.dialogs = list()
        self.setFixedSize(669, 440)

        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

        self.ui.tx_nome.setMaxLength(60)
        self.ui.tx_Email.setMaxLength(50)
        self.ui.tx_Endereco.setMaxLength(60)
        self.ui.tx_Numero.setMaxLength(10)
        self.ui.tx_Cidade.setMaxLength(50)
        self.ui.tx_Estado.setMaxLength(2)
        self.ui.tx_Bairro.setMaxLength(60)

        self.ui.bt_Voltar.clicked.connect(self.sair)
        self.ui.bt_Salvar.clicked.connect(self.validar_campos)
        self.ui.tx_Cep.returnPressed.connect(self.busca_cep)
        self.ui.bt_busca_cep.clicked.connect(self.busca_cep)
        self.ui.tx_Cep.textChanged.connect(self.enable_cidade_estado)
        self.ui.cb_nivel.currentIndexChanged.connect(self.altera_tipo_cliente)
        self.ui.bt_busca_cnpj.clicked.connect(self.busca_cnpj)

        self.ui.bt_busca_cnpj.hide()

    def limpa_campos(self):
        self.ui.tx_cpf.setText("")
        self.ui.tx_nome.setText("")
        self.ui.tx_Email.setText("")
        self.ui.tx_Telefone.setText("")
        self.ui.tx_Cep.setText("")
        self.ui.tx_Cidade.setText("")
        self.ui.tx_Estado.setText("")
        self.ui.tx_Bairro.setText("")
        self.ui.tx_Endereco.setText("")
        self.ui.tx_Numero.setText("")
        self.ui.tx_rg.setText("")
        self.ui.lb_celular.setText("")

    def altera_tipo_cliente(self):
        if self.ui.cb_nivel.currentIndex() == 0:
            self.limpa_campos()
            self.ui.lb_rg.show()
            self.ui.tx_rg.show()
            self.ui.tx_Celular.show()
            self.ui.lb_celular.show()
            self.ui.lb_nome.setText("NOME")
            self.ui.tx_nome.setPlaceholderText("NOME COMPLETO")
            self.ui.lb_cpfcnpj.setText("CPF")
            self.ui.tx_cpf.setInputMask("###.###.###-##")
            self.ui.bt_busca_cnpj.hide()
        else:
            self.limpa_campos()
            self.ui.lb_rg.hide()
            self.ui.tx_rg.hide()
            self.ui.bt_busca_cnpj.show()
            self.ui.tx_Celular.hide()
            self.ui.lb_celular.hide()
            self.ui.lb_nome.setText("NOME FANTASIA")
            self.ui.tx_nome.setPlaceholderText("NOME FANTASIA")
            self.ui.lb_cpfcnpj.setText("CNPJ")
            self.ui.tx_cpf.setInputMask("##.###.###/####-##")

            self.dialog_cnpj()

    def preenche_campos_cnpj(self, dados: JSON):
        self.ui.tx_cpf.setText(retirar_formatacao(dados['cnpj']))
        self.ui.tx_nome.setText(dados['fantasia'])
        self.ui.tx_Email.setText(dados['email'])
        self.ui.tx_Telefone.setText(dados['telefone'])
        self.ui.tx_Cep.setText(retirar_formatacao(dados['cep']))
        self.ui.tx_Cidade.setText(dados['municipio'])
        self.ui.tx_Estado.setText(dados['uf'])
        self.ui.tx_Bairro.setText(dados['bairro'])
        self.ui.tx_Endereco.setText(dados['logradouro'])
        self.ui.tx_Numero.setText(dados['numero'])

    def busca_cnpj(self):
        text = str(retirar_formatacao(self.ui.tx_cpf.text())).strip()
        response = get_empresa_from_cnpj(text)
        self.limpa_campos()
        if response.status_code == 200:
            dados = response.json()
            if dados['status'] == "OK":
                self.preenche_campos_cnpj(dados)
            elif dados['status'] == "ERRO" and dados['message'] == 'CNPJ inválido':
                QMessageBox.warning(self, "Erro", "CNPJ Inválido.")
            else:
                QMessageBox.warning(self, "Erro", "Erro ao buscar CNPJ.")

        elif response.status_code == 500:
            QMessageBox.warning(self, "Erro", "Erro interno do Servidor.")

    def dialog_cnpj(self):
        from Funcoes.funcoes import retirar_formatacao

        while True:
            text, ok = QInputDialog().getText(self, "CNPJ Online",
                                              "Informe o CNPJ para buscar os dados da empresa: ", QLineEdit.Normal)
            if ok and text:
                text = str(retirar_formatacao(text)).strip()
                response = get_empresa_from_cnpj(text)
                if response.status_code == 200:
                    dados = response.json()
                    if dados['status'] == "OK":
                        self.preenche_campos_cnpj(dados)
                        break
                    elif dados['status'] == "ERRO" and dados['message'] == 'CNPJ inválido':
                        q = QMessageBox.question(self, "Erro", "CNPJ Inválido, Deseja buscar novamente?")

                        if q == QMessageBox.No:
                            break
                    else:
                        q = QMessageBox.question(self, "Erro", "Erro ao buscar CNPJ, Deseja buscar novamente?")

                        if q == QMessageBox.No:
                            break
                elif response.status_code == 500:
                    QMessageBox.warning(self, "Erro", "Erro interno do Servidor.")
            else:
                break

    def enable_cidade_estado(self):
        if not self.ui.tx_Cidade.isEnabled():
            self.ui.tx_Cidade.setEnabled(True)
        elif not self.ui.tx_Estado.isEnabled():
            self.ui.tx_Estado.setEnabled(True)

    def busca_cep(self):
        from Funcoes.APIs import get_endereco
        from PyQt5.QtWidgets import QMessageBox

        self.ui.tx_Cidade.setEnabled(True)
        self.ui.tx_Estado.setEnabled(True)

        if not self.ui.tx_Cep.text() == '-':
            try:
                endereco = get_endereco(self.ui.tx_Cep.text())
            except Exception as e:
                QMessageBox.warning(self, "Erro!", f"{e}")
                self.ui.tx_Bairro.setText("")
                self.ui.tx_Cidade.setText("")
                self.ui.tx_Estado.setText("")
                self.ui.tx_Endereco.setText("")
                self.ui.tx_Cep.setText("")
            else:
                self.ui.tx_Bairro.setText("")
                self.ui.tx_Cidade.setText("")
                self.ui.tx_Estado.setText("")
                self.ui.tx_Endereco.setText("")

                if endereco['bairro'] is not None:
                    self.ui.tx_Bairro.setText(endereco['bairro'])
                if endereco['cidade'] is not None:
                    self.ui.tx_Cidade.setText(endereco['cidade'])
                    self.ui.tx_Cidade.setEnabled(False)
                if endereco['logradouro'] is not None:
                    self.ui.tx_Endereco.setText(endereco['logradouro'])
                if endereco['uf'] is not None:
                    self.ui.tx_Estado.setText(endereco['uf'])
                    self.ui.tx_Estado.setEnabled(False)
        else:
            QMessageBox.warning(self, "Erro!", "Favor informar um CEP.")

    def sair(self):
        self.close()

    def validar_campos(self):
        if not self.ui.tx_nome.text():
            self.ui.tx_nome.setFocus()
        elif not self.ui.tx_Email.text():
            self.ui.tx_Email.setFocus()
        elif not self.ui.tx_Estado.text():
            self.ui.tx_Estado.setFocus()
        elif not self.ui.tx_Cidade.text():
            self.ui.tx_Cidade.setFocus()
        elif not self.ui.tx_Bairro.text():
            self.ui.tx_Bairro.setFocus()
        elif not self.ui.tx_Numero.text():
            self.ui.tx_Numero.setFocus()
        elif not self.ui.tx_Endereco.text():
            self.ui.tx_Endereco.setFocus()
        else:
            self.salvar()

    def salvar(self):
        from PyQt5.QtWidgets import QMessageBox
        from Model.Cliente import Cliente

        cli_inserir = Cliente()
        cli_inserir.nome = self.ui.tx_nome.text().upper()
        cli_inserir.cpf = self.ui.tx_cpf.text().upper()
        cli_inserir.rg = self.ui.tx_rg.text().upper()
        cli_inserir.telefone = self.ui.tx_Telefone.text().upper()
        cli_inserir.email = self.ui.tx_Email.text().lower()
        cli_inserir.celular = self.ui.tx_Celular.text().upper()
        cli_inserir.tipo = "FISICA" if self.ui.cb_nivel.currentIndex() == 0 else "JURIDICA"
        cli_inserir.cep = self.ui.tx_Cep.text().upper()
        cli_inserir.rua = self.ui.tx_Endereco.text().upper()
        cli_inserir.nro = self.ui.tx_Numero.text().upper()
        cli_inserir.bairro = self.ui.tx_Bairro.text().upper()
        cli_inserir.cidade = self.ui.tx_Cidade.text().upper()
        cli_inserir.estado = self.ui.tx_Estado.text().upper()

        try:
            cli_inserir.inserir()
        except Exception as error:
            QMessageBox.about(self, "Erro", str(error))
        else:
            QMessageBox.about(self, "Sucesso", "Cadastro efetuado com sucesso!")

        self.limpa_campos()
