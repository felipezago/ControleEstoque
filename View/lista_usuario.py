# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lista_usuario.ui'
#
# Created by: PyQt5 View code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(982, 471)
        Frame.setStyleSheet("background: #FFF;")
        self.fr_titulo_servicos = QtWidgets.QFrame(Frame)
        self.fr_titulo_servicos.setGeometry(QtCore.QRect(0, 0, 981, 60))
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
        self.tb_usuario = QtWidgets.QTableWidget(Frame)
        self.tb_usuario.setGeometry(QtCore.QRect(0, 60, 971, 111))
        self.tb_usuario.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tb_usuario.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tb_usuario.setStyleSheet("QTableView{\n"
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
        self.tb_usuario.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tb_usuario.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tb_usuario.setAutoScrollMargin(20)
        self.tb_usuario.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tb_usuario.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tb_usuario.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tb_usuario.setShowGrid(False)
        self.tb_usuario.setGridStyle(QtCore.Qt.NoPen)
        self.tb_usuario.setWordWrap(False)
        self.tb_usuario.setRowCount(1)
        self.tb_usuario.setObjectName("tb_usuario")
        self.tb_usuario.setColumnCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.tb_usuario.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_usuario.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_usuario.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_usuario.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_usuario.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_usuario.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_usuario.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_usuario.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_usuario.setHorizontalHeaderItem(7, item)
        self.tb_usuario.horizontalHeader().setDefaultSectionSize(120)
        self.tb_usuario.horizontalHeader().setHighlightSections(False)
        self.tb_usuario.horizontalHeader().setStretchLastSection(True)
        self.tb_usuario.verticalHeader().setVisible(False)
        self.tb_usuario.verticalHeader().setDefaultSectionSize(50)
        self.tb_usuario.verticalHeader().setMinimumSectionSize(20)
        self.lb_FormProdutos_6 = QtWidgets.QLabel(Frame)
        self.lb_FormProdutos_6.setGeometry(QtCore.QRect(80, 240, 181, 20))
        self.lb_FormProdutos_6.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_6.setObjectName("lb_FormProdutos_6")
        self.tx_cpf = QtWidgets.QLineEdit(Frame)
        self.tx_cpf.setGeometry(QtCore.QRect(80, 260, 181, 25))
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
        self.fr_botoes.setGeometry(QtCore.QRect(0, 440, 991, 30))
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
        self.bt_salvar.setGeometry(QtCore.QRect(730, 0, 120, 30))
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
        self.tx_id = QtWidgets.QLineEdit(Frame)
        self.tx_id.setGeometry(QtCore.QRect(10, 260, 61, 25))
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
        self.tx_id.setText("")
        self.tx_id.setPlaceholderText("")
        self.tx_id.setObjectName("tx_id")
        self.lb_FormProdutos_7 = QtWidgets.QLabel(Frame)
        self.lb_FormProdutos_7.setGeometry(QtCore.QRect(10, 240, 61, 20))
        self.lb_FormProdutos_7.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_7.setObjectName("lb_FormProdutos_7")
        self.lb_FormProdutos_8 = QtWidgets.QLabel(Frame)
        self.lb_FormProdutos_8.setGeometry(QtCore.QRect(270, 240, 111, 20))
        self.lb_FormProdutos_8.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_8.setObjectName("lb_FormProdutos_8")
        self.tx_nome = QtWidgets.QLineEdit(Frame)
        self.tx_nome.setGeometry(QtCore.QRect(270, 260, 181, 25))
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
        self.tx_fone = QtWidgets.QLineEdit(Frame)
        self.tx_fone.setGeometry(QtCore.QRect(460, 260, 181, 25))
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
        self.tx_fone.setInputMask("")
        self.tx_fone.setText("")
        self.tx_fone.setPlaceholderText("")
        self.tx_fone.setObjectName("tx_fone")
        self.lb_FormProdutos_9 = QtWidgets.QLabel(Frame)
        self.lb_FormProdutos_9.setGeometry(QtCore.QRect(460, 240, 111, 20))
        self.lb_FormProdutos_9.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_9.setObjectName("lb_FormProdutos_9")
        self.lb_FormProdutos_10 = QtWidgets.QLabel(Frame)
        self.lb_FormProdutos_10.setGeometry(QtCore.QRect(650, 240, 111, 20))
        self.lb_FormProdutos_10.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_10.setObjectName("lb_FormProdutos_10")
        self.tx_email = QtWidgets.QLineEdit(Frame)
        self.tx_email.setGeometry(QtCore.QRect(650, 260, 311, 25))
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
        self.lb_FormProdutos_11.setGeometry(QtCore.QRect(10, 290, 111, 20))
        self.lb_FormProdutos_11.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_11.setObjectName("lb_FormProdutos_11")
        self.tx_rg = QtWidgets.QLineEdit(Frame)
        self.tx_rg.setGeometry(QtCore.QRect(10, 310, 181, 25))
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
        self.tx_rg.setInputMask("")
        self.tx_rg.setText("")
        self.tx_rg.setPlaceholderText("")
        self.tx_rg.setObjectName("tx_rg")
        self.lb_FormProdutos_12 = QtWidgets.QLabel(Frame)
        self.lb_FormProdutos_12.setGeometry(QtCore.QRect(200, 290, 111, 20))
        self.lb_FormProdutos_12.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_12.setObjectName("lb_FormProdutos_12")
        self.tx_celular = QtWidgets.QLineEdit(Frame)
        self.tx_celular.setGeometry(QtCore.QRect(200, 310, 241, 25))
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
        self.tx_celular.setInputMask("")
        self.tx_celular.setText("")
        self.tx_celular.setPlaceholderText("")
        self.tx_celular.setObjectName("tx_celular")
        self.tx_login = QtWidgets.QLineEdit(Frame)
        self.tx_login.setGeometry(QtCore.QRect(460, 310, 181, 25))
        self.tx_login.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_login.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"padding-left: 3px;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_login.setInputMask("")
        self.tx_login.setText("")
        self.tx_login.setPlaceholderText("")
        self.tx_login.setObjectName("tx_login")
        self.lb_FormProdutos_13 = QtWidgets.QLabel(Frame)
        self.lb_FormProdutos_13.setGeometry(QtCore.QRect(460, 290, 111, 20))
        self.lb_FormProdutos_13.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_13.setObjectName("lb_FormProdutos_13")
        self.lb_FormProdutos = QtWidgets.QLabel(Frame)
        self.lb_FormProdutos.setGeometry(QtCore.QRect(10, 340, 971, 30))
        self.lb_FormProdutos.setStyleSheet("QLabel{\n"
"font-size: 14px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"\n"
"border-bottom: 2px solid #A2A2A2\n"
"}")
        self.lb_FormProdutos.setObjectName("lb_FormProdutos")
        self.lb_FormProdutos_14 = QtWidgets.QLabel(Frame)
        self.lb_FormProdutos_14.setGeometry(QtCore.QRect(10, 380, 111, 20))
        self.lb_FormProdutos_14.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_14.setObjectName("lb_FormProdutos_14")
        self.tx_senha_antiga = QtWidgets.QLineEdit(Frame)
        self.tx_senha_antiga.setGeometry(QtCore.QRect(10, 400, 181, 25))
        self.tx_senha_antiga.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_senha_antiga.setEchoMode(QtWidgets.QLineEdit.Password)
        self.tx_senha_antiga.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"padding-left: 3px;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_senha_antiga.setInputMask("")
        self.tx_senha_antiga.setText("")
        self.tx_senha_antiga.setPlaceholderText("")
        self.tx_senha_antiga.setObjectName("tx_senha_antiga")
        self.lb_FormProdutos_15 = QtWidgets.QLabel(Frame)
        self.lb_FormProdutos_15.setGeometry(QtCore.QRect(200, 380, 111, 20))
        self.lb_FormProdutos_15.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_15.setObjectName("lb_FormProdutos_15")
        self.tx_nova_senha = QtWidgets.QLineEdit(Frame)
        self.tx_nova_senha.setGeometry(QtCore.QRect(200, 400, 241, 25))
        self.tx_nova_senha.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_nova_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.tx_nova_senha.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"padding-left: 3px;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_nova_senha.setInputMask("")
        self.tx_nova_senha.setText("")
        self.tx_nova_senha.setPlaceholderText("")
        self.tx_nova_senha.setObjectName("tx_nova_senha")
        self.lb_FormProdutos_2 = QtWidgets.QLabel(Frame)
        self.lb_FormProdutos_2.setGeometry(QtCore.QRect(10, 200, 971, 30))
        self.lb_FormProdutos_2.setStyleSheet("QLabel{\n"
"font-size: 14px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"\n"
"border-bottom: 2px solid #A2A2A2\n"
"}")
        self.lb_FormProdutos_2.setObjectName("lb_FormProdutos_2")
        self.tx_nova_senha_2 = QtWidgets.QLineEdit(Frame)
        self.tx_nova_senha_2.setGeometry(QtCore.QRect(450, 400, 241, 25))
        self.tx_nova_senha_2.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_nova_senha_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.tx_nova_senha_2.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"padding-left: 3px;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_nova_senha_2.setInputMask("")
        self.tx_nova_senha_2.setText("")
        self.tx_nova_senha_2.setPlaceholderText("")
        self.tx_nova_senha_2.setObjectName("tx_nova_senha_2")
        self.lb_FormProdutos_16 = QtWidgets.QLabel(Frame)
        self.lb_FormProdutos_16.setGeometry(QtCore.QRect(450, 380, 181, 20))
        self.lb_FormProdutos_16.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_16.setObjectName("lb_FormProdutos_16")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Lista de Usuário"))
        self.lb_tituloClientes_2.setText(_translate("Frame", "USUÁRIO"))
        item = self.tb_usuario.verticalHeaderItem(0)
        item.setText(_translate("Frame", "1"))
        item = self.tb_usuario.horizontalHeaderItem(0)
        item.setText(_translate("Frame", "ID"))
        item = self.tb_usuario.horizontalHeaderItem(1)
        item.setText(_translate("Frame", "CPF"))
        item = self.tb_usuario.horizontalHeaderItem(2)
        item.setText(_translate("Frame", "NOME"))
        item = self.tb_usuario.horizontalHeaderItem(3)
        item.setText(_translate("Frame", "TELEFONE"))
        item = self.tb_usuario.horizontalHeaderItem(4)
        item.setText(_translate("Frame", "EMAIL"))
        item = self.tb_usuario.horizontalHeaderItem(5)
        item.setText(_translate("Frame", "RG"))
        item = self.tb_usuario.horizontalHeaderItem(6)
        item.setText(_translate("Frame", "CELULAR"))
        item = self.tb_usuario.horizontalHeaderItem(7)
        item.setText(_translate("Frame", "USUARIO (LOGIN)"))
        self.lb_FormProdutos_6.setText(_translate("Frame", "CPF"))
        self.bt_cancelar.setText(_translate("Frame", "CANCELAR"))
        self.bt_salvar.setText(_translate("Frame", "EDITAR"))
        self.lb_FormProdutos_7.setText(_translate("Frame", "ID"))
        self.lb_FormProdutos_8.setText(_translate("Frame", "NOME"))
        self.lb_FormProdutos_9.setText(_translate("Frame", "TELEFONE"))
        self.lb_FormProdutos_10.setText(_translate("Frame", "EMAIL"))
        self.lb_FormProdutos_11.setText(_translate("Frame", "RG"))
        self.lb_FormProdutos_12.setText(_translate("Frame", "CELULAR"))
        self.lb_FormProdutos_13.setText(_translate("Frame", "LOGIN"))
        self.lb_FormProdutos.setText(_translate("Frame", "ALTERAR SENHA"))
        self.lb_FormProdutos_14.setText(_translate("Frame", "SENHA ANTIGA"))
        self.lb_FormProdutos_15.setText(_translate("Frame", "NOVA SENHA"))
        self.lb_FormProdutos_2.setText(_translate("Frame", "ALTERAR INFORMAÇÕES"))
        self.lb_FormProdutos_16.setText(_translate("Frame", "CONFIRME A NOVA SENHA"))
