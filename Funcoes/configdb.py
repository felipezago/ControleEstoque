import psycopg2
from PyQt5.QtWidgets import QMessageBox


class Banco:
    import os
    import sys

    path = os.path.abspath(os.path.dirname(sys.argv[0]))

    def __init__(self):
        self.conectado = False

    @staticmethod
    def get_params(filename=os.path.join(path, 'database.ini'), section='POSTGRESQL'):
        from configparser import ConfigParser

        parser = ConfigParser()

        parser.read(filename)

        db = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
        else:
            print('Seção {0} Não encontrada no arquivo: {1}'.format(section, filename))

        return db

    def conecta(self):
        from Funcoes.exceptions import OperationalError
        params = self.get_params()

        conn = None
        try:
            conn = psycopg2.connect(**params)
        except OperationalError:
            self.conectado = False
            QMessageBox.warning("Erro no banco de dados.", "Erro")
        else:
            conn.commit()
            self.conectado = True
        finally:
            if conn is not None:
                conn.close()
            return self.conectado


class ConexaoTeste(object):

    def __init__(self, DbHost="", DbName="", DbUser="", DbPassword=""):
        self.DbHost = DbHost
        self.DbName = DbName
        self.DbUser = DbUser
        self.DbPassword = DbPassword
        self.sucesso = False

    def conectar(self):
        from Funcoes.utils import show_msg

        conn = None
        try:
            conn = psycopg2.connect(host=self.DbHost, database=self.DbName,
                                    user=self.DbUser, password=self.DbPassword)
            conn.commit()
        except Exception as e:
            show_msg(title="Erro", mensagem=f"{e}")
            self.sucesso = False

        else:
            self.sucesso = True
        finally:
            if conn is not None:
                conn.close()
            return self.sucesso



