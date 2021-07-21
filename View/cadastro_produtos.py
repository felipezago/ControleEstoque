# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadastro_produtos.ui'
#
# Created by: PyQt5 View code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Funcoes.tab_order import cadastro_produtos

class Ui_ct_FormProdutos(object):
    def setupUi(self, ct_FormProdutos):
        ct_FormProdutos.setObjectName("ct_FormProdutos")
        ct_FormProdutos.resize(653, 432)
        ct_FormProdutos.setMaximumSize(QtCore.QSize(662, 432))
        self.fr_FormProdutos = QtWidgets.QFrame(ct_FormProdutos)
        self.fr_FormProdutos.setGeometry(QtCore.QRect(0, 0, 661, 431))
        self.fr_FormProdutos.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.fr_FormProdutos.setStyleSheet("background: #FFF;\n"
"border: none")
        self.fr_FormProdutos.setObjectName("fr_FormProdutos")
        self.lb_FormProdutos = QtWidgets.QLabel(self.fr_FormProdutos)
        self.lb_FormProdutos.setGeometry(QtCore.QRect(200, 10, 780, 30))
        self.lb_FormProdutos.setStyleSheet("QLabel{\n"
"font-size: 14px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"\n"
"border-bottom: 2px solid #A2A2A2\n"
"}")
        self.lb_FormProdutos.setObjectName("lb_FormProdutos")
        self.tx_idProduto = QtWidgets.QLineEdit(self.fr_FormProdutos)
        self.tx_idProduto.setEnabled(False)
        self.tx_idProduto.setGeometry(QtCore.QRect(20, 85, 150, 25))
        self.tx_idProduto.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border: 1px solid #A2A2A2;\n"
