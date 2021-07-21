from PyQt5 import QtCore, QtWidgets


class Label(QtWidgets.QLabel):
    clicked = QtCore.pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()
