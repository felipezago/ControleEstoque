# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pesquisa_produtos.ui'
#
# Created by: PyQt5 View code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(1048, 361)
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
        self.bt_inserir = QtWidgets.QPushButton(self.fr_titulo_servicos)
        self.bt_inserir.setGeometry(QtCore.QRect(910, 9, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
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
        self.fr_botoes = QtWidgets.QFrame(Frame)
        self.fr_botoes.setGeometry(QtCore.QRect(0, 330, 1051, 30))
        self.fr_botoes.setStyleSheet("background:#E1DFE0;\n"
"border: none;")
        self.fr_botoes.setObjectName("fr_botoes")
        self.bt_selecionar = QtWidgets.QPushButton(self.fr_botoes)
        self.bt_selecionar.setGeometry(QtCore.QRect(930, 0, 120, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bt_selecionar.setFont(font)
        self.bt_selecionar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_selecionar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_selecionar.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.bt_selecionar.setStyleSheet("QPushButton {\n"
"background-color: #1E87F0;\n"
"color: #FFF\n"
" }\n"
"QPushButton:hover{\n"
"background-color: #40a286\n"
"}")
        self.bt_selecionar.setIconSize(QtCore.QSize(75, 35))
        self.bt_selecionar.setObjectName("bt_selecionar")
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

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Lista de Produtos"))
        self.lb_tituloClientes_2.setText(_translate("Frame", "PRODUTOS"))
        self.bt_inserir.setText(_translate("Frame", "NOVO PRODUTO"))
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
        self.bt_selecionar.setText(_translate("Frame", "SELECIONAR"))
        self.bt_refresh.setToolTip(_translate("Frame", "ATUALIZAR TABELA"))
        self.tx_busca.setPlaceholderText(_translate("Frame", "PROCURAR POR..."))
        self.cb_produtos.setItemText(0, _translate("Frame", "SELECIONE"))
        self.bt_busca.setToolTip(_translate("Frame", "BUSCAR"))
