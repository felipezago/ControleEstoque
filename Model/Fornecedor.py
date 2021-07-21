import psycopg2
from Funcoes.configdb import Banco


class Fornecedor:
    def __init__(self, id="", endereco="", nome="", cnpj="", email="", fone=""):
        self.id = id
        self.endereco = endereco
        self.nome = nome
        self.cnpj = cnpj
        self.email = email
        self.fone = fone

    def get_fornecedor_by_id(self):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM fornecedor WHERE forn_id = \'{self.id}\'')
        row = cur.fetchone()
        cur.close()
        conn.close()
        return row

    @staticmethod
    def get_new_fornecedor():
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('SELECT max(forn_id) FROM fornecedor')
        row = cur.fetchone()
        cur.close()
        conn.close()

        if row[0] is None:
            return 1
        else:
            return int(row[0]) + 1

    def delete_fornecedor_by_id(self):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"DELETE FROM fornecedor WHERE forn_id = {self.id}")
        cur.close()
        conn.commit()
        conn.close()

    @staticmethod
    def get_todos_fornecedores():
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM fornecedor ORDER BY forn_id")
        lista_fornecedores = cur.fetchall()
        cur.close()
        conn.close()
        return lista_fornecedores

    @staticmethod
    def get_todos_fornecedores_tabela():
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"SELECT forn_id, forn_nome, forn_cnpj, forn_email, forn_fone, end_rua, end_bairro, end_numero, "
                    f"end_cidade, end_estado, end_cep FROM fornecedor "
                    f"INNER JOIN endereco ON forn_end_id = end_id "
                    f"ORDER BY forn_id")
        lista_fornecedores = cur.fetchall()
        cur.close()
        conn.close()
        return lista_fornecedores

    @staticmethod
    def qtd_forn():
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"SELECT COUNT(*) FROM fornecedor")
        qtd = cur.fetchall()
        cur.close()
        conn.close()
        return qtd

    def editar(self):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"UPDATE fornecedor SET forn_nome = \'{self.nome}\', forn_cnpj = \'{self.cnpj}\', "
                    f"forn_email = \'{self.email}\', forn_fone = \'{self.fone}\' WHERE forn_id = \'{self.id}\'")
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def get_fornecedores_by_desc(campo, desc):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM fornecedor WHERE {campo} like \'%{desc}%\' ORDER BY forn_id')
        row = cur.fetchall()
        cur.close()
        conn.close()

        if len(row) == 1:
            for a in row:
                return a
        else:
            return row
