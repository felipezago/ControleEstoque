# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/pendencias.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(887, 548)
        Frame.setStyleSheet("background: #FFF;")
        self.tx_busca = QtWidgets.QLineEdit(Frame)
        self.tx_busca.setGeometry(QtCore.QRect(190, 60, 631, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.tx_busca.setFont(font)
        self.tx_busca.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tx_busca.setStyleSheet("QLineEdit {\n"
"color: #000\n"
"}\n"
"")
        self.tx_busca.setObjectName("tx_busca")
        self.cb_vendas = QtWidgets.QComboBox(Frame)
        self.cb_vendas.setGeometry(QtCore.QRect(10, 60, 171, 31))
        self.cb_vendas.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.cb_vendas.setStyleSheet("QComboBox{\n"
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
        self.cb_vendas.setObjectName("cb_vendas")
        self.cb_vendas.addItem("")
        self.cb_vendas.addItem("")
        self.tb_pend = QtWidgets.QTableWidget(Frame)
        self.tb_pend.setGeometry(QtCore.QRect(0, 100, 881, 441))
        self.tb_pend.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tb_pend.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tb_pend.setStyleSheet("QTableView{\n"
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
        self.tb_pend.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tb_pend.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tb_pend.setAutoScrollMargin(20)
        self.tb_pend.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tb_pend.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tb_pend.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tb_pend.setShowGrid(False)
        self.tb_pend.setGridStyle(QtCore.Qt.NoPen)
        self.tb_pend.setWordWrap(False)
        self.tb_pend.setRowCount(1)
        self.tb_pend.setObjectName("tb_pend")
        self.tb_pend.setColumnCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.tb_pend.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_pend.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_pend.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_pend.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_pend.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_pend.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_pend.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_pend.setHorizontalHeaderItem(6, item)
        self.tb_pend.horizontalHeader().setDefaultSectionSize(120)
        self.tb_pend.horizontalHeader().setHighlightSections(False)
        self.tb_pend.horizontalHeader().setStretchLastSection(True)
        self.tb_pend.verticalHeader().setVisible(False)
        self.tb_pend.verticalHeader().setDefaultSectionSize(50)
        self.tb_pend.verticalHeader().setMinimumSectionSize(20)
        self.fr_titulo_servicos = QtWidgets.QFrame(Frame)
        self.fr_titulo_servicos.setGeometry(QtCore.QRect(0, 0, 981, 51))
        self.fr_titulo_servicos.setStyleSheet("")
        self.fr_titulo_servicos.setObjectName("fr_titulo_servicos")
        self.lb_tituloClientes_2 = QtWidgets.QLabel(self.fr_titulo_servicos)
        self.lb_tituloClientes_2.setGeometry(QtCore.QRect(10, 10, 200, 30))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lb_tituloClientes_2.setFont(font)
        self.lb_tituloClientes_2.setStyleSheet("color: rgb(0, 0, 0)")
        self.lb_tituloClientes_2.setObjectName("lb_tituloClientes_2")
        self.bt_refresh = QtWidgets.QPushButton(Frame)
        self.bt_refresh.setGeometry(QtCore.QRect(850, 60, 30, 31))
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
        self.bt_busca = QtWidgets.QPushButton(Frame)
        self.bt_busca.setGeometry(QtCore.QRect(820, 60, 30, 31))
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
        Frame.setWindowTitle(_translate("Frame", "Pendências"))
        self.tx_busca.setPlaceholderText(_translate("Frame", "PROCURAR POR..."))
        self.cb_vendas.setItemText(0, _translate("Frame", "ID"))
        self.cb_vendas.setItemText(1, _translate("Frame", "CLIENTE"))
        item = self.tb_pend.verticalHeaderItem(0)
        item.setText(_translate("Frame", "1"))
        item = self.tb_pend.horizontalHeaderItem(0)
        item.setText(_translate("Frame", "ID"))
        item = self.tb_pend.horizontalHeaderItem(1)
        item.setText(_translate("Frame", "VENDA"))
        item = self.tb_pend.horizontalHeaderItem(2)
        item.setText(_translate("Frame", "CLIENTE"))
        item = self.tb_pend.horizontalHeaderItem(3)
        item.setText(_translate("Frame", "TOTAL DEVIDO"))
        item = self.tb_pend.horizontalHeaderItem(4)
        item.setText(_translate("Frame", "PAGO"))
        item = self.tb_pend.horizontalHeaderItem(5)
        item.setText(_translate("Frame", "RESTANTE"))
        item = self.tb_pend.horizontalHeaderItem(6)
        item.setText(_translate("Frame", "EDITAR"))
        self.lb_tituloClientes_2.setText(_translate("Frame", "PENDÊNCIAS"))
        self.bt_refresh.setToolTip(_translate("Frame", "ATUALIZAR TABELA"))
        self.bt_busca.setToolTip(_translate("Frame", "BUSCAR"))
