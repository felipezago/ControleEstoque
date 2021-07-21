def cadastro_empresa(self, ct_empresa):
    ct_empresa.setTabOrder(self.tx_NomeFantasia, self.tx_RazaoSocial)
    ct_empresa.setTabOrder(self.tx_RazaoSocial, self.tx_Cnpj)
    ct_empresa.setTabOrder(self.tx_Cnpj, self.tx_IE)
    ct_empresa.setTabOrder(self.tx_IE, self.tx_TelefoneEmpresa)
    ct_empresa.setTabOrder(self.tx_TelefoneEmpresa, self.tx_SiteEmpresa)
    ct_empresa.setTabOrder(self.tx_SiteEmpresa, self.tx_EmailEmpresa)
    ct_empresa.setTabOrder(self.tx_EmailEmpresa, self.tx_CepEmpresa)
    ct_empresa.setTabOrder(self.tx_CepEmpresa, self.tx_Endereco)
    ct_empresa.setTabOrder(self.tx_Endereco, self.tx_NumEmpresa)
    ct_empresa.setTabOrder(self.tx_NumEmpresa, self.tx_BairroEmpresa)
    ct_empresa.setTabOrder(self.tx_BairroEmpresa, self.tx_CidadeEmpresa)
    ct_empresa.setTabOrder(self.tx_CidadeEmpresa, self.tx_EstadoEmpresa)
    ct_empresa.setTabOrder(self.tx_EstadoEmpresa, self.bt_AddLogo)
    ct_empresa.setTabOrder(self.bt_AddLogo, self.bt_DelLogo)


def cadastro_categoria(self, ct_FormProdutos):
    ct_FormProdutos.setTabOrder(self.tx_desc_cat, self.tx_PorcentagemVarejo)


def cadastro_clientes(self, ct_FormClientes):
    ct_FormClientes.setTabOrder(self.tx_Id, self.tx_nome)
    ct_FormClientes.setTabOrder(self.tx_nome, self.tx_cpf)
    ct_FormClientes.setTabOrder(self.tx_cpf, self.tx_rg)
    ct_FormClientes.setTabOrder(self.tx_rg, self.tx_Celular)
    ct_FormClientes.setTabOrder(self.tx_Celular, self.tx_Telefone)
    ct_FormClientes.setTabOrder(self.tx_Telefone, self.tx_Email)
    ct_FormClientes.setTabOrder(self.tx_Email, self.tx_Cep)
    ct_FormClientes.setTabOrder(self.tx_Cep, self.tx_Endereco)
    ct_FormClientes.setTabOrder(self.tx_Endereco, self.tx_Numero)
    ct_FormClientes.setTabOrder(self.tx_Numero, self.tx_Bairro)
    ct_FormClientes.setTabOrder(self.tx_Bairro, self.tx_Cidade)
    ct_FormClientes.setTabOrder(self.tx_Cidade, self.tx_Estado)


def cadastro_fornecedor(self, ct_FormFornecedor):
    ct_FormFornecedor.setTabOrder(self.tx_Id, self.tx_NomeFantasia)
    ct_FormFornecedor.setTabOrder(self.tx_NomeFantasia, self.tx_cnpj)
    ct_FormFornecedor.setTabOrder(self.tx_cnpj, self.tx_Telefone)
    ct_FormFornecedor.setTabOrder(self.tx_Telefone, self.tx_Email)
    ct_FormFornecedor.setTabOrder(self.tx_Email, self.tx_Cep)
    ct_FormFornecedor.setTabOrder(self.tx_Cep, self.tx_Endereco)
    ct_FormFornecedor.setTabOrder(self.tx_Endereco, self.tx_Numero)
    ct_FormFornecedor.setTabOrder(self.tx_Numero, self.tx_Bairro)
    ct_FormFornecedor.setTabOrder(self.tx_Bairro, self.tx_Cidade)
    ct_FormFornecedor.setTabOrder(self.tx_Cidade, self.tx_Estado)


def cadastro_produtos(self, ct_FormProdutos):
    ct_FormProdutos.setTabOrder(self.tx_DescricaoProduto, self.tx_codbarras)
    ct_FormProdutos.setTabOrder(self.tx_codbarras, self.cb_forn)
    ct_FormProdutos.setTabOrder(self.cb_forn, self.cb_CategoriaProduto)
    ct_FormProdutos.setTabOrder(self.cb_CategoriaProduto, self.tx_marca)
    ct_FormProdutos.setTabOrder(self.tx_marca, self.tx_EstoqueMaximoProduto)
    ct_FormProdutos.setTabOrder(self.tx_EstoqueMaximoProduto, self.tx_ValorUnitarioProduto)
    ct_FormProdutos.setTabOrder(self.tx_ValorUnitarioProduto, self.bt_SalvarProdutos)
    ct_FormProdutos.setTabOrder(self.tx_idProduto, self.tx_DescricaoProduto)


def cadastro_usuario(self, ct_FormUsuario):
    ct_FormUsuario.setTabOrder(self.tx_nome, self.tx_cpf)
    ct_FormUsuario.setTabOrder(self.tx_cpf, self.tx_rg)
    ct_FormUsuario.setTabOrder(self.tx_rg, self.tx_Celular)
    ct_FormUsuario.setTabOrder(self.tx_Celular, self.tx_Telefone)
    ct_FormUsuario.setTabOrder(self.tx_Telefone, self.tx_Email)
    ct_FormUsuario.setTabOrder(self.tx_Email, self.tx_cep)
    ct_FormUsuario.setTabOrder(self.tx_cep, self.tx_Endereco)
    ct_FormUsuario.setTabOrder(self.tx_Endereco, self.tx_Num)
    ct_FormUsuario.setTabOrder(self.tx_Num, self.tx_Bairro)
    ct_FormUsuario.setTabOrder(self.tx_Bairro, self.tx_Cidade)
    ct_FormUsuario.setTabOrder(self.tx_Cidade, self.tx_Estado)
    ct_FormUsuario.setTabOrder(self.tx_Estado, self.tx_usuario)
    ct_FormUsuario.setTabOrder(self.tx_usuario, self.tx_senha)


def cadastro_veiculo(self, ct_FormVeiculos):
    ct_FormVeiculos.setTabOrder(self.tx_placa, self.tx_modelo)
    ct_FormVeiculos.setTabOrder(self.tx_modelo, self.tx_marca)
    ct_FormVeiculos.setTabOrder(self.tx_marca, self.cb_cliente)


def lista_clientes(self, Frame):
    Frame.setTabOrder(self.tx_cpf, self.tx_nome)
    Frame.setTabOrder(self.tx_nome, self.tx_fone)
    Frame.setTabOrder(self.tx_fone, self.tx_email)
    Frame.setTabOrder(self.tx_email, self.tx_rg)
    Frame.setTabOrder(self.tx_rg, self.tx_celular)
    Frame.setTabOrder(self.tx_celular, self.tx_cep)
    Frame.setTabOrder(self.tx_cep, self.bt_busca_cep)
    Frame.setTabOrder(self.bt_busca_cep, self.tx_bairro)
    Frame.setTabOrder(self.tx_bairro, self.tx_numero)
    Frame.setTabOrder(self.tx_numero, self.tx_cidade)
    Frame.setTabOrder(self.tx_cidade, self.tx_estado)
    Frame.setTabOrder(self.tx_estado, self.tx_rua)
