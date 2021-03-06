def create_tables():
    comm = {"criar_cliente": """
               CREATE TABLE IF NOT EXISTS cliente (
                   clie_id SERIAL PRIMARY KEY,
                   clie_cpf_cnpj VARCHAR(15) NOT NULL UNIQUE,
                   clie_nome VARCHAR(60) NOT NULL,
                   clie_fone VARCHAR(40),
                   clie_email VARCHAR(50) NOT NULL,
                   clie_rg VARCHAR(13),
                   clie_celular VARCHAR(25),
                   clie_tipo VARCHAR(20),
                   clie_rua VARCHAR(60) NOT NULL,
                   clie_bairro VARCHAR(60) NOT NULL,
                   clie_numero VARCHAR(10),
                   clie_cidade VARCHAR(50) NOT NULL,
                   clie_estado VARCHAR(2) NOT NULL,
                   clie_CEP varchar(15)                      
               )
               """,
            "criar_veiculo": """
               CREATE TABLE IF NOT EXISTS veiculo (
                   veic_placa VARCHAR(15) PRIMARY KEY,
                   veic_clie_id INT,
                   veic_marca VARCHAR(50) NOT NULL,
                   veic_modelo VARCHAR(60) NOT NULL,
                   CONSTRAINT fk_veic_clie
                       FOREIGN KEY(veic_clie_id) 
                           REFERENCES cliente(clie_id)
                           ON DELETE CASCADE        
               )
               """,
            "criar_empresas": """
                CREATE TABLE IF NOT EXISTS empresas (
                    emp_cnpj VARCHAR PRIMARY KEY,
                    emp_razaosocial VARCHAR(100) NOT NULL,
                    emp_nomefantasia VARCHAR(100) NOT NULL,
                    emp_inscricaoestadual VARCHAR(40),
                    emp_email VARCHAR(40) NOT NULL,
                    emp_fone VARCHAR(20) NOT NULL,
                    emp_site VARCHAR(100),
                    emp_rua VARCHAR(60) NOT NULL,
                    emp_bairro VARCHAR(60) NOT NULL,
                    emp_numero VARCHAR(10),
                    emp_cidade VARCHAR(50) NOT NULL,
                    emp_estado VARCHAR(2) NOT NULL,
                    emp_CEP varchar(15)
                )
                """,

            "criar_usuarios": """
            CREATE TABLE IF NOT EXISTS usuarios (
                usu_id SERIAL PRIMARY KEY,
                usu_emp_cnpj VARCHAR(20),
                usu_login VARCHAR(255) NOT NULL UNIQUE,
                usu_senha TEXT NOT NULL,
                usu_nivel_acesso VARCHAR(20),
                usu_cpf VARCHAR(15) NOT NULL,
                usu_nome VARCHAR(60) NOT NULL,
                usu_fone VARCHAR(40),
                usu_email VARCHAR(50) NOT NULL,
                usu_rg VARCHAR(13),
                usu_celular VARCHAR(25),
                CONSTRAINT fk_usu_emp
                    FOREIGN KEY(usu_emp_cnpj) 
                        REFERENCES empresas(emp_cnpj)
                        ON DELETE CASCADE ON UPDATE CASCADE
            )
            """,
            "criar_operador": """
                CREATE TABLE IF NOT EXISTS operador (
                    ope_id INT PRIMARY KEY           
                )
            """,
            "criar_emp_img": """
               CREATE TABLE IF NOT EXISTS emp_img (
                   emp_cnpj VARCHAR PRIMARY KEY,
                   img_ext VARCHAR(60) NOT NULL,
                   img_dados BYTEA NOT NULL,
                   FOREIGN KEY (emp_cnpj)
                       REFERENCES empresas (emp_cnpj)
                       ON UPDATE CASCADE ON DELETE CASCADE
               )
               """,

            "criar_fornecedor": """
           CREATE TABLE IF NOT EXISTS fornecedor (
               forn_id SERIAL PRIMARY KEY,
               forn_nome VARCHAR(50) NOT NULL,
               forn_cnpj VARCHAR(20) NOT NULL,            
               forn_email VARCHAR(60) NOT NULL,
               forn_fone VARCHAR(50),
               forn_rua VARCHAR(60) NOT NULL,
               forn_bairro VARCHAR(60) NOT NULL,
               forn_numero VARCHAR(10),
               forn_cidade VARCHAR(50) NOT NULL,
               forn_estado VARCHAR(2) NOT NULL,
               forn_CEP varchar(15)       
           )
           """,
            "criar_categoria": """
           CREATE TABLE IF NOT EXISTS categoria (
               cat_id SERIAL PRIMARY KEY,
               cat_descricao VARCHAR(50)
           )
           """,
            "criar_produtos": """
           CREATE TABLE IF NOT EXISTS produtos (
               prod_id SERIAL PRIMARY KEY,
               prod_forn_id INT,
               prod_cat_id INT,
               prod_estoque INT,
               prod_codbarras VARCHAR(15) NOT NULL,
               prod_desc VARCHAR(50) NOT NULL,
               prod_marca VARCHAR(60) NOT NULL,
               prod_preco FLOAT NOT NULL,  
               CONSTRAINT fk_prod_forn
                   FOREIGN KEY(prod_forn_id) 
                       REFERENCES fornecedor(forn_id)
                       ON DELETE CASCADE, 
               CONSTRAINT fk_prod_cat
                   FOREIGN KEY(prod_cat_id) 
                       REFERENCES categoria(cat_id)
                       ON DELETE CASCADE 
           )
           """,
            "criar_prod_img": """
           CREATE TABLE IF NOT EXISTS prod_img (
               prod_id INTEGER PRIMARY KEY,
               img_ext VARCHAR(60) NOT NULL,
               img_dados BYTEA NOT NULL,
               FOREIGN KEY (prod_id)
                   REFERENCES produtos (prod_id)
                   ON UPDATE CASCADE ON DELETE CASCADE
           )
           """,
            "criar_servi??os": """
           CREATE TABLE IF NOT EXISTS servicos (
               serv_id SERIAL PRIMARY KEY,
               serv_desc VARCHAR(60) NOT NULL,
               serv_preco FLOAT NOT NULL
           )
           """,
            "criar_vendatmp": """
           CREATE TABLE IF NOT EXISTS venda_tmp (
               venda_cod_interno SERIAL PRIMARY KEY,
               venda_clie_id INT,
               venda_veic_placa VARCHAR(15),
               venda_id INT NOT NULL,
               venda_prod_serv_id INT NOT NULL,
               venda_tipo VARCHAR(15) NOT NULL,
               venda_qtd INT DEFAULT 1,
               venda_valor FLOAT NOT NULL,
               venda_desconto FLOAT,
               venda_datahora TIMESTAMP,
               FOREIGN KEY (venda_clie_id)
                    REFERENCES cliente (clie_id)
                        ON UPDATE CASCADE ON DELETE CASCADE
           )
           """,
            "criar_venda": """
           CREATE TABLE IF NOT EXISTS vendas_itens (
               venda_cod_interno SERIAL PRIMARY KEY,
               venda_id INT NOT NULL,
               venda_prod_serv_id INT NOT NULL,
               venda_tipo VARCHAR(15) NOT NULL,
               venda_qtd INT NOT NULL,
               venda_valor FLOAT NOT NULL,               
               venda_desconto FLOAT,
               venda_datahora TIMESTAMP                             
           )
           """,
            "criar_finalizadoras": """
               CREATE TABLE IF NOT EXISTS finalizadoras (
                   fin_id SERIAL PRIMARY KEY,
                   fin_desc VARCHAR(60)
               )
               """,
            "criar_fin_venda": """
                   CREATE TABLE IF NOT EXISTS vendas_fin (
                       vendas_fin_id SERIAL PRIMARY KEY,
                       fin_id INT,
                       vendas_id INT,
                       vendas_fin_valor FLOAT,
                       FOREIGN KEY (fin_id)
                           REFERENCES finalizadoras (fin_id)
                           ON UPDATE CASCADE ON DELETE CASCADE
                   )
                   """,
            "criar_venda_cabe??alho": """
                       CREATE TABLE IF NOT EXISTS vendas (
                           venda_id INT PRIMARY KEY,
                           venda_clie_id INT,
                           venda_veic_placa VARCHAR(15),
                           venda_qtd_itens INT,
                           venda_total_descontos FLOAT,
                           venda_valor_total FLOAT,
                           venda_status VARCHAR(50),
                           venda_datahora TIMESTAMP,
                           FOREIGN KEY (venda_clie_id)
                               REFERENCES cliente (clie_id)
                               ON UPDATE CASCADE ON DELETE CASCADE
                       )
                       """,
            "criar_compratmp": """
              CREATE TABLE IF NOT EXISTS compra_tmp (
                  compra_cod_interno SERIAL PRIMARY KEY,
                  compra_forn_id INT,
                  compra_id INT NOT NULL,
                  compra_prod_id INT NOT NULL,
                  compra_qtd INT DEFAULT 1,
                  compra_valor FLOAT NOT NULL,
                  compra_datahora TIMESTAMP,
                  FOREIGN KEY (compra_forn_id)
                       REFERENCES fornecedor (forn_id)
                           ON UPDATE CASCADE ON DELETE CASCADE,
                  FOREIGN KEY (compra_prod_id)
                        REFERENCES produtos (prod_id)
                            ON UPDATE CASCADE ON DELETE CASCADE
              )
              """,
            "criar_compra": """
              CREATE TABLE IF NOT EXISTS compra_itens (
                  compra_cod_interno SERIAL PRIMARY KEY,
                  compra_id INT NOT NULL,
                  compra_prod_id INT NOT NULL,
                  compra_qtd INT NOT NULL,
                  compra_valor FLOAT NOT NULL,               
                  compra_datahora TIMESTAMP,
                  FOREIGN KEY (compra_prod_id)
                        REFERENCES produtos (prod_id)
                            ON UPDATE CASCADE ON DELETE CASCADE                             
              )
              """,
            "criar_fin_compra": """
                      CREATE TABLE IF NOT EXISTS compra_fin (
                          compra_fin_id SERIAL PRIMARY KEY,
                          fin_id INT,
                          compra_id INT,
                          compra_fin_valor FLOAT,
                          FOREIGN KEY (fin_id)
                              REFERENCES finalizadoras (fin_id)
                              ON UPDATE CASCADE ON DELETE CASCADE
                      )
                      """,
            "criar_compra_cabe??alho": """
                          CREATE TABLE IF NOT EXISTS compras (
                              compra_id INT PRIMARY KEY,
                              compra_forn_id INT,
                              compra_qtd_itens INT,
                              compra_valor_total FLOAT,
                              compra_status VARCHAR(50),
                              compra_datahora TIMESTAMP,
                              FOREIGN KEY (compra_forn_id)
                                   REFERENCES fornecedor (forn_id)
                                       ON UPDATE CASCADE ON DELETE CASCADE
                          )
                          """,
            "criar_pendencias": """
                CREATE TABLE IF NOT EXISTS pendencias(
                    pend_id SERIAL PRIMARY KEY,
                    pend_clie_id INT,
                    pend_venda_id INT,
                    pend_veic_placa VARCHAR(15),
                    pend_datahora TIMESTAMP,
                    pend_valor FLOAT,
                    FOREIGN KEY (pend_clie_id)
                               REFERENCES cliente (clie_id)
                               ON UPDATE CASCADE ON DELETE CASCADE,
                    FOREIGN KEY (pend_venda_id)
                               REFERENCES vendas (venda_id)
                               ON UPDATE CASCADE ON DELETE CASCADE                      
                )
            """,
            "criar_function_prod": """
           CREATE OR REPLACE FUNCTION add_prod(
               descricao VARCHAR,
               codbarra VARCHAR, 
               marca VARCHAR,
               estoque INT,
               preco FLOAT,
               fornecedor_id INT,
               categoria_id INT
           ) RETURNS INTEGER AS $$
           DECLARE
               f_prod_id INT;
           BEGIN
               INSERT INTO produtos (prod_forn_id, prod_cat_id, prod_estoque, prod_codbarras, prod_desc, prod_marca, 
               prod_preco) VALUES (fornecedor_id, categoria_id, estoque, codbarra, descricao, marca, preco) 
               RETURNING prod_id INTO f_prod_id;

               RETURN f_prod_id;
           END;
           $$ LANGUAGE plpgsql;
           """
            }

    conn = None
    import psycopg2
    from Funcoes.configdb import Banco

    params = Banco.get_params()
    try:
        conn = psycopg2.connect(**params)
    except Exception as e:
        print(e.__class__)
        from Funcoes.utils import show_msg
        show_msg("erro", "Erro", "Erro no banco de dados")
        return False
    else:
        cur = conn.cursor()
        for command in comm.values():
            cur.execute(command)
        conn.commit()
        cur.close()
        return True
    finally:
        if conn is not None:
            conn.close()
