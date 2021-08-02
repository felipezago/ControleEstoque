import psycopg2
from Funcoes.banco import conexao
from Model.Endereco import Endereco


class Empresa(Endereco):
    def __init__(self, cnpj="", usuario="", razao_social="", nome_fantasia="", inscricao_estadual="", email="", fone="",
                 site=""):
        super().__init__()
        self.cnpj = cnpj
        self.usuario = usuario
        self.razao_social = razao_social
        self.nome_fantasia = nome_fantasia
        self.inscricao_estadual = inscricao_estadual
        self.email = email
        self.fone = fone
        self.site = site

    @staticmethod
    def get_empresas_by_desc(campo, desc):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f'SELECT emp_cnpj, emp_razaosocial, emp_nomefantasia, emp_inscricaoestadual, emp_email, emp_fone, '
                    f'emp_site, emp_rua, emp_bairro, emp_numero, emp_cidade, emp_estado, emp_cep FROM empresas '
                    f'WHERE {campo} like \'%{desc}%\''
                    f'ORDER BY emp_nomefantasia')
        row = cur.fetchall()
        cur.close()
        conn.close()

        return row

    def get_empresas_pdf(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"""
        SELECT INITCAP(emp_nomefantasia), INITCAP(emp_rua), emp_numero, INITCAP(emp_bairro), emp_fone, 
        CONCAT(SUBSTR(emp_cnpj,1,2),'.',SUBSTR(emp_cnpj,3,3),'.',SUBSTR(emp_cnpj,6,3),'/',SUBSTR(emp_cnpj,9,4), '-', 
        SUBSTR(emp_cnpj,13,2)), initcap(emp_cidade), emp_estado, emp_inscricaoestadual FROM empresas
        WHERE emp_cnpj = \'{self.cnpj}\'""")
        row = cur.fetchone()
        cur.close()
        conn.close()

        return row

    def get_empresa_by_cnpj(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f'SELECT emp_cnpj, emp_razaosocial, emp_nomefantasia, emp_inscricaoestadual, emp_email, emp_fone, '
                    f'emp_site, emp_rua, emp_bairro, emp_numero, emp_cidade, emp_estado, emp_cep FROM empresas '
                    f'WHERE emp_cnpj = \'{self.cnpj}\'')
        row = cur.fetchall()
        cur.close()
        conn.close()
        return row

    def get_empresa_by_cnpj_all(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM empresas '
                    f'WHERE emp_cnpj = \'{self.cnpj}\'')
        row = cur.fetchone()
        cur.close()
        conn.close()
        return row

    @staticmethod
    def get_todas_empresas():
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM empresas ORDER BY emp_nomefantasia')
        row = cur.fetchall()
        cur.close()
        conn.close()
        return row

    @staticmethod
    def get_todas_empresas_tabela():
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f'SELECT emp_cnpj, emp_razaosocial, emp_nomefantasia, emp_inscricaoestadual, emp_email, emp_fone, '
                    f'emp_site, emp_rua, emp_bairro, emp_numero, emp_cidade, emp_estado, emp_cep FROM empresas '
                    f'ORDER BY emp_nomefantasia')
        row = cur.fetchall()
        cur.close()
        conn.close()
        return row

    @staticmethod
    def qtd_emp():
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"SELECT COUNT(*) FROM empresas")
        qtd = cur.fetchall()
        cur.close()
        conn.close()
        return qtd

    def editar(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"UPDATE empresas SET emp_razaosocial = \'{self.razao_social}\', "
                    f"emp_nomefantasia = \'{self.nome_fantasia}\', emp_inscricaoestadual = \'{self.inscricao_estadual}"
                    f"\', emp_email = \'{self.email}\', emp_fone = \'{self.fone}\', emp_site = \'{self.site}\',  "
                    f"emp_rua = \'{self.rua}\', emp_bairro = \'{self.bairro}\', emp_numero = \'{self.numero}\',"
                    f"emp_cidade = \'{self.cidade}\', emp_estado = \'{self.estado}\', emp_cep = \'{self.cep}\'"
                    f"WHERE emp_cnpj = \'{self.cnpj}\'")
        conn.commit()
        cur.close()
        conn.close()

    def delete_empresa(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"DELETE FROM empresas WHERE emp_cnpj = \'{self.cnpj}\'")
        conn.commit()
        cur.close()
        conn.close()

    def gravar_imagem_empresas(self, path_to_file, file_extension):
        """ insert a BLOB into a table """
        conn = None
        try:
            # read data from a picture
            drawing = open(path_to_file, 'rb').read()
            conn = conexao()
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
        conn = conexao()
        cur = conn.cursor()

        cur.execute("UPDATE emp_img SET img_dados = %s WHERE emp_cnpj = %s",
                    (psycopg2.Binary(drawing), self.cnpj))
        conn.commit()
        cur.close()
        conn.close()

    def check_imagem(self):
        """ insert a BLOB into a table """
        conn = conexao()
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
            conn = conexao()
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
                                                      blob[1]).scaledToWidth(150, Qt.
                                                                             TransformationMode(Qt.FastTransformation)))
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

    def ler_imagem_empresas_pdf(self, path_to_dir):
        conn = None
        try:
            conn = conexao()
            cur = conn.cursor()
            cur.execute(""" SELECT emp_nomefantasia, img_ext, img_dados
                            FROM emp_img
                            INNER JOIN empresas on empresas.emp_cnpj = emp_img.emp_cnpj
                            WHERE empresas.emp_cnpj = %s """,
                        (self.cnpj,))
            blob = cur.fetchone()

            if blob is not None:
                open(path_to_dir + str(blob[0]).replace(" ", "").strip() + '.' + blob[1], 'wb').write(blob[2])

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

    def inserir(self):
        conn = conexao()
        cur = conn.cursor()
        cur.execute(f"""
            INSERT INTO empresas (emp_cnpj, emp_razaosocial, emp_nomefantasia, emp_inscricaoestadual, emp_email,emp_fone
                    , emp_site, emp_rua, emp_bairro, emp_numero, emp_cidade, emp_estado, emp_cep) VALUES 
                    (\'{self.cnpj}\', \'{self.razao_social}\', \'{self.nome_fantasia}\', \'{self.inscricao_estadual}
                    \', \'{self.email}\', \'{self.fone}\',  \'{self.site}\', \'{self.rua}\', \'{self.bairro}\', 
                    \'{self.numero}\', \'{self.cidade}\', \'{self.estado}\', \'{self.cep}\')
                """
                    )
        conn.commit()
        cur.close()
        conn.close()
