# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'View/UI/lista_endereco.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(853, 382)
        Frame.setStyleSheet("background: #FFF;")
        self.fr_titulo_servicos = QtWidgets.QFrame(Frame)
        self.fr_titulo_servicos.setGeometry(QtCore.QRect(0, 0, 851, 60))
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
        self.tb_enderecos = QtWidgets.QTableWidget(Frame)
        self.tb_enderecos.setGeometry(QtCore.QRect(0, 60, 851, 111))
        self.tb_enderecos.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tb_enderecos.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tb_enderecos.setStyleSheet("QTableView{\n"
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
        self.tb_enderecos.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tb_enderecos.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tb_enderecos.setAutoScrollMargin(20)
        self.tb_enderecos.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tb_enderecos.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tb_enderecos.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tb_enderecos.setShowGrid(False)
        self.tb_enderecos.setGridStyle(QtCore.Qt.NoPen)
        self.tb_enderecos.setWordWrap(False)
        self.tb_enderecos.setRowCount(1)
        self.tb_enderecos.setObjectName("tb_enderecos")
        self.tb_enderecos.setColumnCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.tb_enderecos.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_enderecos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_enderecos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_enderecos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_enderecos.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_enderecos.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_enderecos.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_enderecos.setHorizontalHeaderItem(6, item)
        self.tb_enderecos.horizontalHeader().setDefaultSectionSize(120)
        self.tb_enderecos.horizontalHeader().setHighlightSections(False)
        self.tb_enderecos.horizontalHeader().setStretchLastSection(True)
        self.tb_enderecos.verticalHeader().setVisible(False)
        self.tb_enderecos.verticalHeader().setDefaultSectionSize(50)
        self.tb_enderecos.verticalHeader().setMinimumSectionSize(20)
        self.lb_FormProdutos_6 = QtWidgets.QLabel(Frame)
        self.lb_FormProdutos_6.setGeometry(QtCore.QRect(650, 240, 181, 20))
        self.lb_FormProdutos_6.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_6.setObjectName("lb_FormProdutos_6")
        self.tx_rua = QtWidgets.QLineEdit(Frame)
        self.tx_rua.setGeometry(QtCore.QRect(650, 260, 181, 25))
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
        self.tx_rua.setPlaceholderText("")
        self.tx_rua.setObjectName("tx_rua")
        self.fr_botoes = QtWidgets.QFrame(Frame)
        self.fr_botoes.setGeometry(QtCore.QRect(-120, 350, 971, 30))
        self.fr_botoes.setStyleSheet("background:#E1DFE0;\n"
"border: none;")
        self.fr_botoes.setObjectName("fr_botoes")
        self.bt_cancelar = QtWidgets.QPushButton(self.fr_botoes)
        self.bt_cancelar.setGeometry(QtCore.QRect(850, 0, 120, 30))
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
        self.bt_salvar.setGeometry(QtCore.QRect(720, 0, 120, 30))
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
        self.tx_bairro = QtWidgets.QLineEdit(Frame)
        self.tx_bairro.setGeometry(QtCore.QRect(270, 260, 181, 25))
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
        self.tx_bairro.setPlaceholderText("")
        self.tx_bairro.setObjectName("tx_bairro")
        self.tx_numero = QtWidgets.QLineEdit(Frame)
        self.tx_numero.setGeometry(QtCore.QRect(460, 260, 181, 25))
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
        self.tx_numero.setPlaceholderText("")
        self.tx_numero.setObjectName("tx_numero")
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
        self.lb_FormProdutos_10.setGeometry(QtCore.QRect(80, 240, 111, 20))
        self.lb_FormProdutos_10.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_10.setObjectName("lb_FormProdutos_10")
        self.tx_cep = QtWidgets.QLineEdit(Frame)
        self.tx_cep.setGeometry(QtCore.QRect(80, 260, 151, 25))
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
        self.tx_cep.setPlaceholderText("")
        self.tx_cep.setObjectName("tx_cep")
        self.lb_FormProdutos_11 = QtWidgets.QLabel(Frame)
        self.lb_FormProdutos_11.setGeometry(QtCore.QRect(10, 290, 111, 20))
        self.lb_FormProdutos_11.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_11.setObjectName("lb_FormProdutos_11")
        self.tx_cidade = QtWidgets.QLineEdit(Frame)
        self.tx_cidade.setGeometry(QtCore.QRect(10, 310, 181, 25))
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
        self.tx_cidade.setPlaceholderText("")
        self.tx_cidade.setObjectName("tx_cidade")
        self.lb_FormProdutos_12 = QtWidgets.QLabel(Frame)
        self.lb_FormProdutos_12.setGeometry(QtCore.QRect(200, 290, 111, 20))
        self.lb_FormProdutos_12.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_12.setObjectName("lb_FormProdutos_12")
        self.tx_estado = QtWidgets.QLineEdit(Frame)
        self.tx_estado.setGeometry(QtCore.QRect(200, 310, 71, 25))
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
        self.tx_estado.setPlaceholderText("")
        self.tx_estado.setObjectName("tx_estado")
        self.lb_FormProdutos = QtWidgets.QLabel(Frame)
        self.lb_FormProdutos.setGeometry(QtCore.QRect(10, 200, 971, 30))
        self.lb_FormProdutos.setStyleSheet("QLabel{\n"
"font-size: 14px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"\n"
"border-bottom: 2px solid #A2A2A2\n"
"}")
        self.lb_FormProdutos.setObjectName("lb_FormProdutos")
        self.bt_busca_cep = QtWidgets.QPushButton(Frame)
        self.bt_busca_cep.setGeometry(QtCore.QRect(230, 260, 31, 25))
        self.bt_busca_cep.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("View/UI/../../Imagens/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_busca_cep.setIcon(icon)
        self.bt_busca_cep.setObjectName("bt_busca_cep")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)
        Frame.setTabOrder(self.tx_id, self.tx_cep)
        Frame.setTabOrder(self.tx_cep, self.bt_busca_cep)
        Frame.setTabOrder(self.bt_busca_cep, self.tx_bairro)
        Frame.setTabOrder(self.tx_bairro, self.tx_numero)
        Frame.setTabOrder(self.tx_numero, self.tx_rua)
        Frame.setTabOrder(self.tx_rua, self.tx_cidade)
        Frame.setTabOrder(self.tx_cidade, self.tx_estado)
        Frame.setTabOrder(self.tx_estado, self.tb_enderecos)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Lista de Endereço"))
        self.lb_tituloClientes_2.setText(_translate("Frame", "ENDEREÇO"))
        item = self.tb_enderecos.verticalHeaderItem(0)
        item.setText(_translate("Frame", "1"))
        item = self.tb_enderecos.horizontalHeaderItem(0)
        item.setText(_translate("Frame", "ID"))
        item = self.tb_enderecos.horizontalHeaderItem(1)
        item.setText(_translate("Frame", "RUA"))
        item = self.tb_enderecos.horizontalHeaderItem(2)
        item.setText(_translate("Frame", "BAIRRO"))
        item = self.tb_enderecos.horizontalHeaderItem(3)
        item.setText(_translate("Frame", "NUMERO"))
        item = self.tb_enderecos.horizontalHeaderItem(4)
        item.setText(_translate("Frame", "CIDADE"))
        item = self.tb_enderecos.horizontalHeaderItem(5)
        item.setText(_translate("Frame", "ESTADO"))
        item = self.tb_enderecos.horizontalHeaderItem(6)
        item.setText(_translate("Frame", "CEP"))
        self.lb_FormProdutos_6.setText(_translate("Frame", "RUA"))
        self.bt_cancelar.setText(_translate("Frame", "CANCELAR"))
        self.bt_salvar.setText(_translate("Frame", "EDITAR"))
        self.lb_FormProdutos_7.setText(_translate("Frame", "ID"))
        self.lb_FormProdutos_8.setText(_translate("Frame", "BAIRRO"))
        self.lb_FormProdutos_9.setText(_translate("Frame", "NUMERO"))
        self.lb_FormProdutos_10.setText(_translate("Frame", "CEP"))
        self.tx_cep.setInputMask(_translate("Frame", "#####-###"))
        self.tx_cep.setText(_translate("Frame", "--"))
        self.lb_FormProdutos_11.setText(_translate("Frame", "CIDADE"))
        self.lb_FormProdutos_12.setText(_translate("Frame", "ESTADO"))
        self.lb_FormProdutos.setText(_translate("Frame", "ALTERAR INFORMAÇÕES"))
        self.bt_busca_cep.setAccessibleName(_translate("Frame", "BUSCA CEP"))
