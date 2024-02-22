from contador import *

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, * args, **kwargs)
        self.setupUi(self)
        
        self.btnContar.clicked.connect(self.contar)
        self.btnBorrar.clicked.connect(self.borrar)
              
    def contar (self):
        nombre = self.txtNombre.text()
        vocales = ['A','E','I','O','U']
        contarv = 0
        consonantes = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
        contarc = 0
        contarl = len(nombre)
        
        for i in nombre.upper():
            if i in vocales:
                contarv += 1
            else:
                continue
            
        for j in nombre.upper():
            if j in consonantes:
                contarc += 1
            else:
                continue
        
        self.imprimir(str(contarv), str(contarl), str(contarc))
            
    def imprimir (self, contarv, contarl ,contarc):
        self.txtVocales.insertPlainText(contarv)
        self.txtLetras.insertPlainText(contarl)
        self.txtConsonantes.insertPlainText(contarc)  
            
    def borrar(self):
        self.txtNombre.setText('')
        self.txtLetras.setPlainText('')
        self.txtVocales.setPlainText('')
        self.txtConsonantes.setPlainText('')
        
if __name__=="__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
