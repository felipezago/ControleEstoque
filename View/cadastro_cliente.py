# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'View/UI/cadastro_clientes.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ct_FormClientes(object):
    def setupUi(self, ct_FormClientes):
        ct_FormClientes.setObjectName("ct_FormClientes")
        ct_FormClientes.resize(669, 440)
        self.fr_FormClientes = QtWidgets.QFrame(ct_FormClientes)
        self.fr_FormClientes.setGeometry(QtCore.QRect(0, 0, 1000, 500))
        self.fr_FormClientes.setStyleSheet("background: #FFF;\n"
"border: none")
        self.fr_FormClientes.setObjectName("fr_FormClientes")
        self.lb_FormProdutos = QtWidgets.QLabel(self.fr_FormClientes)
        self.lb_FormProdutos.setGeometry(QtCore.QRect(100, 10, 880, 30))
        self.lb_FormProdutos.setStyleSheet("QLabel{\n"
"font-size: 14px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"\n"
"border-bottom: 2px solid #A2A2A2\n"
"}")
        self.lb_FormProdutos.setObjectName("lb_FormProdutos")
        self.tx_Id = QtWidgets.QLineEdit(self.fr_FormClientes)
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
        self.lb_FormProdutos_2 = QtWidgets.QLabel(self.fr_FormClientes)
        self.lb_FormProdutos_2.setGeometry(QtCore.QRect(20, 60, 150, 20))
        self.lb_FormProdutos_2.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_2.setObjectName("lb_FormProdutos_2")
        self.tx_nome = QtWidgets.QLineEdit(self.fr_FormClientes)
        self.tx_nome.setGeometry(QtCore.QRect(20, 85, 641, 25))
        self.tx_nome.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_nome.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase;\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_nome.setObjectName("tx_nome")
        self.lb_FormProdutos_3 = QtWidgets.QLabel(self.fr_FormClientes)
        self.lb_FormProdutos_3.setGeometry(QtCore.QRect(20, 120, 190, 20))
        self.lb_FormProdutos_3.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_3.setObjectName("lb_FormProdutos_3")
        self.lb_FormProdutos_4 = QtWidgets.QLabel(self.fr_FormClientes)
        self.lb_FormProdutos_4.setGeometry(QtCore.QRect(236, 120, 190, 20))
        self.lb_FormProdutos_4.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_4.setObjectName("lb_FormProdutos_4")
        self.lb_FormProdutos_5 = QtWidgets.QLabel(self.fr_FormClientes)
        self.lb_FormProdutos_5.setGeometry(QtCore.QRect(20, 180, 196, 20))
        self.lb_FormProdutos_5.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_5.setObjectName("lb_FormProdutos_5")
        self.tx_Celular = QtWidgets.QLineEdit(self.fr_FormClientes)
        self.tx_Celular.setGeometry(QtCore.QRect(20, 205, 196, 25))
        self.tx_Celular.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_Celular.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_Celular.setPlaceholderText("")
        self.tx_Celular.setObjectName("tx_Celular")
        self.tx_rg = QtWidgets.QLineEdit(self.fr_FormClientes)
        self.tx_rg.setGeometry(QtCore.QRect(236, 145, 196, 25))
        self.tx_rg.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_rg.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_rg.setPlaceholderText("")
        self.tx_rg.setObjectName("tx_rg")
        self.lb_FormProdutos_8 = QtWidgets.QLabel(self.fr_FormClientes)
        self.lb_FormProdutos_8.setGeometry(QtCore.QRect(20, 240, 630, 30))
        self.lb_FormProdutos_8.setStyleSheet("QLabel{\n"
"font-size: 14px;\n"
"font-family: \"Arial\";\n"
"font-weight: normal;\n"
"\n"
"border-bottom: 2px solid #A2A2A2;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_8.setObjectName("lb_FormProdutos_8")
        self.tx_Cep = QtWidgets.QLineEdit(self.fr_FormClientes)
        self.tx_Cep.setGeometry(QtCore.QRect(20, 305, 91, 25))
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
        self.lb_FormProdutos_10 = QtWidgets.QLabel(self.fr_FormClientes)
        self.lb_FormProdutos_10.setGeometry(QtCore.QRect(20, 280, 50, 20))
        self.lb_FormProdutos_10.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_10.setObjectName("lb_FormProdutos_10")
        self.fr_BotoesFormProdutos = QtWidgets.QFrame(self.fr_FormClientes)
        self.fr_BotoesFormProdutos.setGeometry(QtCore.QRect(0, 410, 1000, 30))
        self.fr_BotoesFormProdutos.setStyleSheet("background:#E1DFE0;\n"
"border: none;")
        self.fr_BotoesFormProdutos.setObjectName("fr_BotoesFormProdutos")
        self.bt_Voltar = QtWidgets.QPushButton(self.fr_BotoesFormProdutos)
        self.bt_Voltar.setGeometry(QtCore.QRect(550, 0, 120, 30))
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
        self.bt_Salvar = QtWidgets.QPushButton(self.fr_BotoesFormProdutos)
        self.bt_Salvar.setGeometry(QtCore.QRect(420, 0, 120, 30))
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
        self.tx_cpf = QtWidgets.QLineEdit(self.fr_FormClientes)
        self.tx_cpf.setGeometry(QtCore.QRect(20, 145, 196, 25))
        self.tx_cpf.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_cpf.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" \n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_cpf.setPlaceholderText("")
        self.tx_cpf.setObjectName("tx_cpf")
        self.lb_FormProdutos_23 = QtWidgets.QLabel(self.fr_FormClientes)
        self.lb_FormProdutos_23.setGeometry(QtCore.QRect(452, 180, 190, 20))
        self.lb_FormProdutos_23.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_23.setObjectName("lb_FormProdutos_23")
        self.lb_FormProdutos_24 = QtWidgets.QLabel(self.fr_FormClientes)
        self.lb_FormProdutos_24.setGeometry(QtCore.QRect(236, 180, 190, 20))
        self.lb_FormProdutos_24.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_24.setObjectName("lb_FormProdutos_24")
        self.tx_Email = QtWidgets.QLineEdit(self.fr_FormClientes)
        self.tx_Email.setGeometry(QtCore.QRect(452, 205, 196, 25))
        self.tx_Email.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_Email.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_Email.setPlaceholderText("")
        self.tx_Email.setObjectName("tx_Email")
        self.tx_Telefone = QtWidgets.QLineEdit(self.fr_FormClientes)
        self.tx_Telefone.setGeometry(QtCore.QRect(236, 205, 196, 25))
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
        self.lb_FormProdutos_11 = QtWidgets.QLabel(self.fr_FormClientes)
        self.lb_FormProdutos_11.setGeometry(QtCore.QRect(160, 280, 250, 20))
        self.lb_FormProdutos_11.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_11.setObjectName("lb_FormProdutos_11")
        self.tx_Endereco = QtWidgets.QLineEdit(self.fr_FormClientes)
        self.tx_Endereco.setGeometry(QtCore.QRect(160, 305, 400, 25))
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
        self.lb_FormProdutos_12 = QtWidgets.QLabel(self.fr_FormClientes)
        self.lb_FormProdutos_12.setGeometry(QtCore.QRect(580, 280, 50, 20))
        self.lb_FormProdutos_12.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_12.setObjectName("lb_FormProdutos_12")
        self.tx_Numero = QtWidgets.QLineEdit(self.fr_FormClientes)
        self.tx_Numero.setGeometry(QtCore.QRect(580, 305, 70, 25))
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
        self.tx_Numero.setInputMethodHints(QtCore.Qt.ImhNone)
        self.tx_Numero.setInputMask("")
        self.tx_Numero.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tx_Numero.setPlaceholderText("")
        self.tx_Numero.setObjectName("tx_Numero")
        self.tx_Bairro = QtWidgets.QLineEdit(self.fr_FormClientes)
        self.tx_Bairro.setGeometry(QtCore.QRect(20, 360, 260, 25))
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
        self.lb_FormProdutos_13 = QtWidgets.QLabel(self.fr_FormClientes)
        self.lb_FormProdutos_13.setGeometry(QtCore.QRect(20, 335, 120, 20))
        self.lb_FormProdutos_13.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_13.setObjectName("lb_FormProdutos_13")
        self.tx_Cidade = QtWidgets.QLineEdit(self.fr_FormClientes)
        self.tx_Cidade.setGeometry(QtCore.QRect(300, 360, 260, 25))
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
        self.lb_FormProdutos_14 = QtWidgets.QLabel(self.fr_FormClientes)
        self.lb_FormProdutos_14.setGeometry(QtCore.QRect(300, 335, 120, 20))
        self.lb_FormProdutos_14.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_14.setObjectName("lb_FormProdutos_14")
        self.lb_FormProdutos_15 = QtWidgets.QLabel(self.fr_FormClientes)
        self.lb_FormProdutos_15.setGeometry(QtCore.QRect(580, 335, 70, 20))
        self.lb_FormProdutos_15.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormProdutos_15.setObjectName("lb_FormProdutos_15")
        self.tx_Estado = QtWidgets.QLineEdit(self.fr_FormClientes)
        self.tx_Estado.setGeometry(QtCore.QRect(580, 360, 70, 25))
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
        self.bt_busca_cep = QtWidgets.QPushButton(self.fr_FormClientes)
        self.bt_busca_cep.setGeometry(QtCore.QRect(120, 300, 31, 31))
        self.bt_busca_cep.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("View/UI/../../Imagens/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_busca_cep.setIcon(icon)
        self.bt_busca_cep.setObjectName("bt_busca_cep")

        self.retranslateUi(ct_FormClientes)
        QtCore.QMetaObject.connectSlotsByName(ct_FormClientes)
        ct_FormClientes.setTabOrder(self.tx_Id, self.tx_nome)
        ct_FormClientes.setTabOrder(self.tx_nome, self.tx_cpf)
        ct_FormClientes.setTabOrder(self.tx_cpf, self.tx_rg)
        ct_FormClientes.setTabOrder(self.tx_rg, self.tx_Celular)
        ct_FormClientes.setTabOrder(self.tx_Celular, self.tx_Telefone)
        ct_FormClientes.setTabOrder(self.tx_Telefone, self.tx_Email)
        ct_FormClientes.setTabOrder(self.tx_Email, self.tx_Cep)
        ct_FormClientes.setTabOrder(self.tx_Cep, self.bt_busca_cep)
        ct_FormClientes.setTabOrder(self.bt_busca_cep, self.tx_Endereco)
        ct_FormClientes.setTabOrder(self.tx_Endereco, self.tx_Numero)
        ct_FormClientes.setTabOrder(self.tx_Numero, self.tx_Bairro)
        ct_FormClientes.setTabOrder(self.tx_Bairro, self.tx_Cidade)
        ct_FormClientes.setTabOrder(self.tx_Cidade, self.tx_Estado)

    def retranslateUi(self, ct_FormClientes):
        _translate = QtCore.QCoreApplication.translate
        ct_FormClientes.setWindowTitle(_translate("ct_FormClientes", "Cadastro de Clientes"))
        self.lb_FormProdutos.setText(_translate("ct_FormClientes", "FICHA CADASTRAL CLIENTE"))
        self.lb_FormProdutos_2.setText(_translate("ct_FormClientes", "NOME"))
        self.tx_nome.setPlaceholderText(_translate("ct_FormClientes", "NOME COMPLETO"))
        self.lb_FormProdutos_3.setText(_translate("ct_FormClientes", "CPF"))
        self.lb_FormProdutos_4.setText(_translate("ct_FormClientes", "RG"))
        self.lb_FormProdutos_5.setText(_translate("ct_FormClientes", "CELULAR"))
        self.tx_Celular.setInputMask(_translate("ct_FormClientes", "(00) 00000-0000"))
        self.tx_Celular.setText(_translate("ct_FormClientes", "() -"))
        self.tx_rg.setInputMask(_translate("ct_FormClientes", "00.000.000-0"))
        self.lb_FormProdutos_8.setText(_translate("ct_FormClientes", "ENDEREÇO"))
        self.tx_Cep.setInputMask(_translate("ct_FormClientes", "99999-999"))
        self.tx_Cep.setPlaceholderText(_translate("ct_FormClientes", "123456789"))
        self.lb_FormProdutos_10.setText(_translate("ct_FormClientes", "CEP"))
        self.bt_Voltar.setText(_translate("ct_FormClientes", "VOLTAR"))
        self.bt_Salvar.setText(_translate("ct_FormClientes", "SALVAR"))
        self.tx_cpf.setInputMask(_translate("ct_FormClientes", "000.000.000-00"))
        self.tx_cpf.setText(_translate("ct_FormClientes", "..-"))
        self.lb_FormProdutos_23.setText(_translate("ct_FormClientes", "Email"))
        self.lb_FormProdutos_24.setText(_translate("ct_FormClientes", "TELEFONE"))
        self.tx_Telefone.setInputMask(_translate("ct_FormClientes", "(00) 0000-0000"))
        self.lb_FormProdutos_11.setText(_translate("ct_FormClientes", "ENDEREÇO"))
        self.lb_FormProdutos_12.setText(_translate("ct_FormClientes", "Nº"))
        self.lb_FormProdutos_13.setText(_translate("ct_FormClientes", "BAIRRO"))
        self.lb_FormProdutos_14.setText(_translate("ct_FormClientes", "CIDADE"))
        self.lb_FormProdutos_15.setText(_translate("ct_FormClientes", "ESTADO"))
        self.bt_busca_cep.setAccessibleName(_translate("ct_FormClientes", "BUSCA CEP"))
