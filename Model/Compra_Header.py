from Funcoes.banco import conexao
from Model.Fornecedor import Fornecedor


class Compras_Header:
    def __init__(self, id_compra="", fornecedor: Fornecedor = "", qtd_itens="",
                 valor_total="", status="", datahora=""):
        self.id = id_compra
        self.fornecedor = fornecedor
        self.qtd_itens = qtd_itens
        self.valor_total = valor_total
        self.status = status
        self.datahora = datahora

    def inserir(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"INSERT INTO compras (compra_id, compra_forn_id, compra_qtd_itens,"
                    f" compra_valor_total, compra_status, compra_datahora) VALUES ({self.id}, "
                    f"\'{self.fornecedor.id}\', "
                    f"{self.qtd_itens}, "
                    f"{self.valor_total}, \'{self.status}\', \'{self.datahora}\')")
        conn.commit()
        cur.close()
        conn.close()

    def delete_compra(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"DELETE FROM compras WHERE compra_id = {self.id}")
        conn.commit()
        cur.execute(f"DELETE FROM compra_fin WHERE compra_id = {self.id}")
        conn.commit()
        cur.execute(f"DELETE FROM compra_itens WHERE compra_id = {self.id}")
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def get_compras():
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"""
            SELECT compra_id, forn_nome, compra_qtd_itens, 
            ROUND(compra_valor_total::numeric, 2)
            FROM compras
            INNER JOIN fornecedor ON forn_id = compra_forn_id
            ORDER BY compra_id
        """)
        row = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()

        return row

    def busca_compras_by_id(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"""
                SELECT compra_id, forn_nome, compra_qtd_itens,
                ROUND(compra_valor_total::numeric, 2)
                FROM compras
                INNER JOIN fornecedor ON forn_id = compra_forn_id
                WHERE compra_id = {self.id}
                ORDER BY compra_id
            """)
        row = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()

        return row

    def busca_compras_by_forn(self, op):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"""
                SELECT compra_id, forn_nome, compra_qtd_itens,
                ROUND(compra_valor_total::numeric, 2)
                FROM compras
                INNER JOIN fornecedor ON forn_id = compra_forn_id
                WHERE forn_id {op} {self.fornecedor.id}
                ORDER BY compra_id
            """)
        row = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()

        return row

    def busca_compras_by_status(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"""
                 SELECT compra_id, forn_nome, compra_qtd_itens, ROUND(compra_total_descontos::numeric, 2), 
                ROUND(compra_valor_total::numeric, 2), compra_status
                FROM compras
                INNER JOIN fornecedor ON forn_id = compra_forn_id
                WHERE compra_status = \'{self.status}\'
                ORDER BY compra_id
            """)
        row = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()

        return row

    def get_compras_by_id(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"""
             SELECT compra_id, forn_nome, compra_qtd_itens, ROUND(compra_total_descontos::numeric, 2), 
                ROUND(compra_valor_total::numeric, 2), compra_status
                FROM compras
                INNER JOIN fornecedor ON forn_id = compra_forn_id
            WHERE compra_id = {self.id}
            ORDER BY compra_id
        """)
        row = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()

        return row

    def get_compra_pendente_by_id(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"""
            SELECT compra_id, forn_nome, compra_qtd_itens, ROUND(compra_total_descontos::numeric, 2), 
            ROUND(compra_valor_total::numeric, 2), compra_status
            FROM compras
            INNER JOIN fornecedor ON forn_id = compra_forn_id
            WHERE compra_id = {self.id}
            AND compra_status = \'PENDENTE\'
            ORDER BY compra_id
        """)
        row = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()

        return row

    @staticmethod
    def check_pendentes():
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"""
            SELECT * FROM compras
            WHERE  compra_status = \'PENDENTE\'
        """)
        row = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()

        if row is None:
            return 0
        else:
            return row[0]

    @staticmethod
    def check_compras(id_compra):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"""
            SELECT * FROM compras
            WHERE compra_id = {id_compra}
        """)
        row = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()

        if row is None:
            return False
        else:
            return True

    def update(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"""
           UPDATE compras
            SET compra_forn_id = {self.fornecedor.id},
            compra_qtd_itens = {self.qtd_itens},
            compra_valor_total = {self.valor_total},
            compra_status = \'{self.status}\'
            WHERE compra_id = {self.id}
        """)
        conn.commit()
        cur.close()
        conn.close()

    def retorna_hora(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"""
            SELECT compra_datahora FROM compras
            WHERE compra_id = {self.id}
        """)
        row = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()

        return row[0]

    def retorna_cod_forn(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"""
            SELECT compra_forn_id FROM compras
            WHERE compra_id = {self.id}
        """)
        row = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()

        return row[0]

    @staticmethod
    def relatorio_movimento(datainicial, datafinal):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"""
                        SELECT ROUND(SUM(compra_valor_total)::numeric, 2)
                        FROM compras
                        WHERE compra_status = 'FINALIZADO'
                        AND CAST(compra_datahora AS DATE) BETWEEN \'{datainicial}\' AND \'{datafinal}\'
                    """)
        row = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        if row is not None:
            if row[0] is not None:
                return row

