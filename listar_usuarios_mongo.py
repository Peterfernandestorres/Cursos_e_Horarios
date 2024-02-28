import os
import sys
from PyQt5.QtCore import Qt
import mysql.connector as mycon 
os.system ("cls")

from PyQt5.QtWidgets import QApplication , QWidget , QLabel , QLineEdit , QVBoxLayout , QPushButton , QTableWidgetItem , QTableWidget

from pymongo import MongoClient as mc

#Importação da loja Mongo 
client = mc("mongodb://root:808@127.0.0.1:37452")
 
db = client.loja_db


class Exibirusuarios (QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry (100,100,500,300)
        self.setFixedSize (500,300)
        self.setWindowTitle ("Usuários Cadastrados")

        TBusuarios = QTableWidget (self)
        TBusuarios.setColumnCount (4)
        TBusuarios.setRowCount (10)
        
        TBcursos = QTableWidget (self)
        HeaderLine=["Id","Nome Usuario","Senha","Nivel de Acesso"]

        TBcursos.setHorizontalHeaderLabels (HeaderLine)
       
        lintb = 0

        for us in db["usuario"].find():
    
            TBusuarios.setItem (lintb,0,QTableWidgetItem(str(us["_id"])))
            TBusuarios.setItem (lintb,1,QTableWidgetItem(us["nomeusuario"]))
            TBusuarios.setItem (lintb,2,QTableWidgetItem(us["senha"]))
            TBusuarios.setItem (lintb,3,QTableWidgetItem(us["nivel"]))

        layout = QVBoxLayout ()
        layout.addWidget (TBusuarios)
        self.setLayout (layout)

if __name__ == "__main__":
    app = QApplication (sys.argv)
    tela = Exibirusuarios ()
    tela.show()
    sys.exit (app.exec_())