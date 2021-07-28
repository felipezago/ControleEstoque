import psycopg2
from Funcoes.configdb import Banco
from Model.Endereco import Endereco


class Fornecedor(Endereco):
    def __init__(self, id_forn="", nome="", cnpj="", email="", fone=""):
        super().__init__()
        self.id = id_forn
        self.nome = nome
        self.cnpj = cnpj
        self.email = email
        self.fone = fone

    def get_fornecedor_by_id(self):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f'SELECT forn_id, forn_nome, forn_cnpj, forn_email, forn_fone, forn_rua, forn_bairro, forn_numero, '
                    f'forn_cidade, forn_estado, forn_cep FROM fornecedor FROM fornecedor WHERE forn_id = \'{self.id}\'')
        row = cur.fetchone()
        cur.close()
        conn.close()
        return row

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
        cur.execute(f"SELECT forn_id, forn_nome, forn_cnpj, forn_email, forn_fone, forn_rua, forn_bairro, forn_numero, "
                    f"forn_cidade, forn_estado, forn_cep FROM fornecedor "
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
        cur.execute(f'SELECT forn_id, forn_nome, forn_cnpj, forn_email, forn_fone, forn_rua, forn_bairro, forn_numero, '
                    f'forn_cidade, forn_estado, forn_cep FROM fornecedor WHERE {campo} like \'%{desc}%\' '
                    f'ORDER BY forn_id')
        row = cur.fetchall()
        cur.close()
        conn.close()

        if len(row) == 1:
            for a in row:
                return a
        else:
            return row

    def inserir(self):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"INSERT INTO fornecedor (forn_fone, forn_cnpj, forn_email, forn_fone, forn_rua, forn_bairro, "
                    f"forn_numero, forn_cidade, forn_estado, forn_cep) VALUES "
                    f"(\'{self.nome}\', \'{self.cnpj}\', \'{self.email}\', \'{self.email}\', \'{self.rua}\', "
                    f"\'{self.bairro}\', \'{self.numero}\', \'{self.cidade}\', \'{self.estado}\', \'{self.cep}\')")
        conn.commit()
        cur.close()
        conn.close()
