# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/tela_principal.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Funcoes.classes import Label


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(450, 280, 301, 241))
        self.frame.setStyleSheet("background-color: rgb(211, 215, 207);\n"
"background-color: rgb(238, 238, 236);\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lbl_usuario = QtWidgets.QLabel(self.frame)
        self.lbl_usuario.setStyleSheet("color: rgb(238, 238, 236);\n"
"color: rgb(0, 0, 0);")
        self.lbl_usuario.setObjectName("lbl_usuario")
        self.verticalLayout_2.addWidget(self.lbl_usuario)
        self.lbl_ip = QtWidgets.QLabel(self.frame)
        self.lbl_ip.setStyleSheet("color: rgb(238, 238, 236);\n"
"color: rgb(0, 0, 0);")
        self.lbl_ip.setObjectName("lbl_ip")
        self.verticalLayout_2.addWidget(self.lbl_ip)
        self.lbl_bd = QtWidgets.QLabel(self.frame)
        self.lbl_bd.setStyleSheet("color: rgb(238, 238, 236);\n"
"color: rgb(0, 0, 0);")
        self.lbl_bd.setObjectName("lbl_bd")
        self.verticalLayout_2.addWidget(self.lbl_bd)
        self.lbl_data = QtWidgets.QLabel(self.frame)
        self.lbl_data.setStyleSheet("color: rgb(238, 238, 236);\n"
"color: rgb(0, 0, 0);")
        self.lbl_data.setObjectName("lbl_data")
        self.verticalLayout_2.addWidget(self.lbl_data)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setStyleSheet("color: rgb(238, 238, 236);\n"
"color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.frame_atalhos = QtWidgets.QFrame(self.centralwidget)
        self.frame_atalhos.setGeometry(QtCore.QRect(0, 0, 801, 61))
        self.frame_atalhos.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.frame_atalhos.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_atalhos.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_atalhos.setObjectName("frame_atalhos")
        self.lbl_atalho_venda_txt = Label(self.frame_atalhos)
        self.lbl_atalho_venda_txt.setGeometry(QtCore.QRect(6, 40, 111, 20))
        self.lbl_atalho_venda_txt.setObjectName("lbl_atalho_venda_txt")
        self.lbl_atalho_venda = Label(self.frame_atalhos)
        self.lbl_atalho_venda.setGeometry(QtCore.QRect(50, 10, 41, 31))
        self.lbl_atalho_venda.setText("")
        self.lbl_atalho_venda.setPixmap(QtGui.QPixmap("Imagens/add_venda.png"))
        self.lbl_atalho_venda.setObjectName("lbl_atalho_venda")
        self.lbl_atalho_vis_venda_txt = Label(self.frame_atalhos)
        self.lbl_atalho_vis_venda_txt.setGeometry(QtCore.QRect(136, 40, 111, 20))
        self.lbl_atalho_vis_venda_txt.setObjectName("lbl_atalho_vis_venda_txt")
        self.lbl_atalho_vis_venda = Label(self.frame_atalhos)
        self.lbl_atalho_vis_venda.setGeometry(QtCore.QRect(180, 10, 41, 31))
        self.lbl_atalho_vis_venda.setText("")
        self.lbl_atalho_vis_venda.setPixmap(QtGui.QPixmap("Imagens/visualiza.png"))
        self.lbl_atalho_vis_venda.setObjectName("lbl_atalho_vis_venda")
        self.lbl_atalho_abrir_venda = Label(self.frame_atalhos)
        self.lbl_atalho_abrir_venda.setGeometry(QtCore.QRect(260, 40, 111, 20))
        self.lbl_atalho_abrir_venda.setObjectName("lbl_atalho_abrir_venda")
        self.lbl_atalho_abrir_venda_txt = Label(self.frame_atalhos)
        self.lbl_atalho_abrir_venda_txt.setGeometry(QtCore.QRect(300, 10, 41, 31))
        self.lbl_atalho_abrir_venda_txt.setText("")
        self.lbl_atalho_abrir_venda_txt.setPixmap(QtGui.QPixmap("Imagens/abrir_venda.png"))
        self.lbl_atalho_abrir_venda_txt.setObjectName("lbl_atalho_abrir_venda_txt")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menu_cadastros = QtWidgets.QMenu(self.menubar)
        self.menu_cadastros.setObjectName("menu_cadastros")
        self.menu_visualizar = QtWidgets.QMenu(self.menubar)
        self.menu_visualizar.setObjectName("menu_visualizar")
        self.menu_venda = QtWidgets.QMenu(self.menubar)
        self.menu_venda.setObjectName("menu_venda")
        self.menuConfigura_o = QtWidgets.QMenu(self.menubar)
        self.menuConfigura_o.setObjectName("menuConfigura_o")
        self.menuSair = QtWidgets.QMenu(self.menubar)
        self.menuSair.setObjectName("menuSair")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionCadastroUsuarios = QtWidgets.QAction(MainWindow)
        self.actionCadastroUsuarios.setObjectName("actionCadastroUsuarios")
        self.actionCadastroEmpresas = QtWidgets.QAction(MainWindow)
        self.actionCadastroEmpresas.setObjectName("actionCadastroEmpresas")
        self.actionCadastroClientes = QtWidgets.QAction(MainWindow)
        self.actionCadastroClientes.setObjectName("actionCadastroClientes")
        self.actionCadastroVeiculos = QtWidgets.QAction(MainWindow)
        self.actionCadastroVeiculos.setObjectName("actionCadastroVeiculos")
        self.actionCadastroFornecedores = QtWidgets.QAction(MainWindow)
        self.actionCadastroFornecedores.setObjectName("actionCadastroFornecedores")
        self.actionCadastroServicos = QtWidgets.QAction(MainWindow)
        self.actionCadastroServicos.setObjectName("actionCadastroServicos")
        self.actionCadastroProdutos = QtWidgets.QAction(MainWindow)
        self.actionCadastroProdutos.setObjectName("actionCadastroProdutos")
        self.actionSaidaOperador = QtWidgets.QAction(MainWindow)
        self.actionSaidaOperador.setObjectName("actionSaidaOperador")
        self.actionSair_do_Sistema = QtWidgets.QAction(MainWindow)
        self.actionSair_do_Sistema.setObjectName("actionSair_do_Sistema")
        self.actionBanco_de_Dados = QtWidgets.QAction(MainWindow)
        self.actionBanco_de_Dados.setObjectName("actionBanco_de_Dados")
        self.actionNova_Venda = QtWidgets.QAction(MainWindow)
        self.actionNova_Venda.setObjectName("actionNova_Venda")
        self.actionVisualizar_Vendas = QtWidgets.QAction(MainWindow)
        self.actionVisualizar_Vendas.setObjectName("actionVisualizar_Vendas")
        self.actionVisualizaClientes = QtWidgets.QAction(MainWindow)
        self.actionVisualizaClientes.setObjectName("actionVisualizaClientes")
        self.actionVisualizaServicos = QtWidgets.QAction(MainWindow)
        self.actionVisualizaServicos.setObjectName("actionVisualizaServicos")
        self.actionVisualizaProdutos = QtWidgets.QAction(MainWindow)
        self.actionVisualizaProdutos.setObjectName("actionVisualizaProdutos")
        self.actionVisualizaFornecedores = QtWidgets.QAction(MainWindow)
        self.actionVisualizaFornecedores.setObjectName("actionVisualizaFornecedores")
        self.actionVisualizaEmpresas = QtWidgets.QAction(MainWindow)
        self.actionVisualizaEmpresas.setObjectName("actionVisualizaEmpresas")
        self.actionVisualizaUsuarios = QtWidgets.QAction(MainWindow)
        self.actionVisualizaUsuarios.setObjectName("actionVisualizaUsuarios")
        self.actionCadastroCategorias = QtWidgets.QAction(MainWindow)
        self.actionCadastroCategorias.setObjectName("actionCadastroCategorias")
        self.actionVisualizaCategorias = QtWidgets.QAction(MainWindow)
        self.actionVisualizaCategorias.setObjectName("actionVisualizaCategorias")
        self.actionVisualizaEndereco = QtWidgets.QAction(MainWindow)
        self.actionVisualizaEndereco.setObjectName("actionVisualizaEndereco")
        self.actionVisualizaVeiculos = QtWidgets.QAction(MainWindow)
        self.actionVisualizaVeiculos.setObjectName("actionVisualizaVeiculos")
        self.actionCadastroFinalizadoras = QtWidgets.QAction(MainWindow)
        self.actionCadastroFinalizadoras.setObjectName("actionCadastroFinalizadoras")
        self.actionVisualizaFinalizadoras = QtWidgets.QAction(MainWindow)
        self.actionVisualizaFinalizadoras.setObjectName("actionVisualizaFinalizadoras")
        self.actionAbrir_Venda = QtWidgets.QAction(MainWindow)
        self.actionAbrir_Venda.setObjectName("actionAbrir_Venda")
        self.menu_cadastros.addAction(self.actionCadastroUsuarios)
        self.menu_cadastros.addAction(self.actionCadastroEmpresas)
        self.menu_cadastros.addAction(self.actionCadastroClientes)
        self.menu_cadastros.addAction(self.actionCadastroVeiculos)
        self.menu_cadastros.addAction(self.actionCadastroFornecedores)
        self.menu_cadastros.addAction(self.actionCadastroProdutos)
        self.menu_cadastros.addAction(self.actionCadastroServicos)
        self.menu_cadastros.addAction(self.actionCadastroCategorias)
        self.menu_cadastros.addAction(self.actionCadastroFinalizadoras)
        self.menu_visualizar.addAction(self.actionVisualizaUsuarios)
        self.menu_visualizar.addAction(self.actionVisualizaEmpresas)
        self.menu_visualizar.addAction(self.actionVisualizaClientes)
        self.menu_visualizar.addAction(self.actionVisualizaVeiculos)
        self.menu_visualizar.addAction(self.actionVisualizaFornecedores)
        self.menu_visualizar.addAction(self.actionVisualizaProdutos)
        self.menu_visualizar.addAction(self.actionVisualizaServicos)
        self.menu_visualizar.addAction(self.actionVisualizaCategorias)
        self.menu_visualizar.addAction(self.actionVisualizaEndereco)
        self.menu_visualizar.addAction(self.actionVisualizaFinalizadoras)
        self.menu_venda.addAction(self.actionNova_Venda)
        self.menu_venda.addAction(self.actionVisualizar_Vendas)
        self.menu_venda.addAction(self.actionAbrir_Venda)
        self.menuConfigura_o.addAction(self.actionBanco_de_Dados)
        self.menuSair.addAction(self.actionSaidaOperador)
        self.menuSair.addAction(self.actionSair_do_Sistema)
        self.menubar.addAction(self.menu_cadastros.menuAction())
        self.menubar.addAction(self.menu_visualizar.menuAction())
        self.menubar.addAction(self.menu_venda.menuAction())
        self.menubar.addAction(self.menuConfigura_o.menuAction())
        self.menubar.addAction(self.menuSair.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FZR Sistemas"))
        self.lbl_usuario.setText(_translate("MainWindow", "Usuário: FELIPE ZAGO RODRIGUES"))
        self.lbl_ip.setText(_translate("MainWindow", "Ip: 127.000.000.1"))
        self.lbl_bd.setText(_translate("MainWindow", "Base de dados: controles"))
        self.lbl_data.setText(_translate("MainWindow", "12/02/2021 23:00:00"))
        self.label.setText(_translate("MainWindow", "FZR Sistemas"))
        self.lbl_atalho_venda_txt.setText(_translate("MainWindow", "F5 - Nova Venda"))
        self.lbl_atalho_vis_venda_txt.setText(_translate("MainWindow", "F6 - Vis. Vendas"))
        self.lbl_atalho_abrir_venda.setText(_translate("MainWindow", "F7 - Abrir Venda"))
        self.menu_cadastros.setTitle(_translate("MainWindow", "Cadastros"))
        self.menu_visualizar.setTitle(_translate("MainWindow", "Visualizar"))
        self.menu_venda.setTitle(_translate("MainWindow", "Venda"))
        self.menuConfigura_o.setTitle(_translate("MainWindow", "Configuração"))
        self.menuSair.setTitle(_translate("MainWindow", "Sair"))
        self.actionCadastroUsuarios.setText(_translate("MainWindow", "Usuários"))
        self.actionCadastroEmpresas.setText(_translate("MainWindow", "Empresas"))
        self.actionCadastroClientes.setText(_translate("MainWindow", "Clientes"))
        self.actionCadastroVeiculos.setText(_translate("MainWindow", "Veículos"))
        self.actionCadastroFornecedores.setText(_translate("MainWindow", "Fornecedores"))
        self.actionCadastroServicos.setText(_translate("MainWindow", "Serviços"))
        self.actionCadastroProdutos.setText(_translate("MainWindow", "Produtos"))
        self.actionSaidaOperador.setText(_translate("MainWindow", "Saída de Operador"))
        self.actionSair_do_Sistema.setText(_translate("MainWindow", "Sair do Sistema"))
        self.actionBanco_de_Dados.setText(_translate("MainWindow", "Banco de Dados"))
        self.actionNova_Venda.setText(_translate("MainWindow", "Nova Venda"))
        self.actionVisualizar_Vendas.setText(_translate("MainWindow", "Visualizar Vendas"))
        self.actionVisualizaClientes.setText(_translate("MainWindow", "Clientes"))
        self.actionVisualizaServicos.setText(_translate("MainWindow", "Serviços"))
        self.actionVisualizaProdutos.setText(_translate("MainWindow", "Produtos"))
        self.actionVisualizaFornecedores.setText(_translate("MainWindow", "Fornecedores"))
        self.actionVisualizaEmpresas.setText(_translate("MainWindow", "Empresas"))
        self.actionVisualizaUsuarios.setText(_translate("MainWindow", "Usuarios"))
        self.actionCadastroCategorias.setText(_translate("MainWindow", "Categorias"))
        self.actionVisualizaCategorias.setText(_translate("MainWindow", "Categorias"))
        self.actionVisualizaEndereco.setText(_translate("MainWindow", "Endereço"))
        self.actionVisualizaVeiculos.setText(_translate("MainWindow", "Veiculos"))
        self.actionCadastroFinalizadoras.setText(_translate("MainWindow", "Finalizadoras"))
        self.actionVisualizaFinalizadoras.setText(_translate("MainWindow", "Finalizadoras"))
        self.actionAbrir_Venda.setText(_translate("MainWindow", "Abrir Venda"))
