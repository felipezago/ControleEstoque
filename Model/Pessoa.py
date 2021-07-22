import psycopg2
from Funcoes.configdb import Banco
from Model.Endereco import Endereco


class Pessoa:
    def __init__(self, id="", endereco: Endereco = "", cpf="", nome="", fone="", email="", rg="", celular="", tipo=""):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.id = id
        self.fone = fone
        self.rg = rg
        self.tipo = tipo
        self.celular = celular
        self.endereco = endereco

    def get_pessoa_cliente_by_id(self):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM pessoas WHERE pess_id = {self.id} AND pess_tipo = \'CLIENTE\'')
        row = cur.fetchone()
        conn.close()
        cur.close()
        return row

    def get_pessoa_usuario_by_id(self):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM pessoas WHERE pess_id = \'{self.id}\' AND pess_tipo = \'USUÁRIO\'')
        row = cur.fetchone()
        conn.close()
        cur.close()
        return row

    @staticmethod
    def get_pessoa_by_desc_tabela(campo, desc, tipo):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"SELECT clie_id, pess_cpf, pess_nome, pess_fone, pess_email, pess_rg, pess_celular, end_rua, " 
                    f"end_bairro, end_numero, end_cidade, end_estado, end_cep FROM cliente " 
                    f"INNER JOIN pessoas ON clie_pessoa_id = pess_id " 
                    f"INNER JOIN endereco ON pess_end_id = end_id" 
                    f" WHERE {campo} like \'%{desc}%\' AND pess_tipo = \'{tipo}\'")
        row = cur.fetchall()
        conn.close()
        cur.close()
        return row

    @staticmethod
    def get_pessoa_by_desc(campo, desc, tipo):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f'f"SELECT * from pessoas \
                        f" WHERE {campo} like \'%{desc}%\' AND pess_tipo = \'{tipo}\'')
        row = cur.fetchall()
        conn.close()
        cur.close()
        return row

    @staticmethod
    def get_clientes():
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM pessoas WHERE pess_tipo = \'CLIENTE\'')
        row = cur.fetchone()
        conn.close()
        cur.close()
        return row

    @staticmethod
    def get_usuarios():
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM pessoas WHERE pess_tipo = \'USUARIO\'')
        row = cur.fetchone()
        conn.close()
        cur.close()
        return row

    def editar(self):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"UPDATE pessoas SET pess_cpf = \'{self.cpf}\', pess_nome = \'{self.nome}\', "
                    f"pess_fone = \'{self.fone}\', pess_email = \'{self.email}\', pess_rg = \'{self.rg}\', "
                    f"pess_celular = \'{self.celular}\' WHERE pess_id = {self.id}")
        conn.commit()
        cur.close()
        conn.close()
