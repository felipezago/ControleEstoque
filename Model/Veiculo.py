import psycopg2
from Funcoes.configdb import Banco


class Veiculo:
    def __init__(self, placa="", cliente="", marca="", modelo=""):
        self.placa = placa
        self.cliente = cliente
        self.marca = marca
        self.modelo = modelo

    def delete_veiculos_by_id(self):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"DELETE FROM veiculo WHERE veic_placa = \'{self.placa}\'")
        conn.commit()
        cur.close()
        conn.close()

    def inserir_veiculo(self):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(
            f"INSERT INTO veiculo (veic_placa, veic_clie_id, veic_marca, veic_modelo)"
            f"VALUES(\'{self.placa}\', \'{self.cliente.id}\', \'{self.marca}\', \'{self.modelo}\')"
        )
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def get_todos_veiculos():
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM veiculo")
        list = cur.fetchall()
        cur.close()
        conn.close()
        return list

    @staticmethod
    def qtd_cli():
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"SELECT COUNT(*) FROM veiculo")
        qtd = cur.fetchall()
        cur.close()
        conn.close()
        return qtd

    @staticmethod
    def get_veic_by_desc(campo, desc):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM veiculo WHERE {campo} like \'%{desc}%\'')
        row = cur.fetchall()
        conn.close()
        cur.close()
        return row

    def get_veic_by_placa(self):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM veiculo WHERE veic_placa = \'{self.placa}\'')
        row = cur.fetchone()
        conn.close()
        cur.close()
        return row

    def get_veic_by_pessoa(self):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM veiculo WHERE veic_clie_id = {self.cliente.id}')
        row = cur.fetchall()
        conn.close()
        cur.close()
        return row

    def editar(self, placa_antiga):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"UPDATE veiculo SET veic_placa = \'{self.placa}\', veic_clie_id = \'{self.cliente.id}\', "
                    f"veic_marca = \'{self.marca}\', veic_modelo = \'{self.modelo}\' "
                    f"WHERE veic_placa = \'{placa_antiga}\'")
        conn.commit()
        cur.close()
        conn.close()
