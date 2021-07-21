# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadastro_finalizadoras.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ct_FormProdutos(object):
    def setupUi(self, ct_FormProdutos):
        ct_FormProdutos.setObjectName("ct_FormProdutos")
        ct_FormProdutos.resize(285, 160)
        self.fr_FormProdutos = QtWidgets.QFrame(ct_FormProdutos)
        self.fr_FormProdutos.setGeometry(QtCore.QRect(0, 0, 841, 431))
        self.fr_FormProdutos.setStyleSheet("background: #FFF;\n"
"border: none")
        self.fr_FormProdutos.setObjectName("fr_FormProdutos")
        self.lb_FormProdutos = QtWidgets.QLabel(self.fr_FormProdutos)
        self.lb_FormProdutos.setGeometry(QtCore.QRect(0, 10, 780, 30))
        self.lb_FormProdutos.setStyleSheet("QLabel{\n"
"font-size: 14px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"\n"
"border-bottom: 2px solid #A2A2A2\n"
"}")
        self.lb_FormProdutos.setObjectName("lb_FormProdutos")
        self.lb_FormProdutos_6 = QtWidgets.QLabel(self.fr_FormProdutos)
        self.lb_FormProdutos_6.setGeometry(QtCore.QRect(10, 50, 215, 20))
        self.lb_FormProdutos_6.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_6.setObjectName("lb_FormProdutos_6")
        self.tx_desc = QtWidgets.QLineEdit(self.fr_FormProdutos)
        self.tx_desc.setGeometry(QtCore.QRect(10, 70, 271, 25))
        self.tx_desc.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_desc.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_desc.setPlaceholderText("")
        self.tx_desc.setObjectName("tx_desc")
        self.fr_BotoesFormProdutos = QtWidgets.QFrame(self.fr_FormProdutos)
        self.fr_BotoesFormProdutos.setGeometry(QtCore.QRect(-380, 130, 671, 30))
        self.fr_BotoesFormProdutos.setStyleSheet("background:#E1DFE0;\n"
"border: none;")
        self.fr_BotoesFormProdutos.setObjectName("fr_BotoesFormProdutos")
        self.bt_cancelar = QtWidgets.QPushButton(self.fr_BotoesFormProdutos)
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
        self.bt_salvar = QtWidgets.QPushButton(self.fr_BotoesFormProdutos)
        self.bt_salvar.setGeometry(QtCore.QRect(420, 0, 120, 30))
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
"background-color: #7AB32E;\n"
"color: #FFF\n"
" }\n"
"QPushButton:hover{\n"
"background-color: #40a286\n"
"}")
        self.bt_salvar.setIconSize(QtCore.QSize(75, 35))
        self.bt_salvar.setObjectName("bt_salvar")
        self.lb_qtdeMin = QtWidgets.QLabel(self.fr_FormProdutos)
        self.lb_qtdeMin.setGeometry(QtCore.QRect(890, 350, 40, 35))
        self.lb_qtdeMin.setText("")
        self.lb_qtdeMin.setObjectName("lb_qtdeMin")

        self.retranslateUi(ct_FormProdutos)
        QtCore.QMetaObject.connectSlotsByName(ct_FormProdutos)

    def retranslateUi(self, ct_FormProdutos):
        _translate = QtCore.QCoreApplication.translate
        ct_FormProdutos.setWindowTitle(_translate("ct_FormProdutos", "Cadastro de Finalizadoras"))
        self.lb_FormProdutos.setText(_translate("ct_FormProdutos", "FORMAS DE PAGAMENTO"))
        self.lb_FormProdutos_6.setText(_translate("ct_FormProdutos", "DESCRIÇÃO"))
        self.bt_cancelar.setText(_translate("ct_FormProdutos", "CANCELAR"))
        self.bt_salvar.setText(_translate("ct_FormProdutos", "SALVAR"))
