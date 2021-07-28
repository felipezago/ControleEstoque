# -*- coding: utf-8 -*-
from PIL.ImageQt import ImageQt
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtCore import QSize
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon, QPainter
import bcrypt
import tempfile
from pdf2image import convert_from_path


def IconeBotaoTopo(botao, imagem):
    icon = QIcon()
    icon.addPixmap(QPixmap(imagem),
                   QIcon.Normal, QIcon.Off)
    # icon.addPixmap(QPixmap((os.path.join(caminho, imagem)),
    #                              QIcon.Normal, QIcon.Off))
    botao.setIcon(icon)
    botao.setIconSize(QSize(50, 35))


def verificar_criptografia(senha, senhaCriptografada):
    return bcrypt.checkpw(senha, senhaCriptografada)


def criptografar_senha(senha):
    salt = bcrypt.gensalt()
    criptografada = bcrypt.hashpw(senha.encode("utf-8"), salt).decode("utf-8")
    return criptografada


def IconeBotaoMenu(botao, imagem):
    icon = QIcon()
    icon.addPixmap(QPixmap(imagem),
                   QIcon.Normal, QIcon.Off)
    botao.setIcon(icon)
    botao.setIconSize(QSize(25, 25))


def IconeHome(botao, imagem):
    icon = QIcon()
    icon.addPixmap(QPixmap(imagem),
                   QIcon.Normal, QIcon.Off)
    botao.setIcon(icon)
    botao.setIconSize(QSize(130, 120))


def IconeBotaoForm(botao, imagem):
    icon = QIcon()
    icon.addPixmap(QPixmap(imagem),
                   QIcon.Normal, QIcon.Off)
    botao.setIcon(icon)
    botao.setIconSize(QSize(80, 35))


def centralizar(object):
    from PyQt5 import QtWidgets

    qr = object.frameGeometry()
    cp = QtWidgets.QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    object.move(qr.topLeft())


def resource_path(relative_path):
    import os
    import sys

    base_path = getattr(sys, '_MEIPASS', os.path.dirname(
        os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def exec_app(obj):
    app = obj
    app.show()
    centralizar(app)


def formatar_cpf_rg(cpf):
    cpf_formatado = str(cpf).replace('.', '')
    cpf_formatado = cpf_formatado.replace('-', '')
    cpf_formatado = cpf_formatado.replace('/', '')
    return cpf_formatado


def formatar_cnpj(cnpj):
    cnpj_string = str(cnpj)
    cnpj_formatado = f"{cnpj_string[:2]}.{cnpj_string[2:5]}.{cnpj_string[5:8]}/{cnpj_string[8:12]}-{cnpj_string[12:14]}"
    return cnpj_formatado


def formatar_cpf(cpf):
    cpf_string = str(cpf)
    cpf_formatado = f"{cpf_string[:3]}.{cpf_string[3:6]}.{cpf_string[6:9]}-{cpf_string[9:11]}"
    return cpf_formatado


def formatar_rg(rg):
    rg_string = str(rg)
    rg_formatado = f"{rg_string[:2]}.{rg_string[2:5]}.{rg_string[5:8]}-{rg_string[8:9]}"
    return rg_formatado


def retorna_ip():
    import socket

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


def show_msg(tipo_msg="erro", title="", mensagem=""):
    from PyQt5.QtWidgets import QMessageBox
    msg = QMessageBox()
    msg.setWindowTitle(title)
    if tipo_msg == "erro":
        msg.setIcon(QMessageBox.Warning)
    elif tipo_msg == "aviso":
        msg.setIcon(QMessageBox.Information)
    msg.setText(mensagem)
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msg.exec_()


def print_dialog(self, img):
    printer = QPrinter(QPrinter.HighResolution)
    dialog = QPrintDialog(printer, self)

    if dialog.exec_() == QPrintDialog.Accepted:
        with tempfile.TemporaryDirectory() as path:
            images = convert_from_path("PDF/" + img, dpi=300, output_folder=path)
            painter = QPainter()
            painter.begin(printer)
            for i, image in enumerate(images):
                if i > 0:
                    printer.newPage()
                rect = painter.viewport()
                img = ImageQt(image)
                img_scaled = img.scaled(rect.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
                painter.drawImage(rect, img_scaled)
            painter.end()

    remove_pdf("venda")


def remove_pdf(desc):
    import os

    dir_img = f"PDF/{desc}.png"

    if os.path.isfile(dir_img):
        os.remove(dir_img)


if __name__ == '__main__':
    print(formatar_rg("139941357"))
