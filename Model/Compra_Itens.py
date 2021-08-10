from Funcoes.banco import conexao
from Model.Produtos import Produtos


class Compra_Itens:
    def __init__(self, id_v="", id_compra="", id_prod: Produtos = "", qtd="", valor="",
                 data_hora=""):
        self.id = id_v
        self.id_compra = id_compra
        self.id_prod = id_prod
        self.qtd = qtd
        self.valor = valor
        self.data_hora = data_hora

    def get_compras_by_id(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM compra_itens WHERE compra_id = \'{self.id_compra}\'')
        row = cur.fetchall()
        cur.close()
        conn.close()
        return row

    def delete_compra_by_id(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"DELETE FROM compra_itens WHERE compra_id = {self.id_compra}")
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def inserir_compra():
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"INSERT INTO compra_itens SELECT compra_cod_interno, compra_id, compra_prod_id, "
                    f"compra_qtd, compra_valor, compra_datahora from compra_tmp")
        conn.commit()
        cur.close()
        conn.close()

    def detalhes_compra(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f""" SELECT compra_id, prod_desc, compra_qtd, ROUND(compra_valor::numeric, 2), 
            ROUND((compra_qtd * compra_valor)::numeric, 2)
            FROM compra_itens
            INNER JOIN produtos ON compra_prod_id = prod_id
            WHERE compra_id = {self.id_compra}
        """)
        select = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        return select

    def select_produtos_compra(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"""
             SELECT compra_id, compra_prod_id, compra_qtd, prod_estoque
             FROM compra_itens
             INNER JOIN produtos ON compra_prod_id = prod_id
             WHERE compra_id = {self.id_compra}
            """)
        select = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        return select

    def retorna_total(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f'SELECT SUM(compra_valor * compra_qtd) FROM compra_itens WHERE compra_id = \'{self.id_compra}\'')
        row = cur.fetchone()
        cur.close()
        conn.close()
        return row[0]

    def retorna_ultimo_preco(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f'SELECT compra_valor FROM compra_itens WHERE compra_prod_id = {self.id_prod.id}'
                    f'ORDER BY compra_datahora DESC')
        row = cur.fetchone()
        cur.close()
        conn.close()
        if row is not None:
            return row[0]
        else:
            return 0
