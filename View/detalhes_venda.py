# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/detalhes_venda.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(791, 633)
        Frame.setStyleSheet("background: #FFF;")
        self.tb_itens = QtWidgets.QTableWidget(Frame)
        self.tb_itens.setGeometry(QtCore.QRect(0, 180, 781, 181))
        self.tb_itens.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tb_itens.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tb_itens.setStyleSheet("QTableView{\n"
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
"text-transform: uppercase;\n"
"}\n"
"QTableView::item {\n"
"border-bottom: 2px solid #CCC;\n"
"padding: 2px;\n"
"}\n"
"\n"
"")
        self.tb_itens.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tb_itens.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tb_itens.setAutoScrollMargin(20)
        self.tb_itens.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tb_itens.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tb_itens.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tb_itens.setShowGrid(False)
        self.tb_itens.setGridStyle(QtCore.Qt.NoPen)
        self.tb_itens.setWordWrap(False)
        self.tb_itens.setRowCount(1)
        self.tb_itens.setObjectName("tb_itens")
        self.tb_itens.setColumnCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tb_itens.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_itens.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_itens.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_itens.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_itens.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_itens.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_itens.setHorizontalHeaderItem(5, item)
        self.tb_itens.horizontalHeader().setDefaultSectionSize(120)
        self.tb_itens.horizontalHeader().setHighlightSections(False)
        self.tb_itens.horizontalHeader().setStretchLastSection(True)
        self.tb_itens.verticalHeader().setVisible(False)
        self.tb_itens.verticalHeader().setDefaultSectionSize(50)
        self.tb_itens.verticalHeader().setMinimumSectionSize(20)
        self.fr_titulo_servicos = QtWidgets.QFrame(Frame)
        self.fr_titulo_servicos.setGeometry(QtCore.QRect(10, 0, 791, 51))
        self.fr_titulo_servicos.setStyleSheet("")
        self.fr_titulo_servicos.setObjectName("fr_titulo_servicos")
        self.lb_venda = QtWidgets.QLabel(self.fr_titulo_servicos)
        self.lb_venda.setGeometry(QtCore.QRect(10, 10, 311, 30))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lb_venda.setFont(font)
        self.lb_venda.setStyleSheet("color: rgb(0, 0, 0)")
        self.lb_venda.setObjectName("lb_venda")
        self.lb_hora = QtWidgets.QLabel(self.fr_titulo_servicos)
        self.lb_hora.setGeometry(QtCore.QRect(480, 10, 291, 30))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lb_hora.setFont(font)
        self.lb_hora.setStyleSheet("color: rgb(0, 0, 0)")
        self.lb_hora.setObjectName("lb_hora")
        self.lb_tituloClientes_4 = QtWidgets.QLabel(Frame)
        self.lb_tituloClientes_4.setGeometry(QtCore.QRect(10, 60, 111, 21))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lb_tituloClientes_4.setFont(font)
        self.lb_tituloClientes_4.setStyleSheet("color: rgb(0, 0, 0)")
        self.lb_tituloClientes_4.setObjectName("lb_tituloClientes_4")
        self.lb_tituloClientes_5 = QtWidgets.QLabel(Frame)
        self.lb_tituloClientes_5.setGeometry(QtCore.QRect(10, 90, 161, 21))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lb_tituloClientes_5.setFont(font)
        self.lb_tituloClientes_5.setStyleSheet("color: rgb(0, 0, 0)")
        self.lb_tituloClientes_5.setObjectName("lb_tituloClientes_5")
        self.lb_tituloClientes_6 = QtWidgets.QLabel(Frame)
        self.lb_tituloClientes_6.setGeometry(QtCore.QRect(10, 120, 161, 21))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lb_tituloClientes_6.setFont(font)
        self.lb_tituloClientes_6.setStyleSheet("color: rgb(0, 0, 0)")
        self.lb_tituloClientes_6.setObjectName("lb_tituloClientes_6")
        self.lb_tituloClientes_7 = QtWidgets.QLabel(Frame)
        self.lb_tituloClientes_7.setGeometry(QtCore.QRect(10, 380, 221, 30))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lb_tituloClientes_7.setFont(font)
        self.lb_tituloClientes_7.setStyleSheet("color: rgb(0, 0, 0)")
        self.lb_tituloClientes_7.setObjectName("lb_tituloClientes_7")
        self.tb_fin = QtWidgets.QTableWidget(Frame)
        self.tb_fin.setGeometry(QtCore.QRect(0, 420, 791, 171))
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
"text-transform: uppercase;\n"
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
        self.tb_fin.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tb_fin.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_fin.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_fin.setHorizontalHeaderItem(1, item)
        self.tb_fin.horizontalHeader().setDefaultSectionSize(120)
        self.tb_fin.horizontalHeader().setHighlightSections(False)
        self.tb_fin.horizontalHeader().setStretchLastSection(True)
        self.tb_fin.verticalHeader().setVisible(False)
        self.tb_fin.verticalHeader().setDefaultSectionSize(50)
        self.tb_fin.verticalHeader().setMinimumSectionSize(20)
        self.fr_botoes = QtWidgets.QFrame(Frame)
        self.fr_botoes.setGeometry(QtCore.QRect(-190, 600, 991, 30))
        self.fr_botoes.setStyleSheet("background:#E1DFE0;\n"
"border: none;")
        self.fr_botoes.setObjectName("fr_botoes")
        self.bt_cancelar = QtWidgets.QPushButton(self.fr_botoes)
        self.bt_cancelar.setGeometry(QtCore.QRect(860, 0, 120, 30))
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
        self.bt_excluir = QtWidgets.QPushButton(self.fr_botoes)
        self.bt_excluir.setGeometry(QtCore.QRect(730, 0, 120, 30))
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
        self.lb_tituloClientes_8 = QtWidgets.QLabel(Frame)
        self.lb_tituloClientes_8.setGeometry(QtCore.QRect(360, 60, 81, 21))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lb_tituloClientes_8.setFont(font)
        self.lb_tituloClientes_8.setStyleSheet("color: rgb(0, 0, 0)")
        self.lb_tituloClientes_8.setObjectName("lb_tituloClientes_8")
        self.lb_tituloClientes_9 = QtWidgets.QLabel(Frame)
        self.lb_tituloClientes_9.setGeometry(QtCore.QRect(360, 90, 81, 21))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lb_tituloClientes_9.setFont(font)
        self.lb_tituloClientes_9.setStyleSheet("color: rgb(0, 0, 0)")
        self.lb_tituloClientes_9.setObjectName("lb_tituloClientes_9")
        self.lb_total_itens = QtWidgets.QLabel(Frame)
        self.lb_total_itens.setGeometry(QtCore.QRect(170, 60, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lb_total_itens.setFont(font)
        self.lb_total_itens.setStyleSheet("color: rgb(0, 0, 0)")
        self.lb_total_itens.setObjectName("lb_total_itens")
        self.lb_total_descontos = QtWidgets.QLabel(Frame)
        self.lb_total_descontos.setGeometry(QtCore.QRect(170, 90, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lb_total_descontos.setFont(font)
        self.lb_total_descontos.setStyleSheet("color: rgb(0, 0, 0)")
        self.lb_total_descontos.setObjectName("lb_total_descontos")
        self.lb_total_liquido = QtWidgets.QLabel(Frame)
        self.lb_total_liquido.setGeometry(QtCore.QRect(170, 120, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lb_total_liquido.setFont(font)
        self.lb_total_liquido.setStyleSheet("color: rgb(0, 0, 0)")
        self.lb_total_liquido.setObjectName("lb_total_liquido")
        self.lb_cliente = QtWidgets.QLabel(Frame)
        self.lb_cliente.setGeometry(QtCore.QRect(440, 60, 341, 21))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lb_cliente.setFont(font)
        self.lb_cliente.setStyleSheet("color: rgb(0, 0, 0)")
        self.lb_cliente.setObjectName("lb_cliente")
        self.lb_veiculo = QtWidgets.QLabel(Frame)
        self.lb_veiculo.setGeometry(QtCore.QRect(440, 90, 321, 21))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lb_veiculo.setFont(font)
        self.lb_veiculo.setStyleSheet("color: rgb(0, 0, 0)")
        self.lb_veiculo.setObjectName("lb_veiculo")
        self.bt_imprimir = QtWidgets.QPushButton(Frame)
        self.bt_imprimir.setGeometry(QtCore.QRect(730, 140, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.bt_imprimir.setFont(font)
        self.bt_imprimir.setStyleSheet("QPushButton{\n"
"color: #FFF\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #40a286\n"
"}")
        self.bt_imprimir.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Imagens/gtk-print.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_imprimir.setIcon(icon)
        self.bt_imprimir.setObjectName("bt_imprimir")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Detalhes Venda"))
        item = self.tb_itens.verticalHeaderItem(0)
        item.setText(_translate("Frame", "1"))
        item = self.tb_itens.horizontalHeaderItem(0)
        item.setText(_translate("Frame", "ID"))
        item = self.tb_itens.horizontalHeaderItem(1)
        item.setText(_translate("Frame", "DESCRIÇÃO"))
        item = self.tb_itens.horizontalHeaderItem(2)
        item.setText(_translate("Frame", "QTD"))
        item = self.tb_itens.horizontalHeaderItem(3)
        item.setText(_translate("Frame", "VALOR"))
        item = self.tb_itens.horizontalHeaderItem(4)
        item.setText(_translate("Frame", "TOTAL DESCONTOS"))
        item = self.tb_itens.horizontalHeaderItem(5)
        item.setText(_translate("Frame", "TOTAL"))
        self.lb_venda.setText(_translate("Frame", "Venda - Código 09"))
        self.lb_hora.setText(_translate("Frame", "23/12/1998 23:59:00"))
        self.lb_tituloClientes_4.setText(_translate("Frame", "Total Itens:"))
        self.lb_tituloClientes_5.setText(_translate("Frame", "Total Descontos:"))
        self.lb_tituloClientes_6.setText(_translate("Frame", "Total Líquido:"))
        self.lb_tituloClientes_7.setText(_translate("Frame", "Finalizadoras"))
        item = self.tb_fin.verticalHeaderItem(0)
        item.setText(_translate("Frame", "1"))
        item = self.tb_fin.horizontalHeaderItem(0)
        item.setText(_translate("Frame", "DESCRIÇÃO"))
        item = self.tb_fin.horizontalHeaderItem(1)
        item.setText(_translate("Frame", "VALOR PAGO"))
        self.bt_cancelar.setText(_translate("Frame", "CANCELAR"))
        self.bt_excluir.setText(_translate("Frame", "EXCLUIR"))
        self.lb_tituloClientes_8.setText(_translate("Frame", "Cliente:"))
        self.lb_tituloClientes_9.setText(_translate("Frame", "Veículo:"))
        self.lb_total_itens.setText(_translate("Frame", "R$ 5000,00"))
        self.lb_total_descontos.setText(_translate("Frame", "R$ 5000,00"))
        self.lb_total_liquido.setText(_translate("Frame", "R$ 5000,00"))
        self.lb_cliente.setText(_translate("Frame", "Felipe Zago Rodrigues"))
        self.lb_veiculo.setText(_translate("Frame", "Volks - Constelation"))
