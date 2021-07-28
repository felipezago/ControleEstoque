import psycopg2
from Funcoes.configdb import Banco
from Model.Pessoa import Pessoa


class Cliente:
    def __init__(self, id="", pessoa: Pessoa = ""):
        self.id = id
        self.pessoa = pessoa

    def get_cliente_pdf(self):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f'''SELECT INITCAP(pess_nome), 
                    CONCAT(SUBSTR(pess_cpf_cnpj,1,3),'.',SUBSTR(pess_cpf_cnpj,4,3),'.',SUBSTR(pess_cpf_cnpj,7,3),'-',
                    SUBSTR(pess_cpf_cnpj,10,2)), CONCAT(SUBSTR(pess_rg,1,2),'.',SUBSTR(pess_rg,3,3),'.',SUBSTR(pess_rg,6,3),
                    '-',SUBSTR(pess_rg,9,1)), pess_celular, pess_fone, pess_email, INITCAP(end_rua), INITCAP(end_bairro)
                    , end_numero, INITCAP(end_cidade), end_estado from cliente
                    INNER JOIN pessoas ON clie_pessoa_id = pess_id
                    INNER JOIN endereco ON pess_end_id = end_id
                    WHERE clie_id = {self.id}''')
        row = cur.fetchone()
        cur.close()
        conn.close()
        return row

    def get_cliente_by_id(self):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM cliente WHERE clie_id = {self.id}')
        row = cur.fetchone()
        cur.close()
        conn.close()
        return row

    def get_cliente_by_id_tabela(self):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"SELECT clie_id, pess_cpf_cnpj, pess_nome, pess_fone, pess_email, pess_rg, pess_celular, end_rua, "
                    f"end_bairro, end_numero, end_cidade, end_estado, end_cep FROM cliente "
                    f"INNER JOIN pessoas ON clie_pessoa_id = pess_id "
                    f"INNER JOIN endereco ON pess_end_id = end_id WHERE clie_id = {self.id}")
        row = cur.fetchall()
        cur.close()
        conn.close()
        return row

    def get_cliente_by_pessoa(self):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"SELECT clie_id, pess_cpf_cnpj, pess_nome, pess_fone, pess_email, pess_rg, pess_celular, end_rua, "
                    f"end_bairro, end_numero, end_cidade, end_estado, end_cep FROM cliente "
                    f"INNER JOIN pessoas ON clie_pessoa_id = pess_id "
                    f"INNER JOIN endereco ON pess_end_id = end_id WHERE clie_pessoa_id = {self.pessoa.id}")
        row = cur.fetchone()
        cur.close()
        conn.close()
        return row

    def delete_cliente_by_id(self):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"DELETE FROM cliente WHERE clie_id = {self.id}")
        conn.commit()
        cur.execute(f"DELETE FROM pessoas WHERE pess_id = {self.pessoa.id}")
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def get_new_cliente():
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('SELECT max(clie_id) FROM cliente')
        row = cur.fetchone()
        cur.close()
        conn.close()

        if row[0] is None:
            return 1
        else:
            return int(row[0]) + 1

    @staticmethod
    def get_todos_clientes():
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM cliente")
        lista_clientes = cur.fetchall()
        cur.close()
        conn.close()
        return lista_clientes

    @staticmethod
    def get_todos_clientes_tabela():
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"SELECT clie_id, pess_cpf_cnpj, pess_nome, pess_fone, pess_email, pess_rg, pess_celular, end_rua, "
                    f"end_bairro, end_numero, end_cidade, end_estado, end_cep FROM cliente "
                    f"INNER JOIN pessoas ON clie_pessoa_id = pess_id "
                    f"INNER JOIN endereco ON pess_end_id = end_id")
        lista_clientes = cur.fetchall()
        cur.close()
        conn.close()
        return lista_clientes

    @staticmethod
    def qtd_cli():
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"SELECT COUNT(*) FROM cliente")
        qtd = cur.fetchall()
        cur.close()
        conn.close()
        return qtd
