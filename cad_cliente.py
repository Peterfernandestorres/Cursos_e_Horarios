import os
import sys
import mysql.connector as cx
from PyQt5.QtWidgets import QApplication , QWidget , QLabel , QLineEdit , QVBoxLayout , QPushButton , QTableWidgetItem , QTableWidget

from pymongo import MongoClient as mc

#Importação da loja Mongo 
client = mc("mongodb://root:808@127.0.0.1:37452")
 
db = client.loja_db

os.system ("cls")
class cad_cliente (QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry (150,150,750,2000)
        self.setFixedSize (500,550)
        self.setWindowTitle ("Cursos e Horários")

        layout = QVBoxLayout ()

        Labelid = QLabel ("Id: ")
        self.editid = QLineEdit ()

        Labelusuario = QLabel ("Nome Do Usuario: ")
        self.editusuario = QLineEdit ()

        Labelsenha = QLabel ("Senha: ")
        self.editsenha = QLineEdit ()

        Labelnivel = QLabel ("Nivel de Acesso: ")
        self.editnivel = QLineEdit ()

        psbCadastro = QPushButton ("Cadastrar Usuario")

        self.LabelMsg = QLabel ("")

#Layouts
        
        layout.addWidget (Labelusuario)
        layout.addWidget (self.editusuario)

        layout.addWidget (Labelsenha)
        layout.addWidget (self.editsenha)

        layout.addWidget (Labelnivel)
        layout.addWidget (self.editnivel)

        layout.addWidget (psbCadastro)
        psbCadastro.clicked.connect (self.Upcli)
        

        TBusuarios = QTableWidget (self)
        TBusuarios.setColumnCount (4)
        TBusuarios.setRowCount (10)
        
        HeaderLine=["Id","Nome do Usuario","Senha","Nivel de Acesso"]

        TBusuarios.setHorizontalHeaderLabels (HeaderLine)
        
        lintb = 0
        
        for us in db["usuario"].find():
            TBusuarios.setItem (lintb,0,QTableWidgetItem(str(us["_id"])))
            TBusuarios.setItem (lintb,1,QTableWidgetItem(us["nomeusuario"]))
            TBusuarios.setItem (lintb,2,QTableWidgetItem(us["senha"]))
            TBusuarios.setItem (lintb,3,QTableWidgetItem(us["nivel"]))
            lintb+=1

        layout.addWidget (TBusuarios)
        self.setLayout (layout)

    def Upcli(self):
        usuario_id = db["usuario"].insert_one({"nomeusuario":self.editusuario.text(),"senha":self.editsenha.text(),"nivel":self.editnivel.text()}).inserted_id
        print (self.editusuario.text())      
        self.LabelMsg.setText ("Cadastro Preenchido")


if __name__ == "__main__":
    app = QApplication (sys.argv)
    tela = cad_cliente ()
    tela.show()
    sys.exit (app.exec_())