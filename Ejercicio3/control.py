from contador import *
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, * args, **kwargs)
        self.setupUi(self)
        
        self.btnContar.clicked.connect(self.contar)
        self.btnBorrar.clicked.connect(self.borrar)
    
    def contar (self):
        nombre = self.txtNombre.text().upper()
        voc = ["A", "E", "I", "O", "U", "Á", "É", "Í", "Ó", "Ú", "Ü"]
        vocales = 0
        con = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "Ñ", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
        consonantes = 0

        if self.validar_texto(nombre):
            letras = self.contar_letras(nombre)
            for i in nombre:
                if i in voc:
                    vocales+=1
                elif i in con:
                    consonantes+=1
        
            self.imprimir(letras, vocales, consonantes)
        else:
            self.imprimirerror("El texto ingresado no es válido") 

    def validar_texto (self, texto):
        
        lista = texto.split()
        validar = 0
        for palabra in lista:
            if palabra.isalpha():
                validar += 1
            else:
                validar 
        if validar == len(lista):
            return True
        else:
            return False
        
    def contar_letras (self, texto):
        lista = texto.split()
        suma = 0
        for palabra in lista:
            suma += len(palabra)
        return suma
    
    def borrar (self):
        self.txtNombre.setText("")
        self.txtLetras.setPlainText("")
        self.txtVocales.setPlainText("")
        self.txtConsonantes.setPlainText("")
    
    def imprimir (self, let, voc, con):
        self.txtLetras.insertPlainText(str(let))
        self.txtVocales.insertPlainText(str(voc))
        self.txtConsonantes.insertPlainText(str(con))
    
    def imprimirerror (self, e):
        self.txtNombre.setText("")
        self.txtNombre.insert(e)
        
if __name__=="__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec()