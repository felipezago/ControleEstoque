import psycopg2
from Funcoes.configdb import Banco


class Servicos:
    def __init__(self, id="", descricao="", preco=""):
        self.id = id
        self.descricao = descricao
        self.preco = preco

    def get_servico_by_id(self):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM servicos WHERE serv_id = \'{self.id}\'')
        row = cur.fetchone()
        cur.close()
        conn.close()
        return row

    def get_servico_by_preco(self, operador):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM servicos WHERE serv_preco {operador} \'{self.preco}\'')
        row = cur.fetchall()
        cur.close()
        conn.close()
        return row

    @staticmethod
    def get_servicos_by_desc(desc):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM servicos WHERE serv_desc like \'%{desc}%\' order by serv_id')
        row = cur.fetchall()
        cur.close()
        conn.close()

        if len(row) == 1:
            for a in row:
                return a
        else:
            return row

    def delete_servico_by_id(self):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"DELETE FROM servicos WHERE serv_id = {self.id}")
        conn.commit()
        cur.close()
        conn.close()

    def inserir_servico(self):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"INSERT INTO servicos (serv_desc, serv_preco) "
                    f"VALUES (\'{self.descricao}\', {self.preco})")
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def get_todos_servicos():
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM servicos ORDER BY serv_id")
        lista_categorias = cur.fetchall()
        cur.close()
        conn.close()
        return lista_categorias

    def editar_servicos(self):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"UPDATE servicos SET serv_desc = \'{self.descricao}\', serv_preco = {self.preco} "
                    f"WHERE serv_id = {self.id}")
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def ultimo_servico():
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"SELECT MAX(serv_id) FROM servicos")
        id = cur.fetchall()
        cur.close()
        conn.close()
        return id

    @staticmethod
    def qtd_servicos():
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"SELECT COUNT(*) FROM servicos")
        qtd = cur.fetchall()
        cur.close()
        conn.close()
        return qtd