# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lista_veiculos.ui'
#
# Created by: PyQt5 View code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(602, 570)
        Frame.setStyleSheet("background: #FFF;")
        self.fr_titulo_veiculos = QtWidgets.QFrame(Frame)
        self.fr_titulo_veiculos.setGeometry(QtCore.QRect(0, 0, 601, 60))
        self.fr_titulo_veiculos.setStyleSheet("")
        self.fr_titulo_veiculos.setObjectName("fr_titulo_veiculos")
        self.lb_tituloClientes_2 = QtWidgets.QLabel(self.fr_titulo_veiculos)
        self.lb_tituloClientes_2.setGeometry(QtCore.QRect(10, 15, 200, 30))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lb_tituloClientes_2.setFont(font)
        self.lb_tituloClientes_2.setStyleSheet("color: rgb(0, 0, 0)")
        self.lb_tituloClientes_2.setObjectName("lb_tituloClientes_2")
        self.bt_novo = QtWidgets.QPushButton(self.fr_titulo_veiculos)
        self.bt_novo.setGeometry(QtCore.QRect(440, 10, 151, 41))
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
        self.tx_busca = QtWidgets.QLineEdit(Frame)
        self.tx_busca.setGeometry(QtCore.QRect(150, 60, 391, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.tx_busca.setFont(font)
        self.tx_busca.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tx_busca.setStyleSheet("QLineEdit {\n"
"color: #000\n"
"}\n"
"")
        self.tx_busca.setObjectName("tx_busca")
        self.bt_busca = QtWidgets.QPushButton(Frame)
        self.bt_busca.setGeometry(QtCore.QRect(540, 60, 30, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.bt_busca.setFont(font)
        self.bt_busca.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_busca.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_busca.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.bt_busca.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Imagens/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_busca.setIcon(icon)
        self.bt_busca.setObjectName("bt_busca")
        self.tb_veiculos = QtWidgets.QTableWidget(Frame)
        self.tb_veiculos.setGeometry(QtCore.QRect(0, 100, 601, 281))
        self.tb_veiculos.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tb_veiculos.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tb_veiculos.setStyleSheet("QTableView{\n"
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
        self.tb_veiculos.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tb_veiculos.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tb_veiculos.setAutoScrollMargin(20)
        self.tb_veiculos.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tb_veiculos.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tb_veiculos.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tb_veiculos.setShowGrid(False)
        self.tb_veiculos.setGridStyle(QtCore.Qt.NoPen)
        self.tb_veiculos.setWordWrap(False)
        self.tb_veiculos.setRowCount(0)
        self.tb_veiculos.setObjectName("tb_veiculos")
        self.tb_veiculos.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tb_veiculos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_veiculos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_veiculos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_veiculos.setHorizontalHeaderItem(3, item)
        self.tb_veiculos.horizontalHeader().setDefaultSectionSize(120)
        self.tb_veiculos.horizontalHeader().setHighlightSections(False)
        self.tb_veiculos.horizontalHeader().setStretchLastSection(True)
        self.tb_veiculos.verticalHeader().setVisible(False)
        self.tb_veiculos.verticalHeader().setDefaultSectionSize(50)
        self.tb_veiculos.verticalHeader().setMinimumSectionSize(20)
        self.lb_FormProdutos_6 = QtWidgets.QLabel(Frame)
        self.lb_FormProdutos_6.setGeometry(QtCore.QRect(140, 430, 215, 20))
        self.lb_FormProdutos_6.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_6.setObjectName("lb_FormProdutos_6")
        self.tx_marca = QtWidgets.QLineEdit(Frame)
        self.tx_marca.setGeometry(QtCore.QRect(140, 450, 251, 25))
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
        self.tx_marca.setPlaceholderText("")
        self.tx_marca.setObjectName("tx_marca")
        self.fr_botoes = QtWidgets.QFrame(Frame)
        self.fr_botoes.setGeometry(QtCore.QRect(-70, 540, 671, 30))
        self.fr_botoes.setStyleSheet("background:#E1DFE0;\n"
"border: none;")
        self.fr_botoes.setObjectName("fr_botoes")
        self.bt_cancelar = QtWidgets.QPushButton(self.fr_botoes)
        self.bt_cancelar.setGeometry(QtCore.QRect(550, 0, 120, 30))
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
        self.bt_salvar.setGeometry(QtCore.QRect(290, 0, 120, 30))
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
        self.bt_excluir.setGeometry(QtCore.QRect(420, 0, 120, 30))
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
        self.cb_veiculos = QtWidgets.QComboBox(Frame)
        self.cb_veiculos.setGeometry(QtCore.QRect(10, 60, 131, 31))
        self.cb_veiculos.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.cb_veiculos.setStyleSheet("QComboBox{\n"
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
        self.cb_veiculos.setObjectName("cb_veiculos")
        self.cb_veiculos.addItem("")
        self.bt_refresh = QtWidgets.QPushButton(Frame)
        self.bt_refresh.setGeometry(QtCore.QRect(570, 60, 30, 31))
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
        self.tx_placa = QtWidgets.QLineEdit(Frame)
        self.tx_placa.setGeometry(QtCore.QRect(10, 450, 121, 25))
        self.tx_placa.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_placa.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"padding-left: 3px;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_placa.setText("")
        self.tx_placa.setPlaceholderText("")
        self.tx_placa.setObjectName("tx_placa")
        self.lb_FormProdutos_7 = QtWidgets.QLabel(Frame)
        self.lb_FormProdutos_7.setGeometry(QtCore.QRect(10, 430, 61, 20))
        self.lb_FormProdutos_7.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_7.setObjectName("lb_FormProdutos_7")
        self.lb_FormProdutos_8 = QtWidgets.QLabel(Frame)
        self.lb_FormProdutos_8.setGeometry(QtCore.QRect(400, 430, 111, 20))
        self.lb_FormProdutos_8.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_8.setObjectName("lb_FormProdutos_8")
        self.tx_modelo = QtWidgets.QLineEdit(Frame)
        self.tx_modelo.setGeometry(QtCore.QRect(400, 450, 191, 25))
        self.tx_modelo.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_modelo.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"padding-left: 3px;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_modelo.setInputMask("")
        self.tx_modelo.setText("")
        self.tx_modelo.setPlaceholderText("")
        self.tx_modelo.setObjectName("tx_modelo")
        self.lb_FormProdutos = QtWidgets.QLabel(Frame)
        self.lb_FormProdutos.setGeometry(QtCore.QRect(10, 390, 971, 30))
        self.lb_FormProdutos.setStyleSheet("QLabel{\n"
"font-size: 14px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"\n"
"border-bottom: 2px solid #A2A2A2\n"
"}")
        self.lb_FormProdutos.setObjectName("lb_FormProdutos")
        self.cb_cliente = QtWidgets.QComboBox(Frame)
        self.cb_cliente.setGeometry(QtCore.QRect(10, 500, 200, 31))
        self.cb_cliente.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.cb_cliente.setStyleSheet("QComboBox{\n"
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
        self.cb_cliente.setObjectName("cb_cliente")
        self.lb_FormProdutos_9 = QtWidgets.QLabel(Frame)
        self.lb_FormProdutos_9.setGeometry(QtCore.QRect(10, 480, 61, 20))
        self.lb_FormProdutos_9.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_9.setObjectName("lb_FormProdutos_9")

        Frame.setTabOrder(self.tx_placa, self.tx_marca)
        Frame.setTabOrder(self.tx_marca, self.tx_modelo)
        Frame.setTabOrder(self.tx_modelo, self.cb_cliente)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Lista de Veiculos"))
        self.lb_tituloClientes_2.setText(_translate("Frame", "VEICULOS"))
        self.bt_novo.setText(_translate("Frame", "NOVO VEICULO"))
        self.tx_busca.setPlaceholderText(_translate("Frame", "PROCURAR POR..."))
        self.bt_busca.setToolTip(_translate("Frame", "BUSCAR"))
        item = self.tb_veiculos.horizontalHeaderItem(0)
        item.setText(_translate("Frame", "PLACA"))
        item = self.tb_veiculos.horizontalHeaderItem(1)
        item.setText(_translate("Frame", "MARCA"))
        item = self.tb_veiculos.horizontalHeaderItem(2)
        item.setText(_translate("Frame", "MODELO"))
        item = self.tb_veiculos.horizontalHeaderItem(3)
        item.setText(_translate("Frame", "CLIENTE"))
        self.lb_FormProdutos_6.setText(_translate("Frame", "MARCA"))
        self.bt_cancelar.setText(_translate("Frame", "CANCELAR"))
        self.bt_salvar.setText(_translate("Frame", "EDITAR"))
        self.bt_excluir.setText(_translate("Frame", "EXCLUIR"))
        self.cb_veiculos.setItemText(0, _translate("Frame", "SELECIONE"))
        self.bt_refresh.setToolTip(_translate("Frame", "ATUALIZAR TABELA"))
        self.lb_FormProdutos_7.setText(_translate("Frame", "PLACA"))
        self.lb_FormProdutos_8.setText(_translate("Frame", "MODELO"))
        self.lb_FormProdutos.setText(_translate("Frame", "ALTERAR INFORMAÇÕES"))
        self.lb_FormProdutos_9.setText(_translate("Frame", "CLIENTE"))
