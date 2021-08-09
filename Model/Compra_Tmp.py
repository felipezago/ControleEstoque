from Funcoes.banco import conexao
from Model.Fornecedor import Fornecedor


class Compra_Tmp:
    def __init__(self, cod_interno="", fornecedor: Fornecedor = "", id_compra="", id_prod="",
                 qtd="", valor="", data_hora="", status=""):
        self.cod_interno = cod_interno
        self.fornecedor = fornecedor
        self.id_compra = id_compra
        self.id_prod = id_prod
        self.qtd = qtd
        self.valor = valor
        self.data_hora = data_hora
        self.status = status

    def get_compra_by_codinterno(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM compra_tmp WHERE compra_cod_interno = \'{self.cod_interno}\'')
        row = cur.fetchone()
        cur.close()
        conn.close()
        return row

    @staticmethod
    def get_cod_compra():
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f'SELECT DISTINCT(compra_id) FROM compra_tmp')
        row = cur.fetchone()
        cur.close()
        conn.close()
        for a in row:
            return a

    @staticmethod
    def get_compra(desc, operador, valor):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM compra_tmp WHERE {desc} {operador} {valor}')
        row = cur.fetchone()
        cur.close()
        conn.close()
        return row

    @staticmethod
    def delete_compra():
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"DELETE FROM compra_tmp")
        conn.commit()
        cur.close()
        conn.close()

    def inserir_compra(self, id_compra):
        conn = conexao()
        cur_insert = conn.cursor()
        cur_insert.execute(f"INSERT INTO compra_tmp(compra_id, compra_prod_id, "
                           f"compra_qtd, compra_valor, compra_datahora) VALUES "
                           f"({id_compra}, {self.id_prod}, {self.qtd}, {self.valor}, "
                           f"\'{self.data_hora}\')")
        conn.commit()
        cur_insert.close()
        conn.close()

    @staticmethod
    def select_max():
        conn = conexao()
        cur_select_nova_compra = conn.cursor()
        cur_select_nova_compra.execute("SELECT MAX(compra_id) FROM compras")
        select_nova = cur_select_nova_compra.fetchone()
        cur_select_nova_compra.close()

        if select_nova[0] is None:
            return 0
        else:
            return select_nova[0]

    @staticmethod
    def get_compra_atual():
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"SELECT compra_cod_interno, prod_desc, ROUND((compra_valor)::numeric, 2), "
                    f"ROUND((compra_qtd)::numeric, 2), "
                    f"ROUND((compra_qtd * compra_valor)::numeric, 2)"
                    f"FROM compra_tmp "
                    f"INNER JOIN produtos ON prod_id = compra_prod_id "
                    f"ORDER BY compra_cod_interno")
        row = cur.fetchall()
        cur.close()
        conn.close()
        return row

    def inserir_from_itens(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute("INSERT INTO compra_tmp "
                    "SELECT compra_cod_interno, compra_forn_id, compras.compra_id, "
                    "compra_prod_id, compra_qtd, compra_valor,"
                    "compra_itens.compra_datahora "
                    "FROM compras_itens "
                    "INNER JOIN compras "
                    "ON compras.compra_id = compra_itens.compra_id "
                    f"WHERE compras_itens.compra_id = {self.id_compra}")
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def existe_produto_compra(id_produto):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM compra_tmp WHERE compra_prod_id = {id_produto}")
        row = cur.fetchone()
        cur.close()
        conn.close()
        if row is None:
            return False
        else:
            return True

    def add_qtd_item(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"UPDATE compra_tmp SET compra_qtd = compra_qtd + {self.qtd} WHERE compra_prod_id = "
                    f"{self.id_prod}")
        conn.commit()
        cur.close()
        conn.close()

    def delete_item_compra(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"DELETE FROM compra_tmp WHERE compra_cod_interno = {self.cod_interno}")
        conn.commit()
        cur.close()
        conn.close()

    def update_forn(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"UPDATE compra_tmp SET compra_forn_id = \'{self.fornecedor.id}\'")
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def retorna_total():
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"SELECT ROUND(SUM(compra_qtd * compra_valor)::numeric, 2) FROM compra_tmp")
        row = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        if row[0] is None:
            return 0
        else:
            for total in row:
                return total

    @staticmethod
    def check_registros():
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM compra_tmp ORDER BY compra_cod_interno")
        row = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        if row is None:
            return False
        else:
            return True

    @staticmethod
    def qtd_itens():
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"SELECT count(*) FROM compra_tmp")
        row = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        if row[0] is not None:
            return row[0]
        else:
            return 0
