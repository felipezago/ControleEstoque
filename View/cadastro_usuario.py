# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadastro_usuario.ui'
#
# Created by: PyQt5 View code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from Funcoes.tab_order import cadastro_usuario


class Ui_ct_FormUsuario(object):
    def setupUi(self, ct_FormUsuario):
        ct_FormUsuario.setObjectName("ct_FormUsuario")
        ct_FormUsuario.resize(1000, 443)
        ct_FormUsuario.setStyleSheet("background: #FFF;\n"
"border: none")
        self.fr_FormUsuario = QtWidgets.QFrame(ct_FormUsuario)
        self.fr_FormUsuario.setGeometry(QtCore.QRect(0, 0, 1000, 500))
        self.fr_FormUsuario.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_FormUsuario.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_FormUsuario.setObjectName("fr_FormUsuario")
        self.lb_FormFornecedor_21 = QtWidgets.QLabel(self.fr_FormUsuario)
        self.lb_FormFornecedor_21.setGeometry(QtCore.QRect(670, 60, 150, 20))
        self.lb_FormFornecedor_21.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_21.setObjectName("lb_FormFornecedor_21")
        self.tx_Celular = QtWidgets.QLineEdit(self.fr_FormUsuario)
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
        self.lb_FormFornecedor_27 = QtWidgets.QLabel(self.fr_FormUsuario)
        self.lb_FormFornecedor_27.setGeometry(QtCore.QRect(580, 290, 50, 20))
        self.lb_FormFornecedor_27.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_27.setObjectName("lb_FormFornecedor_27")
        self.lb_FormFornecedor_28 = QtWidgets.QLabel(self.fr_FormUsuario)
        self.lb_FormFornecedor_28.setGeometry(QtCore.QRect(20, 290, 50, 20))
        self.lb_FormFornecedor_28.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_28.setObjectName("lb_FormFornecedor_28")
        self.lb_FormFornecedor_23 = QtWidgets.QLabel(self.fr_FormUsuario)
        self.lb_FormFornecedor_23.setGeometry(QtCore.QRect(670, 120, 150, 20))
        self.lb_FormFornecedor_23.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_23.setObjectName("lb_FormFornecedor_23")
        self.lb_FormFornecedor_20 = QtWidgets.QLabel(self.fr_FormUsuario)
        self.lb_FormFornecedor_20.setGeometry(QtCore.QRect(20, 345, 120, 20))
        self.lb_FormFornecedor_20.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_20.setObjectName("lb_FormFornecedor_20")
        self.lb_FormFornecedor_17 = QtWidgets.QLabel(self.fr_FormUsuario)
        self.lb_FormFornecedor_17.setGeometry(QtCore.QRect(20, 60, 150, 20))
        self.lb_FormFornecedor_17.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_17.setObjectName("lb_FormFornecedor_17")
        self.tx_rg = QtWidgets.QLineEdit(self.fr_FormUsuario)
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
        self.lb_FormFornecedor_26 = QtWidgets.QLabel(self.fr_FormUsuario)
        self.lb_FormFornecedor_26.setGeometry(QtCore.QRect(300, 345, 120, 20))
        self.lb_FormFornecedor_26.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_26.setObjectName("lb_FormFornecedor_26")
        self.tx_Telefone = QtWidgets.QLineEdit(self.fr_FormUsuario)
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
        self.lb_FormFornecedor_30 = QtWidgets.QLabel(self.fr_FormUsuario)
        self.lb_FormFornecedor_30.setGeometry(QtCore.QRect(236, 180, 190, 20))
        self.lb_FormFornecedor_30.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_30.setObjectName("lb_FormFornecedor_30")
        self.lb_FormFornecedor_16 = QtWidgets.QLabel(self.fr_FormUsuario)
        self.lb_FormFornecedor_16.setGeometry(QtCore.QRect(580, 345, 70, 20))
        self.lb_FormFornecedor_16.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_16.setObjectName("lb_FormFornecedor_16")
        self.lb_FormFornecedor_6 = QtWidgets.QLabel(self.fr_FormUsuario)
        self.lb_FormFornecedor_6.setGeometry(QtCore.QRect(236, 120, 190, 20))
        self.lb_FormFornecedor_6.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_6.setObjectName("lb_FormFornecedor_6")
        self.tx_Bairro = QtWidgets.QLineEdit(self.fr_FormUsuario)
        self.tx_Bairro.setGeometry(QtCore.QRect(20, 370, 260, 25))
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
        self.tx_Estado = QtWidgets.QLineEdit(self.fr_FormUsuario)
        self.tx_Estado.setGeometry(QtCore.QRect(580, 370, 70, 25))
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
        self.tx_cpf = QtWidgets.QLineEdit(self.fr_FormUsuario)
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
        self.tx_Num = QtWidgets.QLineEdit(self.fr_FormUsuario)
        self.tx_Num.setGeometry(QtCore.QRect(580, 315, 70, 25))
        self.tx_Num.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_Num.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_Num.setInputMask("")
        self.tx_Num.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tx_Num.setPlaceholderText("")
        self.tx_Num.setObjectName("tx_Num")
        self.lb_FormFornecedor = QtWidgets.QLabel(self.fr_FormUsuario)
        self.lb_FormFornecedor.setGeometry(QtCore.QRect(20, 10, 971, 30))
        self.lb_FormFornecedor.setStyleSheet("QLabel{\n"
"font-size: 14px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"\n"
"border-bottom: 2px solid #A2A2A2\n"
"}")
        self.lb_FormFornecedor.setObjectName("lb_FormFornecedor")
        self.lb_FormFornecedor_25 = QtWidgets.QLabel(self.fr_FormUsuario)
        self.lb_FormFornecedor_25.setGeometry(QtCore.QRect(452, 180, 190, 20))
        self.lb_FormFornecedor_25.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_25.setObjectName("lb_FormFornecedor_25")
        self.tx_Cidade = QtWidgets.QLineEdit(self.fr_FormUsuario)
        self.tx_Cidade.setGeometry(QtCore.QRect(300, 370, 260, 25))
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
        self.tx_senha = QtWidgets.QLineEdit(self.fr_FormUsuario)
        self.tx_senha.setGeometry(QtCore.QRect(670, 145, 300, 25))
        self.tx_senha.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_senha.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.tx_senha.setObjectName("tx_senha")
        self.frame = QtWidgets.QFrame(self.fr_FormUsuario)
        self.frame.setGeometry(QtCore.QRect(0, 400, 1000, 40))
        self.frame.setStyleSheet("border-bottom: 2px solid #CCC;\n"
"background: #F7F7F7")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.bt_salvarUsuario = QtWidgets.QPushButton(self.frame)
        self.bt_salvarUsuario.setGeometry(QtCore.QRect(750, 5, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bt_salvarUsuario.setFont(font)
        self.bt_salvarUsuario.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_salvarUsuario.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_salvarUsuario.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.bt_salvarUsuario.setStyleSheet("QPushButton {\n"
"background-color: #7AB32E;\n"
"color: #FFF\n"
" }\n"
"QPushButton:hover{\n"
"background-color: #40a286\n"
"}")
        self.bt_salvarUsuario.setIconSize(QtCore.QSize(75, 35))
        self.bt_salvarUsuario.setObjectName("bt_salvarUsuario")
        self.bt_Voltar = QtWidgets.QPushButton(self.frame)
        self.bt_Voltar.setGeometry(QtCore.QRect(880, 5, 120, 30))
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
        self.tx_cep = QtWidgets.QLineEdit(self.fr_FormUsuario)
        self.tx_cep.setGeometry(QtCore.QRect(20, 315, 131, 25))
        self.tx_cep.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_cep.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_cep.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_cep.setObjectName("tx_cep")
        self.tx_usuario = QtWidgets.QLineEdit(self.fr_FormUsuario)
        self.tx_usuario.setGeometry(QtCore.QRect(670, 85, 300, 25))
        self.tx_usuario.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_usuario.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_usuario.setObjectName("tx_usuario")
        self.lb_FormFornecedor_29 = QtWidgets.QLabel(self.fr_FormUsuario)
        self.lb_FormFornecedor_29.setGeometry(QtCore.QRect(160, 290, 250, 20))
        self.lb_FormFornecedor_29.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_29.setObjectName("lb_FormFornecedor_29")
        self.lb_FormFornecedor_9 = QtWidgets.QLabel(self.fr_FormUsuario)
        self.lb_FormFornecedor_9.setGeometry(QtCore.QRect(20, 180, 196, 20))
        self.lb_FormFornecedor_9.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_9.setObjectName("lb_FormFornecedor_9")
        self.tx_Endereco = QtWidgets.QLineEdit(self.fr_FormUsuario)
        self.tx_Endereco.setGeometry(QtCore.QRect(160, 315, 400, 25))
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
        self.tx_Email = QtWidgets.QLineEdit(self.fr_FormUsuario)
        self.tx_Email.setGeometry(QtCore.QRect(452, 205, 196, 25))
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
        self.lb_FormFornecedor_18 = QtWidgets.QLabel(self.fr_FormUsuario)
        self.lb_FormFornecedor_18.setGeometry(QtCore.QRect(20, 120, 190, 20))
        self.lb_FormFornecedor_18.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_18.setObjectName("lb_FormFornecedor_18")
        self.lb_FormFornecedor_31 = QtWidgets.QLabel(self.fr_FormUsuario)
        self.lb_FormFornecedor_31.setGeometry(QtCore.QRect(20, 250, 630, 30))
        self.lb_FormFornecedor_31.setStyleSheet("QLabel{\n"
"font-size: 14px;\n"
"font-family: \"Arial\";\n"
"font-weight: normal;\n"
"\n"
"border-bottom: 2px solid #A2A2A2;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_31.setObjectName("lb_FormFornecedor_31")
        self.tx_nome = QtWidgets.QLineEdit(self.fr_FormUsuario)
        self.tx_nome.setGeometry(QtCore.QRect(20, 85, 630, 25))
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
        self.tx_senha2 = QtWidgets.QLineEdit(self.fr_FormUsuario)
        self.tx_senha2.setGeometry(QtCore.QRect(670, 205, 300, 25))
        self.tx_senha2.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tx_senha2.setStyleSheet("QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}")
        self.tx_senha2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.tx_senha2.setObjectName("tx_senha2")
        self.lb_FormFornecedor_24 = QtWidgets.QLabel(self.fr_FormUsuario)
        self.lb_FormFornecedor_24.setGeometry(QtCore.QRect(670, 180, 271, 20))
        self.lb_FormFornecedor_24.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.lb_FormFornecedor_24.setObjectName("lb_FormFornecedor_24")

        self.retranslateUi(ct_FormUsuario)
        QtCore.QMetaObject.connectSlotsByName(ct_FormUsuario)

        cadastro_usuario(self, ct_FormUsuario)

    def retranslateUi(self, ct_FormUsuario):
        _translate = QtCore.QCoreApplication.translate
        ct_FormUsuario.setWindowTitle(_translate("ct_FormUsuario", "Cadastro de Usuários"))
        self.lb_FormFornecedor_21.setText(_translate("ct_FormUsuario", "USUÁRIO"))
        self.tx_Celular.setInputMask(_translate("ct_FormUsuario", "(00) 00000-0000"))
        self.tx_Celular.setText(_translate("ct_FormUsuario", "() -"))
        self.lb_FormFornecedor_27.setText(_translate("ct_FormUsuario", "Nº"))
        self.lb_FormFornecedor_28.setText(_translate("ct_FormUsuario", "CEP"))
        self.lb_FormFornecedor_23.setText(_translate("ct_FormUsuario", "SENHA"))
        self.lb_FormFornecedor_20.setText(_translate("ct_FormUsuario", "BAIRRO"))
        self.lb_FormFornecedor_17.setText(_translate("ct_FormUsuario", "NOME COMPLETO"))
        self.tx_rg.setInputMask(_translate("ct_FormUsuario", "00.000.000-0"))
        self.lb_FormFornecedor_26.setText(_translate("ct_FormUsuario", "CIDADE"))
        self.tx_Telefone.setInputMask(_translate("ct_FormUsuario", "(00) 0000-0000"))
        self.lb_FormFornecedor_30.setText(_translate("ct_FormUsuario", "TELEFONE"))
        self.lb_FormFornecedor_16.setText(_translate("ct_FormUsuario", "ESTADO"))
        self.lb_FormFornecedor_6.setText(_translate("ct_FormUsuario", "RG"))
        self.tx_cpf.setInputMask(_translate("ct_FormUsuario", "000.000.000-00"))
        self.tx_cpf.setText(_translate("ct_FormUsuario", "..-"))
        self.lb_FormFornecedor.setText(_translate("ct_FormUsuario", "CADASTRO DE USUÁRIO"))
        self.lb_FormFornecedor_25.setText(_translate("ct_FormUsuario", "Email"))
        self.tx_senha.setPlaceholderText(_translate("ct_FormUsuario", "Senha"))
        self.bt_salvarUsuario.setText(_translate("ct_FormUsuario", "SALVAR"))
        self.bt_Voltar.setText(_translate("ct_FormUsuario", "VOLTAR"))
        self.tx_cep.setInputMask(_translate("ct_FormUsuario", "99999-999"))
        self.tx_cep.setPlaceholderText(_translate("ct_FormUsuario", "123456789"))
        self.tx_usuario.setPlaceholderText(_translate("ct_FormUsuario", "Usuário"))
        self.lb_FormFornecedor_29.setText(_translate("ct_FormUsuario", "ENDEREÇO"))
        self.lb_FormFornecedor_9.setText(_translate("ct_FormUsuario", "CELULAR"))
        self.lb_FormFornecedor_18.setText(_translate("ct_FormUsuario", "CPF"))
        self.lb_FormFornecedor_31.setText(_translate("ct_FormUsuario", "ENDEREÇO"))
        self.tx_nome.setPlaceholderText(_translate("ct_FormUsuario", "nome completo"))
        self.tx_senha2.setPlaceholderText(_translate("ct_FormUsuario", "Digite sua senha novamente"))
        self.lb_FormFornecedor_24.setText(_translate("ct_FormUsuario", "DIGITE A SENHA NOVAMENTE"))