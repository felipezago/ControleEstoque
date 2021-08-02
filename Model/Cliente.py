from Funcoes.banco import conexao
from Model.Pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, id_cli=""):
        super().__init__(id_cli)
        self.id = id_cli

    @staticmethod
    def get_cliente_by_desc(campo, desc):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(
            f'''SELECT clie_id, clie_cpf_cnpj, clie_nome, clie_fone, clie_email, clie_rg, clie_celular, clie_rua, 
                clie_bairro, clie_numero, clie_cidade, clie_estado, clie_cep FROM cliente 
                WHERE {campo} like \'%{desc}%\' '''
        )
        row = cur.fetchall()
        conn.close()
        cur.close()
        return row

    def get_cliente_pdf(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(
            f'''SELECT INITCAP(clie_nome), 
                clie_cpf_cnpj, CONCAT(SUBSTR(clie_rg,1,2),'.',SUBSTR(clie_rg,3,3),'.',SUBSTR(clie_rg,6,3),
                '-',SUBSTR(clie_rg,9,1)), clie_celular, clie_fone, clie_email, INITCAP(clie_rua), INITCAP(clie_bairro)
                , clie_numero, INITCAP(clie_cidade), clie_estado from cliente
                WHERE clie_id = {self.id}''')
        row = cur.fetchone()
        cur.close()
        conn.close()
        return row

    def get_cliente_by_id(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(
            f'SELECT clie_id, clie_cpf_cnpj, clie_nome, clie_fone, clie_email, clie_rg, clie_celular, clie_rua,'
            f'clie_bairro, clie_numero, clie_cidade, clie_estado, clie_cep FROM cliente WHERE clie_id = {self.id}'
        )
        row = cur.fetchone()
        cur.close()
        conn.close()
        return row

    def delete_cliente_by_id(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"DELETE FROM cliente WHERE clie_id = {self.id}")
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def get_todos_clientes():
        conn = conexao()
        cur = conn.cursor()
        cur.execute(
            f"SELECT clie_id, clie_cpf_cnpj, clie_nome, clie_fone, clie_email, clie_rg, clie_celular, clie_rua, "
            f"clie_bairro, clie_numero, clie_cidade, clie_estado, clie_cep FROM cliente ")
        lista_clientes = cur.fetchall()
        cur.close()
        conn.close()
        return lista_clientes

    @staticmethod
    def qtd_cli():
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"SELECT COUNT(*) FROM cliente")
        qtd = cur.fetchall()
        cur.close()
        conn.close()
        return qtd

    def inserir(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(
            f"INSERT INTO cliente (clie_cpf_cnpj, clie_nome, clie_fone, clie_celular, clie_email, clie_rg, clie_tipo, "
            f"clie_rua, clie_bairro, clie_numero, clie_cidade, clie_estado, clie_cep) VALUES "
            f"(\'{self.cpf}\', \'{self.nome}\', \'{self.fone}\', \'{self.celular}\', \'{self.email}\', \'{self.rg}\', "
            f"\'{self.tipo}\', \'{self.rua}\', \'{self.bairro}\', \'{self.numero}\', \'{self.cidade}\', "
            f"\'{self.estado}\', \'{self.cep}\')"
        )
        conn.commit()
        cur.close()
        conn.close()

    def editar(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(
            f"UPDATE cliente SET clie_cpf_cnpj = \'{self.cpf}\', clie_nome = \'{self.nome}\',"
            f" clie_fone = \'{self.fone}\', clie_email = \'{self.email}\', clie_rg = \'{self.rg}\', "
            f"clie_tipo = \'{self.tipo}\', clie_rua = \'{self.rua}\', clie_bairro = \'{self.bairro}\', "
            f"clie_numero = \'{self.numero}\', clie_cidade = \'{self.cidade}\', clie_estado = \'{self.estado}\', "
            f"clie_cep = \'{self.cep}\' "
            f"WHERE clie_id = {self.id}"
        )
        conn.commit()
        cur.close()
        conn.close()
