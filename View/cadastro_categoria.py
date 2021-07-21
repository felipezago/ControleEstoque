# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadastro_categoria.ui'
#
# Created by: PyQt5 View code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Funcoes.tab_order import cadastro_categoria


class Ui_ct_FormCategoria(object):
    def setupUi(self, ct_FormProdutos):
        ct_FormProdutos.setObjectName("ct_FormProdutos")
        ct_FormProdutos.resize(285, 161)
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
        self.tx_desc_cat = QtWidgets.QLineEdit(self.fr_FormProdutos)
        self.tx_desc_cat.setGeometry(QtCore.QRect(10, 70, 271, 25))
        self.tx_desc_cat.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_desc_cat.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_desc_cat.setPlaceholderText("")
        self.tx_desc_cat.setObjectName("tx_desc_cat")
        self.fr_BotoesFormProdutos = QtWidgets.QFrame(self.fr_FormProdutos)
        self.fr_BotoesFormProdutos.setGeometry(QtCore.QRect(-380, 130, 671, 30))
        self.fr_BotoesFormProdutos.setStyleSheet("background:#E1DFE0;\n"
"border: none;")
        self.fr_BotoesFormProdutos.setObjectName("fr_BotoesFormProdutos")
        self.bt_CancelarProdutos = QtWidgets.QPushButton(self.fr_BotoesFormProdutos)
        self.bt_CancelarProdutos.setGeometry(QtCore.QRect(540, 0, 120, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bt_CancelarProdutos.setFont(font)
        self.bt_CancelarProdutos.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_CancelarProdutos.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_CancelarProdutos.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.bt_CancelarProdutos.setStyleSheet("QPushButton {\n"
"background-color: #1E87F0;\n"
"color: #FFF\n"
" }\n"
"QPushButton:hover{\n"
"background-color: #40a286\n"
"}")
        self.bt_CancelarProdutos.setIconSize(QtCore.QSize(75, 35))
        self.bt_CancelarProdutos.setObjectName("bt_CancelarProdutos")
        self.bt_SalvarProdutos = QtWidgets.QPushButton(self.fr_BotoesFormProdutos)
        self.bt_SalvarProdutos.setGeometry(QtCore.QRect(410, 0, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bt_SalvarProdutos.setFont(font)
        self.bt_SalvarProdutos.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_SalvarProdutos.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_SalvarProdutos.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.bt_SalvarProdutos.setStyleSheet("QPushButton {\n"
"background-color: #7AB32E;\n"
"color: #FFF\n"
" }\n"
"QPushButton:hover{\n"
"background-color: #40a286\n"
"}")
        self.bt_SalvarProdutos.setIconSize(QtCore.QSize(75, 35))
        self.bt_SalvarProdutos.setObjectName("bt_SalvarProdutos")
        self.lb_qtdeMin = QtWidgets.QLabel(self.fr_FormProdutos)
        self.lb_qtdeMin.setGeometry(QtCore.QRect(890, 350, 40, 35))
        self.lb_qtdeMin.setText("")
        self.lb_qtdeMin.setObjectName("lb_qtdeMin")
        self.tx_PorcentagemVarejo = QtWidgets.QLineEdit(self.fr_FormProdutos)
        self.tx_PorcentagemVarejo.setGeometry(QtCore.QRect(185, 360, 60, 30))
        self.tx_PorcentagemVarejo.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_PorcentagemVarejo.setStyleSheet("QLineEdit{\n"
"background: #FFF;\n"
"border-radius: 2px;\n"
"color: #7AB32E;\n"
"font: 20px \"Arial\" ;\n"
"font-weight: bold\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_PorcentagemVarejo.setText("")
        self.tx_PorcentagemVarejo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tx_PorcentagemVarejo.setReadOnly(True)
        self.tx_PorcentagemVarejo.setObjectName("tx_PorcentagemVarejo")

        self.retranslateUi(ct_FormProdutos)
        QtCore.QMetaObject.connectSlotsByName(ct_FormProdutos)

        cadastro_categoria(self, ct_FormProdutos)

    def retranslateUi(self, ct_FormProdutos):
        _translate = QtCore.QCoreApplication.translate
        ct_FormProdutos.setWindowTitle(_translate("ct_FormProdutos", "Cadastro de Categorias"))
        self.lb_FormProdutos.setText(_translate("ct_FormProdutos", "CADASTRAR CATEGORIA"))
        self.lb_FormProdutos_6.setText(_translate("ct_FormProdutos", "DESCRIÇÃO CATEGORIA"))
        self.bt_CancelarProdutos.setText(_translate("ct_FormProdutos", "CANCELAR"))
        self.bt_SalvarProdutos.setText(_translate("ct_FormProdutos", "SALVAR"))
