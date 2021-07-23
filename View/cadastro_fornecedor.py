# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'View/UI/cadastro_fornecedor.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ct_FormFornecedor(object):
    def setupUi(self, ct_FormFornecedor):
        ct_FormFornecedor.setObjectName("ct_FormFornecedor")
        ct_FormFornecedor.resize(653, 371)
        self.fr_FormFornecedor = QtWidgets.QFrame(ct_FormFornecedor)
        self.fr_FormFornecedor.setGeometry(QtCore.QRect(0, 0, 1000, 500))
        self.fr_FormFornecedor.setStyleSheet("background: #FFF;\n"
"border: none")
        self.fr_FormFornecedor.setObjectName("fr_FormFornecedor")
        self.lb_FormFornecedor = QtWidgets.QLabel(self.fr_FormFornecedor)
        self.lb_FormFornecedor.setGeometry(QtCore.QRect(100, 10, 880, 30))
        self.lb_FormFornecedor.setStyleSheet("QLabel{\n"
"font-size: 14px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"\n"
"border-bottom: 2px solid #A2A2A2\n"
"}")
        self.lb_FormFornecedor.setObjectName("lb_FormFornecedor")
        self.tx_Id = QtWidgets.QLineEdit(self.fr_FormFornecedor)
        self.tx_Id.setEnabled(False)
        self.tx_Id.setGeometry(QtCore.QRect(20, 10, 50, 30))
        self.tx_Id.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border: 1px solid #A2A2A2;\n"
