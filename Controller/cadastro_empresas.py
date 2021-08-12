from PyQt5 import QtGui
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow, QInputDialog, QMessageBox, QLineEdit
from psycopg2.extensions import JSON
from Funcoes.APIs import get_empresa_from_cnpj
from Funcoes.utils import retirar_formatacao


class CadastroEmpresas(QMainWindow):
    def __init__(self, parent=None):
        super(CadastroEmpresas, self).__init__(parent)
        from View.cadastro_empresa import Ui_ct_empresa
        from PyQt5 import QtCore
        from Funcoes.utils import IconeBotaoMenu, resource_path

        self.ui = Ui_ct_empresa()
        self.ui.setupUi(self)
        self.dialogs = list()
        self.tamanho = self.size()
        self.setFixedSize(self.tamanho)

        self.setWindowIcon(QtGui.QIcon("Imagens/logo_fzr.png"))

        self.caminho_img = None

        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

        IconeBotaoMenu(self.ui.bt_DelLogo,
                       resource_path('../Imagens/edit-delete.png'))
        IconeBotaoMenu(self.ui.bt_AddLogo,
                       resource_path('../Imagens/edit-add.png'))

        self.ui.tx_NomeFantasia.setMaxLength(100)
        self.ui.tx_RazaoSocial.setMaxLength(40)
        self.ui.tx_EmailEmpresa.setMaxLength(40)
        self.ui.tx_TelefoneEmpresa.setMaxLength(20)
        self.ui.tx_SiteEmpresa.setMaxLength(100)
        self.ui.tx_Endereco.setMaxLength(60)
        self.ui.tx_NumEmpresa.setMaxLength(10)
        self.ui.tx_CidadeEmpresa.setMaxLength(50)
        self.ui.tx_EstadoEmpresa.setMaxLength(2)
        self.ui.tx_BairroEmpresa.setMaxLength(60)

        self.ui.bt_AddLogo.clicked.connect(self.add_img)
        self.ui.bt_DelLogo.clicked.connect(self.del_img)
        self.ui.bt_SalvarDadosEmpresa.clicked.connect(self.validar_campos)
        self.ui.bt_cancelar_2.clicked.connect(self.sair)
        self.ui.tx_CepEmpresa.returnPressed.connect(self.busca_cep)
        self.ui.tx_CepEmpresa.textChanged.connect(self.enable_cidade_estado)
        self.ui.bt_busca_cep.clicked.connect(self.busca_cep)
        self.ui.bt_busca_cnpj.clicked.connect(self.busca_cnpj)

        QTimer.singleShot(1, self.dialog_cnpj)

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        self.setFixedSize(self.tamanho)

    def preenche_campos_cnpj(self, dados: JSON):
        self.ui.tx_Cnpj.setText(retirar_formatacao(dados['cnpj']))
        self.ui.tx_NomeFantasia.setText(dados['fantasia'])
        self.ui.tx_RazaoSocial.setText(dados['nome'])
        self.ui.tx_EmailEmpresa.setText(dados['email'])
        self.ui.tx_TelefoneEmpresa.setText(dados['telefone'])
        self.ui.tx_CepEmpresa.setText(retirar_formatacao(dados['cep']))
        self.ui.tx_CidadeEmpresa.setText(dados['municipio'])
        self.ui.tx_EstadoEmpresa.setText(dados['uf'])
        self.ui.tx_BairroEmpresa.setText(dados['bairro'])
        self.ui.tx_Endereco.setText(dados['logradouro'])
        self.ui.tx_NumEmpresa.setText(dados['numero'])

    def busca_cnpj(self):
        if self.ui.tx_Cnpj.text() != "../-----":
            text = str(retirar_formatacao(self.ui.tx_Cnpj.text())).strip()
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
        from Funcoes.utils import retirar_formatacao

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
        if not self.ui.tx_CidadeEmpresa.isEnabled():
            self.ui.tx_CidadeEmpresa.setEnabled(True)
        elif not self.ui.tx_EstadoEmpresa.isEnabled():
            self.ui.tx_EstadoEmpresa.setEnabled(True)

    def busca_cep(self):
        from Funcoes.APIs import get_endereco
        from PyQt5.QtWidgets import QMessageBox

        if not self.ui.tx_CepEmpresa.text() == '-':
            try:
                endereco = get_endereco(self.ui.tx_CepEmpresa.text())
            except BaseException as e:
                QMessageBox.warning(self, "Erro!", f"{e}")
                self.ui.tx_BairroEmpresa.setText("")
                self.ui.tx_CidadeEmpresa.setText("")
                self.ui.tx_EstadoEmpresa.setText("")
                self.ui.tx_Endereco.setText("")
                self.ui.tx_CepEmpresa.setText("")
            else:
                self.ui.tx_BairroEmpresa.setText("")
                self.ui.tx_CidadeEmpresa.setText("")
                self.ui.tx_EstadoEmpresa.setText("")
                self.ui.tx_Endereco.setText("")

                if endereco['bairro'] is not None:
                    self.ui.tx_BairroEmpresa.setText(endereco['bairro'])
                if endereco['cidade'] is not None:
                    self.ui.tx_CidadeEmpresa.setText(endereco['cidade'])
                    self.ui.tx_CidadeEmpresa.setEnabled(False)
                if endereco['logradouro'] is not None:
                    self.ui.tx_Endereco.setText(endereco['logradouro'])
                if endereco['uf'] is not None:
                    self.ui.tx_EstadoEmpresa.setText(endereco['uf'])
                    self.ui.tx_EstadoEmpresa.setEnabled(False)
        else:
            QMessageBox.warning(self, "Erro!", "Favor informar um CEP.")

    def add_img(self):
        from PyQt5.QtCore import Qt
        from PyQt5.QtWidgets import QFileDialog
        from PyQt5.QtGui import QPixmap

        dialog = QFileDialog()
        dialog.setOption(QFileDialog.DontUseNativeDialog, True)

        fname = dialog.getOpenFileName(
            self, "Selecionar Imagem", "", "Image files (*.jpg *.png)")[0]

        self.ui.lb_LogoEmpresa.setPixmap(QPixmap(fname).scaledToWidth(
            150, Qt.TransformationMode(Qt.FastTransformation)))
        # self.lb_FotoProduto.setScaledContents(True)
        self.ui.bt_AddLogo.setHidden(True)
        self.ui.bt_DelLogo.setVisible(True)

        self.caminho_img = fname

    def del_img(self):
        self.ui.lb_LogoEmpresa.clear()
        self.ui.bt_DelLogo.setHidden(True)
        self.ui.bt_AddLogo.setVisible(True)

    def validar_campos(self):
        if not self.ui.tx_RazaoSocial.text():
            self.ui.tx_RazaoSocial.setFocus()
        if not self.ui.tx_NomeFantasia.text():
            self.ui.tx_NomeFantasia.setFocus()
        elif not self.ui.tx_EmailEmpresa.text():
            self.ui.tx_EmailEmpresa.setFocus()
        elif not self.ui.tx_TelefoneEmpresa.text():
            self.ui.tx_TelefoneEmpresa.setFocus()
        elif not self.ui.tx_EstadoEmpresa.text():
            self.ui.tx_EstadoEmpresa.setFocus()
        elif not self.ui.tx_CidadeEmpresa.text():
            self.ui.tx_CidadeEmpresa.setFocus()
        elif not self.ui.tx_BairroEmpresa.text():
            self.ui.tx_BairroEmpresa.setFocus()
        elif not self.ui.tx_NumEmpresa.text():
            self.ui.tx_NumEmpresa.setFocus()
        elif not self.ui.tx_Endereco.text():
            self.ui.tx_Endereco.setFocus()
        else:
            self.salvar()

    def salvar(self):
        from PyQt5.QtWidgets import QMessageBox
        from Funcoes.utils import retirar_formatacao
        from Model.Empresa import Empresa

        emp_inserir = Empresa()

        emp_inserir.nome_fantasia = self.ui.tx_NomeFantasia.text().upper()
        emp_inserir.razao_social = self.ui.tx_RazaoSocial.text().upper()
        emp_inserir.cnpj = retirar_formatacao(self.ui.tx_Cnpj.text().upper())
        emp_inserir.inscricao_estadual = self.ui.tx_IE.text().upper()
        emp_inserir.fone = self.ui.tx_TelefoneEmpresa.text().lower()
        emp_inserir.site = self.ui.tx_SiteEmpresa.text().upper()
        emp_inserir.email = self.ui.tx_EmailEmpresa.text()
        emp_inserir.cep = self.ui.tx_CepEmpresa.text().upper()
        emp_inserir.rua = self.ui.tx_Endereco.text().upper()
        emp_inserir.nro = self.ui.tx_NumEmpresa.text().upper()
        emp_inserir.bairro = self.ui.tx_BairroEmpresa.text().upper()
        emp_inserir.cidade = self.ui.tx_CidadeEmpresa.text().upper()
        emp_inserir.estado = self.ui.tx_EstadoEmpresa.text().upper()

        try:
            emp_inserir.inserir()

            if self.caminho_img:
                emp_inserir.cnpj = retirar_formatacao(emp_inserir.cnpj)
                emp_inserir.gravar_imagem_empresas(self.caminho_img, "png")

        except Exception as error:
            print(error)
            QMessageBox.about(self, "Erro", str(error))
        else:
            QMessageBox.about(self, "Sucesso", "Cadastro efetuado com sucesso!")

    def sair(self):
        self.close()

    def limpa_campos(self):
        self.ui.tx_Cnpj.setText("")
        self.ui.tx_NomeFantasia.setText("")
        self.ui.tx_RazaoSocial.setText("")
        self.ui.tx_EmailEmpresa.setText("")
        self.ui.tx_TelefoneEmpresa.setText("")
        self.ui.tx_SiteEmpresa.setText("")
        self.ui.tx_CepEmpresa.setText("")
        self.ui.tx_CidadeEmpresa.setText("")
        self.ui.tx_EstadoEmpresa.setText("")
        self.ui.tx_BairroEmpresa.setText("")
        self.ui.tx_Endereco.setText("")
        self.ui.tx_NumEmpresa.setText("")
