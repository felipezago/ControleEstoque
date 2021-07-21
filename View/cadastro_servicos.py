# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadastro_servicos.ui'
#
# Created by: PyQt5 View code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ct_FormServicos(object):
    def setupUi(self, ct_FormServicos):
        ct_FormServicos.setObjectName("ct_FormServicos")
        ct_FormServicos.setWindowModality(QtCore.Qt.WindowModal)
        ct_FormServicos.resize(562, 261)
        ct_FormServicos.setMaximumSize(QtCore.QSize(662, 432))
        self.fr_Form_Servicos = QtWidgets.QFrame(ct_FormServicos)
        self.fr_Form_Servicos.setGeometry(QtCore.QRect(0, 0, 661, 271))
        self.fr_Form_Servicos.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.fr_Form_Servicos.setStyleSheet("background: #FFF;\n"
"border: none")
        self.fr_Form_Servicos.setObjectName("fr_Form_Servicos")
        self.lb_FormProdutos = QtWidgets.QLabel(self.fr_Form_Servicos)
        self.lb_FormProdutos.setGeometry(QtCore.QRect(170, 10, 780, 30))
        self.lb_FormProdutos.setStyleSheet("QLabel{\n"
"font-size: 14px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"\n"
"border-bottom: 2px solid #A2A2A2\n"
"}")
        self.lb_FormProdutos.setObjectName("lb_FormProdutos")
        self.lb_FormProdutos_2 = QtWidgets.QLabel(self.fr_Form_Servicos)
        self.lb_FormProdutos_2.setGeometry(QtCore.QRect(170, 50, 150, 20))
        self.lb_FormProdutos_2.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_2.setObjectName("lb_FormProdutos_2")
        self.tx_DescricaoServico = QtWidgets.QLineEdit(self.fr_Form_Servicos)
        self.tx_DescricaoServico.setGeometry(QtCore.QRect(170, 80, 381, 25))
        self.tx_DescricaoServico.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_DescricaoServico.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase;\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_DescricaoServico.setObjectName("tx_DescricaoServico")
        self.lb_FormProdutos_8 = QtWidgets.QLabel(self.fr_Form_Servicos)
        self.lb_FormProdutos_8.setGeometry(QtCore.QRect(20, 120, 960, 30))
        self.lb_FormProdutos_8.setStyleSheet("QLabel{\n"
"font-size: 14px;\n"
"font-family: \"Arial\";\n"
"font-weight: normal;\n"
"\n"
"border-bottom: 2px solid #A2A2A2;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_8.setObjectName("lb_FormProdutos_8")
        self.lb_FormProdutos_12 = QtWidgets.QLabel(self.fr_Form_Servicos)
        self.lb_FormProdutos_12.setGeometry(QtCore.QRect(20, 160, 150, 20))
        self.lb_FormProdutos_12.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_12.setObjectName("lb_FormProdutos_12")
        self.fr_BotoesFormProdutos = QtWidgets.QFrame(self.fr_Form_Servicos)
        self.fr_BotoesFormProdutos.setGeometry(QtCore.QRect(-100, 230, 1000, 30))
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
        self.lb_qtdeMin = QtWidgets.QLabel(self.fr_Form_Servicos)
        self.lb_qtdeMin.setGeometry(QtCore.QRect(890, 350, 40, 35))
        self.lb_qtdeMin.setText("")
        self.lb_qtdeMin.setObjectName("lb_qtdeMin")
        self.label_2 = QtWidgets.QLabel(self.fr_Form_Servicos)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 150, 71))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Imagens/servico.png"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.tx_ValorUnitarioProduto = QtWidgets.QLineEdit(self.fr_Form_Servicos)
        self.tx_ValorUnitarioProduto.setGeometry(QtCore.QRect(20, 190, 150, 30))
        self.tx_ValorUnitarioProduto.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_ValorUnitarioProduto.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 14px \"Arial\" ;\n"
"text-transform: uppercase;\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_ValorUnitarioProduto.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.tx_ValorUnitarioProduto.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tx_ValorUnitarioProduto.setObjectName("tx_ValorUnitarioProduto")
        self.tx_PorcentagemVarejo = QtWidgets.QLineEdit(self.fr_Form_Servicos)
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

        self.retranslateUi(ct_FormServicos)
        QtCore.QMetaObject.connectSlotsByName(ct_FormServicos)

    def retranslateUi(self, ct_FormServicos):
        _translate = QtCore.QCoreApplication.translate
        ct_FormServicos.setWindowTitle(_translate("ct_FormServicos", "Cadastro de Serviços"))
        self.fr_Form_Servicos.setAccessibleName(_translate("ct_FormServicos", "Cadastro de Serviços"))
        self.lb_FormProdutos.setText(_translate("ct_FormServicos", "CADASTRAR SERVIÇO"))
        self.lb_FormProdutos_2.setText(_translate("ct_FormServicos", "DESCRIÇÃO"))
        self.tx_DescricaoServico.setPlaceholderText(_translate("ct_FormServicos", "Descrição Serviço"))
        self.lb_FormProdutos_8.setText(_translate("ct_FormServicos", "PREÇOS"))
        self.lb_FormProdutos_12.setText(_translate("ct_FormServicos", "VALOR DO SERVIÇO"))
        self.bt_cancelar.setText(_translate("ct_FormServicos", "CANCELAR"))
        self.bt_salvar.setText(_translate("ct_FormServicos", "SALVAR"))
        self.tx_ValorUnitarioProduto.setPlaceholderText(_translate("ct_FormServicos", "R$ 0.00"))
