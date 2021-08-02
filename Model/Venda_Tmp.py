from Funcoes.banco import conexao
from Model.Veiculo import Veiculo
from Model.Cliente import Cliente


class Venda_Tmp:
    def __init__(self, cod_interno="", cliente: Cliente = "", veiculo: Veiculo = "", id_venda="", id_prod_serv="",
                 tipo="", qtd="", valor="", desconto="", data_hora="", status=""):
        self.cod_interno = cod_interno
        self.veiculo = veiculo
        self.cliente = cliente
        self.id_venda = id_venda
        self.id_prod_serv = id_prod_serv
        self.tipo = tipo
        self.qtd = qtd
        self.valor = valor
        self.desconto = desconto
        self.data_hora = data_hora
        self.status = status

    def get_venda_by_codinterno(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM venda_tmp WHERE venda_cod_interno = \'{self.cod_interno}\'')
        row = cur.fetchone()
        cur.close()
        conn.close()
        return row

    @staticmethod
    def get_cod_venda():
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f'SELECT DISTINCT(venda_id) FROM venda_tmp')
        row = cur.fetchone()
        cur.close()
        conn.close()
        for a in row:
            return a

    @staticmethod
    def get_venda(desc, operador, valor):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM venda_tmp WHERE {desc} {operador} {valor}')
        row = cur.fetchone()
        cur.close()
        conn.close()
        return row

    @staticmethod
    def delete_venda():
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"DELETE FROM venda_tmp")
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def delete_descontos():
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"UPDATE venda_tmp SET venda_desconto = 0")
        conn.commit()
        cur.close()
        conn.close()

    def inserir_venda(self):
        conn = conexao()
        cur_select_nova_venda = conn.cursor()
        cur_select_nova_venda.execute("SELECT MAX(venda_id) FROM vendas")
        select_nova = cur_select_nova_venda.fetchone()
        cur_select_nova_venda.close()

        if select_nova[0] is None:
            self.id_venda = 1
        else:
            self.id_venda = select_nova[0] + 1

        cur_insert = conn.cursor()

        cur_insert.execute(f"INSERT INTO venda_tmp(venda_veic_placa, venda_id, venda_prod_serv_id, venda_tipo, "
                           f"venda_qtd, venda_valor, venda_desconto, venda_datahora) VALUES "
                           f"(null, {self.id_venda}, {self.id_prod_serv}, \'{self.tipo}\', {self.qtd}, {self.valor}, "
                           f"{self.desconto}, \'{self.data_hora}\')")
        conn.commit()
        cur_insert.close()
        conn.close()

    @staticmethod
    def get_venda_atual():
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM venda_tmp ORDER BY venda_cod_interno")
        row = cur.fetchall()
        cur.close()
        conn.close()
        return row

    def inserir_from_itens(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute("INSERT INTO venda_tmp "
                    "SELECT venda_cod_interno, venda_clie_id, venda_veic_placa, vendas.venda_id, "
                    "venda_prod_serv_id, venda_tipo, venda_qtd, venda_valor, venda_desconto, venda_datahora "
                    "FROM vendas_itens "
                    "INNER JOIN vendas "
                    "ON vendas.venda_id = vendas_itens.venda_id "
                    f"WHERE vendas_itens.venda_id = {self.id_venda}")
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def existe_produto_venda(id_produto):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM venda_tmp WHERE venda_prod_serv_id = {id_produto} AND venda_tipo = \'PRODUTO\'")
        row = cur.fetchone()
        cur.close()
        conn.close()
        if row is None:
            return False
        else:
            return True

    @staticmethod
    def existe_servico_venda(id_produto):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM venda_tmp WHERE venda_prod_serv_id = {id_produto} AND venda_tipo = \'SERVIÇO\'")
        row = cur.fetchone()
        cur.close()
        conn.close()
        if row is None:
            return False
        else:
            return True

    def add_qtd_item(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"UPDATE venda_tmp SET venda_qtd = venda_qtd + {self.qtd} WHERE venda_prod_serv_id = "
                    f"{self.id_prod_serv} AND venda_tipo = \'{self.tipo}\'")
        conn.commit()
        cur.close()
        conn.close()

    def delete_item_venda(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"DELETE FROM venda_tmp WHERE venda_cod_interno = {self.cod_interno}")
        conn.commit()
        cur.close()
        conn.close()

    def update_cliente(self):
        conn = conexao()
        cur = conn.cursor()

        if self.veiculo.placa:
            cur.execute(f"UPDATE venda_tmp SET venda_clie_id = \'{self.cliente.id}\', "
                        f"venda_veic_placa = \'{self.veiculo.placa}\'")
        else:
            cur.execute(f"UPDATE venda_tmp SET venda_clie_id = \'{self.cliente.id}\', "
                        f"venda_veic_placa = null")
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def retorna_total():
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"SELECT SUM(venda_qtd * venda_valor - venda_desconto)::numeric FROM venda_tmp")
        row = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        if row[0] is None:
            return 0
        else:
            for total in row:
                return total

    @staticmethod
    def check_registros():
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM venda_tmp ORDER BY venda_cod_interno")
        row = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        if row is None:
            return False
        else:
            return True

    @staticmethod
    def soma_descontos():
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"SELECT SUM(venda_desconto)::numeric FROM venda_tmp")
        row = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        if row[0] is None:
            return 0
        else:
            return row[0]

    def inserir_desconto_item(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"UPDATE venda_tmp SET venda_desconto = {self.desconto} "
                    f"WHERE venda_cod_interno = {self.cod_interno}")
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def qtd_itens():
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"SELECT count(*) FROM venda_tmp")
        row = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        if row[0] is not None:
            return row[0]
        else:
            return 0
