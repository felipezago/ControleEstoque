# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'View/UI/lista_clientes.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(982, 610)
        Frame.setStyleSheet("background: #FFF;")
        self.fr_titulo_clientes = QtWidgets.QFrame(Frame)
        self.fr_titulo_clientes.setGeometry(QtCore.QRect(0, 0, 981, 60))
        self.fr_titulo_clientes.setStyleSheet("")
        self.fr_titulo_clientes.setObjectName("fr_titulo_clientes")
        self.lb_tituloClientes_2 = QtWidgets.QLabel(self.fr_titulo_clientes)
        self.lb_tituloClientes_2.setGeometry(QtCore.QRect(10, 15, 200, 30))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lb_tituloClientes_2.setFont(font)
        self.lb_tituloClientes_2.setStyleSheet("color: rgb(0, 0, 0)")
        self.lb_tituloClientes_2.setObjectName("lb_tituloClientes_2")
        self.bt_novo = QtWidgets.QPushButton(self.fr_titulo_clientes)
        self.bt_novo.setGeometry(QtCore.QRect(820, 10, 151, 41))
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
        self.tb_clientes = QtWidgets.QTableWidget(Frame)
        self.tb_clientes.setGeometry(QtCore.QRect(0, 100, 971, 211))
        self.tb_clientes.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tb_clientes.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tb_clientes.setStyleSheet("QTableView{\n"
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
        self.tb_clientes.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tb_clientes.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tb_clientes.setAutoScrollMargin(20)
        self.tb_clientes.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tb_clientes.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tb_clientes.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tb_clientes.setShowGrid(False)
        self.tb_clientes.setGridStyle(QtCore.Qt.NoPen)
        self.tb_clientes.setWordWrap(False)
        self.tb_clientes.setRowCount(1)
        self.tb_clientes.setObjectName("tb_clientes")
        self.tb_clientes.setColumnCount(13)
        item = QtWidgets.QTableWidgetItem()
        self.tb_clientes.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_clientes.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_clientes.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_clientes.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_clientes.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_clientes.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_clientes.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_clientes.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_clientes.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_clientes.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_clientes.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_clientes.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_clientes.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_clientes.setHorizontalHeaderItem(12, item)
        self.tb_clientes.horizontalHeader().setDefaultSectionSize(120)
        self.tb_clientes.horizontalHeader().setHighlightSections(False)
        self.tb_clientes.horizontalHeader().setStretchLastSection(True)
        self.tb_clientes.verticalHeader().setVisible(False)
        self.tb_clientes.verticalHeader().setDefaultSectionSize(50)
        self.tb_clientes.verticalHeader().setMinimumSectionSize(20)
        self.lb_FormProdutos_6 = QtWidgets.QLabel(Frame)
        self.lb_FormProdutos_6.setGeometry(QtCore.QRect(70, 360, 181, 20))
        self.lb_FormProdutos_6.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_6.setObjectName("lb_FormProdutos_6")
        self.tx_cpf = QtWidgets.QLineEdit(Frame)
        self.tx_cpf.setGeometry(QtCore.QRect(70, 380, 141, 25))
        self.tx_cpf.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_cpf.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"padding-left: 3px;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_cpf.setPlaceholderText("")
        self.tx_cpf.setObjectName("tx_cpf")
        self.fr_botoes = QtWidgets.QFrame(Frame)
        self.fr_botoes.setGeometry(QtCore.QRect(0, 580, 991, 30))
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
        self.tx_id = QtWidgets.QLineEdit(Frame)
        self.tx_id.setGeometry(QtCore.QRect(10, 380, 51, 25))
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
        self.lb_FormProdutos_8.setGeometry(QtCore.QRect(220, 360, 111, 20))
        self.lb_FormProdutos_8.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_8.setObjectName("lb_FormProdutos_8")
        self.tx_nome = QtWidgets.QLineEdit(Frame)
        self.tx_nome.setGeometry(QtCore.QRect(220, 380, 301, 25))
        self.tx_nome.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_nome.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"padding-left: 3px;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_nome.setInputMask("")
        self.tx_nome.setText("")
        self.tx_nome.setPlaceholderText("")
        self.tx_nome.setObjectName("tx_nome")
        self.tx_rg = QtWidgets.QLineEdit(Frame)
        self.tx_rg.setGeometry(QtCore.QRect(10, 440, 121, 25))
        self.tx_rg.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_rg.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"padding-left: 3px;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_rg.setPlaceholderText("")
        self.tx_rg.setObjectName("tx_rg")
        self.lb_FormProdutos_9 = QtWidgets.QLabel(Frame)
        self.lb_FormProdutos_9.setGeometry(QtCore.QRect(10, 420, 131, 20))
        self.lb_FormProdutos_9.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_9.setObjectName("lb_FormProdutos_9")
        self.lb_FormProdutos_10 = QtWidgets.QLabel(Frame)
        self.lb_FormProdutos_10.setGeometry(QtCore.QRect(730, 360, 111, 20))
        self.lb_FormProdutos_10.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_10.setObjectName("lb_FormProdutos_10")
        self.tx_email = QtWidgets.QLineEdit(Frame)
        self.tx_email.setGeometry(QtCore.QRect(730, 380, 241, 25))
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
        self.lb_FormProdutos_11.setGeometry(QtCore.QRect(140, 420, 111, 20))
        self.lb_FormProdutos_11.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_11.setObjectName("lb_FormProdutos_11")
        self.tx_celular = QtWidgets.QLineEdit(Frame)
        self.tx_celular.setGeometry(QtCore.QRect(140, 440, 121, 25))
        self.tx_celular.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_celular.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"padding-left: 3px;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_celular.setPlaceholderText("")
        self.tx_celular.setObjectName("tx_celular")
        self.lb_FormProdutos_12 = QtWidgets.QLabel(Frame)
        self.lb_FormProdutos_12.setGeometry(QtCore.QRect(530, 360, 111, 20))
        self.lb_FormProdutos_12.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_12.setObjectName("lb_FormProdutos_12")
        self.tx_fone = QtWidgets.QLineEdit(Frame)
        self.tx_fone.setGeometry(QtCore.QRect(530, 380, 191, 25))
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
        self.lb_FormProdutos.setGeometry(QtCore.QRect(10, 480, 971, 30))
        self.lb_FormProdutos.setStyleSheet("QLabel{\n"
"font-size: 14px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"\n"
"border-bottom: 2px solid #A2A2A2\n"
"}")
        self.lb_FormProdutos.setObjectName("lb_FormProdutos")
        self.lb_FormProdutos_14 = QtWidgets.QLabel(Frame)
        self.lb_FormProdutos_14.setGeometry(QtCore.QRect(790, 520, 111, 20))
        self.lb_FormProdutos_14.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_14.setObjectName("lb_FormProdutos_14")
        self.tx_rua = QtWidgets.QLineEdit(Frame)
        self.tx_rua.setGeometry(QtCore.QRect(790, 540, 181, 25))
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
        self.lb_FormProdutos_15.setGeometry(QtCore.QRect(160, 520, 111, 20))
        self.lb_FormProdutos_15.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_15.setObjectName("lb_FormProdutos_15")
        self.tx_bairro = QtWidgets.QLineEdit(Frame)
        self.tx_bairro.setGeometry(QtCore.QRect(160, 540, 241, 25))
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
        self.tx_numero.setGeometry(QtCore.QRect(410, 540, 101, 25))
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
        self.lb_FormProdutos_16.setGeometry(QtCore.QRect(410, 520, 181, 20))
        self.lb_FormProdutos_16.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_16.setObjectName("lb_FormProdutos_16")
        self.lb_FormProdutos_17 = QtWidgets.QLabel(Frame)
        self.lb_FormProdutos_17.setGeometry(QtCore.QRect(520, 520, 111, 20))
        self.lb_FormProdutos_17.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_17.setObjectName("lb_FormProdutos_17")
        self.tx_cidade = QtWidgets.QLineEdit(Frame)
        self.tx_cidade.setGeometry(QtCore.QRect(520, 540, 191, 25))
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
        self.lb_FormProdutos_18.setGeometry(QtCore.QRect(720, 520, 61, 20))
        self.lb_FormProdutos_18.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_18.setObjectName("lb_FormProdutos_18")
        self.tx_estado = QtWidgets.QLineEdit(Frame)
        self.tx_estado.setGeometry(QtCore.QRect(720, 540, 61, 25))
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
        self.tx_cep.setGeometry(QtCore.QRect(10, 540, 101, 25))
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
        self.lb_FormProdutos_19.setGeometry(QtCore.QRect(10, 520, 141, 20))
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
        self.cb_clientes = QtWidgets.QComboBox(Frame)
        self.cb_clientes.setGeometry(QtCore.QRect(10, 60, 171, 31))
        self.cb_clientes.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.cb_clientes.setStyleSheet("QComboBox{\n"
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
        self.cb_clientes.setObjectName("cb_clientes")
        self.cb_clientes.addItem("")
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
        self.bt_busca_cep = QtWidgets.QPushButton(Frame)
        self.bt_busca_cep.setGeometry(QtCore.QRect(110, 540, 31, 25))
        self.bt_busca_cep.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Imagens/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_busca_cep.setIcon(icon2)
        self.bt_busca_cep.setObjectName("bt_busca_cep")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)
        Frame.setTabOrder(self.tx_id, self.tx_cpf)
        Frame.setTabOrder(self.tx_cpf, self.tx_nome)
        Frame.setTabOrder(self.tx_nome, self.tx_fone)
        Frame.setTabOrder(self.tx_fone, self.tx_email)
        Frame.setTabOrder(self.tx_email, self.tx_rg)
        Frame.setTabOrder(self.tx_rg, self.tx_celular)
        Frame.setTabOrder(self.tx_celular, self.tx_cep)
        Frame.setTabOrder(self.tx_cep, self.bt_busca_cep)
        Frame.setTabOrder(self.bt_busca_cep, self.tx_bairro)
        Frame.setTabOrder(self.tx_bairro, self.tx_numero)
        Frame.setTabOrder(self.tx_numero, self.tx_cidade)
        Frame.setTabOrder(self.tx_cidade, self.tx_estado)
        Frame.setTabOrder(self.tx_estado, self.tx_rua)
        Frame.setTabOrder(self.tx_rua, self.tb_clientes)
        Frame.setTabOrder(self.tb_clientes, self.cb_clientes)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Lista de Clientes"))
        self.lb_tituloClientes_2.setText(_translate("Frame", "CLIENTES"))
        self.bt_novo.setText(_translate("Frame", "NOVO CLIENTE"))
        item = self.tb_clientes.verticalHeaderItem(0)
        item.setText(_translate("Frame", "1"))
        item = self.tb_clientes.horizontalHeaderItem(0)
        item.setText(_translate("Frame", "ID"))
        item = self.tb_clientes.horizontalHeaderItem(1)
        item.setText(_translate("Frame", "CPF"))
        item = self.tb_clientes.horizontalHeaderItem(2)
        item.setText(_translate("Frame", "NOME"))
        item = self.tb_clientes.horizontalHeaderItem(3)
        item.setText(_translate("Frame", "FONE"))
        item = self.tb_clientes.horizontalHeaderItem(4)
        item.setText(_translate("Frame", "EMAIL"))
        item = self.tb_clientes.horizontalHeaderItem(5)
        item.setText(_translate("Frame", "RG"))
        item = self.tb_clientes.horizontalHeaderItem(6)
        item.setText(_translate("Frame", "CELULAR"))
        item = self.tb_clientes.horizontalHeaderItem(7)
        item.setText(_translate("Frame", "RUA"))
        item = self.tb_clientes.horizontalHeaderItem(8)
        item.setText(_translate("Frame", "BAIRRO"))
        item = self.tb_clientes.horizontalHeaderItem(9)
        item.setText(_translate("Frame", "NUMERO"))
        item = self.tb_clientes.horizontalHeaderItem(10)
        item.setText(_translate("Frame", "CIDADE"))
        item = self.tb_clientes.horizontalHeaderItem(11)
        item.setText(_translate("Frame", "ESTADO"))
        item = self.tb_clientes.horizontalHeaderItem(12)
        item.setText(_translate("Frame", "CEP"))
        self.lb_FormProdutos_6.setText(_translate("Frame", "CPF"))
        self.tx_cpf.setInputMask(_translate("Frame", "###.###.###-##"))
        self.bt_cancelar.setText(_translate("Frame", "CANCELAR"))
        self.bt_salvar.setText(_translate("Frame", "EDITAR"))
        self.bt_excluir.setText(_translate("Frame", "EXCLUIR"))
        self.lb_FormProdutos_7.setText(_translate("Frame", "ID"))
        self.lb_FormProdutos_8.setText(_translate("Frame", "NOME "))
        self.tx_rg.setInputMask(_translate("Frame", "##.###.###-#"))
        self.tx_rg.setText(_translate("Frame", "..---"))
        self.lb_FormProdutos_9.setText(_translate("Frame", "RG"))
        self.lb_FormProdutos_10.setText(_translate("Frame", "EMAIL"))
        self.lb_FormProdutos_11.setText(_translate("Frame", "CELULAR"))
        self.tx_celular.setInputMask(_translate("Frame", "(##) #####-####"))
        self.tx_celular.setText(_translate("Frame", "() ------"))
        self.lb_FormProdutos_12.setText(_translate("Frame", "FONE"))
        self.tx_fone.setInputMask(_translate("Frame", "(##) ####-####"))
        self.tx_fone.setText(_translate("Frame", "() ---"))
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
        self.cb_clientes.setItemText(0, _translate("Frame", "SELECIONE"))
        self.bt_busca.setToolTip(_translate("Frame", "BUSCAR"))
        self.bt_busca_cep.setAccessibleName(_translate("Frame", "BUSCA CEP"))