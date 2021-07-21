import psycopg2
from Funcoes.configdb import Banco


class Endereco:
    def __init__(self, end_id="", rua="", bairro="", numero="", cidade="", estado="", cep=""):
        self.rua = rua
        self.bairro = bairro
        self.numero = numero
        self.cidade = cidade
        self.estado = estado
        self.cep = cep
        self.id = end_id

    def get_endereco_by_id(self):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM endereco WHERE end_id = \'{self.id}\'')
        row = cur.fetchone()
        cur.close()
        conn.close()
        return row

    def inserir_end(self):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f'INSERT INTO endereco (end_rua, end_bairro, end_numero, end_cidade, end_estado, end_cep) '
                    f'VALUES(\'{self.rua}\','
                            f'\'{self.bairro}\', '
                            f'\'{self.numero}\', '
                            f'\'{self.cidade}\', '
                            f'\'{self.estado}\', '
                            f'\'{self.cep}\'); '
                    )
        conn.commit()
        cur.close()
        conn.close()

    def delete_endereco_by_id(self):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"DELETE FROM endereco WHERE end_id = {self.id}")
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def get_todos_enderecos():
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM endereco ORDER BY end_id")
        lista_end = cur.fetchall()
        cur.close()
        conn.close()
        return lista_end

    def editar(self):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"UPDATE endereco SET end_rua = \'{self.rua}\', end_bairro = \'{self.bairro}\', "
                    f"end_numero = \'{self.numero}\', end_cidade = \'{self.cidade}\', end_estado = \'{self.estado}\', "
                    f"end_cep = \'{self.cep}\' WHERE end_id = {self.id}")
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def ultimo_end():
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"SELECT MAX(end_id) FROM endereco")
        id_cat = cur.fetchone()
        cur.close()
        conn.close()
        return id_cat

    @staticmethod
    def qtd_end():
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"SELECT COUNT(*) FROM endereco")
        qtd = cur.fetchall()
        cur.close()
        conn.close()
        return qtd
