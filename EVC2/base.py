# Form implementation generated from reading ui file 'base.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 81, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 140, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(220, 220, 220);")
        self.label.setObjectName("label")
        self.txtFrase = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txtFrase.setGeometry(QtCore.QRect(250, 140, 501, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.txtFrase.setFont(font)
        self.txtFrase.setObjectName("txtFrase")
        self.txtRPalabras = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.txtRPalabras.setGeometry(QtCore.QRect(60, 310, 191, 181))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtRPalabras.setFont(font)
        self.txtRPalabras.setObjectName("txtRPalabras")
        self.txtRLetras = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.txtRLetras.setGeometry(QtCore.QRect(310, 310, 91, 181))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtRLetras.setFont(font)
        self.txtRLetras.setPlainText("")
        self.txtRLetras.setObjectName("txtRLetras")
        self.txtRVocales = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.txtRVocales.setGeometry(QtCore.QRect(420, 310, 91, 181))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtRVocales.setFont(font)
        self.txtRVocales.setObjectName("txtRVocales")
        self.txtRConsonantes = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.txtRConsonantes.setGeometry(QtCore.QRect(530, 310, 91, 181))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtRConsonantes.setFont(font)
        self.txtRConsonantes.setObjectName("txtRConsonantes")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(310, 270, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(420, 270, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(530, 270, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.btnContar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnContar.setGeometry(QtCore.QRect(350, 190, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btnContar.setFont(font)
        self.btnContar.setObjectName("btnContar")
        self.btnNuevo = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnNuevo.setGeometry(QtCore.QRect(590, 500, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btnNuevo.setFont(font)
        self.btnNuevo.setObjectName("btnNuevo")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        self.label.setText(_translate("MainWindow", "Ingrese una frase:"))
        self.label_2.setText(_translate("MainWindow", "Letras:"))
        self.label_3.setText(_translate("MainWindow", "Vocales:"))
        self.label_4.setText(_translate("MainWindow", "Consonantes:"))
        self.btnContar.setText(_translate("MainWindow", "Contar"))
        self.btnNuevo.setText(_translate("MainWindow", "Nuevo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
