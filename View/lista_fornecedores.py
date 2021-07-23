# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'View/UI/lista_fornecedores.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(981, 540)
        Frame.setStyleSheet("background: #FFF;")
        self.fr_titulo_servicos = QtWidgets.QFrame(Frame)
        self.fr_titulo_servicos.setGeometry(QtCore.QRect(0, 0, 981, 60))
        self.fr_titulo_servicos.setStyleSheet("")
        self.fr_titulo_servicos.setObjectName("fr_titulo_servicos")
        self.lb_tituloClientes_2 = QtWidgets.QLabel(self.fr_titulo_servicos)
        self.lb_tituloClientes_2.setGeometry(QtCore.QRect(10, 15, 221, 30))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lb_tituloClientes_2.setFont(font)
        self.lb_tituloClientes_2.setStyleSheet("color: rgb(0, 0, 0)")
        self.lb_tituloClientes_2.setObjectName("lb_tituloClientes_2")
        self.bt_novo = QtWidgets.QPushButton(self.fr_titulo_servicos)
        self.bt_novo.setGeometry(QtCore.QRect(810, 10, 161, 41))
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
        self.tb_fornecedores = QtWidgets.QTableWidget(Frame)
        self.tb_fornecedores.setGeometry(QtCore.QRect(0, 100, 971, 211))
        self.tb_fornecedores.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tb_fornecedores.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tb_fornecedores.setStyleSheet("QTableView{\n"
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
        self.tb_fornecedores.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tb_fornecedores.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tb_fornecedores.setAutoScrollMargin(20)
        self.tb_fornecedores.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tb_fornecedores.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tb_fornecedores.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tb_fornecedores.setShowGrid(False)
        self.tb_fornecedores.setGridStyle(QtCore.Qt.NoPen)
        self.tb_fornecedores.setWordWrap(False)
        self.tb_fornecedores.setRowCount(1)
        self.tb_fornecedores.setObjectName("tb_fornecedores")
        self.tb_fornecedores.setColumnCount(11)
        item = QtWidgets.QTableWidgetItem()
        self.tb_fornecedores.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_fornecedores.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_fornecedores.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_fornecedores.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_fornecedores.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_fornecedores.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_fornecedores.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_fornecedores.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_fornecedores.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_fornecedores.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_fornecedores.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_fornecedores.setHorizontalHeaderItem(10, item)
        self.tb_fornecedores.horizontalHeader().setDefaultSectionSize(120)
        self.tb_fornecedores.horizontalHeader().setHighlightSections(False)
        self.tb_fornecedores.horizontalHeader().setStretchLastSection(True)
        self.tb_fornecedores.verticalHeader().setVisible(False)
        self.tb_fornecedores.verticalHeader().setDefaultSectionSize(50)
        self.tb_fornecedores.verticalHeader().setMinimumSectionSize(20)
        self.fr_botoes = QtWidgets.QFrame(Frame)
        self.fr_botoes.setGeometry(QtCore.QRect(0, 510, 991, 30))
        self.fr_botoes.setStyleSheet("background:#E1DFE0;\n"
"border: none;")
        self.fr_botoes.setObjectName("fr_botoes")
        self.bt_cancelar = QtWidgets.QPushButton(self.fr_botoes)
        self.bt_cancelar.setGeometry(QtCore.QRect(860, 0, 120, 30))
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
        self.bt_salvar.setGeometry(QtCore.QRect(600, 0, 120, 30))
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
        self.bt_excluir.setGeometry(QtCore.QRect(730, 0, 120, 30))
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
        self.tx_cnpj = QtWidgets.QLineEdit(Frame)
        self.tx_cnpj.setGeometry(QtCore.QRect(90, 380, 131, 25))
        self.tx_cnpj.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_cnpj.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"padding-left: 3px;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_cnpj.setPlaceholderText("")
        self.tx_cnpj.setObjectName("tx_cnpj")
        self.lb_FormProdutos_7 = QtWidgets.QLabel(Frame)
        self.lb_FormProdutos_7.setGeometry(QtCore.QRect(90, 360, 61, 20))
        self.lb_FormProdutos_7.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_7.setObjectName("lb_FormProdutos_7")
        self.lb_FormProdutos_8 = QtWidgets.QLabel(Frame)
        self.lb_FormProdutos_8.setGeometry(QtCore.QRect(230, 360, 111, 20))
        self.lb_FormProdutos_8.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_8.setObjectName("lb_FormProdutos_8")
        self.tx_nome_fantasia = QtWidgets.QLineEdit(Frame)
        self.tx_nome_fantasia.setGeometry(QtCore.QRect(230, 380, 361, 25))
        self.tx_nome_fantasia.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_nome_fantasia.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"padding-left: 3px;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_nome_fantasia.setInputMask("")
        self.tx_nome_fantasia.setText("")
        self.tx_nome_fantasia.setPlaceholderText("")
        self.tx_nome_fantasia.setObjectName("tx_nome_fantasia")
        self.lb_FormProdutos_10 = QtWidgets.QLabel(Frame)
        self.lb_FormProdutos_10.setGeometry(QtCore.QRect(600, 360, 111, 20))
        self.lb_FormProdutos_10.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_10.setObjectName("lb_FormProdutos_10")
        self.tx_email = QtWidgets.QLineEdit(Frame)
        self.tx_email.setGeometry(QtCore.QRect(600, 380, 241, 25))
        self.tx_email.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_email.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"padding-left: 3px;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_email.setInputMask("")
        self.tx_email.setText("")
        self.tx_email.setPlaceholderText("")
        self.tx_email.setObjectName("tx_email")
        self.lb_FormProdutos_11 = QtWidgets.QLabel(Frame)
        self.lb_FormProdutos_11.setGeometry(QtCore.QRect(850, 360, 111, 20))
        self.lb_FormProdutos_11.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_11.setObjectName("lb_FormProdutos_11")
        self.tx_fone = QtWidgets.QLineEdit(Frame)
        self.tx_fone.setGeometry(QtCore.QRect(850, 380, 121, 25))
        self.tx_fone.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_fone.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"padding-left: 3px;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_fone.setPlaceholderText("")
        self.tx_fone.setObjectName("tx_fone")
        self.lb_FormProdutos = QtWidgets.QLabel(Frame)
        self.lb_FormProdutos.setGeometry(QtCore.QRect(10, 410, 971, 30))
        self.lb_FormProdutos.setStyleSheet("QLabel{\n"
"font-size: 14px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"\n"
"border-bottom: 2px solid #A2A2A2\n"
"}")
        self.lb_FormProdutos.setObjectName("lb_FormProdutos")
        self.lb_FormProdutos_14 = QtWidgets.QLabel(Frame)
        self.lb_FormProdutos_14.setGeometry(QtCore.QRect(780, 450, 111, 20))
        self.lb_FormProdutos_14.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_14.setObjectName("lb_FormProdutos_14")
        self.tx_rua = QtWidgets.QLineEdit(Frame)
        self.tx_rua.setGeometry(QtCore.QRect(780, 470, 191, 25))
        self.tx_rua.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_rua.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"padding-left: 3px;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_rua.setInputMask("")
        self.tx_rua.setText("")
        self.tx_rua.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.tx_rua.setPlaceholderText("")
        self.tx_rua.setObjectName("tx_rua")
        self.lb_FormProdutos_15 = QtWidgets.QLabel(Frame)
        self.lb_FormProdutos_15.setGeometry(QtCore.QRect(150, 450, 111, 20))
        self.lb_FormProdutos_15.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_15.setObjectName("lb_FormProdutos_15")
        self.tx_bairro = QtWidgets.QLineEdit(Frame)
        self.tx_bairro.setGeometry(QtCore.QRect(150, 470, 241, 25))
        self.tx_bairro.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_bairro.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"padding-left: 3px;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_bairro.setInputMask("")
        self.tx_bairro.setText("")
        self.tx_bairro.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.tx_bairro.setPlaceholderText("")
        self.tx_bairro.setObjectName("tx_bairro")
        self.lb_FormProdutos_2 = QtWidgets.QLabel(Frame)
        self.lb_FormProdutos_2.setGeometry(QtCore.QRect(10, 320, 971, 30))
        self.lb_FormProdutos_2.setStyleSheet("QLabel{\n"
"font-size: 14px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"\n"
"border-bottom: 2px solid #A2A2A2\n"
"}")
        self.lb_FormProdutos_2.setObjectName("lb_FormProdutos_2")
        self.tx_numero = QtWidgets.QLineEdit(Frame)
        self.tx_numero.setGeometry(QtCore.QRect(400, 470, 101, 25))
        self.tx_numero.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_numero.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"padding-left: 3px;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_numero.setInputMask("")
        self.tx_numero.setText("")
        self.tx_numero.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.tx_numero.setPlaceholderText("")
        self.tx_numero.setObjectName("tx_numero")
        self.lb_FormProdutos_16 = QtWidgets.QLabel(Frame)
        self.lb_FormProdutos_16.setGeometry(QtCore.QRect(400, 450, 181, 20))
        self.lb_FormProdutos_16.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_16.setObjectName("lb_FormProdutos_16")
        self.lb_FormProdutos_17 = QtWidgets.QLabel(Frame)
        self.lb_FormProdutos_17.setGeometry(QtCore.QRect(510, 450, 111, 20))
        self.lb_FormProdutos_17.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_17.setObjectName("lb_FormProdutos_17")
        self.tx_cidade = QtWidgets.QLineEdit(Frame)
        self.tx_cidade.setGeometry(QtCore.QRect(510, 470, 191, 25))
        self.tx_cidade.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_cidade.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"padding-left: 3px;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_cidade.setInputMask("")
        self.tx_cidade.setText("")
        self.tx_cidade.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.tx_cidade.setPlaceholderText("")
        self.tx_cidade.setObjectName("tx_cidade")
        self.lb_FormProdutos_18 = QtWidgets.QLabel(Frame)
        self.lb_FormProdutos_18.setGeometry(QtCore.QRect(710, 450, 61, 20))
        self.lb_FormProdutos_18.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_18.setObjectName("lb_FormProdutos_18")
        self.tx_estado = QtWidgets.QLineEdit(Frame)
        self.tx_estado.setGeometry(QtCore.QRect(710, 470, 61, 25))
        self.tx_estado.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_estado.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"padding-left: 3px;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_estado.setInputMask("")
        self.tx_estado.setText("")
        self.tx_estado.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.tx_estado.setPlaceholderText("")
        self.tx_estado.setObjectName("tx_estado")
        self.tx_cep = QtWidgets.QLineEdit(Frame)
        self.tx_cep.setGeometry(QtCore.QRect(10, 470, 91, 25))
        self.tx_cep.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_cep.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"padding-left: 3px;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_cep.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.tx_cep.setPlaceholderText("")
        self.tx_cep.setObjectName("tx_cep")
        self.lb_FormProdutos_19 = QtWidgets.QLabel(Frame)
        self.lb_FormProdutos_19.setGeometry(QtCore.QRect(10, 450, 141, 20))
        self.lb_FormProdutos_19.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_19.setObjectName("lb_FormProdutos_19")
        self.bt_refresh = QtWidgets.QPushButton(Frame)
        self.bt_refresh.setGeometry(QtCore.QRect(950, 60, 30, 31))
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
        self.tx_busca.setGeometry(QtCore.QRect(190, 60, 731, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.tx_busca.setFont(font)
        self.tx_busca.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tx_busca.setStyleSheet("QLineEdit {\n"
"color: #000\n"
"}\n"
"")
        self.tx_busca.setObjectName("tx_busca")
        self.cb_fornecedores = QtWidgets.QComboBox(Frame)
        self.cb_fornecedores.setGeometry(QtCore.QRect(10, 60, 171, 31))
        self.cb_fornecedores.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.cb_fornecedores.setStyleSheet("QComboBox{\n"
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
        self.cb_fornecedores.setObjectName("cb_fornecedores")
        self.cb_fornecedores.addItem("")
        self.bt_busca = QtWidgets.QPushButton(Frame)
        self.bt_busca.setGeometry(QtCore.QRect(920, 60, 30, 31))
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
        self.lb_FormProdutos_13 = QtWidgets.QLabel(Frame)
        self.lb_FormProdutos_13.setGeometry(QtCore.QRect(10, 360, 61, 20))
        self.lb_FormProdutos_13.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_13.setObjectName("lb_FormProdutos_13")
        self.tx_id = QtWidgets.QLineEdit(Frame)
        self.tx_id.setGeometry(QtCore.QRect(10, 380, 71, 25))
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
        self.bt_busca_cep = QtWidgets.QPushButton(Frame)
        self.bt_busca_cep.setGeometry(QtCore.QRect(100, 470, 31, 25))
        self.bt_busca_cep.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Imagens/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_busca_cep.setIcon(icon2)
        self.bt_busca_cep.setObjectName("bt_busca_cep")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)
        Frame.setTabOrder(self.tx_id, self.tx_cnpj)
        Frame.setTabOrder(self.tx_cnpj, self.tx_nome_fantasia)
        Frame.setTabOrder(self.tx_nome_fantasia, self.tx_email)
        Frame.setTabOrder(self.tx_email, self.tx_fone)
        Frame.setTabOrder(self.tx_fone, self.tx_cep)
        Frame.setTabOrder(self.tx_cep, self.bt_busca_cep)
        Frame.setTabOrder(self.bt_busca_cep, self.tx_bairro)
        Frame.setTabOrder(self.tx_bairro, self.tx_numero)
        Frame.setTabOrder(self.tx_numero, self.tx_cidade)
        Frame.setTabOrder(self.tx_cidade, self.tx_estado)
        Frame.setTabOrder(self.tx_estado, self.tx_rua)
        Frame.setTabOrder(self.tx_rua, self.tb_fornecedores)
        Frame.setTabOrder(self.tb_fornecedores, self.cb_fornecedores)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Lista de Fornecedores"))
        self.lb_tituloClientes_2.setText(_translate("Frame", "FORNECEDORES"))
        self.bt_novo.setText(_translate("Frame", "NOVO FORNECEDOR"))
        item = self.tb_fornecedores.verticalHeaderItem(0)
        item.setText(_translate("Frame", "1"))
        item = self.tb_fornecedores.horizontalHeaderItem(0)
        item.setText(_translate("Frame", "ID"))
        item = self.tb_fornecedores.horizontalHeaderItem(1)
        item.setText(_translate("Frame", "NOME FANTASIA"))
        item = self.tb_fornecedores.horizontalHeaderItem(2)
        item.setText(_translate("Frame", "CNPJ"))
        item = self.tb_fornecedores.horizontalHeaderItem(3)
        item.setText(_translate("Frame", "EMAIL"))
        item = self.tb_fornecedores.horizontalHeaderItem(4)
        item.setText(_translate("Frame", "FONE"))
        item = self.tb_fornecedores.horizontalHeaderItem(5)
        item.setText(_translate("Frame", "RUA"))
        item = self.tb_fornecedores.horizontalHeaderItem(6)
        item.setText(_translate("Frame", "BAIRRO"))
        item = self.tb_fornecedores.horizontalHeaderItem(7)
        item.setText(_translate("Frame", "NUMERO"))
        item = self.tb_fornecedores.horizontalHeaderItem(8)
        item.setText(_translate("Frame", "CIDADE"))
        item = self.tb_fornecedores.horizontalHeaderItem(9)
        item.setText(_translate("Frame", "ESTADO"))
        item = self.tb_fornecedores.horizontalHeaderItem(10)
        item.setText(_translate("Frame", "CEP"))
        self.bt_cancelar.setText(_translate("Frame", "CANCELAR"))
        self.bt_salvar.setText(_translate("Frame", "EDITAR"))
        self.bt_excluir.setText(_translate("Frame", "EXCLUIR"))
        self.tx_cnpj.setInputMask(_translate("Frame", "##.###.###/####-##"))
        self.tx_cnpj.setText(_translate("Frame", "../-----"))
        self.lb_FormProdutos_7.setText(_translate("Frame", "CNPJ"))
        self.lb_FormProdutos_8.setText(_translate("Frame", "NOME FANTASIA"))
        self.lb_FormProdutos_10.setText(_translate("Frame", "EMAIL"))
        self.lb_FormProdutos_11.setText(_translate("Frame", "FONE"))
        self.tx_fone.setInputMask(_translate("Frame", "(##) ####-####"))
        self.tx_fone.setText(_translate("Frame", "() -----"))
        self.lb_FormProdutos.setText(_translate("Frame", "ENDEREÇO"))
        self.lb_FormProdutos_14.setText(_translate("Frame", "RUA"))
        self.lb_FormProdutos_15.setText(_translate("Frame", "BAIRRO"))
        self.lb_FormProdutos_2.setText(_translate("Frame", "ALTERAR INFORMAÇÕES"))
        self.lb_FormProdutos_16.setText(_translate("Frame", "NUMERO"))
        self.lb_FormProdutos_17.setText(_translate("Frame", "CIDADE"))
        self.lb_FormProdutos_18.setText(_translate("Frame", "ESTADO"))
        self.tx_cep.setInputMask(_translate("Frame", "#####-###"))
        self.tx_cep.setText(_translate("Frame", "-----"))
        self.lb_FormProdutos_19.setText(_translate("Frame", "CEP"))
        self.bt_refresh.setToolTip(_translate("Frame", "ATUALIZAR TABELA"))
        self.tx_busca.setPlaceholderText(_translate("Frame", "PROCURAR POR..."))
        self.cb_fornecedores.setItemText(0, _translate("Frame", "SELECIONE"))
        self.bt_busca.setToolTip(_translate("Frame", "BUSCAR"))
        self.lb_FormProdutos_13.setText(_translate("Frame", "ID"))
        self.bt_busca_cep.setAccessibleName(_translate("Frame", "BUSCA CEP"))