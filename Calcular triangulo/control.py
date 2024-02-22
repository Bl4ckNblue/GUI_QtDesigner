from triangulo import *
from math import sqrt as raiz
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, * args, **kwargs)
        self.setupUi(self)
        
        self.btnCalcular.clicked.connect(self.calcular)
        self.btnNuevo.clicked.connect(self.nuevo)
        
    def imprimir (self, a, b ):
        self.txtPerimetro.insertPlainText(f"Perimetro: {a}")
        self.txtArea.insertPlainText(f"Area: {b}")
     
    def calcular (self):
        
        lado1 = int(self.txtLado1.text())
        lado2 = int(self.txtLado2.text())
        base = int(self.txtBase.text())
        
        #Perimetro
        perimetro = (lado1 + lado2 + base)
        
        #Area
        spe = perimetro/2
        heron = raiz(spe*(spe-lado1)*(spe-lado2)*(spe-base))
        altura = (2*heron)/base
        area = round ((1/2)*base*altura, 2)
        
        self.imprimir(perimetro, area)
    
    def nuevo(self):
        self.txtLado1.setText('')
        self.txtLado2.setText('')
        self.txtBase.setText('')
        self.txtPerimetro.setPlainText('')
        self.txtArea.setPlainText('')
        
if __name__=="__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
