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
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.627, y1:0.642, x2:0, y2:0.989, stop:0.0746269 rgba(0, 116, 0, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 30, 271, 91))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 140, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.txtNombre = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txtNombre.setGeometry(QtCore.QRect(180, 150, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtNombre.setFont(font)
        self.txtNombre.setObjectName("txtNombre")
        self.txtLetras = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.txtLetras.setGeometry(QtCore.QRect(60, 320, 191, 141))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtLetras.setFont(font)
        self.txtLetras.setObjectName("txtLetras")
        self.txtVocales = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.txtVocales.setGeometry(QtCore.QRect(310, 320, 191, 141))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtVocales.setFont(font)
        self.txtVocales.setObjectName("txtVocales")
        self.txtConsonantes = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.txtConsonantes.setGeometry(QtCore.QRect(550, 320, 191, 141))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtConsonantes.setFont(font)
        self.txtConsonantes.setObjectName("txtConsonantes")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 260, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(310, 260, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(550, 260, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.btnContar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnContar.setGeometry(QtCore.QRect(260, 210, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnContar.setFont(font)
        self.btnContar.setObjectName("btnContar")
        self.btnBorrar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnBorrar.setGeometry(QtCore.QRect(570, 480, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnBorrar.setFont(font)
        self.btnBorrar.setObjectName("btnBorrar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
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
        self.label.setText(_translate("MainWindow", "EJERCICIO 3"))
        self.label_2.setText(_translate("MainWindow", "NOMBRE :"))
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
