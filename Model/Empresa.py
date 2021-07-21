import psycopg2
from Funcoes.configdb import Banco


class Empresa:
    def __init__(self, cnpj="", endereco="", usuario="", razao_social="", nome_fantasia="", inscricao_estadual="",
                 email="", fone="", site=""):
        self.cnpj = cnpj
        self.endereco = endereco
        self.usuario = usuario
        self.razao_social = razao_social
        self.nome_fantasia = nome_fantasia
        self.inscricao_estadual = inscricao_estadual
        self.email = email
        self.fone = fone
        self.site = site

    @staticmethod
    def get_empresas_by_desc(campo, desc):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM empresas WHERE {campo} like \'%{desc}%\'')
        row = cur.fetchall()
        cur.close()
        conn.close()

        if len(row) == 1:
            for a in row:
                return a
        else:
            return row

    def get_empresa_by_cnpj(self):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM empresas WHERE emp_cnpj = \'{self.cnpj}\'')
        row = cur.fetchone()
        cur.close()
        conn.close()
        return row

    @staticmethod
    def get_todas_empresas():
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM empresas ORDER BY emp_nomefantasia')
        row = cur.fetchall()
        cur.close()
        conn.close()
        return row

    @staticmethod
    def qtd_emp():
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"SELECT COUNT(*) FROM empresas")
        qtd = cur.fetchall()
        cur.close()
        conn.close()
        return qtd

    def editar(self):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"UPDATE empresas SET emp_cnpj = \'{self.cnpj}\', emp_razaosocial = \'{self.razao_social}\', "
                    f"emp_nomefantasia = \'{self.nome_fantasia}\', emp_inscricaoestadual = \'{self.inscricao_estadual}"
                    f"\', emp_email = \'{self.email}\', emp_fone = \'{self.fone}\', emp_site = \'{self.site}\' "
                    f"WHERE emp_cnpj = \'{self.cnpj}\'")
        conn.commit()
        cur.close()
        conn.close()

    def delete_empresa(self):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"DELETE FROM empresas WHERE emp_cnpj = \'{self.cnpj}\'")
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def alterar_cnpj(novo_cnpj, cnpj_antigo):
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"UPDATE empresas SET emp_cnpj = \'{novo_cnpj}\' "
                    f"WHERE emp_cnpj = \'{cnpj_antigo}\'")
        conn.commit()
        cur.close()
        conn.close()

    def gravar_imagem_empresas(self, path_to_file, file_extension):
        """ insert a BLOB into a table """
        conn = None
        try:
            # read data from a picture
            drawing = open(path_to_file, 'rb').read()
            config = Banco()
            params = config.get_params()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute("INSERT INTO emp_img(emp_cnpj, img_ext, img_dados) " +
                        "VALUES(%s,%s,%s)",
                        (self.cnpj, file_extension, psycopg2.Binary(drawing)))
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

        cur.execute("UPDATE emp_img SET img_dados = %s WHERE emp_cnpj = %s",
                    (psycopg2.Binary(drawing), self.cnpj))
        conn.commit()
        cur.close()
        conn.close()

    def check_imagem(self):
        """ insert a BLOB into a table """
        config = Banco()
        params = config.get_params()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM emp_img WHERE emp_cnpj = \'{self.cnpj}\'")
        row = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return row

    def ler_imagem_empresas(self, s, path_to_dir):
        from PyQt5.QtCore import Qt
        from PyQt5.QtGui import QPixmap
        conn = None
        try:
            config = Banco()
            params = config.get_params()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute(""" SELECT emp_nomefantasia, img_ext, img_dados
                            FROM emp_img
                            INNER JOIN empresas on empresas.emp_cnpj = emp_img.emp_cnpj
                            WHERE empresas.emp_cnpj = %s """,
                        (self.cnpj,))
            blob = cur.fetchone()

            if blob is not None:
                open(path_to_dir + str(blob[0]).replace(" ", "").strip() + '.' + blob[1], 'wb').write(blob[2])

                # colocando a imagem em um label
                s.ui.lb_LogoEmpresa.setPixmap(QPixmap(path_to_dir + str(blob[0]).replace(" ", "").strip() + '.' +
                                                      blob[1]).scaledToWidth(150, Qt.TransformationMode(
                    Qt.FastTransformation)))
                cur.close()
            else:
                return False

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return False
        else:
            return True
        finally:
            if conn is not None:
                conn.close()
