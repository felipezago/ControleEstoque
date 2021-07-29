import psycopg2
from Funcoes.configdb import Banco
from Funcoes.funcoes import show_msg
from Model.Pessoa import Pessoa
from Model.Empresa import Empresa


class Usuario(Pessoa):
    def __init__(self, id_usu="", login="", senha="", empresa: Empresa = "", nivel=""):
        super().__init__()
        self.login = login
        self.senha = senha
        self.id = id_usu
        self.empresa = empresa
        self.nivel = nivel

    @staticmethod
    def get_usu_by_desc(campo, desc):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(
            (f'SELECT usu_id, usu_cpf, usu_nome, usu_fone, usu_email, usu_rg, usu_celular, usu_login, '
             f'usu_nivel_acesso, emp_nomefantasia, emp_cnpj FROM usuarios '
             f'INNER JOIN empresas ON emp_cnpj = usu_emp_cnpj '
             f' WHERE {campo} like \'%{desc}%\' ')
        )
        row = cur.fetchall()
        conn.close()
        cur.close()
        return row

    def get_usuario_by_id(self):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f'SELECT usu_id, usu_cpf, usu_nome, usu_fone, usu_email, usu_rg, usu_celular, usu_login, '
                    f'usu_nivel_acesso, emp_nomefantasia, emp_cnpj FROM usuarios '
                    f'INNER JOIN empresas ON emp_cnpj = usu_emp_cnpj '
                    f'WHERE usu_id = {self.id}')
        row = cur.fetchone()
        cur.close()
        conn.close()
        return row

    @staticmethod
    def get_todos_usuarios():
        config = Banco()
        params = config.get_params()
        conn = None
        try:
            conn = psycopg2.connect(**params)
        except Exception as e:
            print(e)
            show_msg(title="Erro", mensagem="Erro no banco")
        else:
            cur = conn.cursor()
            cur.execute(f'SELECT usu_id, usu_cpf, usu_nome, usu_fone, usu_email, usu_rg, usu_celular, usu_login, '
                        f'usu_nivel_acesso, emp_nomefantasia FROM usuarios '
                        f'INNER JOIN empresas ON emp_cnpj = usu_emp_cnpj '
                        f'ORDER BY usu_id')
            lista = cur.fetchall()
            cur.close()
            return lista
        finally:
            if conn is not None:
                conn.close()

    def editar(self):
        from Funcoes.funcoes import criptografar_senha

        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        if self.senha:
            cur.execute(f"UPDATE usuarios SET usu_login = \'{self.login}\', usu_nivel_acesso = \'{self.nivel}\',"
                        f"usu_cpf = \'{self.cpf}\', usu_nome = \'{self.nome}\', usu_fone = \'{self.fone}\',"
                        f"usu_email = \'{self.email}\', usu_rg = \'{self.rg}\', usu_celular = \'{self.celular}\',"
                        f"usu_emp_cnpj = \'{self.empresa.cnpj}\', "
                        f"usu_senha = \'{criptografar_senha(self.senha)}\'"
                        f"WHERE usu_id = {self.id}")
            conn.commit()
            print("Senha alterada com sucesso!")
        else:
            cur.execute(
                f"UPDATE usuarios SET usu_login = \'{self.login}\', usu_nivel_acesso = \'{self.nivel}\',"
                f"usu_cpf = \'{self.cpf}\', usu_nome = \'{self.nome}\', usu_fone = \'{self.fone}\',"
                f"usu_email = \'{self.email}\', usu_rg = \'{self.rg}\', usu_celular = \'{self.celular}\',"
                f"usu_emp_cnpj = \'{self.empresa.cnpj}\' "
                f"WHERE usu_id = {self.id}")
            conn.commit()
        cur.close()
        conn.close()

    def get_senha_criptografada(self):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"SELECT usu_senha FROM usuarios WHERE usu_id = {self.id}")
        senha = cur.fetchone()
        cur.close()
        conn.close()
        return senha

    def inserir(self):
        from Funcoes.funcoes import criptografar_senha, retirar_formatacao

        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(
            f"INSERT INTO usuarios (usu_emp_cnpj, usu_login, usu_senha, usu_nivel_acesso, usu_cpf,"
            f" usu_nome, usu_fone, usu_email, usu_rg, usu_celular) VALUES "
            f"(\'{retirar_formatacao(self.empresa.cnpj)}\', \'{self.login}\', \'{criptografar_senha(self.senha)}\', "
            f"\'{self.nivel}\', \'{retirar_formatacao(self.cpf)}\', \'{self.nome}\', \'{self.fone}\', \'{self.email}\',"
            f"\'{retirar_formatacao(self.rg)}\', \'{self.celular}\')"
        )
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def qtd_usu():
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"SELECT COUNT(*) FROM usuarios")
        qtd = cur.fetchall()
        cur.close()
        conn.close()
        return qtd

    def delete_usuario_by_id(self):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"DELETE FROM usuarios WHERE usu_id = \'{self.id}\'")
        conn.commit()
        cur.close()
        conn.close()
