def create_tables():
    comm = {"criar_endereco": """
            CREATE TABLE IF NOT EXISTS endereco (
                end_id SERIAL PRIMARY KEY,
                end_rua VARCHAR(60) NOT NULL,
                end_bairro VARCHAR(60) NOT NULL,
                end_numero VARCHAR(10) NOT NULL,
                end_cidade VARCHAR(50) NOT NULL,
                end_estado VARCHAR(2) NOT NULL,
                end_CEP varchar(15)
            )
            """,
            "criar_pessoas": """
            CREATE TABLE IF NOT EXISTS pessoas (
                pess_id SERIAL PRIMARY KEY,
                pess_end_id INT,
                pess_cpf VARCHAR(11) NOT NULL,
                pess_nome VARCHAR(60) NOT NULL,
                pess_fone VARCHAR(40),
                pess_email VARCHAR(50) NOT NULL,
                pess_rg VARCHAR(13),
                pess_celular VARCHAR(25),
                pess_tipo VARCHAR(50) NOT NULL,
                CONSTRAINT fk_pess_end
                    FOREIGN KEY(pess_end_id) 
                        REFERENCES endereco(end_id)
                        ON DELETE CASCADE
            )
            """,
            "criar_usuarios": """
            CREATE TABLE IF NOT EXISTS usuarios (
                usu_id SERIAL PRIMARY KEY,
                usu_pessoa_id INT,
                usu_emp_cnpj VARCHAR(20),
                usu_nome VARCHAR(255) NOT NULL UNIQUE,
                usu_senha TEXT NOT NULL,
                usu_nivel_acesso VARCHAR(20),
                CONSTRAINT fk_usu_pess
                    FOREIGN KEY(usu_pessoa_id) 
                        REFERENCES pessoas(pess_id)
                        ON DELETE CASCADE,
                CONSTRAINT fk_usu_emp
                    FOREIGN KEY(usu_emp_cnpj) 
                        REFERENCES empresas(emp_cnpj)
                        ON DELETE CASCADE
            )
            """,
            "criar_operador": """
                CREATE TABLE IF NOT EXISTS operador (
                    ope_id INT PRIMARY KEY           
                )
            """,
            "criar_empresas": """
            CREATE TABLE IF NOT EXISTS empresas (
                emp_cnpj VARCHAR PRIMARY KEY,
                emp_end_id INT,
                emp_razaosocial VARCHAR(100) NOT NULL,
                emp_nomefantasia VARCHAR(100) NOT NULL,
                emp_inscricaoestadual VARCHAR(40),
                emp_email VARCHAR(40) NOT NULL,
                emp_fone VARCHAR(20) NOT NULL,
                emp_site VARCHAR(100),
                CONSTRAINT fk_emp_end
                    FOREIGN KEY(emp_end_id) 
                        REFERENCES endereco(end_id)
                        ON DELETE CASCADE
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
            "criar_cliente": """
           CREATE TABLE IF NOT EXISTS cliente (
               clie_id SERIAL PRIMARY KEY,
               clie_pessoa_id INT,
               CONSTRAINT fk_clie_pess
                   FOREIGN KEY(clie_pessoa_id) 
                       REFERENCES pessoas(pess_id)
                       ON DELETE CASCADE      
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
            "criar_fornecedor": """
           CREATE TABLE IF NOT EXISTS fornecedor (
               forn_id SERIAL PRIMARY KEY,
               forn_end_id INT,
               forn_nome VARCHAR(50) NOT NULL,
               forn_cnpj VARCHAR(20) NOT NULL,            
               forn_email VARCHAR(60) NOT NULL,
               forn_fone VARCHAR(50),
               CONSTRAINT fk_forn_end
                   FOREIGN KEY(forn_end_id) 
                       REFERENCES endereco(end_id)
                       ON DELETE CASCADE         
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
            "criar_serviços": """
           CREATE TABLE IF NOT EXISTS servicos (
               serv_id SERIAL PRIMARY KEY,
               serv_desc VARCHAR(60) NOT NULL,
               serv_preco FLOAT NOT NULL
           )
           """,
            "criar_vendatmp": """
           CREATE TABLE IF NOT EXISTS venda_tmp (
               venda_cod_interno SERIAL PRIMARY KEY,
               venda_veic_placa VARCHAR(15),
               venda_id INT NOT NULL,
               venda_prod_serv_id INT NOT NULL,
               venda_tipo VARCHAR(15) NOT NULL,
               venda_qtd INT DEFAULT 1,
               venda_valor FLOAT NOT NULL,
               venda_desconto FLOAT,
               venda_datahora TIMESTAMP,
               FOREIGN KEY (venda_veic_placa)
                   REFERENCES veiculo (veic_placa)
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
            "criar_venda_cabeçalho": """
                       CREATE TABLE IF NOT EXISTS vendas (
                           venda_id INT PRIMARY KEY,
                           venda_veic_placa VARCHAR(15),
                           venda_qtd_itens INT,
                           venda_total_descontos FLOAT,
                           venda_valor_total FLOAT,
                           venda_status VARCHAR(50),
                            FOREIGN KEY (venda_veic_placa)
                               REFERENCES veiculo (veic_placa)
                               ON UPDATE CASCADE ON DELETE CASCADE 
                       )
                       """,

            "criar_procedure_usuario": """
                   CREATE OR REPLACE PROCEDURE add_usuario(
                           rua VARCHAR,
                           bairro VARCHAR,
                           nro VARCHAR,
                           cidade VARCHAR,
                           estado VARCHAR,
                           cep VARCHAR,
                           cpf VARCHAR,
                           nome VARCHAR,
                           fone VARCHAR,
                           email VARCHAR,
                           rg VARCHAR,
                           celular VARCHAR,
                           tipo VARCHAR,
                           usuario VARCHAR,
                           senha VARCHAR,
                           emp_cnpj VARCHAR,
                           nivel_acesso VARCHAR
                   ) 
                   AS $$
                   DECLARE
                       f_end_id INT;
                       f_pess_id INT;
                   BEGIN
                       -- inserindo endereço
                       INSERT INTO endereco (end_rua, end_bairro, end_numero, end_cidade, end_estado, end_cep)
                       VALUES (rua, bairro, nro, cidade, estado, cep)
                       RETURNING end_id INTO f_end_id;

                       -- inserindo pessoa
                       INSERT INTO pessoas (pess_end_id, pess_cpf, pess_nome, pess_fone, 
                       pess_email, pess_rg, pess_celular, pess_tipo)
                       VALUES(f_end_id, cpf, nome, fone, email, rg, celular, tipo)
                       RETURNING pess_id INTO f_pess_id;

                       -- inserindo usuário
                       INSERT INTO usuarios (usu_pessoa_id, usu_emp_cnpj, usu_nome, usu_senha, usu_nivel_acesso)
                       VALUEs(f_pess_id, emp_cnpj, usuario, senha, nivel_acesso);

                   END;
                   $$
                   LANGUAGE PLPGSQL;

               """,
            "criar_procedure_fornecedor": """
           CREATE OR REPLACE PROCEDURE add_fornecedor(
                           rua VARCHAR,
                           bairro VARCHAR,
                           nro VARCHAR,
                           cidade VARCHAR,
                           estado VARCHAR,
                           cep VARCHAR,
                           cnpj VARCHAR,
                           nome VARCHAR,
                           fone VARCHAR,
                           email VARCHAR                                                
                   ) 
                   AS $$
                   DECLARE
                       f_end_id INT;
                   BEGIN
                       -- inserindo endereço
                       INSERT INTO endereco (end_rua, end_bairro, end_numero, end_cidade, end_estado, end_cep)
                       VALUES (rua, bairro, nro, cidade, estado, cep)
                       RETURNING end_id INTO f_end_id;

                       -- inserindo fornecedor
                       INSERT INTO fornecedor (forn_end_id, forn_nome, forn_cnpj, forn_email, forn_fone)
                       VALUEs(f_end_id, nome, cnpj, email, fone);
                   END;
                   $$
                   LANGUAGE PLPGSQL;
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
           """,
            "criar_procedure_empresa": """
           CREATE OR REPLACE PROCEDURE add_empresa(
                               rua VARCHAR,
                               bairro VARCHAR,
                               nro VARCHAR,
                               cidade VARCHAR,
                               estado VARCHAR,
                               cep VARCHAR,            	
                               cnpj VARCHAR,
                               nomefantasia VARCHAR, 
                               razaosocial VARCHAR,
                               inscricao VARCHAR,
                               fone VARCHAR,
                               site VARCHAR,
                               email VARCHAR
                       ) 
                   AS $$
                   DECLARE
                       f_end_id INT;
                   BEGIN
                       -- inserindo endereço
                       INSERT INTO endereco (end_rua, end_bairro, end_numero, end_cidade, end_estado, end_cep)
                       VALUES (rua, bairro, nro, cidade, estado, cep)
                       RETURNING end_id INTO f_end_id;

                       -- inserindo empresa
                           INSERT INTO empresas (emp_cnpj, emp_end_id, emp_razaosocial, emp_nomefantasia
                           , 
                                                 emp_inscricaoestadual, emp_email, emp_fone, emp_site) 
                           VALUES (cnpj, f_end_id, razaosocial, nomefantasia, inscricao, email,
                                  fone, site);

                       END;
                   $$
                   LANGUAGE PLPGSQL;
           """,
            "criar_procedure_clientes": """
           CREATE OR REPLACE PROCEDURE add_clientes(
                           rua VARCHAR,
                           bairro VARCHAR,
                           nro VARCHAR,
                           cidade VARCHAR,
                           estado VARCHAR,
                           cep VARCHAR,
                           cpf VARCHAR,
                           nome VARCHAR,
                           fone VARCHAR,
                           email VARCHAR,
                           rg VARCHAR,
                           celular VARCHAR,
                           tipo VARCHAR                      
                   ) 
                   AS $$
                   DECLARE
                       f_end_id INT;
                       f_pess_id INT;
                   BEGIN
                       -- inserindo endereço
                       INSERT INTO endereco (end_rua, end_bairro, end_numero, end_cidade, end_estado, end_cep)
                       VALUES (rua, bairro, nro, cidade, estado, cep)
                       RETURNING end_id INTO f_end_id;

                       -- inserindo pessoa
                       INSERT INTO pessoas (pess_end_id, pess_cpf, pess_nome, pess_fone, 
                       pess_email, pess_rg, pess_celular, pess_tipo)
                       VALUES(f_end_id, cpf, nome, fone, email, rg, celular, tipo)
                       RETURNING pess_id INTO f_pess_id;

                       -- inserindo CLIENTE
                       INSERT INTO cliente (clie_pessoa_id)
                       VALUES(f_pess_id);

                   END;
                   $$
                   LANGUAGE PLPGSQL;
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
        from Funcoes.funcoes import show_msg
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
