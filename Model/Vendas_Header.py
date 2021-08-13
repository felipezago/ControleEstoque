from Funcoes.banco import conexao
from Model.Veiculo import Veiculo
from Model.Cliente import Cliente


class Vendas_Header:
    def __init__(self, id_venda="", cliente: Cliente = "", veiculo: Veiculo = "", qtd_itens="", total_descontos="",
                 valor_total="", status="", datahora=""):
        self.id = id_venda
        self.veiculo = veiculo
        self.cliente = cliente
        self.qtd_itens = qtd_itens
        self.total_descontos = total_descontos
        self.valor_total = valor_total
        self.status = status
        self.datahora = datahora

    def inserir(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"INSERT INTO vendas (venda_id, venda_veic_placa, venda_clie_id, venda_qtd_itens,"
                    f" venda_total_descontos, venda_valor_total, venda_status, venda_datahora) VALUES ({self.id}, "
                    f"\'{self.veiculo.placa if self.veiculo.placa else 'null'}\', \'{self.cliente.id}\', "
                    f"{self.qtd_itens}, {self.total_descontos}, "
                    f"{self.valor_total}, \'{self.status}\', \'{self.datahora}\')")
        conn.commit()
        cur.close()
        conn.close()

    def delete_venda(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"DELETE FROM vendas WHERE venda_id = {self.id}")
        conn.commit()
        cur.execute(f"DELETE FROM vendas_fin WHERE vendas_id = {self.id}")
        conn.commit()
        cur.execute(f"DELETE FROM vendas_itens WHERE venda_id = {self.id}")
        conn.commit()
        conn.commit()
        cur.close()
        conn.close()

    def get_venda_pdf(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"SELECT ROUND(venda_valor_total::numeric, 2), ROUND(venda_total_descontos::numeric, 2), "
                    f"ROUND((venda_valor_total + venda_total_descontos)::numeric, 2) "
                    f"FROM vendas"
                    f" WHERE venda_id = {self.id}")
        row = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()

        return row

    @staticmethod
    def get_vendas():
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"""
            SELECT venda_id, clie_nome, veic_modelo, venda_qtd_itens, ROUND(venda_total_descontos::numeric, 2), 
            ROUND(venda_valor_total::numeric, 2), venda_status
            FROM vendas
            INNER join cliente ON venda_clie_id = clie_id
            LEFT JOIN veiculo ON veic_placa = venda_veic_placa
            ORDER BY venda_id
        """)
        row = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()

        return row

    def busca_vendas_by_id(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"""
                SELECT venda_id, clie_nome, veic_modelo, venda_qtd_itens, ROUND(venda_total_descontos::numeric, 2), 
                ROUND(venda_valor_total::numeric, 2), venda_status
                FROM vendas
                INNER join cliente ON venda_clie_id = clie_id
                LEFT JOIN veiculo ON veic_placa = venda_veic_placa
                WHERE venda_id = {self.id}
                ORDER BY venda_id
            """)
        row = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()

        return row

    def busca_vendas_by_cliente(self, op):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"""
                SELECT venda_id, clie_nome, veic_modelo, venda_qtd_itens, ROUND(venda_total_descontos::numeric, 2), 
                ROUND(venda_valor_total::numeric, 2), venda_status
                FROM vendas
                INNER join cliente ON venda_clie_id = clie_id
                LEFT JOIN veiculo ON veic_placa = venda_veic_placa
                WHERE clie_id {op} {self.cliente.id}
                ORDER BY venda_id
            """)
        row = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()

        return row

    def busca_vendas_by_status(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"""
                SELECT venda_id, clie_nome, veic_modelo, venda_qtd_itens, ROUND(venda_total_descontos::numeric, 2), 
                ROUND(venda_valor_total::numeric, 2), venda_status
                FROM vendas
                INNER join cliente ON venda_clie_id = clie_id
                LEFT JOIN veiculo ON veic_placa = venda_veic_placa
                WHERE venda_status = \'{self.status}\'
                ORDER BY venda_id
            """)
        row = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()

        return row

    def get_vendas_by_id(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"""
            SELECT * FROM vendas
            WHERE venda_id = {self.id}
            ORDER BY venda_id
        """)
        row = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()

        return row

    def get_venda_pendente_by_id(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"""
            SELECT * FROM vendas
            WHERE venda_id = {self.id}
            AND venda_status = \'PENDENTE\'
            ORDER BY venda_id
        """)
        row = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()

        return row

    @staticmethod
    def check_pendentes():
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"""
            SELECT * FROM vendas
            WHERE  venda_status = \'PENDENTE\'
        """)
        row = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()

        if row is None:
            return 0
        else:
            return row[0]

    @staticmethod
    def check_vendas(id_venda):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"""
            SELECT * FROM vendas
            WHERE venda_id = {id_venda}
        """)
        row = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()

        if row is None:
            return False
        else:
            return True

    def update(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"""
           UPDATE vendas
            SET venda_clie_id = {self.cliente.id},
            venda_veic_placa = \'{self.veiculo.placa if self.veiculo.placa else 'null'}\',
            venda_qtd_itens = {self.qtd_itens},
            venda_total_descontos = {self.total_descontos},
            venda_valor_total = {self.valor_total},
            venda_status = \'{self.status}\'
            WHERE venda_id = {self.id}
        """)
        conn.commit()
        cur.close()
        conn.close()

    def retorna_hora(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"""
            SELECT venda_datahora FROM vendas
            WHERE venda_id = {self.id}
        """)
        row = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()

        return row[0]

    def retorna_placa_veiculo(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"""
            SELECT venda_veic_placa FROM vendas
            WHERE venda_id = {self.id}
        """)
        row = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()

        if row[0] == "null":
            return 0
        else:
            return row[0]

    def retorna_cod_cliente(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"""
            SELECT venda_clie_id FROM vendas
            WHERE venda_id = {self.id}
        """)
        row = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()

        return row[0]

    @staticmethod
    def relatorio_movimento(datainicial, datafinal):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"""
                    SELECT ROUND(SUM(venda_valor_total + venda_total_descontos)::NUMERIC, 2), 
                    ROUND(SUM(venda_total_descontos)::NUMERIC, 2), 
                    ROUND((SUM(venda_valor_total + venda_total_descontos)::NUMERIC - 
                    SUM(venda_total_descontos)::NUMERIC), 2)
                    FROM vendas
                    WHERE venda_status = 'FINALIZADO'
                    AND CAST(venda_datahora AS DATE) BETWEEN \'{datainicial}\' AND \'{datafinal}\'
                """)
        row = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        if row is not None:
            if row[0] is not None:
                return row


