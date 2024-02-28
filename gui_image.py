import os
import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QApplication , QLabel , QMainWindow , QWidget , QHBoxLayout

os.system ("cls")


class GuImage (QWidget):
    def __init__(self):
        super().__init__()

        labelTexto = QLabel ("Olá, Gato Feio !")
        labelimagem = QLabel ("")
        labelimagem.setPixmap (QPixmap("cat.jpg"))
        labelimagem.setScaledContents(True)

        layout = QHBoxLayout ()
        layout.addWidget(labelTexto)
        layout.addWidget(labelimagem)

        self.setGeometry (100,100,500,600)
        self.setWindowTitle ("Imagem em Label (Gato Mal Humorado)")
        self.setLayout (layout)


app = QApplication (sys.argv)
tela = GuImage()
tela.show()
app.exec_()

