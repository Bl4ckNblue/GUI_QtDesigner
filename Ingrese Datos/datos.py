# Form implementation generated from reading ui file 'datos.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(896, 651)
        MainWindow.setStyleSheet("QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(85, 0, 127, 255), stop:1 rgba(137, 137, 137, 255));}")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 150, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 200, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 250, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 300, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 350, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.rbtnMale = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.rbtnMale.setGeometry(QtCore.QRect(140, 260, 111, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.rbtnMale.setFont(font)
        self.rbtnMale.setStyleSheet("color: rgb(255, 255, 255);")
        self.rbtnMale.setObjectName("rbtnMale")
        self.cbonCategoria = QtWidgets.QComboBox(parent=self.centralwidget)
        self.cbonCategoria.setGeometry(QtCore.QRect(160, 300, 151, 41))
        self.cbonCategoria.setStyleSheet("background-color: rgb(167, 167, 167);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.cbonCategoria.setEditable(False)
        self.cbonCategoria.setObjectName("cbonCategoria")
        self.cbonCategoria.addItem("")
        self.cbonCategoria.addItem("")
        self.cbonCategoria.addItem("")
        self.cbonCategoria.addItem("")
        self.checkFutbol = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkFutbol.setGeometry(QtCore.QRect(150, 360, 101, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkFutbol.setFont(font)
        self.checkFutbol.setObjectName("checkFutbol")
        self.rbtnFemale = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.rbtnFemale.setGeometry(QtCore.QRect(260, 260, 111, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.rbtnFemale.setFont(font)
        self.rbtnFemale.setStyleSheet("color: rgb(255, 255, 255);")
        self.rbtnFemale.setObjectName("rbtnFemale")
        self.txtNombre = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txtNombre.setGeometry(QtCore.QRect(140, 150, 241, 41))
        self.txtNombre.setStyleSheet("background-color: rgb(167, 167, 167);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.txtNombre.setObjectName("txtNombre")
        self.txtApellido = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txtApellido.setGeometry(QtCore.QRect(140, 200, 241, 41))
        self.txtApellido.setStyleSheet("background-color: rgb(167, 167, 167);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.txtApellido.setObjectName("txtApellido")
        self.checkVolley = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkVolley.setGeometry(QtCore.QRect(150, 380, 101, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkVolley.setFont(font)
        self.checkVolley.setObjectName("checkVolley")
        self.checkBailar = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBailar.setGeometry(QtCore.QRect(150, 440, 101, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBailar.setFont(font)
        self.checkBailar.setObjectName("checkBailar")
        self.checkCantar = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkCantar.setGeometry(QtCore.QRect(150, 420, 101, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkCantar.setFont(font)
        self.checkCantar.setObjectName("checkCantar")
        self.checkBasket = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBasket.setGeometry(QtCore.QRect(150, 400, 101, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBasket.setFont(font)
        self.checkBasket.setObjectName("checkBasket")
        self.checkCaminar = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkCaminar.setGeometry(QtCore.QRect(150, 460, 101, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkCaminar.setFont(font)
        self.checkCaminar.setObjectName("checkCaminar")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(190, 30, 421, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.btnGuardar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnGuardar.setGeometry(QtCore.QRect(100, 490, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnGuardar.setFont(font)
        self.btnGuardar.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0.0511364 rgba(110, 23, 154, 255), stop:1 rgba(255, 255, 255, 255));")
        self.btnGuardar.setObjectName("btnGuardar")
        self.btnNuevo = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnNuevo.setGeometry(QtCore.QRect(230, 490, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnNuevo.setFont(font)
        self.btnNuevo.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0.0511364 rgba(110, 23, 154, 255), stop:1 rgba(255, 255, 255, 255));")
        self.btnNuevo.setObjectName("btnNuevo")
        self.txtMostrarDatos = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.txtMostrarDatos.setGeometry(QtCore.QRect(440, 120, 391, 411))
        self.txtMostrarDatos.setStyleSheet("background-color: rgb(167, 167, 167);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.txtMostrarDatos.setObjectName("txtMostrarDatos")
        self.btnLimpiar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnLimpiar.setGeometry(QtCore.QRect(550, 540, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnLimpiar.setFont(font)
        self.btnLimpiar.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0.0511364 rgba(110, 23, 154, 255), stop:1 rgba(255, 255, 255, 255));")
        self.btnLimpiar.setObjectName("btnLimpiar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 896, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Nombre:"))
        self.label_2.setText(_translate("MainWindow", "Apellido:"))
        self.label_3.setText(_translate("MainWindow", "Sexo:"))
        self.label_4.setText(_translate("MainWindow", "Categoria:"))
        self.label_5.setText(_translate("MainWindow", "Hobbies:"))
        self.rbtnMale.setText(_translate("MainWindow", "Masculino"))
        self.cbonCategoria.setCurrentText(_translate("MainWindow", "Elija"))
        self.cbonCategoria.setItemText(0, _translate("MainWindow", "Elija"))
        self.cbonCategoria.setItemText(1, _translate("MainWindow", "Alta"))
        self.cbonCategoria.setItemText(2, _translate("MainWindow", "Media"))
        self.cbonCategoria.setItemText(3, _translate("MainWindow", "Baja"))
        self.checkFutbol.setText(_translate("MainWindow", "Futbol"))
        self.rbtnFemale.setText(_translate("MainWindow", "Femenino"))
        self.checkVolley.setText(_translate("MainWindow", "Volley"))
        self.checkBailar.setText(_translate("MainWindow", "Bailar"))
        self.checkCantar.setText(_translate("MainWindow", "Cantar"))
        self.checkBasket.setText(_translate("MainWindow", "Basket"))
        self.checkCaminar.setText(_translate("MainWindow", "Caminar"))
        self.label_6.setText(_translate("MainWindow", "Ingrese sus Datos"))
        self.btnGuardar.setText(_translate("MainWindow", "Guardar"))
        self.btnNuevo.setText(_translate("MainWindow", "Nuevo"))
        self.btnLimpiar.setText(_translate("MainWindow", "Limpiar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
