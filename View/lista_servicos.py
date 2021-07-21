# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lista_servicos.ui'
#
# Created by: PyQt5 View code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(522, 522)
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
        self.bt_novo = QtWidgets.QPushButton(self.fr_titulo_servicos)
        self.bt_novo.setGeometry(QtCore.QRect(360, 10, 151, 41))
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
        self.lb_FormProdutos_6 = QtWidgets.QLabel(Frame)
        self.lb_FormProdutos_6.setGeometry(QtCore.QRect(80, 430, 215, 20))
        self.lb_FormProdutos_6.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_6.setObjectName("lb_FormProdutos_6")
        self.tx_desc_serv = QtWidgets.QLineEdit(Frame)
        self.tx_desc_serv.setGeometry(QtCore.QRect(80, 450, 311, 25))
        self.tx_desc_serv.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_desc_serv.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"padding-left: 3px;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_desc_serv.setPlaceholderText("")
        self.tx_desc_serv.setObjectName("tx_desc_serv")
        self.fr_botoes = QtWidgets.QFrame(Frame)
        self.fr_botoes.setGeometry(QtCore.QRect(-150, 490, 671, 30))
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
        self.tx_id = QtWidgets.QLineEdit(Frame)
        self.tx_id.setGeometry(QtCore.QRect(10, 450, 61, 25))
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
        self.tx_preco = QtWidgets.QLineEdit(Frame)
        self.tx_preco.setGeometry(QtCore.QRect(400, 450, 111, 25))
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

        Frame.setTabOrder(self.tx_desc_serv, self.tx_preco)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Lista de Serviços"))
        self.lb_tituloClientes_2.setText(_translate("Frame", "SERVIÇOS"))
        self.bt_novo.setText(_translate("Frame", "NOVO SERVIÇO"))
        self.tx_busca_servicos.setPlaceholderText(_translate("Frame", "PROCURAR POR..."))
        self.bt_busca_servicos.setToolTip(_translate("Frame", "BUSCAR"))
        item = self.tb_servicos.horizontalHeaderItem(0)
        item.setText(_translate("Frame", "ID"))
        item = self.tb_servicos.horizontalHeaderItem(1)
        item.setText(_translate("Frame", "DESCRIÇÃO"))
        item = self.tb_servicos.horizontalHeaderItem(2)
        item.setText(_translate("Frame", "PREÇO"))
        self.lb_FormProdutos_6.setText(_translate("Frame", "DESCRIÇÃO "))
        self.bt_cancelar.setText(_translate("Frame", "CANCELAR"))
        self.bt_salvar.setText(_translate("Frame", "EDITAR"))
        self.bt_excluir.setText(_translate("Frame", "EXCLUIR"))
        self.cb_servicos.setItemText(0, _translate("Frame", "SELECIONE"))
        self.bt_refresh.setToolTip(_translate("Frame", "ATUALIZAR TABELA"))
        self.lb_FormProdutos_7.setText(_translate("Frame", "ID"))
        self.lb_FormProdutos_8.setText(_translate("Frame", "PREÇO"))
        self.lb_FormProdutos.setText(_translate("Frame", "ALTERAR INFORMAÇÕES"))
