import psycopg2
from Funcoes.configdb import Banco
from Funcoes.funcoes import show_msg
from Model.Pessoa import Pessoa
from Model.Empresa import Empresa


class Usuario:
    def __init__(self, id="", pessoa: Pessoa = "", empresa: Empresa = "", nome="", senha=""):
        self.nome = nome
        self.senha = senha
        self.id = id
        self.pessoa = pessoa
        self.empresa = empresa

    def get_usuario_by_id(self):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM usuarios WHERE usu_id = {self.id}')
        row = cur.fetchone()
        cur.close()
        conn.close()
        return row

    def get_usuario_by_pessoa(self):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f'SELECT usu_id, pess_cpf_cnpj, pess_nome, pess_fone, pess_email, pess_rg, pess_celular, usu_nome '
                    f'FROM usuarios '
                    f'INNER JOIN pessoas ON usu_pessoa_id = pess_id '
                    f'WHERE usu_pessoa_id = {self.pessoa.id}')
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
            cur.execute(f"SELECT * FROM usuarios ORDER BY usu_id")
            lista_end = cur.fetchall()
            cur.close()
            return lista_end
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
            cur.execute(f"UPDATE usuarios SET usu_nome = \'{self.nome}\', usu_senha = \'{criptografar_senha(self.senha)}\'"
                        f"WHERE usu_id = {self.id}")
            conn.commit()
            print("Senha alterada com sucesso!")
        else:
            cur.execute(
                f"UPDATE usuarios SET usu_nome = \'{self.nome}\' "
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