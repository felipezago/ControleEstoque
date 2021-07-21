# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lista_finalizadoras.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(495, 511)
        Frame.setStyleSheet("background: #FFF;")
        self.fr_TituloClientes = QtWidgets.QFrame(Frame)
        self.fr_TituloClientes.setGeometry(QtCore.QRect(0, 0, 491, 60))
        self.fr_TituloClientes.setStyleSheet("")
        self.fr_TituloClientes.setObjectName("fr_TituloClientes")
        self.lb_tituloClientes_2 = QtWidgets.QLabel(self.fr_TituloClientes)
        self.lb_tituloClientes_2.setGeometry(QtCore.QRect(10, 15, 200, 30))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lb_tituloClientes_2.setFont(font)
        self.lb_tituloClientes_2.setStyleSheet("color: rgb(0, 0, 0)")
        self.lb_tituloClientes_2.setObjectName("lb_tituloClientes_2")
        self.bt_novo = QtWidgets.QPushButton(self.fr_TituloClientes)
        self.bt_novo.setGeometry(QtCore.QRect(310, 10, 171, 41))
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
        self.tx_busca.setGeometry(QtCore.QRect(150, 60, 281, 31))
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
        self.bt_busca.setGeometry(QtCore.QRect(430, 60, 30, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.bt_busca.setFont(font)
        self.bt_busca.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_busca.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_busca.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.bt_busca.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Imagens/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("Imagens/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_busca.setIcon(icon)
        self.bt_busca.setObjectName("bt_busca")
        self.tb_finalizadoras = QtWidgets.QTableWidget(Frame)
        self.tb_finalizadoras.setGeometry(QtCore.QRect(10, 100, 481, 261))
        self.tb_finalizadoras.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tb_finalizadoras.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tb_finalizadoras.setStyleSheet("QTableView{\n"
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
        self.tb_finalizadoras.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tb_finalizadoras.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tb_finalizadoras.setAutoScrollMargin(20)
        self.tb_finalizadoras.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tb_finalizadoras.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tb_finalizadoras.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tb_finalizadoras.setShowGrid(False)
        self.tb_finalizadoras.setGridStyle(QtCore.Qt.NoPen)
        self.tb_finalizadoras.setWordWrap(False)
        self.tb_finalizadoras.setRowCount(0)
        self.tb_finalizadoras.setObjectName("tb_finalizadoras")
        self.tb_finalizadoras.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(0, 0, 0))
        brush = QtGui.QBrush(QtGui.QColor(80, 79, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tb_finalizadoras.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(80, 79, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tb_finalizadoras.setHorizontalHeaderItem(1, item)
        self.tb_finalizadoras.horizontalHeader().setDefaultSectionSize(120)
        self.tb_finalizadoras.horizontalHeader().setHighlightSections(False)
        self.tb_finalizadoras.horizontalHeader().setStretchLastSection(True)
        self.tb_finalizadoras.verticalHeader().setVisible(False)
        self.tb_finalizadoras.verticalHeader().setDefaultSectionSize(50)
        self.tb_finalizadoras.verticalHeader().setMinimumSectionSize(20)
        self.lb_FormProdutos_6 = QtWidgets.QLabel(Frame)
        self.lb_FormProdutos_6.setGeometry(QtCore.QRect(90, 420, 215, 20))
        self.lb_FormProdutos_6.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_6.setObjectName("lb_FormProdutos_6")
        self.tx_desc = QtWidgets.QLineEdit(Frame)
        self.tx_desc.setGeometry(QtCore.QRect(90, 440, 301, 25))
        self.tx_desc.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_desc.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"padding-left: 3px;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_desc.setPlaceholderText("")
        self.tx_desc.setObjectName("tx_desc")
        self.fr_botoes = QtWidgets.QFrame(Frame)
        self.fr_botoes.setGeometry(QtCore.QRect(-180, 480, 671, 30))
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
        self.cb_fin = QtWidgets.QComboBox(Frame)
        self.cb_fin.setGeometry(QtCore.QRect(10, 60, 131, 31))
        self.cb_fin.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.cb_fin.setStyleSheet("QComboBox{\n"
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
        self.cb_fin.setObjectName("cb_fin")
        self.cb_fin.addItem("")
        self.bt_refresh = QtWidgets.QPushButton(Frame)
        self.bt_refresh.setGeometry(QtCore.QRect(460, 60, 30, 31))
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
        self.tx_id.setGeometry(QtCore.QRect(10, 440, 61, 25))
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
        self.lb_FormProdutos_7.setGeometry(QtCore.QRect(10, 420, 61, 20))
        self.lb_FormProdutos_7.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_7.setObjectName("lb_FormProdutos_7")
        self.lb_FormProdutos = QtWidgets.QLabel(Frame)
        self.lb_FormProdutos.setGeometry(QtCore.QRect(10, 380, 971, 30))
        self.lb_FormProdutos.setStyleSheet("QLabel{\n"
"font-size: 14px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"\n"
"border-bottom: 2px solid #A2A2A2\n"
"}")
        self.lb_FormProdutos.setObjectName("lb_FormProdutos")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Lista de Finalizadoras"))
        self.lb_tituloClientes_2.setText(_translate("Frame", "FINALIZADORAS"))
        self.bt_novo.setText(_translate("Frame", "NOVA FINALIZADORA"))
        self.tx_busca.setPlaceholderText(_translate("Frame", "PROCURAR POR..."))
        self.bt_busca.setToolTip(_translate("Frame", "BUSCAR"))
        item = self.tb_finalizadoras.horizontalHeaderItem(0)
        item.setText(_translate("Frame", "ID"))
        item = self.tb_finalizadoras.horizontalHeaderItem(1)
        item.setText(_translate("Frame", "DESCRIÇÃO CATEGORIA"))
        self.lb_FormProdutos_6.setText(_translate("Frame", "DESCRIÇÃO CATEGORIA"))
        self.bt_cancelar.setText(_translate("Frame", "CANCELAR"))
        self.bt_salvar.setText(_translate("Frame", "EDITAR"))
        self.bt_excluir.setText(_translate("Frame", "EXCLUIR"))
        self.cb_fin.setItemText(0, _translate("Frame", "SELECIONE"))
        self.bt_refresh.setToolTip(_translate("Frame", "ATUALIZAR TABELA"))
        self.lb_FormProdutos_7.setText(_translate("Frame", "ID"))
        self.lb_FormProdutos.setText(_translate("Frame", "ALTERAR INFORMAÇÕES"))
