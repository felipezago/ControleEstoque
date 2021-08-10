from Funcoes.banco import conexao
from Model.Veiculo import Veiculo
from Model.Vendas_Header import Vendas_Header
from Model.Cliente import Cliente


class Pendencias:
    def __init__(self, pend_id="", cliente: Cliente = "", venda: Vendas_Header = "", veiculo: Veiculo = "",
                 datahora="", valor=""):
        self.id = pend_id
        self.cliente = cliente
        self.venda = venda
        self.veiculo = veiculo
        self.datahora = datahora
        self.valor = valor

    def update(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"""
                   UPDATE pendencias
                    SET pend_clie_id = {self.cliente.id},
                    pend_veic_placa = \'{self.veiculo.placa}\',
                    pend_valor = {self.valor}
                    WHERE pend_venda_id = {self.venda.id}
                """)
        conn.commit()
        cur.close()
        conn.close()

    def inserir(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(
            f"INSERT INTO pendencias (pend_clie_id, pend_venda_id, pend_veic_placa, pend_datahora, pend_valor) "
            f"VALUES "
            f"({self.cliente.id}, {self.venda.id}, \'{self.veiculo.placa if self.veiculo.placa else 'null'}\', "
            f"\'{self.datahora}\', {self.valor})")
        conn.commit()
        cur.close()
        conn.close()

    def delete(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"DELETE FROM pendencias WHERE pend_venda_id = {self.venda.id}")
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def todas_pendencias():
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"SELECT pend_id, pend_venda_id, clie_nome, ROUND(pend_valor::numeric, 2) FROM pendencias "
                    f"INNER JOIN cliente ON clie_id = pend_clie_id")
        row = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()

        return row

    def busca_pendencias_by_cliente(self, op):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"SELECT pend_id, pend_venda_id, clie_nome, ROUND(pend_valor::numeric, 2) FROM pendencias "
                    f"INNER JOIN cliente ON clie_id = pend_clie_id"
                    f"AND clie_id {op} {self.cliente.id}")
        conn.commit()
        cur.close()
        conn.close()

    def busca_pendencias_by_id(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"SELECT pend_id, pend_venda_id, clie_nome, ROUND(pend_valor::numeric, 2) FROM pendencias "
                    f"INNER JOIN cliente ON clie_id = pend_clie_id"
                    f"AND pend_id = {self.id}")
        conn.commit()
        cur.close()
        conn.close()

