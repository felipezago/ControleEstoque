from Funcoes.banco import conexao
from Model.Finalizadoras import Finalizadoras


class Venda_Fin:
    def __init__(self, id_fin="", finalizadoras: Finalizadoras = "", venda_id="", valor=""):
        self.id = id_fin
        self.finalizadoras = finalizadoras
        self.venda_id = venda_id
        self.valor = valor

    def valor_pago(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f'SELECT SUM(vendas_fin_valor)::numeric FROM vendas_fin WHERE vendas_id = {self.venda_id}')
        row = cur.fetchone()
        cur.close()
        conn.close()

        if row[0] is None:
            return 0
        else:
            return row[0]

    def get_fins_venda(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM vendas_fin WHERE vendas_id = {self.venda_id}')
        row = cur.fetchall()
        cur.close()
        conn.close()
        return row

    def get_fins_venda_pdf(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f'SELECT fin_desc, vendas_fin_valor FROM vendas_fin '
                    f'INNER JOIN finalizadoras ON vendas_fin.fin_id = finalizadoras.fin_id '
                    f'WHERE vendas_id =  {self.venda_id}')
        row = cur.fetchall()
        cur.close()
        conn.close()
        return row

    def inserir_fin_venda(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"INSERT INTO vendas_fin (fin_id, vendas_id, vendas_fin_valor) "
                    f"VALUES ({self.finalizadoras.id}, {self.venda_id}, {self.valor})")
        conn.commit()
        cur.close()
        conn.close()

    def delete_fin_by_cod(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"DELETE FROM vendas_fin WHERE vendas_fin_id = {self.id}")
        conn.commit()
        cur.close()
        conn.close()

    def delete_fin_by_venda(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"DELETE FROM vendas_fin WHERE vendas_id = {self.venda_id}")
        conn.commit()
        cur.close()
        conn.close()
