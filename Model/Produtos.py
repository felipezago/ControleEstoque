import psycopg2
from Funcoes.configdb import Banco


class Produtos:
    def __init__(self, id="", fornecedor="", estoque="", codbarras="", descricao="", marca="", preco="", categoria=""):
        self.id = id
        self.fornecedor = fornecedor
        self.estoque = estoque
        self.codbarras = codbarras
        self.descricao = descricao
        self.marca = marca
        self.preco = preco
        self.categoria = categoria

    @staticmethod
    def get_produtos_by_desc(campo, desc):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM produtos WHERE {campo} like \'%{desc}%\' order by prod_id')
        row = cur.fetchall()
        cur.close()
        conn.close()

        if len(row) == 1:
            for a in row:
                return a
        else:
            return row

    def get_produto_by_id(self):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM produtos WHERE prod_id = {self.id}')
        row = cur.fetchone()
        conn.close()
        cur.close()
        return row

    def get_produto_by_fornecedor(self):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM produtos WHERE prod_forn_id = {self.fornecedor.id}')
        row = cur.fetchall()
        conn.close()
        cur.close()
        return row

    def get_produto_by_categoria(self):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM produtos WHERE prod_cat_id = {self.categoria.id}')
        row = cur.fetchall()
        conn.close()
        cur.close()
        return row

    @staticmethod
    def delete_produtos_by_id(id_prod):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"DELETE FROM produtos WHERE prod_id = {id_prod}")
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def get_new_produto():
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('SELECT max(prod_id) FROM produtos')
        row = cur.fetchone()
        cur.close()
        conn.close()

        if row[0] is None:
            return 1
        else:
            return int(row[0]) + 1

    @staticmethod
    def inserir_produtos(forn_id, cat_it, estoque, codbarras, descricao, marca, preco):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"INSERT INTO produtos (prod_forn_id, prod_cat_id, prod_estoque, prod_codbarras, prod_desc, "
                    f"prod_marca, prod_preco) VALUES ({forn_id}, {cat_it}, {estoque}, \'{codbarras}\', \'{descricao}\')"
                    f",\'{marca}\', {preco}")
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def get_todos_produtos():
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM produtos ORDER BY prod_id')
        row = cur.fetchall()
        cur.close()
        conn.close()
        return row

    @staticmethod
    def qtd_prod():
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"SELECT COUNT(*) FROM produtos")
        qtd = cur.fetchall()
        cur.close()
        conn.close()
        return qtd

    def editar(self):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"UPDATE produtos SET prod_cat_id = {self.categoria.id}, prod_forn_id = {self.fornecedor.id}, "
                    f"prod_estoque = {self.estoque}, prod_codbarras = \'{self.codbarras}\', "
                    f"prod_desc = \'{self.descricao}\', prod_marca = \'{self.marca}\', prod_preco = {self.preco} "
                    f"WHERE prod_id = {self.id}")
        conn.commit()
        cur.close()
        conn.close()

    def delete(self):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"DELETE FROM produtos WHERE prod_id = {self.id}")
        conn.commit()
        cur.close()
        conn.close()

    def gravar_imagem_produtos(self, path_to_file, file_extension):
        """ insert a BLOB into a table """
        conn = None
        try:
            # read data from a picture
            drawing = open(path_to_file, 'rb').read()
            config = Banco()
            params = config.get_params()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute("INSERT INTO prod_img(prod_id, img_ext, img_dados) " +
                        "VALUES(%s,%s,%s)",
                        (self.id, file_extension, psycopg2.Binary(drawing)))
            conn.commit()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    def atualizar_imagem(self, path_to_file):
        drawing = open(path_to_file, 'rb').read()
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute("UPDATE prod_img SET img_dados = %s WHERE prod_id = %s",
                    (psycopg2.Binary(drawing), self.id))
        conn.commit()
        cur.close()
        conn.close()

    def check_imagem(self):
        """ insert a BLOB into a table """
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM prod_img WHERE prod_id = \'{self.id}\'")
        row = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return row

    def ler_imagem_produtos(self, s, path_to_dir):
        from PyQt5.QtCore import Qt
        from PyQt5.QtGui import QPixmap
        conn = None
        try:
            config = Banco()
            params = config.get_params()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute(""" SELECT prod_desc, img_ext, img_dados
                            FROM prod_img
                            INNER JOIN produtos on produtos.prod_id = prod_img.prod_id
                            WHERE produtos.prod_id = %s """,
                        (self.id,))
            blob = cur.fetchone()

            if blob is not None:
                open(path_to_dir + blob[0] + '.' + blob[1], 'wb').write(blob[2])

                # colocando a imagem em um label
                s.ui.lb_foto_prod.setPixmap(QPixmap(path_to_dir + blob[0] + '.' + blob[1]).scaledToWidth(
                    150, Qt.TransformationMode(Qt.FastTransformation)))
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
