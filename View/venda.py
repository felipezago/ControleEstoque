# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'venda.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(778, 593)
        Frame.setStyleSheet("background: #FFF;")
        self.fr_titulo_servicos = QtWidgets.QFrame(Frame)
        self.fr_titulo_servicos.setGeometry(QtCore.QRect(0, 0, 981, 60))
        self.fr_titulo_servicos.setStyleSheet("")
        self.fr_titulo_servicos.setObjectName("fr_titulo_servicos")
        self.lb_tituloClientes_2 = QtWidgets.QLabel(self.fr_titulo_servicos)
        self.lb_tituloClientes_2.setGeometry(QtCore.QRect(10, 15, 391, 30))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lb_tituloClientes_2.setFont(font)
        self.lb_tituloClientes_2.setStyleSheet("color: rgb(0, 0, 0)")
        self.lb_tituloClientes_2.setObjectName("lb_tituloClientes_2")
        self.fr_botoes = QtWidgets.QFrame(Frame)
        self.fr_botoes.setGeometry(QtCore.QRect(-200, 560, 991, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        self.fr_botoes.setFont(font)
        self.fr_botoes.setStyleSheet("background:#E1DFE0;\n"
"border: none;")
        self.fr_botoes.setObjectName("fr_botoes")
        self.bt_cancelar = QtWidgets.QPushButton(self.fr_botoes)
        self.bt_cancelar.setGeometry(QtCore.QRect(819, 0, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
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
        self.bt_finalizar = QtWidgets.QPushButton(self.fr_botoes)
        self.bt_finalizar.setGeometry(QtCore.QRect(480, 0, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bt_finalizar.setFont(font)
        self.bt_finalizar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_finalizar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_finalizar.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.bt_finalizar.setStyleSheet("QPushButton {\n"
"    background-color: rgb(78, 154, 6);\n"
"color: #FFF\n"
" }\n"
"QPushButton:hover{\n"
"    background-color: #40a286\n"
"}")
        self.bt_finalizar.setIconSize(QtCore.QSize(75, 35))
        self.bt_finalizar.setObjectName("bt_finalizar")
        self.bt_aberto = QtWidgets.QPushButton(self.fr_botoes)
        self.bt_aberto.setGeometry(QtCore.QRect(650, 0, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bt_aberto.setFont(font)
        self.bt_aberto.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_aberto.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_aberto.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.bt_aberto.setStyleSheet("QPushButton {\n"
"    background-color: rgb(186, 176, 48);\n"
"color: #FFF\n"
" }\n"
"QPushButton:hover{\n"
"    background-color: rgb(217, 202, 49);\n"
"}")
        self.bt_aberto.setIconSize(QtCore.QSize(75, 35))
        self.bt_aberto.setObjectName("bt_aberto")
        self.tx_busca_item = QtWidgets.QLineEdit(Frame)
        self.tx_busca_item.setGeometry(QtCore.QRect(160, 210, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(9)
        self.tx_busca_item.setFont(font)
        self.tx_busca_item.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tx_busca_item.setStyleSheet("QLineEdit {\n"
"color: #000\n"
"}\n"
"")
        self.tx_busca_item.setObjectName("tx_busca_item")
        self.bt_busca_item = QtWidgets.QPushButton(Frame)
        self.bt_busca_item.setGeometry(QtCore.QRect(260, 210, 30, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(9)
        self.bt_busca_item.setFont(font)
        self.bt_busca_item.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_busca_item.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_busca_item.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.bt_busca_item.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Imagens/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_busca_item.setIcon(icon)
        self.bt_busca_item.setObjectName("bt_busca_item")
        self.cb_selec = QtWidgets.QComboBox(Frame)
        self.cb_selec.setGeometry(QtCore.QRect(10, 210, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cb_selec.setFont(font)
        self.cb_selec.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.cb_selec.setStyleSheet("QComboBox{\n"
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
        self.cb_selec.setObjectName("cb_selec")
        self.cb_selec.addItem("")
        self.tb_venda = QtWidgets.QTableWidget(Frame)
        self.tb_venda.setGeometry(QtCore.QRect(0, 290, 841, 181))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.tb_venda.setFont(font)
        self.tb_venda.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tb_venda.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tb_venda.setStyleSheet("QTableView{\n"
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
        self.tb_venda.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tb_venda.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tb_venda.setAutoScrollMargin(20)
        self.tb_venda.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tb_venda.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tb_venda.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tb_venda.setShowGrid(False)
        self.tb_venda.setGridStyle(QtCore.Qt.NoPen)
        self.tb_venda.setWordWrap(False)
        self.tb_venda.setRowCount(0)
        self.tb_venda.setObjectName("tb_venda")
        self.tb_venda.setColumnCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.tb_venda.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_venda.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_venda.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_venda.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_venda.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_venda.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_venda.setHorizontalHeaderItem(6, item)
        self.tb_venda.horizontalHeader().setDefaultSectionSize(120)
        self.tb_venda.horizontalHeader().setHighlightSections(False)
        self.tb_venda.horizontalHeader().setStretchLastSection(True)
        self.tb_venda.verticalHeader().setVisible(False)
        self.tb_venda.verticalHeader().setDefaultSectionSize(50)
        self.tb_venda.verticalHeader().setMinimumSectionSize(20)
        self.lb_tituloClientes_3 = QtWidgets.QLabel(Frame)
        self.lb_tituloClientes_3.setGeometry(QtCore.QRect(20, 250, 391, 30))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lb_tituloClientes_3.setFont(font)
        self.lb_tituloClientes_3.setStyleSheet("color: rgb(0, 0, 0)")
        self.lb_tituloClientes_3.setObjectName("lb_tituloClientes_3")
        self.lb_tituloClientes_4 = QtWidgets.QLabel(Frame)
        self.lb_tituloClientes_4.setGeometry(QtCore.QRect(532, 480, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lb_tituloClientes_4.setFont(font)
        self.lb_tituloClientes_4.setStyleSheet("color: rgb(0, 0, 0)")
        self.lb_tituloClientes_4.setObjectName("lb_tituloClientes_4")
        self.lb_valor_parcial = QtWidgets.QLabel(Frame)
        self.lb_valor_parcial.setGeometry(QtCore.QRect(700, 480, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lb_valor_parcial.setFont(font)
        self.lb_valor_parcial.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lb_valor_parcial.setStyleSheet("color: rgb(0, 0, 0)")
        self.lb_valor_parcial.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lb_valor_parcial.setObjectName("lb_valor_parcial")
        self.tx_qtd = QtWidgets.QLineEdit(Frame)
        self.tx_qtd.setGeometry(QtCore.QRect(600, 210, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(9)
        self.tx_qtd.setFont(font)
        self.tx_qtd.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tx_qtd.setStyleSheet("QLineEdit {\n"
"color: #000\n"
"}\n"
"")
        self.tx_qtd.setText("")
        self.tx_qtd.setPlaceholderText("")
        self.tx_qtd.setObjectName("tx_qtd")
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(600, 190, 41, 17))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setGeometry(QtCore.QRect(160, 190, 91, 17))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.bt_inserir = QtWidgets.QPushButton(Frame)
        self.bt_inserir.setGeometry(QtCore.QRect(600, 250, 161, 31))
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
        self.lb_FormFornecedor = QtWidgets.QLabel(Frame)
        self.lb_FormFornecedor.setGeometry(QtCore.QRect(10, 150, 950, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lb_FormFornecedor.setFont(font)
        self.lb_FormFornecedor.setStyleSheet("QLabel{\n"
"font-size: 14px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"\n"
"border-bottom: 2px solid #A2A2A2\n"
"}")
        self.lb_FormFornecedor.setObjectName("lb_FormFornecedor")
        self.lb_FormFornecedor_2 = QtWidgets.QLabel(Frame)
        self.lb_FormFornecedor_2.setGeometry(QtCore.QRect(10, 50, 950, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lb_FormFornecedor_2.setFont(font)
        self.lb_FormFornecedor_2.setStyleSheet("QLabel{\n"
"font-size: 14px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"\n"
"border-bottom: 2px solid #A2A2A2\n"
"}")
        self.lb_FormFornecedor_2.setObjectName("lb_FormFornecedor_2")
        self.tx_busca_cliente = QtWidgets.QLineEdit(Frame)
        self.tx_busca_cliente.setGeometry(QtCore.QRect(10, 110, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(9)
        self.tx_busca_cliente.setFont(font)
        self.tx_busca_cliente.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tx_busca_cliente.setStyleSheet("QLineEdit {\n"
"color: #000\n"
"}\n"
"")
        self.tx_busca_cliente.setText("")
        self.tx_busca_cliente.setObjectName("tx_busca_cliente")
        self.bt_busca_cliente = QtWidgets.QPushButton(Frame)
        self.bt_busca_cliente.setGeometry(QtCore.QRect(110, 110, 30, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(9)
        self.bt_busca_cliente.setFont(font)
        self.bt_busca_cliente.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_busca_cliente.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_busca_cliente.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.bt_busca_cliente.setText("")
        self.bt_busca_cliente.setIcon(icon)
        self.bt_busca_cliente.setObjectName("bt_busca_cliente")
        self.label_6 = QtWidgets.QLabel(Frame)
        self.label_6.setGeometry(QtCore.QRect(10, 90, 91, 17))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.tx_nome_cliente = QtWidgets.QLineEdit(Frame)
        self.tx_nome_cliente.setGeometry(QtCore.QRect(150, 110, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(9)
        self.tx_nome_cliente.setFont(font)
        self.tx_nome_cliente.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tx_nome_cliente.setStyleSheet("QLineEdit {\n"
"color: #000\n"
"}\n"
"")
        self.tx_nome_cliente.setText("")
        self.tx_nome_cliente.setPlaceholderText("")
        self.tx_nome_cliente.setObjectName("tx_nome_cliente")
        self.label_7 = QtWidgets.QLabel(Frame)
        self.label_7.setGeometry(QtCore.QRect(150, 90, 91, 17))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Frame)
        self.label_8.setGeometry(QtCore.QRect(300, 190, 91, 17))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.tx_descricao_prod = QtWidgets.QLineEdit(Frame)
        self.tx_descricao_prod.setGeometry(QtCore.QRect(300, 210, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(9)
        self.tx_descricao_prod.setFont(font)
        self.tx_descricao_prod.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tx_descricao_prod.setStyleSheet("QLineEdit {\n"
"color: #000\n"
"}\n"
"")
        self.tx_descricao_prod.setText("")
        self.tx_descricao_prod.setPlaceholderText("")
        self.tx_descricao_prod.setObjectName("tx_descricao_prod")
        self.cb_veiculo = QtWidgets.QComboBox(Frame)
        self.cb_veiculo.setGeometry(QtCore.QRect(360, 110, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cb_veiculo.setFont(font)
        self.cb_veiculo.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.cb_veiculo.setStyleSheet("QComboBox{\n"
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
        self.cb_veiculo.setObjectName("cb_veiculo")
        self.label_9 = QtWidgets.QLabel(Frame)
        self.label_9.setGeometry(QtCore.QRect(360, 90, 91, 17))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Frame)
        self.label_10.setGeometry(QtCore.QRect(10, 190, 91, 17))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(9)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.bt_excluir = QtWidgets.QPushButton(Frame)
        self.bt_excluir.setGeometry(QtCore.QRect(10, 480, 161, 31))
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
        self.bt_add_veiculo = QtWidgets.QPushButton(Frame)
        self.bt_add_veiculo.setGeometry(QtCore.QRect(560, 110, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.bt_add_veiculo.setFont(font)
        self.bt_add_veiculo.setStyleSheet("QPushButton{\n"
"background: #7AB32E;\n"
"color: #FFF;\n"
"border: 1px solid green\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #40a286\n"
"}")
        self.bt_add_veiculo.setText("")
        icon = QtGui.QIcon.fromTheme("add")
        self.bt_add_veiculo.setIcon(icon)
        self.bt_add_veiculo.setObjectName("bt_add_veiculo")
        self.label_4 = QtWidgets.QLabel(Frame)
        self.label_4.setGeometry(QtCore.QRect(510, 190, 51, 17))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.tx_valor = QtWidgets.QLineEdit(Frame)
        self.tx_valor.setGeometry(QtCore.QRect(510, 210, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(9)
        self.tx_valor.setFont(font)
        self.tx_valor.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tx_valor.setStyleSheet("QLineEdit {\n"
"color: #000\n"
"}\n"
"")
        self.tx_valor.setText("")
        self.tx_valor.setPlaceholderText("")
        self.tx_valor.setObjectName("tx_valor")
        self.label_5 = QtWidgets.QLabel(Frame)
        self.label_5.setGeometry(QtCore.QRect(680, 190, 51, 17))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.tx_total = QtWidgets.QLineEdit(Frame)
        self.tx_total.setGeometry(QtCore.QRect(680, 210, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(9)
        self.tx_total.setFont(font)
        self.tx_total.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tx_total.setStyleSheet("QLineEdit {\n"
"color: #000\n"
"}\n"
"")
        self.tx_total.setText("")
        self.tx_total.setPlaceholderText("")
        self.tx_total.setObjectName("tx_total")
        self.bt_descontos = QtWidgets.QPushButton(Frame)
        self.bt_descontos.setGeometry(QtCore.QRect(180, 480, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bt_descontos.setFont(font)
        self.bt_descontos.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_descontos.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_descontos.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.bt_descontos.setStyleSheet("QPushButton {\n"
"background-color: #1E87F0;\n"
"color: #FFF\n"
" }\n"
"QPushButton:hover{\n"
"background-color: #40a286\n"
"}")
        self.bt_descontos.setIconSize(QtCore.QSize(75, 35))
        self.bt_descontos.setObjectName("bt_descontos")
        self.lb_tituloClientes_5 = QtWidgets.QLabel(Frame)
        self.lb_tituloClientes_5.setGeometry(QtCore.QRect(560, 500, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lb_tituloClientes_5.setFont(font)
        self.lb_tituloClientes_5.setStyleSheet("color: rgb(0, 0, 0);\n"
"margin-left: 30pt;")
        self.lb_tituloClientes_5.setObjectName("lb_tituloClientes_5")
        self.lb_descontos = QtWidgets.QLabel(Frame)
        self.lb_descontos.setGeometry(QtCore.QRect(700, 500, 71, 21))
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
        self.lb_tituloClientes_6 = QtWidgets.QLabel(Frame)
        self.lb_tituloClientes_6.setGeometry(QtCore.QRect(555, 520, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lb_tituloClientes_6.setFont(font)
        self.lb_tituloClientes_6.setStyleSheet("color: rgb(0, 0, 0)")
        self.lb_tituloClientes_6.setObjectName("lb_tituloClientes_6")
        self.lb_valor_pago = QtWidgets.QLabel(Frame)
        self.lb_valor_pago.setGeometry(QtCore.QRect(700, 520, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lb_valor_pago.setFont(font)
        self.lb_valor_pago.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lb_valor_pago.setStyleSheet("color: rgb(0, 0, 0)")
        self.lb_valor_pago.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lb_valor_pago.setObjectName("lb_valor_pago")
        self.bt_alterar_cliente = QtWidgets.QPushButton(Frame)
        self.bt_alterar_cliente.setGeometry(QtCore.QRect(610, 110, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bt_alterar_cliente.setFont(font)
        self.bt_alterar_cliente.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_alterar_cliente.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_alterar_cliente.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.bt_alterar_cliente.setStyleSheet("QPushButton {\n"
"    background-color: rgb(186, 176, 48);\n"
"color: #FFF\n"
" }\n"
"QPushButton:hover{\n"
"    background-color: rgb(217, 202, 49);\n"
"}")
        self.bt_alterar_cliente.setIconSize(QtCore.QSize(75, 35))
        self.bt_alterar_cliente.setObjectName("bt_alterar_cliente")
        self.lb_tituloClientes_7 = QtWidgets.QLabel(Frame)
        self.lb_tituloClientes_7.setGeometry(QtCore.QRect(550, 540, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lb_tituloClientes_7.setFont(font)
        self.lb_tituloClientes_7.setStyleSheet("color: rgb(0, 0, 0)")
        self.lb_tituloClientes_7.setObjectName("lb_tituloClientes_7")
        self.lb_valor_total = QtWidgets.QLabel(Frame)
        self.lb_valor_total.setGeometry(QtCore.QRect(700, 540, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lb_valor_total.setFont(font)
        self.lb_valor_total.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lb_valor_total.setStyleSheet("color: rgb(0, 0, 0)")
        self.lb_valor_total.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lb_valor_total.setObjectName("lb_valor_total")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)
        Frame.setTabOrder(self.cb_selec, self.tb_venda)
        Frame.setTabOrder(self.tb_venda, self.cb_veiculo)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Venda"))
        self.lb_tituloClientes_2.setText(_translate("Frame", "VENDA - SAÍDA DE ESTOQUE"))
        self.bt_cancelar.setText(_translate("Frame", "CANCELAR"))
        self.bt_finalizar.setText(_translate("Frame", "PAGAMENTO"))
        self.bt_aberto.setText(_translate("Frame", "DEIXAR EM ABERTO"))
        self.tx_busca_item.setPlaceholderText(_translate("Frame", "Código"))
        self.bt_busca_item.setToolTip(_translate("Frame", "BUSCAR"))
        self.cb_selec.setItemText(0, _translate("Frame", "SELECIONE"))
        item = self.tb_venda.horizontalHeaderItem(0)
        item.setText(_translate("Frame", "ID"))
        item = self.tb_venda.horizontalHeaderItem(1)
        item.setText(_translate("Frame", "DESCRIÇÃO"))
        item = self.tb_venda.horizontalHeaderItem(2)
        item.setText(_translate("Frame", "VL. UNIT."))
        item = self.tb_venda.horizontalHeaderItem(3)
        item.setText(_translate("Frame", "QTD"))
        item = self.tb_venda.horizontalHeaderItem(4)
        item.setText(_translate("Frame", "VL. TOTAL"))
        item = self.tb_venda.horizontalHeaderItem(5)
        item.setText(_translate("Frame", "DESCONTO"))
        item = self.tb_venda.horizontalHeaderItem(6)
        item.setText(_translate("Frame", "TIPO"))
        self.lb_tituloClientes_3.setText(_translate("Frame", "ITENS"))
        self.lb_tituloClientes_4.setText(_translate("Frame", "VALOR PARCIAL: R$ "))
        self.lb_valor_parcial.setText(_translate("Frame", "5000,00"))
        self.label.setText(_translate("Frame", "QTD"))
        self.label_2.setText(_translate("Frame", "ITEM"))
        self.bt_inserir.setText(_translate("Frame", "INSERIR"))
        self.lb_FormFornecedor.setText(_translate("Frame", "INSERIR "))
        self.lb_FormFornecedor_2.setText(_translate("Frame", "CABEÇALHO"))
        self.tx_busca_cliente.setPlaceholderText(_translate("Frame", "Código"))
        self.bt_busca_cliente.setToolTip(_translate("Frame", "BUSCAR"))
        self.label_6.setText(_translate("Frame", "CLIENTE"))
        self.label_7.setText(_translate("Frame", "NOME"))
        self.label_8.setText(_translate("Frame", "DESCRIÇÃO"))
        self.label_9.setText(_translate("Frame", "VEÍCULO"))
        self.label_10.setText(_translate("Frame", "TIPO"))
        self.bt_excluir.setText(_translate("Frame", "EXCLUIR ITEM"))
        self.label_4.setText(_translate("Frame", "VALOR"))
        self.label_5.setText(_translate("Frame", "TOTAL"))
        self.bt_descontos.setText(_translate("Frame", "DESCONTOS"))
        self.lb_tituloClientes_5.setText(_translate("Frame", "DESCONTOS: R$ "))
        self.lb_descontos.setText(_translate("Frame", "5000,00"))
        self.lb_tituloClientes_6.setText(_translate("Frame", "VALOR PAGO: R$ "))
        self.lb_valor_pago.setText(_translate("Frame", "5000,00"))
        self.bt_alterar_cliente.setText(_translate("Frame", "ALTERAR CLIENTE"))
        self.lb_tituloClientes_7.setText(_translate("Frame", "VALOR TOTAL: R$ "))
        self.lb_valor_total.setText(_translate("Frame", "5000,00"))
