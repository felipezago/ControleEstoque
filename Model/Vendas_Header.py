from Funcoes.banco import conexao
from Model.Veiculo import Veiculo
from Model.Cliente import Cliente


class Vendas_Header:
    def __init__(self, id_venda="", cliente: Cliente = "", veiculo: Veiculo = "", qtd_itens="", total_descontos="",
                 valor_total="", status=""):
        self.id = id_venda
        self.veiculo = veiculo
        self.cliente = cliente
        self.qtd_itens = qtd_itens
        self.total_descontos = total_descontos
        self.valor_total = valor_total
        self.status = status

    def inserir(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"INSERT INTO vendas (venda_id, venda_veic_placa, venda_clie_id, venda_qtd_itens,"
                    f" venda_total_descontos, venda_valor_total, venda_status) VALUES ({self.id}, "
                    f"\'{self.veiculo.placa if self.veiculo.placa else 'null'}\', \'{self.cliente.id}\', "
                    f"{self.qtd_itens}, {self.total_descontos}, "
                    f"{self.valor_total}, \'{self.status}\')")
        conn.commit()
        cur.close()
        conn.close()

    def delete(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"DELETE FROM vendas WHERE venda_id = {self.id})")
        conn.commit()
        cur.close()
        conn.close()

    def get_venda_pdf(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"SELECT ROUND(venda_valor_total::numeric, 2), ROUND(venda_total_descontos::numeric, 2), "
                    f"ROUND((venda_valor_total + venda_total_descontos)::numeric, 2) "
                    f"FROM vendas"
                    f" WHERE venda_id = {self.id}")
        row = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()

        return row

    @staticmethod
    def get_vendas():
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"""
            SELECT venda_id, clie_nome, veic_modelo, venda_qtd_itens, ROUND(venda_total_descontos::numeric, 2), ROUND(venda_valor_total::numeric, 2), venda_status
            FROM vendas
            INNER join cliente ON venda_clie_id = clie_id
            INNER JOIN veiculo ON veic_placa = venda_veic_placa
            ORDER BY venda_id
        """)
        row = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()

        return row

    def get_vendas_by_id(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"""
            SELECT * FROM vendas
            WHERE venda_id = {self.id}
            ORDER BY venda_id
        """)
        row = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()

        return row

    def update(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"""
           UPDATE vendas
            SET venda_clie_id = {self.cliente.id},
            venda_veic_placa = \'{self.veiculo.placa}\',
            venda_qtd_itens = {self.qtd_itens},
            venda_total_descontos = {self.total_descontos},
            venda_valor_total = {self.valor_total},
            venda_status = \'{self.status}\'
            WHERE venda_id = {self.id}
        """)
        conn.commit()
        cur.close()
        conn.close()

