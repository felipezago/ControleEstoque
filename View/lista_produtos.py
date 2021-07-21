# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lista_produtos.ui'
#
# Created by: PyQt5 View code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(1048, 562)
        Frame.setAutoFillBackground(False)
        Frame.setStyleSheet("background: #FFF;")
        self.fr_titulo_servicos = QtWidgets.QFrame(Frame)
        self.fr_titulo_servicos.setGeometry(QtCore.QRect(0, 0, 1051, 60))
        self.fr_titulo_servicos.setStyleSheet("")
        self.fr_titulo_servicos.setObjectName("fr_titulo_servicos")
        self.lb_tituloClientes_2 = QtWidgets.QLabel(self.fr_titulo_servicos)
        self.lb_tituloClientes_2.setGeometry(QtCore.QRect(10, 15, 200, 30))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lb_tituloClientes_2.setFont(font)
        self.lb_tituloClientes_2.setStyleSheet("color: rgb(0, 0, 0)")
        self.lb_tituloClientes_2.setObjectName("lb_tituloClientes_2")
        self.bt_novo = QtWidgets.QPushButton(self.fr_titulo_servicos)
        self.bt_novo.setGeometry(QtCore.QRect(890, 10, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bt_novo.setFont(font)
        self.bt_novo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_novo.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_novo.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.bt_novo.setStyleSheet("QPushButton {\n"
"background-color: #7AB32E;\n"
"color: #FFF\n"
" }\n"
"QPushButton:hover{\n"
"background-color: #40a286\n"
"}")
        self.bt_novo.setIconSize(QtCore.QSize(75, 35))
        self.bt_novo.setObjectName("bt_novo")
        self.tb_produtos = QtWidgets.QTableWidget(Frame)
        self.tb_produtos.setGeometry(QtCore.QRect(0, 100, 1041, 211))
        self.tb_produtos.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tb_produtos.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tb_produtos.setStyleSheet("QTableView{\n"
"color: #797979;\n"
"font-weight: bold;\n"
"font-size: 13px;\n"
"background: #FFF;\n"
"padding: 0 0 0 5px;\n"
"}\n"
"QHeaderView:section{\n"
"background: #FFF;\n"
"padding: 5px 0 ;\n"
"font-size: 12px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #797979;\n"
"border: none;\n"
"border-bottom: 2px solid #CCC;\n"
"text-transform: uppercase\n"
"}\n"
"QTableView::item {\n"
"border-bottom: 2px solid #CCC;\n"
"padding: 2px;\n"
"}\n"
"\n"
"")
        self.tb_produtos.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tb_produtos.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tb_produtos.setAutoScrollMargin(20)
        self.tb_produtos.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tb_produtos.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tb_produtos.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tb_produtos.setShowGrid(False)
        self.tb_produtos.setGridStyle(QtCore.Qt.NoPen)
        self.tb_produtos.setWordWrap(False)
        self.tb_produtos.setRowCount(1)
        self.tb_produtos.setObjectName("tb_produtos")
        self.tb_produtos.setColumnCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.tb_produtos.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_produtos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_produtos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_produtos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_produtos.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_produtos.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_produtos.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_produtos.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_produtos.setHorizontalHeaderItem(7, item)
        self.tb_produtos.horizontalHeader().setDefaultSectionSize(120)
        self.tb_produtos.horizontalHeader().setHighlightSections(False)
        self.tb_produtos.horizontalHeader().setStretchLastSection(True)
        self.tb_produtos.verticalHeader().setVisible(False)
        self.tb_produtos.verticalHeader().setDefaultSectionSize(50)
        self.tb_produtos.verticalHeader().setMinimumSectionSize(20)
        self.lb_FormProdutos_6 = QtWidgets.QLabel(Frame)
        self.lb_FormProdutos_6.setGeometry(QtCore.QRect(80, 360, 181, 20))
        self.lb_FormProdutos_6.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_6.setObjectName("lb_FormProdutos_6")
        self.tx_codbarras = QtWidgets.QLineEdit(Frame)
        self.tx_codbarras.setGeometry(QtCore.QRect(80, 380, 161, 25))
        self.tx_codbarras.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_codbarras.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"padding-left: 3px;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_codbarras.setText("")
        self.tx_codbarras.setPlaceholderText("")
        self.tx_codbarras.setObjectName("tx_codbarras")
        self.fr_botoes = QtWidgets.QFrame(Frame)
        self.fr_botoes.setGeometry(QtCore.QRect(0, 530, 1051, 30))
        self.fr_botoes.setStyleSheet("background:#E1DFE0;\n"
"border: none;")
        self.fr_botoes.setObjectName("fr_botoes")
        self.bt_cancelar = QtWidgets.QPushButton(self.fr_botoes)
        self.bt_cancelar.setGeometry(QtCore.QRect(930, 0, 120, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bt_cancelar.setFont(font)
        self.bt_cancelar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_cancelar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_cancelar.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.bt_cancelar.setStyleSheet("QPushButton {\n"
"background-color: #1E87F0;\n"
"color: #FFF\n"
" }\n"
"QPushButton:hover{\n"
"background-color: #40a286\n"
"}")
        self.bt_cancelar.setIconSize(QtCore.QSize(75, 35))
        self.bt_cancelar.setObjectName("bt_cancelar")
        self.bt_salvar = QtWidgets.QPushButton(self.fr_botoes)
        self.bt_salvar.setGeometry(QtCore.QRect(670, 0, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bt_salvar.setFont(font)
        self.bt_salvar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_salvar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_salvar.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.bt_salvar.setStyleSheet("QPushButton {\n"
"    background-color: rgb(186, 176, 48);\n"
"color: #FFF\n"
" }\n"
"QPushButton:hover{\n"
"    background-color: rgb(217, 202, 49);\n"
"}")
        self.bt_salvar.setIconSize(QtCore.QSize(75, 35))
        self.bt_salvar.setObjectName("bt_salvar")
        self.bt_excluir = QtWidgets.QPushButton(self.fr_botoes)
        self.bt_excluir.setGeometry(QtCore.QRect(800, 0, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bt_excluir.setFont(font)
        self.bt_excluir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_excluir.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_excluir.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.bt_excluir.setStyleSheet("QPushButton {\n"
"    background-color: rgb(203, 46, 46);\n"
"color: #FFF\n"
" }\n"
"QPushButton:hover{\n"
"    background-color: rgb(253, 99, 99);\n"
"}")
        self.bt_excluir.setIconSize(QtCore.QSize(75, 35))
        self.bt_excluir.setObjectName("bt_excluir")
        self.tx_id = QtWidgets.QLineEdit(Frame)
        self.tx_id.setGeometry(QtCore.QRect(10, 380, 61, 25))
        self.tx_id.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_id.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"padding-left: 3px;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_id.setInputMask("")
        self.tx_id.setText("")
        self.tx_id.setPlaceholderText("")
        self.tx_id.setObjectName("tx_id")
        self.lb_FormProdutos_7 = QtWidgets.QLabel(Frame)
        self.lb_FormProdutos_7.setGeometry(QtCore.QRect(10, 360, 61, 20))
        self.lb_FormProdutos_7.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_7.setObjectName("lb_FormProdutos_7")
        self.lb_FormProdutos_8 = QtWidgets.QLabel(Frame)
        self.lb_FormProdutos_8.setGeometry(QtCore.QRect(250, 360, 111, 20))
        self.lb_FormProdutos_8.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_8.setObjectName("lb_FormProdutos_8")
        self.tx_estoque = QtWidgets.QLineEdit(Frame)
        self.tx_estoque.setGeometry(QtCore.QRect(250, 380, 71, 25))
        self.tx_estoque.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_estoque.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"padding-left: 3px;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_estoque.setInputMask("")
        self.tx_estoque.setText("")
        self.tx_estoque.setPlaceholderText("")
        self.tx_estoque.setObjectName("tx_estoque")
        self.lb_FormProdutos_10 = QtWidgets.QLabel(Frame)
        self.lb_FormProdutos_10.setGeometry(QtCore.QRect(540, 360, 111, 20))
        self.lb_FormProdutos_10.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_10.setObjectName("lb_FormProdutos_10")
        self.tx_marca = QtWidgets.QLineEdit(Frame)
        self.tx_marca.setGeometry(QtCore.QRect(540, 380, 201, 25))
        self.tx_marca.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_marca.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"padding-left: 3px;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_marca.setInputMask("")
        self.tx_marca.setText("")
        self.tx_marca.setPlaceholderText("")
        self.tx_marca.setObjectName("tx_marca")
        self.lb_FormProdutos_11 = QtWidgets.QLabel(Frame)
        self.lb_FormProdutos_11.setGeometry(QtCore.QRect(750, 360, 111, 20))
        self.lb_FormProdutos_11.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_11.setObjectName("lb_FormProdutos_11")
        self.tx_preco = QtWidgets.QLineEdit(Frame)
        self.tx_preco.setGeometry(QtCore.QRect(750, 380, 121, 25))
        self.tx_preco.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_preco.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"padding-left: 3px;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_preco.setInputMask("")
        self.tx_preco.setText("")
        self.tx_preco.setPlaceholderText("")
        self.tx_preco.setObjectName("tx_preco")
        self.lb_FormProdutos_12 = QtWidgets.QLabel(Frame)
        self.lb_FormProdutos_12.setGeometry(QtCore.QRect(330, 360, 111, 20))
        self.lb_FormProdutos_12.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_12.setObjectName("lb_FormProdutos_12")
        self.tx_descricao = QtWidgets.QLineEdit(Frame)
        self.tx_descricao.setGeometry(QtCore.QRect(330, 380, 201, 25))
        self.tx_descricao.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_descricao.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"padding-left: 3px;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_descricao.setInputMask("")
        self.tx_descricao.setText("")
        self.tx_descricao.setPlaceholderText("")
        self.tx_descricao.setObjectName("tx_descricao")
        self.lb_FormProdutos_2 = QtWidgets.QLabel(Frame)
        self.lb_FormProdutos_2.setGeometry(QtCore.QRect(10, 320, 1031, 30))
        self.lb_FormProdutos_2.setStyleSheet("QLabel{\n"
"font-size: 14px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"\n"
"border-bottom: 2px solid #A2A2A2\n"
"}")
        self.lb_FormProdutos_2.setObjectName("lb_FormProdutos_2")
        self.bt_refresh = QtWidgets.QPushButton(Frame)
        self.bt_refresh.setGeometry(QtCore.QRect(1010, 60, 30, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.bt_refresh.setFont(font)
        self.bt_refresh.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_refresh.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_refresh.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.bt_refresh.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Imagens/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_refresh.setIcon(icon)
        self.bt_refresh.setObjectName("bt_refresh")
        self.tx_busca = QtWidgets.QLineEdit(Frame)
        self.tx_busca.setGeometry(QtCore.QRect(190, 60, 791, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.tx_busca.setFont(font)
        self.tx_busca.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tx_busca.setStyleSheet("QLineEdit {\n"
"color: #000\n"
"}\n"
"")
        self.tx_busca.setObjectName("tx_busca")
        self.cb_produtos = QtWidgets.QComboBox(Frame)
        self.cb_produtos.setGeometry(QtCore.QRect(10, 60, 171, 31))
        self.cb_produtos.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.cb_produtos.setStyleSheet("QComboBox{\n"
"background: #fff;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase\n"
"}\n"
"QComboBox:Focus {\n"
"border: 1px solid red;\n"
"}\n"
" QComboBox::drop-down {\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 25px;\n"
"     border-left-width: 1px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"QComboBox::down-arrow {\n"
"     image: url(\"Imagens/down.png\");\n"
" }\n"
"")
        self.cb_produtos.setObjectName("cb_produtos")
        self.cb_produtos.addItem("")
        self.bt_busca = QtWidgets.QPushButton(Frame)
        self.bt_busca.setGeometry(QtCore.QRect(980, 60, 30, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.bt_busca.setFont(font)
        self.bt_busca.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_busca.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_busca.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.bt_busca.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Imagens/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_busca.setIcon(icon1)
        self.bt_busca.setObjectName("bt_busca")
        self.lb_foto_prod = QtWidgets.QLabel(Frame)
        self.lb_foto_prod.setGeometry(QtCore.QRect(880, 380, 161, 141))
        self.lb_foto_prod.setStyleSheet("border: 1px solid #A2A2A2;\n")
        self.lb_foto_prod.setText("")
        self.lb_foto_prod.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_foto_prod.setObjectName("lb_foto_prod")
        self.bt_DelLogo = QtWidgets.QPushButton(Frame)
        self.bt_DelLogo.setGeometry(QtCore.QRect(1010, 490, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.bt_DelLogo.setFont(font)
        self.bt_DelLogo.setStyleSheet("QPushButton{\n"
"background: #7AB32E;\n"
"color: #FFF\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #40a286\n"
"}")
        self.bt_DelLogo.setText("")
        self.bt_DelLogo.setObjectName("bt_DelLogo")
        self.bt_AddLogo = QtWidgets.QPushButton(Frame)
        self.bt_AddLogo.setGeometry(QtCore.QRect(1010, 490, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.bt_AddLogo.setFont(font)
        self.bt_AddLogo.setStyleSheet("QPushButton{\n"
"background: #7AB32E;\n"
"color: #FFF\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #40a286\n"
"}")
        self.bt_AddLogo.setText("")
        self.bt_AddLogo.setObjectName("bt_AddLogo")
        self.lb_FormFornecedor_21 = QtWidgets.QLabel(Frame)
        self.lb_FormFornecedor_21.setGeometry(QtCore.QRect(880, 360, 150, 20))
        self.lb_FormFornecedor_21.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_21.setObjectName("lb_FormFornecedor_21")
        self.cb_fornecedor = QtWidgets.QComboBox(Frame)
        self.cb_fornecedor.setGeometry(QtCore.QRect(10, 430, 251, 31))
        self.cb_fornecedor.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.cb_fornecedor.setStyleSheet("QComboBox{\n"
"background: #fff;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase\n"
"}\n"
"QComboBox:Focus {\n"
"border: 1px solid red;\n"
"}\n"
" QComboBox::drop-down {\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 25px;\n"
"     border-left-width: 1px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"QComboBox::down-arrow {\n"
"     image: url(\"Imagens/down.png\");\n"
" }\n"
"")
        self.cb_fornecedor.setObjectName("cb_fornecedor")
        self.cb_fornecedor.addItem("")
        self.cb_categoria = QtWidgets.QComboBox(Frame)
        self.cb_categoria.setGeometry(QtCore.QRect(270, 430, 211, 31))
        self.cb_categoria.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.cb_categoria.setStyleSheet("QComboBox{\n"
"background: #fff;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase\n"
"}\n"
"QComboBox:Focus {\n"
"border: 1px solid red;\n"
"}\n"
" QComboBox::drop-down {\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 25px;\n"
"     border-left-width: 1px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"QComboBox::down-arrow {\n"
"     image: url(\"Imagens/down.png\");\n"
" }\n"
"")
        self.cb_categoria.setObjectName("cb_categoria")
        self.cb_categoria.addItem("")
        self.lb_FormProdutos_13 = QtWidgets.QLabel(Frame)
        self.lb_FormProdutos_13.setGeometry(QtCore.QRect(10, 410, 111, 20))
        self.lb_FormProdutos_13.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_13.setObjectName("lb_FormProdutos_13")
        self.lb_FormProdutos_14 = QtWidgets.QLabel(Frame)
        self.lb_FormProdutos_14.setGeometry(QtCore.QRect(270, 410, 111, 20))
        self.lb_FormProdutos_14.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_14.setObjectName("lb_FormProdutos_14")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

        Frame.setTabOrder(self.tx_id, self.tx_codbarras)
        Frame.setTabOrder(self.tx_codbarras, self.tx_estoque)
        Frame.setTabOrder(self.tx_estoque, self.tx_descricao)
        Frame.setTabOrder(self.tx_descricao, self.tx_marca)
        Frame.setTabOrder(self.tx_marca, self.tx_preco)
        Frame.setTabOrder(self.tx_preco, self.cb_fornecedor)
        Frame.setTabOrder(self.cb_fornecedor, self.cb_categoria)
        Frame.setTabOrder(self.cb_categoria, self.lb_foto_prod)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Lista de Produtos"))
        self.lb_tituloClientes_2.setText(_translate("Frame", "PRODUTOS"))
        self.bt_novo.setText(_translate("Frame", "NOVO PRODUTO"))
        item = self.tb_produtos.verticalHeaderItem(0)
        item.setText(_translate("Frame", "1"))
        item = self.tb_produtos.horizontalHeaderItem(0)
        item.setText(_translate("Frame", "ID"))
        item = self.tb_produtos.horizontalHeaderItem(1)
        item.setText(_translate("Frame", "CODIGO DE BARRAS"))
        item = self.tb_produtos.horizontalHeaderItem(2)
        item.setText(_translate("Frame", "ESTOQUE"))
        item = self.tb_produtos.horizontalHeaderItem(3)
        item.setText(_translate("Frame", "DESCRIÇÃO"))
        item = self.tb_produtos.horizontalHeaderItem(4)
        item.setText(_translate("Frame", "MARCA"))
        item = self.tb_produtos.horizontalHeaderItem(5)
        item.setText(_translate("Frame", "PREÇO"))
        item = self.tb_produtos.horizontalHeaderItem(6)
        item.setText(_translate("Frame", "FORNECEDOR"))
        item = self.tb_produtos.horizontalHeaderItem(7)
        item.setText(_translate("Frame", "CATEGORIA"))
        self.lb_FormProdutos_6.setText(_translate("Frame", "CODIGO DE BARRAS"))
        self.bt_cancelar.setText(_translate("Frame", "CANCELAR"))
        self.bt_salvar.setText(_translate("Frame", "EDITAR"))
        self.bt_excluir.setText(_translate("Frame", "EXCLUIR"))
        self.lb_FormProdutos_7.setText(_translate("Frame", "ID"))
        self.lb_FormProdutos_8.setText(_translate("Frame", "ESTOQUE"))
        self.lb_FormProdutos_10.setText(_translate("Frame", "MARCA"))
        self.lb_FormProdutos_11.setText(_translate("Frame", "PREÇO"))
        self.lb_FormProdutos_12.setText(_translate("Frame", "DESCRIÇÃO"))
        self.lb_FormProdutos_2.setText(_translate("Frame", "ALTERAR INFORMAÇÕES"))
        self.bt_refresh.setToolTip(_translate("Frame", "ATUALIZAR TABELA"))
        self.tx_busca.setPlaceholderText(_translate("Frame", "PROCURAR POR..."))
        self.cb_produtos.setItemText(0, _translate("Frame", "SELECIONE"))
        self.bt_busca.setToolTip(_translate("Frame", "BUSCAR"))
        self.bt_DelLogo.setToolTip(_translate("Frame", "<html><head/><body><p>Deletar Imagem</p></body></html>"))
        self.bt_AddLogo.setToolTip(_translate("Frame", "<html><head/><body><p>CADASTRAR IMGEM</p></body></html>"))
        self.lb_FormFornecedor_21.setText(_translate("Frame", "IMAGEM DO PRODUTO"))
        self.cb_fornecedor.setItemText(0, _translate("Frame", "SELECIONE"))
        self.cb_categoria.setItemText(0, _translate("Frame", "SELECIONE"))
        self.lb_FormProdutos_13.setText(_translate("Frame", "FORNECEDOR"))
        self.lb_FormProdutos_14.setText(_translate("Frame", "CATEGORIA"))
