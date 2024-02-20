import os
import sys
from PyQt5.QtCore import Qt
import mysql.connector as mycon 
os.system ("cls")

from PyQt5.QtWidgets import QApplication , QWidget , QLabel , QLineEdit , QVBoxLayout , QPushButton , QTableWidgetItem , QTableWidget

cx = mycon.connect (
    host = "127.0.0.1",
    port = "6556",
    user = "root",
    password = "808",
    database = "cursos_senac" 
    )
cursor = cx.cursor ()

class ExibirCursos (QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry (100,100,500,300)
        self.setWindowTitle ("cursos Cadastrados")

        TBcursos = QTableWidget (self)
        TBcursos.setColumnCount (4)
        TBcursos.setRowCount (10)
        
        TBcursos = QTableWidget (self)
        HeaderLine=["cursos","Hora"]

        TBcursos.setHorizontalHeaderLabels (HeaderLine)
        cursor.execute ("select * from cursos")
        lintb = 0
        for linha in cursor:
            TBcursos.setItem (lintb,0,QTableWidgetItem(str(linha[0])))
            TBcursos.setItem (lintb,0,QTableWidgetItem(linha[1]))
            TBcursos.setItem (lintb,0,QTableWidgetItem(linha[2]))
            TBcursos.setItem (lintb,0,QTableWidgetItem(linha[3]))

        layout = QVBoxLayout ()
        layout.addWidget (TBcursos)
        self.setLayout (layout)

if __name__ == "__main__":
    app = QApplication (sys.argv)
    tela = ExibirCursos ()
    tela.show()
    sys.exit (app.exec_())