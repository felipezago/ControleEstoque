# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lista_categorias.ui'
#
# Created by: PyQt5 View code generator 5.14.1
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
        self.bt_novo.setGeometry(QtCore.QRect(330, 10, 151, 41))
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
        self.tx_busca_categorias = QtWidgets.QLineEdit(Frame)
        self.tx_busca_categorias.setGeometry(QtCore.QRect(150, 60, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.tx_busca_categorias.setFont(font)
        self.tx_busca_categorias.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tx_busca_categorias.setStyleSheet("QLineEdit {\n"
"color: #000\n"
"}\n"
"")
        self.tx_busca_categorias.setObjectName("tx_busca_categorias")
        self.bt_busca_categorias = QtWidgets.QPushButton(Frame)
        self.bt_busca_categorias.setGeometry(QtCore.QRect(430, 60, 30, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.bt_busca_categorias.setFont(font)
        self.bt_busca_categorias.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_busca_categorias.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_busca_categorias.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.bt_busca_categorias.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Imagens/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_busca_categorias.setIcon(icon)
        self.bt_busca_categorias.setObjectName("bt_busca_categorias")
        self.tb_categorias = QtWidgets.QTableWidget(Frame)
        self.tb_categorias.setGeometry(QtCore.QRect(0, 100, 491, 261))
        self.tb_categorias.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tb_categorias.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tb_categorias.setStyleSheet("QTableView{\n"
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
        self.tb_categorias.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tb_categorias.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tb_categorias.setAutoScrollMargin(20)
        self.tb_categorias.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tb_categorias.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tb_categorias.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tb_categorias.setShowGrid(False)
        self.tb_categorias.setGridStyle(QtCore.Qt.NoPen)
        self.tb_categorias.setWordWrap(False)
        self.tb_categorias.setRowCount(0)
        self.tb_categorias.setObjectName("tb_categorias")
        self.tb_categorias.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe View")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(0, 0, 0))
        brush = QtGui.QBrush(QtGui.QColor(80, 79, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tb_categorias.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Segoe View")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(80, 79, 79))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tb_categorias.setHorizontalHeaderItem(1, item)
        self.tb_categorias.horizontalHeader().setDefaultSectionSize(120)
        self.tb_categorias.horizontalHeader().setHighlightSections(False)
        self.tb_categorias.horizontalHeader().setStretchLastSection(True)
        self.tb_categorias.verticalHeader().setVisible(False)
        self.tb_categorias.verticalHeader().setDefaultSectionSize(50)
        self.tb_categorias.verticalHeader().setMinimumSectionSize(20)
        self.lb_FormProdutos_6 = QtWidgets.QLabel(Frame)
        self.lb_FormProdutos_6.setGeometry(QtCore.QRect(90, 420, 215, 20))
        self.lb_FormProdutos_6.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_6.setObjectName("lb_FormProdutos_6")
        self.tx_desc_cat = QtWidgets.QLineEdit(Frame)
        self.tx_desc_cat.setGeometry(QtCore.QRect(90, 440, 301, 25))
        self.tx_desc_cat.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_desc_cat.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"padding-left: 3px;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_desc_cat.setPlaceholderText("")
        self.tx_desc_cat.setObjectName("tx_desc_cat")
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
        self.cb_categoria = QtWidgets.QComboBox(Frame)
        self.cb_categoria.setGeometry(QtCore.QRect(10, 60, 131, 31))
        self.cb_categoria.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.cb_categoria.setStyleSheet("QComboBox{\n"
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
        self.cb_categoria.setObjectName("cb_categoria")
        self.cb_categoria.addItem("")
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
        Frame.setWindowTitle(_translate("Frame", "Lista de Categorias"))
        self.lb_tituloClientes_2.setText(_translate("Frame", "CATEGORIAS"))
        self.bt_novo.setText(_translate("Frame", "NOVA CATEGORIA"))
        self.tx_busca_categorias.setPlaceholderText(_translate("Frame", "PROCURAR POR..."))
        self.bt_busca_categorias.setToolTip(_translate("Frame", "BUSCAR"))
        item = self.tb_categorias.horizontalHeaderItem(0)
        item.setText(_translate("Frame", "ID"))
        item = self.tb_categorias.horizontalHeaderItem(1)
        item.setText(_translate("Frame", "DESCRIÇÃO CATEGORIA"))
        self.lb_FormProdutos_6.setText(_translate("Frame", "DESCRIÇÃO CATEGORIA"))
        self.bt_cancelar.setText(_translate("Frame", "CANCELAR"))
        self.bt_salvar.setText(_translate("Frame", "EDITAR"))
        self.bt_excluir.setText(_translate("Frame", "EXCLUIR"))
        self.cb_categoria.setItemText(0, _translate("Frame", "SELECIONE"))
        self.bt_refresh.setToolTip(_translate("Frame", "ATUALIZAR TABELA"))
        self.lb_FormProdutos_7.setText(_translate("Frame", "ID"))
        self.lb_FormProdutos.setText(_translate("Frame", "ALTERAR INFORMAÇÕES"))
