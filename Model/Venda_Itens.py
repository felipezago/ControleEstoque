import psycopg2
from Funcoes.configdb import Banco


class Vendas:
    def __init__(self, id_v="", id_venda="", id_prod_serv="", tipo="", qtd="", valor="", desconto="", data_hora=""):
        self.id = id_v
        self.id_venda = id_venda
        self.id_prod_serv = id_prod_serv
        self.tipo = tipo
        self.qtd = qtd
        self.valor = valor
        self.desconto = desconto
        self.data_hora = data_hora

    def get_vendas_by_id(self):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM vendas_itens WHERE id_venda = \'{self.id_venda}\'')
        row = cur.fetchone()
        cur.close()
        conn.close()
        return row

    def delete_venda_by_id(self):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"DELETE FROM vendas_itens WHERE id_venda = {self.id_venda}")
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def inserir_venda():
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"INSERT INTO vendas_itens SELECT venda_cod_interno, venda_id, venda_prod_serv_id, venda_tipo, "
                    f"venda_qtd, venda_valor, venda_desconto, venda_datahora from venda_tmp")
        conn.commit()
        cur.close()
        conn.close()

    def select_tb_pdf(self):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"""
            SELECT venda_prod_serv_id, CASE 
                                            WHEN venda_tipo = 'PRODUTO' THEN prod_desc
                                            WHEN venda_tipo = 'SERVIÇO' THEN serv_desc 
                                        END, 
                                        venda_qtd, venda_valor, (venda_qtd * venda_valor), venda_desconto, 
                                        ROUND(venda_valor * venda_qtd - venda_desconto) AS total
                                        FROM vendas_itens
            INNER JOIN produtos ON venda_prod_serv_id = prod_id
            LEFT JOIN servicos ON venda_prod_serv_id = serv_id
            WHERE venda_id = {self.id_venda}
            """)
        select = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        return select
