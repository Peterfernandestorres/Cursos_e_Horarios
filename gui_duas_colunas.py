import os
import sys

from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout,QHBoxLayout, QStyle , QLineEdit , QTableWidget , QTableWidgetItem 
from PyQt5.QtGui import QPixmap

os.system ("cls")

class GuiDuasColunas(QWidget):

    def __init__(self):
        super().__init__()

        self.total = 0.0
        self.linha = 0
        self.setGeometry(0,25,1590,840)
        self.setWindowTitle("Caixa da Padaria")

        layoutVerEs = QVBoxLayout()
        layoutVerDi = QVBoxLayout()
        layoutHor = QHBoxLayout()


        labelColEsq = QLabel()
        labelColEsq.setStyleSheet("QLabel{background-color:#3e2723;}")
        labelColEsq.setFixedWidth (700)

        labelColDir = QLabel()
        labelColDir.setStyleSheet("QLabel{background-color:#3e2723}")
        labelColEsq.setFixedWidth(700)

        labelLogo = QLabel ()
        labelLogo.setPixmap (QPixmap ("zarla-trigo.png"))
        labelLogo.setScaledContents (True)
        

        labelNomeProduto = QLabel ("Nome do produto")
        labelNomeProduto.setStyleSheet("QLabel{background-color:white;front-size:15pt}")
        self.NomeProdutoEdit = QLineEdit ()
        self.NomeProdutoEdit.setStyleSheet("QLineEdit{padding:10px;front-size:15pt}")

        labelCodigoProduto = QLabel ("Código do produto")
        labelCodigoProduto.setStyleSheet("QLabel{background-color:white;front-size:15pt}")
        self.CodigoprodutoEdit = QLineEdit ()
        self.CodigoprodutoEdit.setStyleSheet("QLineEdit{padding:10px;front-size:15pt}")

        labelquantidade = QLabel ("Quantidade do produto")
        labelquantidade.setStyleSheet("QLabel{background-color:white;front-size:15pt}")
        self.quantidadeEdit = QLineEdit ()
        self.quantidadeEdit.setStyleSheet("QLineEdit{padding:10px;front-size:15pt}")

        labeldescricao = QLabel ("Descricao do produto")
        labeldescricao.setStyleSheet("QLabel{background-color:white;front-size:15pt}")
        self.descricaoEdit = QLineEdit ()
        self.descricaoEdit.setStyleSheet("QLineEdit{padding:10px;front-size:15pt}")

        labelPreco = QLabel ("Preço do produto")
        labelPreco.setStyleSheet("QLabel{background-color:white;front-size:15pt}")
        self.PrecoEdit = QLineEdit ()
        self.PrecoEdit.setStyleSheet("QLineEdit{padding:10px;front-size:15pt}")

        labelSubTotalProduto = QLabel ("Subtotal do produto")
        labelSubTotalProduto.setStyleSheet("QLabel{background-color:white;front-size:15pt}")
        self.SubTotalProdutoEdit = QLineEdit ()
        self.SubTotalEditProduto = QLineEdit ("0,00")
        self.SubTotalProdutoEdit.setEnabled (False)
        self.SubTotalProdutoEdit.setStyleSheet("QLineEdit{padding:10px;front-size:15pt}")
        self.SubTotalProdutoEdit.setFixedHeight (70)

        labelTotal = QLabel ("Total a Pagar")
        labelTotal.setStyleSheet("QLabel{background-color:white;front-size:15pt}")
        self.TotalEdit = QLineEdit ("0,00")
        self.TotalEdit.setEnabled (False)
        self.TotalEdit.setStyleSheet("QLineEdit{padding:10px;front-size:15pt}")
        self.TotalEdit.setFixedHeight (70)
        


        layoutVerEs.addWidget(labelLogo)
        
        layoutVerEs.addWidget(labelNomeProduto)
        layoutVerEs.addWidget(self.NomeProdutoEdit)

        layoutVerEs.addWidget(labelCodigoProduto)
        layoutVerEs.addWidget(self.CodigoprodutoEdit)

        layoutVerEs.addWidget(labelPreco)
        layoutVerEs.addWidget(self.PrecoEdit)

        layoutVerEs.addWidget(labelquantidade)
        layoutVerEs.addWidget(self.quantidadeEdit)
        
        layoutVerEs.addWidget(labeldescricao)
        layoutVerEs.addWidget(self.descricaoEdit)

        layoutVerEs.addWidget(labelSubTotalProduto)
        layoutVerEs.addWidget(self.SubTotalProdutoEdit)

        layoutVerDi.addWidget(labelTotal)
        layoutVerDi.addWidget(self.TotalEdit)


        # Criando a tabela de dados do lado Direito

        self.tbResumo = QTableWidget(self)
        self.tbResumo.setColumnCount (5)
        self.tbResumo.setRowCount (10)

        # Criando o Cabeçalho para a tabela Resumo

        titulos = ["Códigos","Nome Produto","Quantidade","Preço Unitario","Preço Total"]
        self.tbResumo.setHorizontalHeaderLabels (titulos)
        layoutVerDi.addWidget (self.tbResumo)
        labelColDir.setLayout (layoutVerDi)
      

        # Abas de Layout 

        labelColEsq.setLayout(layoutVerEs)
        layoutHor.addWidget(labelColEsq)
        layoutHor.addWidget(labelColDir)

        self.setLayout(layoutHor)

        self.keyPressEvent = self.keyPressEvent

def keyPressEvent(self, e):



    print ("event", e)
    if (e.key() == Qt._F2):
        print (' Você Teclou F2')
        self.tbResumo.setItem (self.linha,0,QTableWidgetItem(str(self.codigoEdit.text())))
        self.tbResumo.setItem (self.linha,1,QTableWidgetItem(str(self.NomeProdutoEdit.text())))
        self.tbResumo.setItem (self.linha,2,QTableWidgetItem(str(self.quantidadeEdit.text())))
        self.tbResumo.setItem (self.linha,3,QTableWidgetItem(str(self.descricaoEdit.text())))
        self.tbResumo.setItem (self.linha,4,QTableWidgetItem(str(self.PrecoEdit.text())))
        self.tbResumo.setItem (self.linha,5,QTableWidgetItem(str(self.SubTotalProdutoEdit.text())))
        self.linha+=1

        self.total+=float(self.SubTotalEdit.text())
        self.totalPagarEdit.setText(str(self.total))

        # Limpar os LineEdit
        self.codigoEdit.setText ("")
        self.NomeProdutoEdit.setText ("")
        self.quantidadeEdit.setText ("")
        self.descricaoEdit.setText ("")
        self.PrecoEdit.setText ("")
        self.SubTotalProdutoEdit.setText ("Aperta a Tecla F3 para ver o SubTotal Do Produto")


    elif(e.key() == Qt.Key_F3):
        print (' Você Teclou F3')
        qnt = self.quantidadeEdit.text()
        prc = self.PrecoEdit.text()
        res = float (qnt) * float (prc)
        self.SubTotalProdutoEdit.setText(str(res))


app = QApplication (sys.argv)
tela = GuiDuasColunas()
tela.show()
app.exec_()
