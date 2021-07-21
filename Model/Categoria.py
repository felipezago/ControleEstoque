import psycopg2
from Funcoes.configdb import Banco


class Categoria:
    def __init__(self, id="", descricao=""):
        self.id = id
        self.descricao = descricao

    def get_categoria_by_id(self):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM categoria WHERE cat_id = \'{self.id}\' order by cat_id')
        row = cur.fetchone()
        cur.close()
        conn.close()
        return row

    @staticmethod
    def get_categorias_by_desc(desc):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM categoria WHERE cat_descricao like \'%{desc}%\' order by cat_id')
        row = cur.fetchall()
        cur.close()
        conn.close()

        if len(row) == 1:
            for a in row:
                return a
        else:
            return row

    def delete_categoria_by_id(self):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"DELETE FROM categoria WHERE cat_id = {self.id}")
        conn.commit()
        cur.close()
        conn.close()

    def inserir_categoria(self):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"INSERT INTO categoria (cat_descricao) VALUES (\'{self.descricao}\')")
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def get_todas_categorias():
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM categoria ORDER BY cat_id")
        lista_categorias = cur.fetchall()
        cur.close()
        conn.close()
        return lista_categorias

    def editar_categorias(self):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"UPDATE categoria SET cat_descricao = \'{self.descricao}\' "
                    f"WHERE cat_id = {self.id}")
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def ultima_categoria():
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"SELECT MAX(cat_id) FROM categoria")
        id_cat = cur.fetchone()
        cur.close()
        conn.close()
        return id_cat

    @staticmethod
    def qtd_categorias():
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"SELECT COUNT(*) FROM categoria")
        qtd = cur.fetchall()
        cur.close()
        conn.close()
        return qtd
