# Form implementation generated from reading ui file 'contador.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(798, 468)
        MainWindow.setStyleSheet("background-color: rgb(9, 130, 167);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 20, 711, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(220, 0, 0);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 140, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.txtNombre = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txtNombre.setGeometry(QtCore.QRect(250, 130, 391, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.txtNombre.setFont(font)
        self.txtNombre.setStyleSheet("border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"background-color: rgb(11, 232, 225);\n"
"border-color: rgb(255, 0, 0);")
        self.txtNombre.setObjectName("txtNombre")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 240, 140, 25))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(280, 240, 140, 25))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(520, 240, 151, 25))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.txtLetras = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.txtLetras.setGeometry(QtCore.QRect(20, 270, 141, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.txtLetras.setFont(font)
        self.txtLetras.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtLetras.setObjectName("txtLetras")
        self.txtVocales = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.txtVocales.setGeometry(QtCore.QRect(280, 270, 141, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.txtVocales.setFont(font)
        self.txtVocales.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtVocales.setObjectName("txtVocales")
        self.txtConsonantes = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.txtConsonantes.setGeometry(QtCore.QRect(520, 270, 141, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.txtConsonantes.setFont(font)
        self.txtConsonantes.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtConsonantes.setObjectName("txtConsonantes")
        self.btnContar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnContar.setGeometry(QtCore.QRect(380, 190, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnContar.setFont(font)
        self.btnContar.setStyleSheet("background-color: rgb(148, 148, 148);\n"
"color: rgb(255, 255, 255);")
        self.btnContar.setObjectName("btnContar")
        self.btnBorrar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnBorrar.setGeometry(QtCore.QRect(650, 370, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnBorrar.setFont(font)
        self.btnBorrar.setStyleSheet("background-color: rgb(121, 121, 121);\n"
"color: rgb(255, 255, 255);")
        self.btnBorrar.setObjectName("btnBorrar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 21))
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
        self.label.setText(_translate("MainWindow", "Contador de Letras, Vocales y Consonantes"))
        self.label_2.setText(_translate("MainWindow", "Ingrese un nombre: "))
        self.label_3.setText(_translate("MainWindow", "Letras:"))
        self.label_4.setText(_translate("MainWindow", "Vocales:"))
        self.label_5.setText(_translate("MainWindow", "Consonantes:"))
        self.btnContar.setText(_translate("MainWindow", "Contar"))
        self.btnBorrar.setText(_translate("MainWindow", "Borrar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
