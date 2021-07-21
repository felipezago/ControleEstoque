# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'descontos.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(751, 501)
        Frame.setAutoFillBackground(False)
        Frame.setStyleSheet("background: #FFF;")
        self.fr_titulo_servicos = QtWidgets.QFrame(Frame)
        self.fr_titulo_servicos.setGeometry(QtCore.QRect(0, 0, 1051, 51))
        self.fr_titulo_servicos.setStyleSheet("")
        self.fr_titulo_servicos.setObjectName("fr_titulo_servicos")
        self.lb_tituloClientes_2 = QtWidgets.QLabel(self.fr_titulo_servicos)
        self.lb_tituloClientes_2.setGeometry(QtCore.QRect(10, 10, 171, 30))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lb_tituloClientes_2.setFont(font)
        self.lb_tituloClientes_2.setStyleSheet("color: rgb(0, 0, 0)")
        self.lb_tituloClientes_2.setObjectName("lb_tituloClientes_2")
        self.fr_botoes = QtWidgets.QFrame(Frame)
        self.fr_botoes.setGeometry(QtCore.QRect(0, 470, 751, 30))
        self.fr_botoes.setStyleSheet("background:#E1DFE0;\n"
"border: none;")
        self.fr_botoes.setObjectName("fr_botoes")
        self.bt_sair = QtWidgets.QPushButton(self.fr_botoes)
        self.bt_sair.setGeometry(QtCore.QRect(599, 0, 151, 30))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bt_sair.setFont(font)
        self.bt_sair.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_sair.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_sair.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.bt_sair.setStyleSheet("QPushButton {\n"
"background-color: #1E87F0;\n"
"color: #FFF\n"
" }\n"
"QPushButton:hover{\n"
"background-color: #40a286\n"
"}")
        self.bt_sair.setIconSize(QtCore.QSize(75, 35))
        self.bt_sair.setObjectName("bt_sair")
        self.tx_valor = QtWidgets.QLineEdit(Frame)
        self.tx_valor.setGeometry(QtCore.QRect(180, 90, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.tx_valor.setFont(font)
        self.tx_valor.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tx_valor.setStyleSheet("QLineEdit {\n"
"color: #000\n"
"}\n"
"")
        self.tx_valor.setPlaceholderText("")
        self.tx_valor.setObjectName("tx_valor")
        self.cb_tipo_desconto = QtWidgets.QComboBox(Frame)
        self.cb_tipo_desconto.setGeometry(QtCore.QRect(10, 90, 161, 31))
        self.cb_tipo_desconto.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.cb_tipo_desconto.setStyleSheet("QComboBox{\n"
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
        self.cb_tipo_desconto.setObjectName("cb_tipo_desconto")
        self.cb_tipo_desconto.addItem("")
        self.cb_tipo_desconto.addItem("")
        self.cb_tipo_desconto.addItem("")
        self.cb_tipo_desconto.addItem("")
        self.cb_tipo_desconto.addItem("")
        self.label_8 = QtWidgets.QLabel(Frame)
        self.label_8.setGeometry(QtCore.QRect(10, 70, 171, 17))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Frame)
        self.label_9.setGeometry(QtCore.QRect(180, 70, 61, 17))
        self.label_9.setObjectName("label_9")
        self.bt_inserir = QtWidgets.QPushButton(Frame)
        self.bt_inserir.setGeometry(QtCore.QRect(350, 90, 161, 30))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bt_inserir.setFont(font)
        self.bt_inserir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_inserir.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_inserir.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.bt_inserir.setStyleSheet("QPushButton {\n"
"    background-color: rgb(78, 154, 6);\n"
"color: #FFF\n"
" }\n"
"QPushButton:hover{\n"
"    background-color: #40a286\n"
"}")
        self.bt_inserir.setIconSize(QtCore.QSize(75, 35))
        self.bt_inserir.setObjectName("bt_inserir")
        self.tb_itens_venda = QtWidgets.QTableWidget(Frame)
        self.tb_itens_venda.setGeometry(QtCore.QRect(0, 150, 751, 261))
        self.tb_itens_venda.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tb_itens_venda.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tb_itens_venda.setStyleSheet("QTableView{\n"
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
        self.tb_itens_venda.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tb_itens_venda.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tb_itens_venda.setAutoScrollMargin(20)
        self.tb_itens_venda.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tb_itens_venda.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tb_itens_venda.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tb_itens_venda.setShowGrid(False)
        self.tb_itens_venda.setGridStyle(QtCore.Qt.NoPen)
        self.tb_itens_venda.setWordWrap(False)
        self.tb_itens_venda.setRowCount(0)
        self.tb_itens_venda.setObjectName("tb_itens_venda")
        self.tb_itens_venda.setColumnCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tb_itens_venda.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_itens_venda.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_itens_venda.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_itens_venda.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_itens_venda.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_itens_venda.setHorizontalHeaderItem(5, item)
        self.tb_itens_venda.horizontalHeader().setDefaultSectionSize(120)
        self.tb_itens_venda.horizontalHeader().setHighlightSections(False)
        self.tb_itens_venda.horizontalHeader().setStretchLastSection(True)
        self.tb_itens_venda.verticalHeader().setVisible(False)
        self.tb_itens_venda.verticalHeader().setDefaultSectionSize(50)
        self.tb_itens_venda.verticalHeader().setMinimumSectionSize(20)
        self.lb_descontos = QtWidgets.QLabel(Frame)
        self.lb_descontos.setGeometry(QtCore.QRect(670, 420, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lb_descontos.setFont(font)
        self.lb_descontos.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lb_descontos.setStyleSheet("color: rgb(0, 0, 0)")
        self.lb_descontos.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lb_descontos.setObjectName("lb_descontos")
        self.lb_tituloClientes_4 = QtWidgets.QLabel(Frame)
        self.lb_tituloClientes_4.setGeometry(QtCore.QRect(500, 440, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lb_tituloClientes_4.setFont(font)
        self.lb_tituloClientes_4.setStyleSheet("color: rgb(0, 0, 0)")
        self.lb_tituloClientes_4.setObjectName("lb_tituloClientes_4")
        self.lb_total = QtWidgets.QLabel(Frame)
        self.lb_total.setGeometry(QtCore.QRect(670, 440, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lb_total.setFont(font)
        self.lb_total.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lb_total.setStyleSheet("color: rgb(0, 0, 0)")
        self.lb_total.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lb_total.setObjectName("lb_total")
        self.lb_tituloClientes_5 = QtWidgets.QLabel(Frame)
        self.lb_tituloClientes_5.setGeometry(QtCore.QRect(510, 420, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lb_tituloClientes_5.setFont(font)
        self.lb_tituloClientes_5.setStyleSheet("color: rgb(0, 0, 0);\n"
"margin-left: 30pt;")
        self.lb_tituloClientes_5.setObjectName("lb_tituloClientes_5")
        self.bt_excluir = QtWidgets.QPushButton(Frame)
        self.bt_excluir.setGeometry(QtCore.QRect(10, 430, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
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

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Descontos"))
        self.lb_tituloClientes_2.setText(_translate("Frame", "DESCONTOS"))
        self.bt_sair.setText(_translate("Frame", "SAIR"))
        self.cb_tipo_desconto.setItemText(0, _translate("Frame", "SELECIONE"))
        self.cb_tipo_desconto.setItemText(1, _translate("Frame", "PERCENTUAL TOTAL"))
        self.cb_tipo_desconto.setItemText(2, _translate("Frame", "PERCENTUAL ITEM"))
        self.cb_tipo_desconto.setItemText(3, _translate("Frame", "VALOR TOTAL"))
        self.cb_tipo_desconto.setItemText(4, _translate("Frame", "VALOR ITEM"))
        self.label_8.setText(_translate("Frame", "TIPO DE DESCONTO"))
        self.label_9.setText(_translate("Frame", "VALOR"))
        self.bt_inserir.setText(_translate("Frame", "CONCEDER"))
        item = self.tb_itens_venda.horizontalHeaderItem(0)
        item.setText(_translate("Frame", "ID"))
        item = self.tb_itens_venda.horizontalHeaderItem(1)
        item.setText(_translate("Frame", "DESCRIÇÃO"))
        item = self.tb_itens_venda.horizontalHeaderItem(2)
        item.setText(_translate("Frame", "VL. UNIT"))
        item = self.tb_itens_venda.horizontalHeaderItem(3)
        item.setText(_translate("Frame", "QTD"))
        item = self.tb_itens_venda.horizontalHeaderItem(4)
        item.setText(_translate("Frame", "VL. TOTAL"))
        item = self.tb_itens_venda.horizontalHeaderItem(5)
        item.setText(_translate("Frame", "DESCONTO"))
        self.lb_descontos.setText(_translate("Frame", "5000,00"))
        self.lb_tituloClientes_4.setText(_translate("Frame", "VALOR TOTAL: R$ "))
        self.lb_total.setText(_translate("Frame", "5000,00"))
        self.lb_tituloClientes_5.setText(_translate("Frame", "DESCONTOS: R$"))
        self.bt_excluir.setText(_translate("Frame", "EXCLUIR DESCONTOS"))
