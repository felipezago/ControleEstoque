# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/abrir_venda.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(225, 85)
        Frame.setStyleSheet("background: #fff")
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(10, 20, 141, 17))
        self.label.setObjectName("label")
        self.tx_codigo = QtWidgets.QLineEdit(Frame)
        self.tx_codigo.setGeometry(QtCore.QRect(10, 40, 171, 25))
        self.tx_codigo.setObjectName("tx_codigo")
        self.bt_busca = QtWidgets.QPushButton(Frame)
        self.bt_busca.setGeometry(QtCore.QRect(180, 40, 31, 25))
        self.bt_busca.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Imagens/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_busca.setIcon(icon)
        self.bt_busca.setObjectName("bt_busca")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Abrir Venda"))
        self.label.setText(_translate("Frame", "Informe o Código"))
