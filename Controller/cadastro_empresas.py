from PyQt5.QtWidgets import QMainWindow


class CadastroEmpresas(QMainWindow):
    def __init__(self):
        super(CadastroEmpresas, self).__init__()
        from View.cadastro_empresa import Ui_ct_empresa
        from PyQt5 import QtCore
        from Funcoes.funcoes import IconeBotaoMenu, resource_path

        self.ui = Ui_ct_empresa()
        self.ui.setupUi(self)
        self.dialogs = list()
        self.setFixedSize(1000, 445)

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

    def enable_cidade_estado(self):
        if not self.ui.tx_CidadeEmpresa.isEnabled():
            self.ui.tx_CidadeEmpresa.setEnabled(True)
        elif not self.ui.tx_EstadoEmpresa.isEnabled():
            self.ui.tx_EstadoEmpresa.setEnabled(True)

    def busca_cep(self):
        from Funcoes.funcoes import get_endereco
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
        from Model.Operador import Operador
        from Funcoes.funcoes import formatar_cpf_rg
        from Funcoes.configdb import Banco
        from Model.Usuario import Usuario
        from Model.Empresa import Empresa
        from Model.Pessoa import Pessoa
        import psycopg2

        # campos empresa
        nome_fantasia = self.ui.tx_NomeFantasia.text().upper()
        razao_social = self.ui.tx_RazaoSocial.text().upper()
        cnpj = self.ui.tx_Cnpj.text().upper()
        inscricao = self.ui.tx_IE.text().upper()
        fone = self.ui.tx_TelefoneEmpresa.text().lower()
        site = self.ui.tx_SiteEmpresa.text().upper()
        email = self.ui.tx_EmailEmpresa.text()

        # campos endereço
        cep = self.ui.tx_CepEmpresa.text().upper()
        rua = self.ui.tx_Endereco.text().upper()
        nro = self.ui.tx_NumEmpresa.text().upper()
        bairro = self.ui.tx_BairroEmpresa.text().upper()
        cidade = self.ui.tx_CidadeEmpresa.text().upper()
        estado = self.ui.tx_EstadoEmpresa.text().upper()

        conn = None
        try:
            config = Banco()
            params = config.get_params()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()

            usu_id = Operador.get_operador_atual()[0]
            usuario = Usuario()
            usuario.pessoa = Pessoa()
            usuario.pessoa.id = int(usu_id)
            u = usuario.get_usuario_by_pessoa()

            cur.execute(f"CALL add_empresa(\'{rua}\', \'{bairro}\', \'{nro}\', \'{cidade}\', \'{estado}\', "
                        f"\'{cep}\', \'{formatar_cpf_rg(cnpj)}\', \'{nome_fantasia}\', \'{razao_social}\',"
                        f"\'{inscricao}\', \'{fone}\', \'{site}\', \'{email}\', "
                        f"{u[0]})")
            conn.commit()
            cur.close()

            if self.caminho_img:
                emp = Empresa()
                emp.cnpj = formatar_cpf_rg(cnpj)
                emp.gravar_imagem_empresas(self.caminho_img, "png")

        except Exception as error:
            print(error)
            QMessageBox.about(self, "Erro", str(error))
        else:
            QMessageBox.about(self, "Sucesso", "Cadastro efetuado com sucesso!")

        conn.close()

    def sair(self):
        self.close()