"color: #000;\n"
"font-size: 14px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"\n"
"}")
        self.tx_Id.setText("")
        self.tx_Id.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_Id.setObjectName("tx_Id")
        self.lb_FormFornecedor_2 = QtWidgets.QLabel(self.fr_FormFornecedor)
        self.lb_FormFornecedor_2.setGeometry(QtCore.QRect(20, 60, 150, 20))
        self.lb_FormFornecedor_2.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_2.setObjectName("lb_FormFornecedor_2")
        self.tx_NomeFantasia = QtWidgets.QLineEdit(self.fr_FormFornecedor)
        self.tx_NomeFantasia.setGeometry(QtCore.QRect(20, 85, 401, 25))
        self.tx_NomeFantasia.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_NomeFantasia.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase;\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_NomeFantasia.setObjectName("tx_NomeFantasia")
        self.lb_FormFornecedor_3 = QtWidgets.QLabel(self.fr_FormFornecedor)
        self.lb_FormFornecedor_3.setGeometry(QtCore.QRect(430, 60, 190, 20))
        self.lb_FormFornecedor_3.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_3.setObjectName("lb_FormFornecedor_3")
        self.lb_FormFornecedor_5 = QtWidgets.QLabel(self.fr_FormFornecedor)
        self.lb_FormFornecedor_5.setGeometry(QtCore.QRect(20, 120, 196, 20))
        self.lb_FormFornecedor_5.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_5.setObjectName("lb_FormFornecedor_5")
        self.tx_Telefone = QtWidgets.QLineEdit(self.fr_FormFornecedor)
        self.tx_Telefone.setGeometry(QtCore.QRect(20, 140, 196, 25))
        self.tx_Telefone.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_Telefone.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_Telefone.setPlaceholderText("")
        self.tx_Telefone.setObjectName("tx_Telefone")
        self.lb_FormFornecedor_8 = QtWidgets.QLabel(self.fr_FormFornecedor)
        self.lb_FormFornecedor_8.setGeometry(QtCore.QRect(20, 180, 630, 30))
        self.lb_FormFornecedor_8.setStyleSheet("QLabel{\n"
"font-size: 14px;\n"
"font-family: \"Arial\";\n"
"font-weight: normal;\n"
"\n"
"border-bottom: 2px solid #A2A2A2;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_8.setObjectName("lb_FormFornecedor_8")
        self.tx_Cep = QtWidgets.QLineEdit(self.fr_FormFornecedor)
        self.tx_Cep.setGeometry(QtCore.QRect(20, 240, 101, 25))
        self.tx_Cep.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_Cep.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_Cep.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_Cep.setObjectName("tx_Cep")
        self.lb_FormFornecedor_10 = QtWidgets.QLabel(self.fr_FormFornecedor)
        self.lb_FormFornecedor_10.setGeometry(QtCore.QRect(20, 215, 50, 20))
        self.lb_FormFornecedor_10.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_10.setObjectName("lb_FormFornecedor_10")
        self.fr_BotoesFormFornecedor = QtWidgets.QFrame(self.fr_FormFornecedor)
        self.fr_BotoesFormFornecedor.setGeometry(QtCore.QRect(-340, 340, 1000, 30))
        self.fr_BotoesFormFornecedor.setStyleSheet("background:#E1DFE0;\n"
"border: none;")
        self.fr_BotoesFormFornecedor.setObjectName("fr_BotoesFormFornecedor")
        self.bt_Voltar = QtWidgets.QPushButton(self.fr_BotoesFormFornecedor)
        self.bt_Voltar.setGeometry(QtCore.QRect(880, 0, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bt_Voltar.setFont(font)
        self.bt_Voltar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_Voltar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_Voltar.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.bt_Voltar.setStyleSheet("QPushButton {\n"
"background-color: #1E87F0;\n"
"color: #FFF\n"
" }\n"
"QPushButton:hover{\n"
"background-color: #40a286\n"
"}")
        self.bt_Voltar.setIconSize(QtCore.QSize(75, 35))
        self.bt_Voltar.setObjectName("bt_Voltar")
        self.bt_Salvar = QtWidgets.QPushButton(self.fr_BotoesFormFornecedor)
        self.bt_Salvar.setGeometry(QtCore.QRect(750, 0, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bt_Salvar.setFont(font)
        self.bt_Salvar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_Salvar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_Salvar.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.bt_Salvar.setStyleSheet("QPushButton {\n"
"background-color: #7AB32E;\n"
"color: #FFF\n"
" }\n"
"QPushButton:hover{\n"
"background-color: #40a286\n"
"}")
        self.bt_Salvar.setIconSize(QtCore.QSize(75, 35))
        self.bt_Salvar.setObjectName("bt_Salvar")
        self.tx_cnpj = QtWidgets.QLineEdit(self.fr_FormFornecedor)
        self.tx_cnpj.setGeometry(QtCore.QRect(430, 85, 221, 25))
        self.tx_cnpj.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_cnpj.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_cnpj.setPlaceholderText("")
        self.tx_cnpj.setObjectName("tx_cnpj")
        self.lb_FormFornecedor_23 = QtWidgets.QLabel(self.fr_FormFornecedor)
        self.lb_FormFornecedor_23.setGeometry(QtCore.QRect(230, 120, 190, 20))
        self.lb_FormFornecedor_23.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_23.setObjectName("lb_FormFornecedor_23")
        self.tx_Email = QtWidgets.QLineEdit(self.fr_FormFornecedor)
        self.tx_Email.setGeometry(QtCore.QRect(230, 140, 196, 25))
        self.tx_Email.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_Email.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_Email.setPlaceholderText("")
        self.tx_Email.setObjectName("tx_Email")
        self.lb_FormFornecedor_11 = QtWidgets.QLabel(self.fr_FormFornecedor)
        self.lb_FormFornecedor_11.setGeometry(QtCore.QRect(160, 215, 250, 20))
        self.lb_FormFornecedor_11.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_11.setObjectName("lb_FormFornecedor_11")
        self.tx_Endereco = QtWidgets.QLineEdit(self.fr_FormFornecedor)
        self.tx_Endereco.setGeometry(QtCore.QRect(160, 240, 400, 25))
        self.tx_Endereco.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_Endereco.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_Endereco.setInputMask("")
        self.tx_Endereco.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tx_Endereco.setPlaceholderText("")
        self.tx_Endereco.setObjectName("tx_Endereco")
        self.lb_FormFornecedor_12 = QtWidgets.QLabel(self.fr_FormFornecedor)
        self.lb_FormFornecedor_12.setGeometry(QtCore.QRect(580, 215, 50, 20))
        self.lb_FormFornecedor_12.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_12.setObjectName("lb_FormFornecedor_12")
        self.tx_Numero = QtWidgets.QLineEdit(self.fr_FormFornecedor)
        self.tx_Numero.setGeometry(QtCore.QRect(580, 240, 70, 25))
        self.tx_Numero.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_Numero.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_Numero.setInputMask("")
        self.tx_Numero.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tx_Numero.setPlaceholderText("")
        self.tx_Numero.setObjectName("tx_Numero")
        self.tx_Bairro = QtWidgets.QLineEdit(self.fr_FormFornecedor)
        self.tx_Bairro.setGeometry(QtCore.QRect(20, 295, 260, 25))
        self.tx_Bairro.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_Bairro.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_Bairro.setInputMask("")
        self.tx_Bairro.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tx_Bairro.setPlaceholderText("")
        self.tx_Bairro.setObjectName("tx_Bairro")
        self.lb_FormFornecedor_13 = QtWidgets.QLabel(self.fr_FormFornecedor)
        self.lb_FormFornecedor_13.setGeometry(QtCore.QRect(20, 270, 120, 20))
        self.lb_FormFornecedor_13.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_13.setObjectName("lb_FormFornecedor_13")
        self.tx_Cidade = QtWidgets.QLineEdit(self.fr_FormFornecedor)
        self.tx_Cidade.setGeometry(QtCore.QRect(300, 295, 260, 25))
        self.tx_Cidade.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_Cidade.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_Cidade.setInputMask("")
        self.tx_Cidade.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tx_Cidade.setPlaceholderText("")
        self.tx_Cidade.setObjectName("tx_Cidade")
        self.lb_FormFornecedor_14 = QtWidgets.QLabel(self.fr_FormFornecedor)
        self.lb_FormFornecedor_14.setGeometry(QtCore.QRect(300, 270, 120, 20))
        self.lb_FormFornecedor_14.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_14.setObjectName("lb_FormFornecedor_14")
        self.lb_FormFornecedor_15 = QtWidgets.QLabel(self.fr_FormFornecedor)
        self.lb_FormFornecedor_15.setGeometry(QtCore.QRect(580, 270, 70, 20))
        self.lb_FormFornecedor_15.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_15.setObjectName("lb_FormFornecedor_15")
        self.tx_Estado = QtWidgets.QLineEdit(self.fr_FormFornecedor)
        self.tx_Estado.setGeometry(QtCore.QRect(580, 295, 70, 25))
        self.tx_Estado.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_Estado.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_Estado.setInputMask("")
        self.tx_Estado.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tx_Estado.setPlaceholderText("")
        self.tx_Estado.setObjectName("tx_Estado")
        self.bt_busca_cep = QtWidgets.QPushButton(self.fr_FormFornecedor)
        self.bt_busca_cep.setGeometry(QtCore.QRect(130, 240, 21, 31))
        self.bt_busca_cep.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("View/UI/../../Imagens/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_busca_cep.setIcon(icon)
        self.bt_busca_cep.setObjectName("bt_busca_cep")

        self.retranslateUi(ct_FormFornecedor)
        QtCore.QMetaObject.connectSlotsByName(ct_FormFornecedor)
        ct_FormFornecedor.setTabOrder(self.tx_Id, self.tx_NomeFantasia)
        ct_FormFornecedor.setTabOrder(self.tx_NomeFantasia, self.tx_cnpj)
        ct_FormFornecedor.setTabOrder(self.tx_cnpj, self.tx_Telefone)
        ct_FormFornecedor.setTabOrder(self.tx_Telefone, self.tx_Email)
        ct_FormFornecedor.setTabOrder(self.tx_Email, self.tx_Cep)
        ct_FormFornecedor.setTabOrder(self.tx_Cep, self.bt_busca_cep)
        ct_FormFornecedor.setTabOrder(self.bt_busca_cep, self.tx_Endereco)
        ct_FormFornecedor.setTabOrder(self.tx_Endereco, self.tx_Numero)
        ct_FormFornecedor.setTabOrder(self.tx_Numero, self.tx_Bairro)
        ct_FormFornecedor.setTabOrder(self.tx_Bairro, self.tx_Cidade)
        ct_FormFornecedor.setTabOrder(self.tx_Cidade, self.tx_Estado)

    def retranslateUi(self, ct_FormFornecedor):
        _translate = QtCore.QCoreApplication.translate
        ct_FormFornecedor.setWindowTitle(_translate("ct_FormFornecedor", "Cadastro Fornecedores"))
        self.lb_FormFornecedor.setText(_translate("ct_FormFornecedor", "FICHA CADASTRAL FORNECEDOR"))
        self.lb_FormFornecedor_2.setText(_translate("ct_FormFornecedor", "NOME FANTASIA"))
        self.tx_NomeFantasia.setPlaceholderText(_translate("ct_FormFornecedor", "NOME FANTASIA"))
        self.lb_FormFornecedor_3.setText(_translate("ct_FormFornecedor", "CNPJ"))
        self.lb_FormFornecedor_5.setText(_translate("ct_FormFornecedor", "TELEFONE "))
        self.tx_Telefone.setInputMask(_translate("ct_FormFornecedor", "(00) 0000-00000"))
        self.tx_Telefone.setText(_translate("ct_FormFornecedor", "() -"))
        self.lb_FormFornecedor_8.setText(_translate("ct_FormFornecedor", "ENDEREÇO"))
        self.tx_Cep.setInputMask(_translate("ct_FormFornecedor", "99999-999"))
        self.tx_Cep.setPlaceholderText(_translate("ct_FormFornecedor", "123456789"))
        self.lb_FormFornecedor_10.setText(_translate("ct_FormFornecedor", "CEP"))
        self.bt_Voltar.setText(_translate("ct_FormFornecedor", "VOLTAR"))
        self.bt_Salvar.setText(_translate("ct_FormFornecedor", "SALVAR"))
        self.tx_cnpj.setInputMask(_translate("ct_FormFornecedor", "##.###.###/####-##"))
        self.tx_cnpj.setText(_translate("ct_FormFornecedor", "../-----"))
        self.lb_FormFornecedor_23.setText(_translate("ct_FormFornecedor", "Email"))
        self.lb_FormFornecedor_11.setText(_translate("ct_FormFornecedor", "ENDEREÇO"))
        self.lb_FormFornecedor_12.setText(_translate("ct_FormFornecedor", "Nº"))
        self.lb_FormFornecedor_13.setText(_translate("ct_FormFornecedor", "BAIRRO"))
        self.lb_FormFornecedor_14.setText(_translate("ct_FormFornecedor", "CIDADE"))
        self.lb_FormFornecedor_15.setText(_translate("ct_FormFornecedor", "ESTADO"))
        self.bt_busca_cep.setAccessibleName(_translate("ct_FormFornecedor", "BUSCA CEP"))