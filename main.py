if __name__ == '__main__':
    from Model.Operador import Operador
    from Funcoes.configdb import Banco
    import sys
    from PyQt5.QtWidgets import QApplication
    from Funcoes.criar_tabelas import create_tables
    from Controller.tela_principal import exec_main
    from Controller.login import exec_login
    from Controller.configuracao_db import exec_conf_db
    from Funcoes.utils import except_hook

    conexao = Banco()
    conexao.conecta()
    sys.excepthook = except_hook
    app = QApplication(sys.argv)

    if conexao.conectado:

        create_tables()
        if Operador.verifica_operador_ativo():
            exec_main()
        else:
            exec_login()
    else:
        exec_conf_db()
