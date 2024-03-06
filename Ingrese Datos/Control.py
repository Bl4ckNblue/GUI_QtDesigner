from datos import *

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, * args, **kwargs)
        self.setupUi(self)
        
        self.btnGuardar.clicked.connect(self.guardar)
        self.btnNuevo.clicked.connect(self.nuevo)
        self.btnLimpiar.clicked.connect(self.limpiar)
 
        self.DatosGuardados = {'Nombre': '', 
                               'Apellido': '', 
                               'Sexo': '', 
                               'Categoria': '', 
                               'Hobbies': ''
                               }
        
    def guardar(self):
        
        nombre = self.txtNombre.text()
        apellido = self.txtApellido.text()
       
        if self.rbtnMale.isChecked():
            sexo = 'Masculino'
        elif self.rbtnFemale.isChecked():
            sexo = 'Femenino'
        else:
            sexo = ''
            
        categoria = self.cbonCategoria.currentText()
        
        hobb = []
        if self.checkFutbol.isChecked():
            hobb.append('Futbol')
        if self.checkVolley.isChecked():
            hobb.append('Volley')
        if self.checkBasket.isChecked():
            hobb.append('Basket')
        if self.checkBailar.isChecked():
            hobb.append('Bailar')
        if self.checkCantar.isChecked():
            hobb.append('Cantar')
        if self.checkCaminar.isChecked():
            hobb.append('Caminar')
        hobbies = ', '.join(hobb)
        
        self.DatosGuardados ['Nombre'] = nombre
        self.DatosGuardados ['Apellido'] = apellido  
        self.DatosGuardados ['Sexo'] = sexo
        self.DatosGuardados ['Categoria'] = categoria  
        self.DatosGuardados ['Hobbies'] = hobbies
        
        self.txtMostrarDatos.appendPlainText('\nAlumno : ')
        for key, value in self.DatosGuardados.items():
            self.txtMostrarDatos.appendPlainText(f"{key} : {value}")
        
    def nuevo (self):
        self.txtNombre.setText('')
        self.txtApellido.setText('')
        self.rbtnMale.setChecked(False)
        self.rbtnFemale.setChecked(False)
        self.cbonCategoria.setCurrentIndex(0)
        self.checkFutbol.setChecked(False)
        self.checkVolley.setChecked(False)
        self.checkBasket.setChecked(False)
        self.checkBailar.setChecked(False)
        self.checkCantar.setChecked(False)
        self.checkCaminar.setChecked(False)
    
    def limpiar (self):
        self.txtMostrarDatos.setPlainText('')
               
if __name__=="__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
