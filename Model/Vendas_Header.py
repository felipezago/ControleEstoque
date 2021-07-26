import psycopg2
from Funcoes.configdb import Banco
from Model.Veiculo import Veiculo


class Vendas_Header:
    def __init__(self, id_venda="", veiculo: Veiculo = "", qtd_itens="", total_descontos="", valor_total="", status=""):
        self.id = id_venda
        self.veiculo = veiculo
        self.qtd_itens = qtd_itens
        self.total_descontos = total_descontos
        self.valor_total = valor_total
        self.status = status

    def inserir(self):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"INSERT INTO vendas (venda_id, venda_veic_placa, venda_qtd_itens, venda_total_descontos, "
                    f"venda_valor_total, venda_status) VALUES ({self.id}, \'{self.veiculo.placa}\', {self.qtd_itens}, "
                    f"{self.total_descontos}, {self.valor_total}, \'{self.status}\')")
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
        cur.execute(f"SELECT venda_valor_total::numeric, venda_total_descontos::numeric, "
                    f"(venda_valor_total + venda_total_descontos)::numeric "
                    f"FROM vendas"
                    f" WHERE venda_id = {self.id}")
        row = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()

        return row
