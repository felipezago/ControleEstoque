import psycopg2
from Funcoes.configdb import Banco
from Model.Veiculo import Veiculo
from Model.Cliente import Cliente


class Vendas_Header:
    def __init__(self, id_venda="", cliente: Cliente = "", veiculo: Veiculo = "", qtd_itens="", total_descontos="", valor_total="", status=""):
        self.id = id_venda
        self.veiculo = veiculo
        self.cliente = cliente
        self.qtd_itens = qtd_itens
        self.total_descontos = total_descontos
        self.valor_total = valor_total
        self.status = status

    def inserir(self):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        if self.veiculo.placa:
            cur.execute(f"INSERT INTO vendas (venda_id, venda_veic_placa, venda_clie_id, venda_qtd_itens,"
                        f" venda_total_descontos, venda_valor_total, venda_status) VALUES ({self.id}, "
                        f"\'{self.veiculo.placa}\', \'{self.cliente.id}\', {self.qtd_itens}, {self.total_descontos}, "
                        f"{self.valor_total}, \'{self.status}\')")
        else:
            cur.execute(f"INSERT INTO vendas (venda_id, venda_veic_placa, venda_clie_id, venda_qtd_itens,"
                        f" venda_total_descontos, venda_valor_total, venda_status) VALUES ({self.id}, "
                        f"null, \'{self.cliente.id}\', {self.qtd_itens}, {self.total_descontos}, "
                        f"{self.valor_total}, \'{self.status}\')")
        conn.commit()
        cur.close()
        conn.close()

    def delete(self):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"DELETE FROM vendas WHERE venda_id = {self.id})")
        conn.commit()
        cur.close()
        conn.close()

    def get_venda_pdf(self):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
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
