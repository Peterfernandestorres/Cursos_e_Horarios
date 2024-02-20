import os
import sys
import mysql.connector as mc
os.system ("cls")

from PyQt5.QtWidgets import QApplication , QWidget , QLabel , QLineEdit , QVBoxLayout , QPushButton

con = mc.connect (
    host = "127.0.0.1",
    port = "6556",
    user = "root",
    password = "808",
    database = "cursos_senac" 
    )

cursor = con.cursor ()

class Cursos (QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry (30,40,600,300)
        self.setWindowTitle ("Cadastro De Cursoss")

        Labelhora = QLabel ("Horário do Curso: ")
        self.edithora = QLineEdit ()

        Labelcursos = QLabel ("Nome do Curso: ")
        self.editcursos = QLineEdit ()

        psbCadastro = QPushButton ("Cadastrar")

        self.LabelMsg = QLabel ("")

        layout = QVBoxLayout ()
        layout.addWidget (Labelhora)
        layout.addWidget (self.edithora)

        layout.addWidget (Labelcursos)
        layout.addWidget (self.editcursos)

        layout.addWidget (psbCadastro)
        psbCadastro.clicked.connect (self.cadCli)

        layout.addWidget (self.LabelMsg)

        self.setLayout (layout)

    def cadCli(self):
        cursor.execute ("Insert into alunos (hora,cursos)values(%s,%s)",
                        (self.edithora.text(),self.editcursos.text()))
        print (self.edithora.text())
        con.commit ()
        self.LabelMsg.setText ("aluno Cadastrado")

if __name__ == "__main__":
    app = QApplication (sys.argv)
    tela = Cursos ()
    tela.show()
    sys.exit (app.exec_())