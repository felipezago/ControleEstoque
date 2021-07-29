from PyQt5.QtWidgets import QMainWindow, QMessageBox, QInputDialog, QLineEdit
from psycopg2.extensions import JSON

from Funcoes.APIs import get_empresa_from_cnpj
from Funcoes.funcoes import retirar_formatacao
from Model.Fornecedor import Fornecedor


class CadastroFornecedor(QMainWindow):
    def __init__(self, parent=None):
        super(CadastroFornecedor, self).__init__(parent)
        from View.cadastro_fornecedor import Ui_ct_FormFornecedor
        from PyQt5 import QtCore

        # setando View
        self.ui = Ui_ct_FormFornecedor()
        self.ui.setupUi(self)
        self.setFixedSize(653, 371)

        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

        # ação dos botões
        self.ui.bt_Salvar.clicked.connect(self.valida_campos)
        self.ui.bt_Voltar.clicked.connect(self.fechar)
        self.ui.bt_busca_cep.clicked.connect(self.busca_cep)
        self.ui.tx_Cep.returnPressed.connect(self.busca_cep)
        self.ui.tx_Cep.textChanged.connect(self.enable_cidade_estado)
        self.ui.bt_busca_cnpj.clicked.connect(self.busca_cnpj)

        self.ui.tx_NomeFantasia.setMaxLength(50)
        self.ui.tx_Email.setMaxLength(60)
        self.ui.tx_Endereco.setMaxLength(60)
        self.ui.tx_Numero.setMaxLength(10)
        self.ui.tx_Cidade.setMaxLength(50)
        self.ui.tx_Estado.setMaxLength(2)
        self.ui.tx_Bairro.setMaxLength(60)

    def limpa_campos(self):
        self.ui.tx_cnpj.setText("")
        self.ui.tx_Email.setText("")
        self.ui.tx_Telefone.setText("")
        self.ui.tx_Cep.setText("")
        self.ui.tx_Cidade.setText("")
        self.ui.tx_Estado.setText("")
        self.ui.tx_Bairro.setText("")
        self.ui.tx_Endereco.setText("")
        self.ui.tx_Numero.setText("")

    def preenche_campos_cnpj(self, dados: JSON):
        self.ui.tx_cnpj.setText(retirar_formatacao(dados['cnpj']))
        self.ui.tx_NomeFantasia.setText(dados['fantasia'])
        self.ui.tx_Email.setText(dados['email'])
        self.ui.tx_Telefone.setText(dados['telefone'])
        self.ui.tx_Cep.setText(retirar_formatacao(dados['cep']))
        self.ui.tx_Cidade.setText(dados['municipio'])
        self.ui.tx_Estado.setText(dados['uf'])
        self.ui.tx_Bairro.setText(dados['bairro'])
        self.ui.tx_Endereco.setText(dados['logradouro'])
        self.ui.tx_Numero.setText(dados['numero'])

    def busca_cnpj(self):
        if self.ui.tx_cnpj.text() != "../-----":
            text = str(retirar_formatacao(self.ui.tx_cnpj.text())).strip()
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
        else:
            self.dialog_cnpj()

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

        if not self.ui.tx_Cep.text() == '-':
            try:
                endereco = get_endereco(self.ui.tx_Cep.text())
            except BaseException as e:
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

    def valida_campos(self):
        if not self.ui.tx_NomeFantasia.text():
            self.ui.tx_NomeFantasia.setFocus()
        elif not self.ui.tx_cnpj.text() or self.ui.tx_cnpj.text() == "../----":
            self.ui.tx_cnpj.setFocus()
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
        from Funcoes.funcoes import retirar_formatacao

        forn_inserir = Fornecedor()

        forn_inserir.nome = self.ui.tx_NomeFantasia.text().upper()
        forn_inserir.cnpj = retirar_formatacao(self.ui.tx_cnpj.text().upper())
        forn_inserir.fone = self.ui.tx_Telefone.text().upper()
        forn_inserir.email = self.ui.tx_Email.text().lower()
        forn_inserir.cep = retirar_formatacao(self.ui.tx_Cep.text().upper())
        forn_inserir.rua = self.ui.tx_Endereco.text().upper()
        forn_inserir.numero = self.ui.tx_Numero.text().upper()
        forn_inserir.bairro = self.ui.tx_Bairro.text().upper()
        forn_inserir.cidade = self.ui.tx_Cidade.text().upper()
        forn_inserir.estado = self.ui.tx_Estado.text().upper()

        try:
            forn_inserir.inserir()
        except Exception as error:
            QMessageBox.about(self, "Erro", str(error))
        else:
            QMessageBox.about(self, "Sucesso", "Cadastro efetuado com sucesso!")
            self.fechar()

    def fechar(self):
        self.close()
