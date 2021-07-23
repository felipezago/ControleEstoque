from Funcoes.create_table_pdf import PDF
from Model.Venda_Itens import Vendas
from Model.Venda_Fin import Venda_Fin
from Model.Vendas_Header import Vendas_Header
from Model.Empresa import Empresa
from Model.Cliente import Cliente


class PDF_Venda(PDF):
    def footer(self):
        self.set_y(34)
        self.set_font('helvetica', 'B', 10)
        self.set_fill_color(255, 255, 255)
        self.rect(4, 285, 202, 5)
        self.cell(w=205, h=507, align='C', txt="SEM VALOR FISCAL", border=0)
        self.cell(-30, 520, 'Pagina ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')


def gerar_pdf(venda_id, emp_cnpj, clie_id):
    emp = Empresa()
    emp.cnpj = emp_cnpj
    empresa = emp.get_empresas_pdf()

    v = Vendas()
    v.id_venda = venda_id
    vend = v.select_tb_pdf()
    colunas_venda = ["Código", "Item", "Qtd.", "Vl. Unit.", "Vl. Total", "Desconto", "Total Liq."]
    vend.insert(0, colunas_venda)

    v_fin = Venda_Fin()
    v_fin.venda_id = venda_id
    fins = v_fin.get_fins_venda_pdf()
    colunas_fin = ["Finalizadora", "Valor Pago"]
    fins.insert(0, colunas_fin)

    header = Vendas_Header()
    header.id = venda_id

    header_venda = header.get_venda_pdf()
    print(header_venda)

    c = Cliente()
    c.id = clie_id
    cliente = c.get_cliente_pdf()

    pdf_venda = PDF_Venda(empresa=empresa, cliente=cliente)

    pdf_venda.set_font('helvetica', 'B', 10)
    pdf_venda.text(5, 85, "Venda:")
    pdf_venda.ln(55)
    pdf_venda.create_table(table_data=vend, cell_width=[20, 60, 24, 24, 24, 24, 24], x_start=5)
    pdf_venda.ln(5)
    pdf_venda.set_font('helvetica', 'B', 12)
    pdf_venda.cell(center=True, txt=f"Valor Bruto:     R$    {header_venda[2]}", border=0)
    pdf_venda.ln(5)
    pdf_venda.cell(center=True, txt=f"Descontos:       R$    {header_venda[1]} ", border=0)
    pdf_venda.ln(5)
    pdf_venda.cell(center=True, txt=f"Valor Líquido:  R$    {header_venda[0]}", border=0)
    pdf_venda.ln(5)

    pdf_venda.cell(center=False, txt="Finalização", border=0)
    pdf_venda.ln(5)
    pdf_venda.create_table(table_data=fins, cell_width='uneven', x_start=10)
    pdf_venda.set_font('helvetica', 'B', 10)
    pdf_venda.ln(5)
    pdf_venda.cell(center=False, txt=f"Valor Pago:     R$ {v_fin.valor_pago()}", border=0)
    pdf_venda.ln(5)

    restante = header_venda[0] - v_fin.valor_pago()
    if restante > 0:
        pdf_venda.cell(center=False, txt=f"Restante:        R$ {restante}", border=0)
    else:
        pdf_venda.cell(center=False, txt=f"Troco:        R$ {restante*-1}", border=0)
    pdf_venda.set_auto_page_break(auto=True, margin=15)
    pdf_venda.alias_nb_pages()
    pdf_venda.output("PDF/venda.pdf")


if __name__ == '__main__':
    gerar_pdf(7, '04325195000109', 4)
