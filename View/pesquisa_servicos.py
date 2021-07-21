# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pesquisa_servicos.ui'
#
# Created by: PyQt5 View code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(522, 431)
        Frame.setStyleSheet("background: #FFF;")
        self.fr_titulo_servicos = QtWidgets.QFrame(Frame)
        self.fr_titulo_servicos.setGeometry(QtCore.QRect(0, 0, 521, 60))
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
        self.bt_inserir.setGeometry(QtCore.QRect(380, 9, 131, 41))
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
        self.tx_busca_servicos = QtWidgets.QLineEdit(Frame)
        self.tx_busca_servicos.setGeometry(QtCore.QRect(150, 60, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.tx_busca_servicos.setFont(font)
        self.tx_busca_servicos.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tx_busca_servicos.setStyleSheet("QLineEdit {\n"
"color: #000\n"
"}\n"
"")
        self.tx_busca_servicos.setObjectName("tx_busca_servicos")
        self.bt_busca_servicos = QtWidgets.QPushButton(Frame)
        self.bt_busca_servicos.setGeometry(QtCore.QRect(460, 60, 30, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.bt_busca_servicos.setFont(font)
        self.bt_busca_servicos.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_busca_servicos.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_busca_servicos.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.bt_busca_servicos.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Imagens/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_busca_servicos.setIcon(icon)
        self.bt_busca_servicos.setObjectName("bt_busca_servicos")
        self.tb_servicos = QtWidgets.QTableWidget(Frame)
        self.tb_servicos.setGeometry(QtCore.QRect(0, 100, 511, 281))
        self.tb_servicos.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tb_servicos.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tb_servicos.setStyleSheet("QTableView{\n"
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
        self.tb_servicos.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tb_servicos.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tb_servicos.setAutoScrollMargin(20)
        self.tb_servicos.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tb_servicos.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tb_servicos.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tb_servicos.setShowGrid(False)
        self.tb_servicos.setGridStyle(QtCore.Qt.NoPen)
        self.tb_servicos.setWordWrap(False)
        self.tb_servicos.setRowCount(0)
        self.tb_servicos.setObjectName("tb_servicos")
        self.tb_servicos.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tb_servicos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_servicos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_servicos.setHorizontalHeaderItem(2, item)
        self.tb_servicos.horizontalHeader().setDefaultSectionSize(120)
        self.tb_servicos.horizontalHeader().setHighlightSections(False)
        self.tb_servicos.horizontalHeader().setStretchLastSection(True)
        self.tb_servicos.verticalHeader().setVisible(False)
        self.tb_servicos.verticalHeader().setDefaultSectionSize(50)
        self.tb_servicos.verticalHeader().setMinimumSectionSize(20)
        self.fr_botoes = QtWidgets.QFrame(Frame)
        self.fr_botoes.setGeometry(QtCore.QRect(-150, 400, 671, 30))
        self.fr_botoes.setStyleSheet("background:#E1DFE0;\n"
"border: none;")
        self.fr_botoes.setObjectName("fr_botoes")
        self.bt_selecionar = QtWidgets.QPushButton(self.fr_botoes)
        self.bt_selecionar.setGeometry(QtCore.QRect(550, 0, 120, 30))
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
        self.cb_servicos = QtWidgets.QComboBox(Frame)
        self.cb_servicos.setGeometry(QtCore.QRect(10, 60, 131, 31))
        self.cb_servicos.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.cb_servicos.setStyleSheet("QComboBox{\n"
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
        self.cb_servicos.setObjectName("cb_servicos")
        self.cb_servicos.addItem("")
        self.bt_refresh = QtWidgets.QPushButton(Frame)
        self.bt_refresh.setGeometry(QtCore.QRect(490, 60, 30, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.bt_refresh.setFont(font)
        self.bt_refresh.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_refresh.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_refresh.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.bt_refresh.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Imagens/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_refresh.setIcon(icon1)
        self.bt_refresh.setObjectName("bt_refresh")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Lista de Serviços"))
        self.lb_tituloClientes_2.setText(_translate("Frame", "SERVIÇOS"))
        self.bt_inserir.setText(_translate("Frame", "NOVO SERVIÇO"))
        self.tx_busca_servicos.setPlaceholderText(_translate("Frame", "PROCURAR POR..."))
        self.bt_busca_servicos.setToolTip(_translate("Frame", "BUSCAR"))
        item = self.tb_servicos.horizontalHeaderItem(0)
        item.setText(_translate("Frame", "ID"))
        item = self.tb_servicos.horizontalHeaderItem(1)
        item.setText(_translate("Frame", "DESCRIÇÃO"))
        item = self.tb_servicos.horizontalHeaderItem(2)
        item.setText(_translate("Frame", "PREÇO"))
        self.bt_selecionar.setText(_translate("Frame", "SELECIONAR"))
        self.cb_servicos.setItemText(0, _translate("Frame", "SELECIONE"))
        self.bt_refresh.setToolTip(_translate("Frame", "ATUALIZAR TABELA"))
