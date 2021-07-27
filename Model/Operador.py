import psycopg2
from Funcoes.configdb import Banco
from PyQt5.QtWidgets import QMessageBox


class Operador:
    def __init__(self, usuario=""):
        self.usuario = usuario

    @staticmethod
    def get_operador_atual():
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM operador')
        row = cur.fetchone()
        cur.close()
        conn.close()
        return row

    @staticmethod
    def inserir_operador(id_usuario):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(
            f'INSERT INTO operador (ope_id) '
            f'VALUES({id_usuario}); '
        )
        conn.commit()
        cur.execute("SELECT MAX(ope_id) FROM operador")
        row = cur.fetchone()
        cur.close()
        conn.close()
        # retorna id criado
        return row[0]

    @staticmethod
    def sair_operador():
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("DELETE FROM operador")
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def verifica_operador_ativo():
        config = Banco()
        params = config.get_params()
        try:
            conn = psycopg2.connect(**params)
        except Exception as e:
            print(e)
            msg = QMessageBox()
            msg.setWindowTitle("Erro")
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Erro no banco de dados.")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.show()
        else:
            cur = conn.cursor()
            cur.execute("SELECT * FROM operador")
            linha = cur.fetchone()
            cur.close()
            conn.close()
            if linha is not None:
                return True
            else:
                return False
