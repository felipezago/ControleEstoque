# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadastro_veiculo.ui'
#
# Created by: PyQt5 View code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from Funcoes.tab_order import cadastro_veiculo


class Ui_ct_FormVeiculos(object):
    def setupUi(self, ct_FormVeiculos):
        ct_FormVeiculos.setObjectName("ct_FormVeiculos")
        ct_FormVeiculos.setWindowModality(QtCore.Qt.WindowModal)
        ct_FormVeiculos.resize(562, 283)
        ct_FormVeiculos.setMaximumSize(QtCore.QSize(662, 432))
        ct_FormVeiculos.setAcceptDrops(False)


        self.fr_Form_Veiculos = QtWidgets.QFrame(ct_FormVeiculos)
        self.fr_Form_Veiculos.setGeometry(QtCore.QRect(0, 0, 661, 321))
        self.fr_Form_Veiculos.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.fr_Form_Veiculos.setStyleSheet("background: #FFF;\n"
"border: none")
        self.fr_Form_Veiculos.setObjectName("fr_Form_Veiculos")
        self.lb_FormProdutos = QtWidgets.QLabel(self.fr_Form_Veiculos)
        self.lb_FormProdutos.setGeometry(QtCore.QRect(170, 10, 780, 30))
        self.lb_FormProdutos.setStyleSheet("QLabel{\n"
"font-size: 14px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"\n"
"border-bottom: 2px solid #A2A2A2\n"
"}")
        self.lb_FormProdutos.setObjectName("lb_FormProdutos")
        self.lb_FormProdutos_2 = QtWidgets.QLabel(self.fr_Form_Veiculos)
        self.lb_FormProdutos_2.setGeometry(QtCore.QRect(170, 50, 150, 20))
        self.lb_FormProdutos_2.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_2.setObjectName("lb_FormProdutos_2")
        self.tx_placa = QtWidgets.QLineEdit(self.fr_Form_Veiculos)
        self.tx_placa.setGeometry(QtCore.QRect(170, 80, 381, 25))
        self.tx_placa.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_placa.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase;\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_placa.setInputMethodHints(QtCore.Qt.ImhNone)
        self.tx_placa.setPlaceholderText("")
        self.tx_placa.setObjectName("tx_placa")
        self.lb_FormProdutos_8 = QtWidgets.QLabel(self.fr_Form_Veiculos)
        self.lb_FormProdutos_8.setGeometry(QtCore.QRect(10, 170, 960, 30))
        self.lb_FormProdutos_8.setStyleSheet("QLabel{\n"
"font-size: 14px;\n"
"font-family: \"Arial\";\n"
"font-weight: normal;\n"
"\n"
"border-bottom: 2px solid #A2A2A2;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_8.setObjectName("lb_FormProdutos_8")
        self.fr_BotoesFormProdutos = QtWidgets.QFrame(self.fr_Form_Veiculos)
        self.fr_BotoesFormProdutos.setGeometry(QtCore.QRect(-100, 250, 1000, 30))
        self.fr_BotoesFormProdutos.setStyleSheet("background:#E1DFE0;\n"
"border: none;")
        self.fr_BotoesFormProdutos.setObjectName("fr_BotoesFormProdutos")
        self.bt_cancelar = QtWidgets.QPushButton(self.fr_BotoesFormProdutos)
        self.bt_cancelar.setGeometry(QtCore.QRect(540, 0, 120, 30))
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
        self.bt_salvar.setGeometry(QtCore.QRect(410, 0, 120, 30))
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
        self.lb_qtdeMin = QtWidgets.QLabel(self.fr_Form_Veiculos)
        self.lb_qtdeMin.setGeometry(QtCore.QRect(890, 350, 40, 35))
        self.lb_qtdeMin.setText("")
        self.lb_qtdeMin.setObjectName("lb_qtdeMin")
        self.label_2 = QtWidgets.QLabel(self.fr_Form_Veiculos)
        self.label_2.setGeometry(QtCore.QRect(0, 50, 150, 71))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Imagens/truck.png"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.tx_PorcentagemVarejo = QtWidgets.QLineEdit(self.fr_Form_Veiculos)
        self.tx_PorcentagemVarejo.setGeometry(QtCore.QRect(170, 360, 60, 30))
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
        self.lb_FormProdutos_13 = QtWidgets.QLabel(self.fr_Form_Veiculos)
        self.lb_FormProdutos_13.setGeometry(QtCore.QRect(170, 120, 150, 20))
        self.lb_FormProdutos_13.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_13.setObjectName("lb_FormProdutos_13")
        self.tx_modelo = QtWidgets.QLineEdit(self.fr_Form_Veiculos)
        self.tx_modelo.setGeometry(QtCore.QRect(170, 150, 171, 30))
        self.tx_modelo.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_modelo.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 14px \"Arial\" ;\n"
"text-transform: uppercase;\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_modelo.setInputMethodHints(QtCore.Qt.ImhNone)
        self.tx_modelo.setPlaceholderText("")
        self.tx_modelo.setObjectName("tx_modelo")
        self.lb_FormProdutos_14 = QtWidgets.QLabel(self.fr_Form_Veiculos)
        self.lb_FormProdutos_14.setGeometry(QtCore.QRect(380, 120, 150, 20))
        self.lb_FormProdutos_14.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_14.setObjectName("lb_FormProdutos_14")
        self.tx_marca = QtWidgets.QLineEdit(self.fr_Form_Veiculos)
        self.tx_marca.setGeometry(QtCore.QRect(379, 150, 171, 30))
        self.tx_marca.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_marca.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 14px \"Arial\" ;\n"
"text-transform: uppercase;\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_marca.setInputMethodHints(QtCore.Qt.ImhNone)
        self.tx_marca.setPlaceholderText("")
        self.tx_marca.setObjectName("tx_marca")
        self.cb_cliente = QtWidgets.QComboBox(self.fr_Form_Veiculos)
        self.cb_cliente.setGeometry(QtCore.QRect(10, 210, 190, 25))
        self.cb_cliente.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.cb_cliente.setStyleSheet("QComboBox{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
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
        self.cb_cliente.addItem("")
        self.bt_add_cliente = QtWidgets.QPushButton(self.fr_Form_Veiculos)
        self.bt_add_cliente.setGeometry(QtCore.QRect(200, 210, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.bt_add_cliente.setFont(font)
        self.bt_add_cliente.setStyleSheet("QPushButton{\n"
"background: #7AB32E;\n"
"color: #FFF\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #40a286\n"
"}")
        self.bt_add_cliente.setText("")
        self.bt_add_cliente.setObjectName("bt_add_cliente")

        cadastro_veiculo(self, ct_FormVeiculos)

        self.retranslateUi(ct_FormVeiculos)
        QtCore.QMetaObject.connectSlotsByName(ct_FormVeiculos)

    def retranslateUi(self, ct_FormVeiculos):
        _translate = QtCore.QCoreApplication.translate
        ct_FormVeiculos.setWindowTitle(_translate("ct_FormVeiculos", "Cadastro de Veiculos"))
        self.fr_Form_Veiculos.setAccessibleName(_translate("ct_FormVeiculos", "Cadastro de Veiculos"))
        self.lb_FormProdutos.setText(_translate("ct_FormVeiculos", "CADASTRAR VEICULO"))
        self.lb_FormProdutos_2.setText(_translate("ct_FormVeiculos", "PLACA"))
        self.lb_FormProdutos_8.setText(_translate("ct_FormVeiculos", "CLIENTE"))
        self.bt_cancelar.setText(_translate("ct_FormVeiculos", "CANCELAR"))
        self.bt_salvar.setText(_translate("ct_FormVeiculos", "SALVAR"))
        self.lb_FormProdutos_13.setText(_translate("ct_FormVeiculos", "MODELO"))
        self.lb_FormProdutos_14.setText(_translate("ct_FormVeiculos", "MARCA"))
        self.cb_cliente.setItemText(0, _translate("ct_FormVeiculos", "SELECIONE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ct_FormVeiculos = QtWidgets.QFrame()
    ui = Ui_ct_FormVeiculos()
    ui.setupUi(ct_FormVeiculos)
    ct_FormVeiculos.show()
    sys.exit(app.exec_())
