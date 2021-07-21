# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'finalizar.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(552, 471)
        Frame.setAutoFillBackground(False)
        Frame.setStyleSheet("background: #FFF;")
        self.fr_titulo_servicos = QtWidgets.QFrame(Frame)
        self.fr_titulo_servicos.setGeometry(QtCore.QRect(0, 0, 1051, 51))
        self.fr_titulo_servicos.setStyleSheet("")
        self.fr_titulo_servicos.setObjectName("fr_titulo_servicos")
        self.lb_tituloClientes_2 = QtWidgets.QLabel(self.fr_titulo_servicos)
        self.lb_tituloClientes_2.setGeometry(QtCore.QRect(10, 10, 151, 30))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lb_tituloClientes_2.setFont(font)
        self.lb_tituloClientes_2.setStyleSheet("color: rgb(0, 0, 0)")
        self.lb_tituloClientes_2.setObjectName("lb_tituloClientes_2")
        self.tb_fin = QtWidgets.QTableWidget(Frame)
        self.tb_fin.setGeometry(QtCore.QRect(10, 130, 531, 231))
        self.tb_fin.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tb_fin.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tb_fin.setStyleSheet("QTableView{\n"
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
        self.tb_fin.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tb_fin.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tb_fin.setAutoScrollMargin(20)
        self.tb_fin.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tb_fin.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tb_fin.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tb_fin.setShowGrid(False)
        self.tb_fin.setGridStyle(QtCore.Qt.NoPen)
        self.tb_fin.setWordWrap(False)
        self.tb_fin.setRowCount(1)
        self.tb_fin.setObjectName("tb_fin")
        self.tb_fin.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tb_fin.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_fin.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_fin.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_fin.setHorizontalHeaderItem(2, item)
        self.tb_fin.horizontalHeader().setDefaultSectionSize(120)
        self.tb_fin.horizontalHeader().setHighlightSections(False)
        self.tb_fin.horizontalHeader().setStretchLastSection(True)
        self.tb_fin.verticalHeader().setVisible(False)
        self.tb_fin.verticalHeader().setDefaultSectionSize(50)
        self.tb_fin.verticalHeader().setMinimumSectionSize(20)
        self.fr_botoes = QtWidgets.QFrame(Frame)
        self.fr_botoes.setGeometry(QtCore.QRect(-40, 440, 591, 30))
        self.fr_botoes.setStyleSheet("background:#E1DFE0;\n"
"border: none;")
        self.fr_botoes.setObjectName("fr_botoes")
        self.bt_sair = QtWidgets.QPushButton(self.fr_botoes)
        self.bt_sair.setGeometry(QtCore.QRect(470, 0, 120, 30))
        font = QtGui.QFont()
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
        self.tx_valor.setGeometry(QtCore.QRect(250, 90, 151, 31))
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
        self.cb_pagamento = QtWidgets.QComboBox(Frame)
        self.cb_pagamento.setGeometry(QtCore.QRect(10, 90, 201, 31))
        self.cb_pagamento.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.cb_pagamento.setStyleSheet("QComboBox{\n"
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
        self.cb_pagamento.setObjectName("cb_pagamento")
        self.cb_pagamento.addItem("")
        self.label_8 = QtWidgets.QLabel(Frame)
        self.label_8.setGeometry(QtCore.QRect(10, 70, 171, 17))
        self.label_8.setObjectName("label_8")
        self.bt_add_finalizadora = QtWidgets.QPushButton(Frame)
        self.bt_add_finalizadora.setGeometry(QtCore.QRect(210, 90, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.bt_add_finalizadora.setFont(font)
        self.bt_add_finalizadora.setStyleSheet("QPushButton{\n"
"background: #7AB32E;\n"
"color: #FFF\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #40a286\n"
"}")
        self.bt_add_finalizadora.setText("")
        icon = QtGui.QIcon.fromTheme("add")
        self.bt_add_finalizadora.setIcon(icon)
        self.bt_add_finalizadora.setObjectName("bt_add_finalizadora")
        self.label_9 = QtWidgets.QLabel(Frame)
        self.label_9.setGeometry(QtCore.QRect(250, 70, 171, 17))
        self.label_9.setObjectName("label_9")
        self.bt_inserir = QtWidgets.QPushButton(Frame)
        self.bt_inserir.setGeometry(QtCore.QRect(410, 90, 131, 30))
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
        self.lb_descontos = QtWidgets.QLabel(Frame)
        self.lb_descontos.setGeometry(QtCore.QRect(720, 440, 71, 21))
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
        self.lb_valor_parcial = QtWidgets.QLabel(Frame)
        self.lb_valor_parcial.setGeometry(QtCore.QRect(720, 420, 71, 21))
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
        self.lb_tituloClientes_6 = QtWidgets.QLabel(Frame)
        self.lb_tituloClientes_6.setGeometry(QtCore.QRect(570, 460, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lb_tituloClientes_6.setFont(font)
        self.lb_tituloClientes_6.setStyleSheet("color: rgb(0, 0, 0)")
        self.lb_tituloClientes_6.setObjectName("lb_tituloClientes_6")
        self.lb_tituloClientes_7 = QtWidgets.QLabel(Frame)
        self.lb_tituloClientes_7.setGeometry(QtCore.QRect(580, 440, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lb_tituloClientes_7.setFont(font)
        self.lb_tituloClientes_7.setStyleSheet("color: rgb(0, 0, 0);\n"
"margin-left: 30pt;")
        self.lb_tituloClientes_7.setObjectName("lb_tituloClientes_7")
        self.lb_valor_total = QtWidgets.QLabel(Frame)
        self.lb_valor_total.setGeometry(QtCore.QRect(720, 460, 71, 21))
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
        self.lb_pago = QtWidgets.QLabel(Frame)
        self.lb_pago.setGeometry(QtCore.QRect(470, 390, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lb_pago.setFont(font)
        self.lb_pago.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lb_pago.setStyleSheet("color: rgb(0, 0, 0)")
        self.lb_pago.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lb_pago.setObjectName("lb_pago")
        self.lb_tituloClientes_8 = QtWidgets.QLabel(Frame)
        self.lb_tituloClientes_8.setGeometry(QtCore.QRect(325, 370, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lb_tituloClientes_8.setFont(font)
        self.lb_tituloClientes_8.setStyleSheet("color: rgb(0, 0, 0)")
        self.lb_tituloClientes_8.setObjectName("lb_tituloClientes_8")
        self.lb_total = QtWidgets.QLabel(Frame)
        self.lb_total.setGeometry(QtCore.QRect(470, 370, 71, 21))
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
        self.lb_tituloClientes_9 = QtWidgets.QLabel(Frame)
        self.lb_tituloClientes_9.setGeometry(QtCore.QRect(350, 410, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lb_tituloClientes_9.setFont(font)
        self.lb_tituloClientes_9.setStyleSheet("color: rgb(0, 0, 0)")
        self.lb_tituloClientes_9.setObjectName("lb_tituloClientes_9")
        self.lb_tituloClientes_10 = QtWidgets.QLabel(Frame)
        self.lb_tituloClientes_10.setGeometry(QtCore.QRect(390, 390, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lb_tituloClientes_10.setFont(font)
        self.lb_tituloClientes_10.setStyleSheet("color: rgb(0, 0, 0);\n"
"margin-left: 30pt;")
        self.lb_tituloClientes_10.setObjectName("lb_tituloClientes_10")
        self.lb_restante = QtWidgets.QLabel(Frame)
        self.lb_restante.setGeometry(QtCore.QRect(470, 410, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lb_restante.setFont(font)
        self.lb_restante.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lb_restante.setStyleSheet("color: rgb(0, 0, 0)")
        self.lb_restante.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lb_restante.setObjectName("lb_restante")
        self.bt_excluir = QtWidgets.QPushButton(Frame)
        self.bt_excluir.setGeometry(QtCore.QRect(10, 400, 171, 31))
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
        Frame.setWindowTitle(_translate("Frame", "Finalizar"))
        self.lb_tituloClientes_2.setText(_translate("Frame", "FINALIZAR"))
        item = self.tb_fin.verticalHeaderItem(0)
        item.setText(_translate("Frame", "1"))
        item = self.tb_fin.horizontalHeaderItem(0)
        item.setText(_translate("Frame", "ID"))
        item = self.tb_fin.horizontalHeaderItem(1)
        item.setText(_translate("Frame", "FINALIZADORA"))
        item = self.tb_fin.horizontalHeaderItem(2)
        item.setText(_translate("Frame", "VALOR PAGO"))
        self.bt_sair.setText(_translate("Frame", "SAIR"))
        self.cb_pagamento.setItemText(0, _translate("Frame", "SELECIONE"))
        self.label_8.setText(_translate("Frame", "FORMA DE PAGAMENTO"))
        self.label_9.setText(_translate("Frame", "VALOR"))
        self.bt_inserir.setText(_translate("Frame", "INSERIR"))
        self.lb_descontos.setText(_translate("Frame", "5000,00"))
        self.lb_valor_parcial.setText(_translate("Frame", "5000,00"))
        self.lb_tituloClientes_6.setText(_translate("Frame", "VALOR TOTAL: R$ "))
        self.lb_tituloClientes_7.setText(_translate("Frame", "DESCONTOS: R$ "))
        self.lb_valor_total.setText(_translate("Frame", "5000,00"))
        self.lb_pago.setText(_translate("Frame", "5000,00"))
        self.lb_tituloClientes_8.setText(_translate("Frame", "VALOR TOTAL: R$ "))
        self.lb_total.setText(_translate("Frame", "5000,00"))
        self.lb_tituloClientes_9.setText(_translate("Frame", "RESTANTE: R$"))
        self.lb_tituloClientes_10.setText(_translate("Frame", "PAGO: R$"))
        self.lb_restante.setText(_translate("Frame", "5000,00"))
        self.bt_excluir.setText(_translate("Frame", "EXCLUIR FINALIZAÇÃO"))
