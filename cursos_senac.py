import os
import sys
from PyQt5.QtCore import Qt
import mysql.connector as cx
os.system ("cls")

from PyQt5.QtWidgets import QApplication , QWidget , QLabel , QLineEdit , QVBoxLayout , QPushButton , QTableWidgetItem , QTableWidget

con = cx.connect (
    host = "127.0.0.1",
    port = "6556",
    user = "root",
    password = "808",
    database = "cursos_senac" 
    )

cursor = con.cursor ()

class lista_de_cursos (QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry (150,150,750,500)
        self.setWindowTitle ("Horários")

        layout = QVBoxLayout ()

        Labelid = QLabel ("Cursos: ")
        self.editcursos = QLineEdit ()

        Labelhora = QLabel ("Horário do Curso: ")
        self.edithora = QLineEdit ()

        psbCadastro = QPushButton ("Cadastrar")

        self.LabelMsg = QLabel ("")

        layout.addWidget (Labelid)
        layout.addWidget (self.editcursos)
        
        layout.addWidget (Labelhora)
        layout.addWidget (self.edithora)

        layout.addWidget (psbCadastro)
        psbCadastro.clicked.connect (self.Upcli)

        TBalunos = QTableWidget (self)
        TBalunos.setColumnCount (4)
        TBalunos.setRowCount (10)
        
        HeaderLine=["Cursos","Horários","cadastrar"]

        TBalunos.setHorizontalHeaderLabels (HeaderLine)
        cursor.execute ("select * from Horários")
        lintb = 0
        for linha in cursor:
            TBalunos.setItem (lintb,0,QTableWidgetItem(str(linha[0])))
            TBalunos.setItem (lintb,1,QTableWidgetItem(linha[1]))
            TBalunos.setItem (lintb,2,QTableWidgetItem(linha[2]))
            TBalunos.setItem (lintb,3,QTableWidgetItem(linha[3]))
            lintb+=1

        layout.addWidget (TBalunos)
        self.setLayout (layout)

# adicionar os informação no banco de dados -----------------------------------------------------------------------------------------------
    def Upcli(self):
        if(self.editid.text==""):
            print ("não é possivel atualizar sem o Curso e os Horários Corretos")
        elif(self.edithora.text ==""and self.editcursos.text ==""):
                print("Não é  possivel atualizar se tiver todos os campo em branco")
#atualizar só um campo -----------------------------------------------------------------------------------------------------------------                
#Horário
        elif(self.edithora.text != ""and self.editcursos.text ==""):
            cursor.execute("update hora set hora_curso=%s where hora_cursos=%s",(self.edithora.text(),self.editcursos.text()))
#cursos
        elif(self.edithora.text == ""and self.editcursos.text !=""):
            cursor.execute("update hora set cursos=%s where hora_cursos=%s",(self.edithora.text(),self.editcursos.text()))

# atualizar tudo
        else:
            cursor.execute("update alunos set nome_aluno=%s,cursos=%s,cadastro=%s where alunos_cursos=%s",
                           (self.edithora.text(),self.editcursos.text()))
        cx.commit()
        print("Todas as modificação foram realizadas !!!")
if __name__ == "__main__":
    app = QApplication (sys.argv)
    tela = lista_de_cursos ()
    tela.show()
    sys.exit (app.exec_())