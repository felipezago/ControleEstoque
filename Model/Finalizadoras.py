from Funcoes.banco import conexao


class Finalizadoras:
    def __init__(self, fin_id="", descricao=""):
        self.id = fin_id
        self.descricao = descricao

    def get_finalizadora_by_id(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM finalizadoras WHERE fin_id = \'{self.id}\'')
        row = cur.fetchone()
        cur.close()
        conn.close()
        return row

    @staticmethod
    def get_fin_by_desc(desc):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM finalizadoras WHERE fin_desc like \'%{desc}%\' order by fin_id')
        row = cur.fetchall()
        cur.close()
        conn.close()

        if len(row) == 1:
            for a in row:
                return a
        else:
            return row

    def delete_fin_by_id(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"DELETE FROM finalizadoras WHERE fin_id = {self.id}")
        conn.commit()
        cur.close()
        conn.close()

    def inserir_finalizadora(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"INSERT INTO finalizadoras (fin_desc) "
                    f"VALUES (\'{self.descricao}\')")
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def get_todas_finalizadoras():
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM finalizadoras ORDER BY fin_id")
        lista_categorias = cur.fetchall()
        cur.close()
        conn.close()
        return lista_categorias

    def editar_finalizadoras(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"UPDATE finalizadoras SET fin_desc = \'{self.descricao}\'"
                    f"WHERE fin_id = {self.id}")
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def ultima_fin():
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"SELECT MAX(fin_id) FROM finalizadoras")
        fin_id = cur.fetchone()
        cur.close()
        conn.close()
        return fin_id

    @staticmethod
    def qtd_fin():
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"SELECT COUNT(*) FROM finalizadoras")
        qtd = cur.fetchall()
        cur.close()
        conn.close()
        return qtd
