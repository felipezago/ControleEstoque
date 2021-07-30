def cadastro_categoria(self, ct_FormProdutos):
    ct_FormProdutos.setTabOrder(self.tx_desc_cat, self.tx_PorcentagemVarejo)


def cadastro_produtos(self, ct_FormProdutos):
    ct_FormProdutos.setTabOrder(self.tx_DescricaoProduto, self.tx_codbarras)
    ct_FormProdutos.setTabOrder(self.tx_codbarras, self.cb_forn)
    ct_FormProdutos.setTabOrder(self.cb_forn, self.cb_CategoriaProduto)
    ct_FormProdutos.setTabOrder(self.cb_CategoriaProduto, self.tx_marca)
    ct_FormProdutos.setTabOrder(self.tx_marca, self.tx_EstoqueMaximoProduto)
    ct_FormProdutos.setTabOrder(self.tx_EstoqueMaximoProduto, self.tx_ValorUnitarioProduto)
    ct_FormProdutos.setTabOrder(self.tx_ValorUnitarioProduto, self.bt_SalvarProdutos)
    ct_FormProdutos.setTabOrder(self.tx_idProduto, self.tx_DescricaoProduto)


def cadastro_veiculo(self, ct_FormVeiculos):
    ct_FormVeiculos.setTabOrder(self.tx_placa, self.tx_modelo)
    ct_FormVeiculos.setTabOrder(self.tx_modelo, self.tx_marca)
    ct_FormVeiculos.setTabOrder(self.tx_marca, self.cb_cliente)
