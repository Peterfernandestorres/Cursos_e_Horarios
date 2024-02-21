import os
import sys
import mysql.connector as cx
from PyQt5.QtWidgets import QApplication , QWidget , QLabel , QLineEdit , QVBoxLayout , QPushButton , QTableWidgetItem , QTableWidget

con = cx.connect (
    host = "127.0.0.1",
    port = "6556",
    user = "root",
    password = "808",
    database = "banco_cursos" 
    )

cursor = con.cursor ()

os.system ("cls")
class cursos_senac (QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry (150,150,750,500)
        self.setWindowTitle ("Cursos e Horários")

        layout = QVBoxLayout ()

        Labelid = QLabel ("Cursos: ")
        self.editcursos = QLineEdit ()

        Labelhora = QLabel ("Horário: ")
        self.edithora = QLineEdit ()

        Labeldisponivel = QLabel ("Disponivel: ")
        self.editdisponivel = QLineEdit ()

        psbCadastro = QPushButton ("Cadastrar Curso e Horário")

        self.LabelMsg = QLabel ("")

        layout.addWidget (Labelid)
        layout.addWidget (self.editcursos)
        
        layout.addWidget (Labelhora)
        layout.addWidget (self.edithora)

        layout.addWidget (Labeldisponivel)
        layout.addWidget (self.editdisponivel)

        layout.addWidget (psbCadastro)
        psbCadastro.clicked.connect (self.Upcli)

        TBcursos = QTableWidget (self)
        TBcursos.setColumnCount (3)
        TBcursos.setRowCount (10)
        
        HeaderLine=["Cursos","Hora","Disponivel"]

        TBcursos.setHorizontalHeaderLabels (HeaderLine)
        cursor.execute ("select * from tbcursos")
        lintb = 0
        for linha in cursor:
            TBcursos.setItem (lintb,0,QTableWidgetItem(str(linha[0])))
            TBcursos.setItem (lintb,1,QTableWidgetItem(linha[1]))
            TBcursos.setItem (lintb,2,QTableWidgetItem(linha[2]))
            lintb+=1

        layout.addWidget (TBcursos)
        self.setLayout (layout)

# adicionar os informação no banco de dados -----------------------------------------------------------------------------------------------
    def Upcli(self):
        cursor.execute("insert into tbcursos (cursos,hora,disponivel)values(%s,%s,%s)",
                       (self.editcursos.text(),self.edithora.text(),self.editdisponivel.text()))
        con.commit()
        print("Todas as modificação foram realizadas !!!")
if __name__ == "__main__":
    app = QApplication (sys.argv)
    tela = cursos_senac ()
    tela.show()
    sys.exit (app.exec_())