"color: #000;\n"
"font-size: 14px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"\n"
"}")
        self.tx_idProduto.setText("")
        self.tx_idProduto.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tx_idProduto.setObjectName("tx_idProduto")
        self.lb_FotoProduto = QtWidgets.QLabel(self.fr_FormProdutos)
        self.lb_FotoProduto.setGeometry(QtCore.QRect(20, 110, 150, 150))
        self.lb_FotoProduto.setStyleSheet("border: 1px solid #A2A2A2;\n")
        self.lb_FotoProduto.setText("")
        self.lb_FotoProduto.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_FotoProduto.setObjectName("lb_FotoProduto")
        self.lb_FormProdutos_2 = QtWidgets.QLabel(self.fr_FormProdutos)
        self.lb_FormProdutos_2.setGeometry(QtCore.QRect(200, 60, 150, 20))
        self.lb_FormProdutos_2.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_2.setObjectName("lb_FormProdutos_2")
        self.tx_DescricaoProduto = QtWidgets.QLineEdit(self.fr_FormProdutos)
        self.tx_DescricaoProduto.setGeometry(QtCore.QRect(200, 85, 450, 25))
        self.tx_DescricaoProduto.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_DescricaoProduto.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase;\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_DescricaoProduto.setObjectName("tx_DescricaoProduto")
        self.lb_FormProdutos_3 = QtWidgets.QLabel(self.fr_FormProdutos)
        self.lb_FormProdutos_3.setGeometry(QtCore.QRect(200, 185, 215, 20))
        self.lb_FormProdutos_3.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_3.setObjectName("lb_FormProdutos_3")
        self.lb_FormProdutos_4 = QtWidgets.QLabel(self.fr_FormProdutos)
        self.lb_FormProdutos_4.setGeometry(QtCore.QRect(435, 185, 215, 20))
        self.lb_FormProdutos_4.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_4.setObjectName("lb_FormProdutos_4")
        self.lb_FormProdutos_8 = QtWidgets.QLabel(self.fr_FormProdutos)
        self.lb_FormProdutos_8.setGeometry(QtCore.QRect(20, 290, 960, 30))
        self.lb_FormProdutos_8.setStyleSheet("QLabel{\n"
"font-size: 14px;\n"
"font-family: \"Arial\";\n"
"font-weight: normal;\n"
"\n"
"border-bottom: 2px solid #A2A2A2;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_8.setObjectName("lb_FormProdutos_8")
        self.lb_FormProdutos_12 = QtWidgets.QLabel(self.fr_FormProdutos)
        self.lb_FormProdutos_12.setGeometry(QtCore.QRect(20, 330, 150, 20))
        self.lb_FormProdutos_12.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_12.setObjectName("lb_FormProdutos_12")
        self.fr_BotoesFormProdutos = QtWidgets.QFrame(self.fr_FormProdutos)
        self.fr_BotoesFormProdutos.setGeometry(QtCore.QRect(0, 400, 1000, 30))
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
        self.lb_FormProdutos_15 = QtWidgets.QLabel(self.fr_FormProdutos)
        self.lb_FormProdutos_15.setGeometry(QtCore.QRect(270, 360, 150, 20))
        self.lb_FormProdutos_15.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #000\n"
"}")
        self.lb_FormProdutos_15.setObjectName("lb_FormProdutos_15")
        self.lb_FormProdutos_17 = QtWidgets.QLabel(self.fr_FormProdutos)
        self.lb_FormProdutos_17.setGeometry(QtCore.QRect(270, 380, 150, 10))
        self.lb_FormProdutos_17.setStyleSheet("QLabel{\n"
"font-size: 8px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: normal;\n"
"color: #000\n"
"}")
        self.lb_FormProdutos_17.setObjectName("lb_FormProdutos_17")
        self.lb_porcVar = QtWidgets.QLabel(self.fr_FormProdutos)
        self.lb_porcVar.setGeometry(QtCore.QRect(245, 360, 20, 30))
        self.lb_porcVar.setStyleSheet("QLabel{\n"
"font-size: 20px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #7AB32E\n"
"}")
        self.lb_porcVar.setObjectName("lb_porcVar")
        self.label_2 = QtWidgets.QLabel(self.fr_FormProdutos)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 150, 50))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Imagens/CodBarra.png"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.bt_AddImagem = QtWidgets.QPushButton(self.fr_FormProdutos)
        self.bt_AddImagem.setGeometry(QtCore.QRect(140, 230, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.bt_AddImagem.setFont(font)
        self.bt_AddImagem.setStyleSheet("QPushButton{\n"
"background: #7AB32E;\n"
"color: #FFF\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #40a286\n"
"}")
        self.bt_AddImagem.setText("")
        self.bt_AddImagem.setObjectName("bt_AddImagem")
        self.bt_DelImagem = QtWidgets.QPushButton(self.fr_FormProdutos)
        self.bt_DelImagem.setGeometry(QtCore.QRect(140, 230, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.bt_DelImagem.setFont(font)
        self.bt_DelImagem.setStyleSheet("QPushButton{\n"
"background: #7AB32E;\n"
"color: #FFF\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #40a286\n"
"}")
        self.bt_DelImagem.setText("")
        self.bt_DelImagem.setObjectName("bt_DelImagem")
        self.tx_codbarras = QtWidgets.QLineEdit(self.fr_FormProdutos)
        self.tx_codbarras.setGeometry(QtCore.QRect(200, 150, 215, 25))
        self.tx_codbarras.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_codbarras.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_codbarras.setText("")
        self.tx_codbarras.setPlaceholderText("")
        self.tx_codbarras.setObjectName("tx_codbarras")
        self.lb_FormProdutos_7 = QtWidgets.QLabel(self.fr_FormProdutos)
        self.lb_FormProdutos_7.setGeometry(QtCore.QRect(200, 120, 215, 20))
        self.lb_FormProdutos_7.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_7.setObjectName("lb_FormProdutos_7")
        self.lb_FormProdutos_9 = QtWidgets.QLabel(self.fr_FormProdutos)
        self.lb_FormProdutos_9.setGeometry(QtCore.QRect(430, 120, 215, 20))
        self.lb_FormProdutos_9.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_9.setObjectName("lb_FormProdutos_9")
        self.cb_forn = QtWidgets.QComboBox(self.fr_FormProdutos)
        self.cb_forn.setGeometry(QtCore.QRect(430, 150, 190, 25))
        self.cb_forn.setStyleSheet("QComboBox{\n"
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
        self.cb_forn.setObjectName("cb_forn")
        self.cb_forn.addItem("")
        self.bt_addForn = QtWidgets.QPushButton(self.fr_FormProdutos)
        self.bt_addForn.setGeometry(QtCore.QRect(620, 150, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.bt_addForn.setFont(font)
        self.bt_addForn.setStyleSheet("QPushButton{\n"
"background: #7AB32E;\n"
"color: #FFF\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #40a286\n"
"}")
        self.bt_addForn.setText("")
        self.bt_addForn.setObjectName("bt_addForn")
        self.tx_marca = QtWidgets.QLineEdit(self.fr_FormProdutos)
        self.tx_marca.setGeometry(QtCore.QRect(430, 210, 215, 25))
        self.tx_marca.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_marca.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_marca.setPlaceholderText("")
        self.tx_marca.setObjectName("tx_marca")
        self.bt_AddCategoriaProduto = QtWidgets.QPushButton(self.fr_FormProdutos)
        self.bt_AddCategoriaProduto.setGeometry(QtCore.QRect(390, 210, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.bt_AddCategoriaProduto.setFont(font)
        self.bt_AddCategoriaProduto.setStyleSheet("QPushButton{\n"
"background: #7AB32E;\n"
"color: #FFF\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #40a286\n"
"}")
        self.bt_AddCategoriaProduto.setText("")
        self.bt_AddCategoriaProduto.setObjectName("bt_AddCategoriaProduto")
        self.cb_CategoriaProduto = QtWidgets.QComboBox(self.fr_FormProdutos)
        self.cb_CategoriaProduto.setGeometry(QtCore.QRect(200, 210, 190, 25))
        self.cb_CategoriaProduto.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.cb_CategoriaProduto.setStyleSheet("QComboBox{\n"
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
        self.cb_CategoriaProduto.setObjectName("cb_CategoriaProduto")
        self.cb_CategoriaProduto.addItem("")
        self.lb_FormProdutos_6 = QtWidgets.QLabel(self.fr_FormProdutos)
        self.lb_FormProdutos_6.setGeometry(QtCore.QRect(200, 250, 215, 20))
        self.lb_FormProdutos_6.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_6.setObjectName("lb_FormProdutos_6")
        self.tx_EstoqueMaximoProduto = QtWidgets.QLineEdit(self.fr_FormProdutos)
        self.tx_EstoqueMaximoProduto.setGeometry(QtCore.QRect(200, 270, 215, 25))
        self.tx_EstoqueMaximoProduto.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_EstoqueMaximoProduto.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_EstoqueMaximoProduto.setPlaceholderText("")
        self.tx_EstoqueMaximoProduto.setObjectName("tx_EstoqueMaximoProduto")
        self.tx_ValorUnitarioProduto = QtWidgets.QLineEdit(self.fr_FormProdutos)
        self.tx_ValorUnitarioProduto.setGeometry(QtCore.QRect(20, 360, 150, 30))
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
        self.tx_PorcentagemVarejo = QtWidgets.QLineEdit(self.fr_FormProdutos)
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
        self.lb_FormProdutos.raise_()
        self.tx_idProduto.raise_()
        self.lb_FotoProduto.raise_()
        self.lb_FormProdutos_2.raise_()
        self.tx_DescricaoProduto.raise_()
        self.lb_FormProdutos_3.raise_()
        self.lb_FormProdutos_4.raise_()
        self.lb_FormProdutos_8.raise_()
        self.lb_FormProdutos_12.raise_()
        self.fr_BotoesFormProdutos.raise_()
        self.lb_qtdeMin.raise_()
        self.lb_FormProdutos_15.raise_()
        self.lb_FormProdutos_17.raise_()
        self.lb_porcVar.raise_()
        self.label_2.raise_()
        self.bt_DelImagem.raise_()
        self.bt_AddImagem.raise_()
        self.tx_codbarras.raise_()
        self.lb_FormProdutos_7.raise_()
        self.lb_FormProdutos_9.raise_()
        self.cb_forn.raise_()
        self.bt_addForn.raise_()
        self.tx_marca.raise_()
        self.bt_AddCategoriaProduto.raise_()
        self.cb_CategoriaProduto.raise_()
        self.lb_FormProdutos_6.raise_()
        self.tx_EstoqueMaximoProduto.raise_()
        self.tx_ValorUnitarioProduto.raise_()
        self.tx_PorcentagemVarejo.raise_()

        cadastro_produtos(self, ct_FormProdutos)

        self.retranslateUi(ct_FormProdutos)
        QtCore.QMetaObject.connectSlotsByName(ct_FormProdutos)

    def retranslateUi(self, ct_FormProdutos):
        _translate = QtCore.QCoreApplication.translate
        ct_FormProdutos.setWindowTitle(_translate("ct_FormProdutos", "Cadastro de Produtos"))
        self.lb_FormProdutos.setText(_translate("ct_FormProdutos", "CADASTRAR PRODUTO"))
        self.lb_FormProdutos_2.setText(_translate("ct_FormProdutos", "DESCRIÇÃO"))
        self.tx_DescricaoProduto.setPlaceholderText(_translate("ct_FormProdutos", "Descrição Produto"))
        self.lb_FormProdutos_3.setText(_translate("ct_FormProdutos", "CATEGORIA"))
        self.lb_FormProdutos_4.setText(_translate("ct_FormProdutos", "MARCA"))
        self.lb_FormProdutos_8.setText(_translate("ct_FormProdutos", "PREÇOS"))
        self.lb_FormProdutos_12.setText(_translate("ct_FormProdutos", "PREÇO DE VENDA"))
        self.bt_CancelarProdutos.setText(_translate("ct_FormProdutos", "CANCELAR"))
        self.bt_SalvarProdutos.setText(_translate("ct_FormProdutos", "SALVAR"))
        self.lb_FormProdutos_15.setText(_translate("ct_FormProdutos", "MARGEM LUCRO"))
        self.lb_FormProdutos_17.setText(_translate("ct_FormProdutos", "(APROXIMADA NO VAREJO)"))
        self.lb_porcVar.setText(_translate("ct_FormProdutos", "%"))
        self.bt_AddImagem.setToolTip(_translate("ct_FormProdutos", "<html><head/><body><p>CADASTRAR IMGEM</p></body></html>"))
        self.bt_DelImagem.setToolTip(_translate("ct_FormProdutos", "<html><head/><body><p>Deletar Imagem</p></body></html>"))
        self.lb_FormProdutos_7.setText(_translate("ct_FormProdutos", "CODIGO DE BARRAS"))
        self.lb_FormProdutos_9.setText(_translate("ct_FormProdutos", "FORNECEDOR"))
        self.cb_forn.setItemText(0, _translate("ct_FormProdutos", "SELECIONE"))
        self.cb_CategoriaProduto.setItemText(0, _translate("ct_FormProdutos", "SELECIONE"))
        self.lb_FormProdutos_6.setText(_translate("ct_FormProdutos", "ESTOQUE"))
        self.tx_ValorUnitarioProduto.setPlaceholderText(_translate("ct_FormProdutos", "R$ 0.00"))
