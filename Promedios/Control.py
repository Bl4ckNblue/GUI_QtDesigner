from calculador import *

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, * args, **kwargs)
        self.setupUi(self)
        
        self.btnCalcular.clicked.connect(self.calcular)
        self.btnNuevo.clicked.connect(self.nuevo)
        
    def imprimir (self, m):
        self.txtResultado.insertPlainText(m + '\n')
     
    def calcular (self):
        nota1 = int(self.txtNota1.text())
        nota2 = int(self.txtNota2.text())
        nota3 = int(self.txtNota3.text())
        
        p = round((nota1+nota2+nota3) / 3, 2)

        c = "Desaprobado"
        
        if p > 12.5:
            c = "Aprobado"
        
        self.imprimir("Promedio: " + str(p))
        self.imprimir("Condicion: " + c)
    
    def nuevo(self):
        self.txtNota1.setText('')
        self.txtNota2.setText('')
        self.txtNota3.setText('')
        self.txtResultado.setPlainText('')
        
if __name__=="__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
