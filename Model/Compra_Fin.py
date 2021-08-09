from Funcoes.banco import conexao
from Model.Finalizadoras import Finalizadoras


class Compra_Fin:
    def __init__(self, id_fin="", finalizadoras: Finalizadoras = "", compra_id="", valor=""):
        self.id = id_fin
        self.finalizadoras = finalizadoras
        self.compra_id = compra_id
        self.valor = valor

    def valor_pago(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f'SELECT SUM(compra_fin_valor)::numeric FROM compra_fin WHERE compra_id = {self.compra_id}')
        row = cur.fetchone()
        cur.close()
        conn.close()

        if row[0] is None:
            return 0
        else:
            return row[0]

    def get_fins_compra(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM compra_fin WHERE compra_id = {self.compra_id} '
                    f'ORDER BY compra_fin_id')
        row = cur.fetchall()
        cur.close()
        conn.close()
        return row

    def inserir_fin_compra(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"INSERT INTO compra_fin (fin_id, compra_id, compra_fin_valor) "
                    f"VALUES ({self.finalizadoras.id}, {self.compra_id}, {self.valor})")
        conn.commit()
        cur.close()
        conn.close()

    def delete_fin_by_cod(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"DELETE FROM compra_fin WHERE compra_fin_id = {self.id}")
        conn.commit()
        cur.close()
        conn.close()

    def delete_fin_by_compra(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"DELETE FROM compra_fin WHERE compra_id = {self.compra_id}")
        conn.commit()
        cur.close()
        conn.close()

    def check_fin(self, cod):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM compra_fin "
                    f"INNER JOIN finalizadoras ON compra_fin.fin_id = finalizadoras.fin_id "
                    f"WHERE compra_id = {self.compra_id} AND compra_fin.fin_id = {cod}")
        row = cur.fetchone()
        cur.close()
        conn.close()
        if row is not None:
            return True
        else:
            return False

    def update_fin_compra(self, cod):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"UPDATE compra_fin SET compra_fin_valor = compra_fin_valor + {self.valor} "
                    f"WHERE compra_id = {self.compra_id}"
                    f"AND fin_id = {cod}")
        conn.commit()
        cur.close()
        conn.close()
