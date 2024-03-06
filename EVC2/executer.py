from base import *

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, * args, **kwargs)
        self.setupUi(self)

        self.btnContar.clicked.connect(self.contar)
        self.btnNuevo.clicked.connect(self.nuevo)
        
    def contar (self):
        texto = self.txtFrase.text().upper()
        plbrs = texto.split()
        voc = ["A", "E", "I", "O", "U", "Á", "É", "Í", "Ó", "Ú", "Ü"] 
        con = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "Ñ", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
        
        if self.validar_texto(texto):
            
            for palabra in plbrs:
                letras = self.contar_letras(palabra)
                vocales = 0
                consonantes = 0
                for pala in palabra:
                    if pala in voc:
                        vocales+=1
                    elif pala in con:
                        consonantes+=1
                self.imprimir(palabra.lower(), letras, vocales, consonantes)
        else:
            self.imprimirerror("El texto ingresado no es válido") 
    
    def imprimir (self,pal, let, voc, con):
        self.txtRPalabras.insertPlainText(str(f"{pal}\n"))
        self.txtRLetras.insertPlainText(str(f"{let}\n"))
        self.txtRVocales.insertPlainText(str(f"{voc}\n")) 
        self.txtRConsonantes.insertPlainText(str(f"{con}\n"))  

    def nuevo (self):
        self.txtFrase.setText("")
        self.txtRPalabras.setPlainText("")
        self.txtRLetras.setPlainText("")
        self.txtRVocales.setPlainText("") 
        self.txtRConsonantes.setPlainText("")  
    
    def imprimirerror (self, e):
        self.txtFrase.setText("")
        self.txtFrase.insert(e)         
                
    def contar_letras (self, texto):
        if texto.isdigit():
            return 0
        else:
            return len(texto)
    
    def validar_texto (self, texto):
        
        lista = texto.split()
        validar = 0
        for palabra in lista:
            if palabra.isalpha():
                validar += 1
            else:
                validar += 1
        if validar == len(lista):
            return True
        else:
            return False
 
if __name__=="__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
