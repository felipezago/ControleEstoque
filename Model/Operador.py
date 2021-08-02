from Funcoes.banco import conexao
from PyQt5.QtWidgets import QMessageBox


class Operador:
    def __init__(self, usuario=""):
        self.usuario = usuario

    @staticmethod
    def get_operador_atual():
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM operador')
        row = cur.fetchone()
        cur.close()
        conn.close()
        return row

    @staticmethod
    def inserir_operador(id_usuario):
        conn = conexao()
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
        conn = conexao()
        cur = conn.cursor()
        cur.execute("DELETE FROM operador")
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def verifica_operador_ativo():
        try:
            conn = conexao()
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
