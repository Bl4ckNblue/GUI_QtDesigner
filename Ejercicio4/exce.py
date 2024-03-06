from triangulo import *
from math import sqrt as raiz
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, * args, **kwargs)
        self.setupUi(self)
        
        self.btnProcesar.clicked.connect(self.procesar)
        self.btnNuevo.clicked.connect(self.nuevo)

    def procesar (self):
        lA = self.txtA.text()
        lB = self.txtB.text()
        lC = self.txtC.text()
        
        if lA.isalpha() or lB.isalpha() or lC.isalpha():
            self.imprimir("Debe ingresar solo valores numéricos")
        else:
            ladoA = float(lA)
            ladoB = float(lB)
            ladoC = float(lC)
            if self.validar_triangulo(ladoA, ladoB, ladoC):
                #Perímetro
                p = ladoA + ladoB + ladoC
                #Área
                spe = p/2
                heron = raiz(spe*(spe-ladoA)*(spe-ladoB)*(spe-ladoC))

                self.imprimir(f'Perimetro : {p}')
                self.imprimir(f'Area : {heron:.4f}')
            else:
                self.imprimir('Los valores no forman un triángulo')
    
    def validar_triangulo (self, a, b, c):
        if (b - c < a < b + c and a - c < b < a + c and b - a < c < b + a):
            return True
        else:
            return False

    def nuevo (self):
        self.txtA.setText("")
        self.txtB.setText("")
        self.txtC.setText("")
        self.txtR.setPlainText("")
    
    def imprimir (self, m):
        self.txtR.insertPlainText(m + '\n')
if __name__=="__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
