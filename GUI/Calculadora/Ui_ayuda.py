# Form implementation generated from reading ui file 'c:\Users\aleva\OneDrive - Instituto Politecnico Nacional\Desktop\Documentos\Programing_Python\GUI\Calculadora\ayuda.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ayuda_2(object):
    def setupUi(self, ayuda_2):
        ayuda_2.setObjectName("ayuda_2")
        ayuda_2.resize(408, 307)
        ayuda_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\aleva\\OneDrive - Instituto Politecnico Nacional\\Desktop\\Documentos\\Programing_Python\\GUI\\Calculadora\\../../../../../../Downloads/help.jpeg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        ayuda_2.setWindowIcon(icon)
        ayuda_2.setAnimated(True)
        ayuda_2.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(parent=ayuda_2)
        self.centralwidget.setObjectName("centralwidget")
        self.Help = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.Help.setGeometry(QtCore.QRect(0, 0, 411, 271))
        self.Help.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.OpenHandCursor))
        self.Help.setObjectName("Help")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -20, 451, 351))
        self.label.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.raise_()
        self.Help.raise_()
        ayuda_2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=ayuda_2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 408, 22))
        self.menubar.setObjectName("menubar")
        self.ayuda = QtWidgets.QMenu(parent=self.menubar)
        self.ayuda.setObjectName("ayuda")
        ayuda_2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=ayuda_2)
        self.statusbar.setObjectName("statusbar")
        ayuda_2.setStatusBar(self.statusbar)
        self.menubar.addAction(self.ayuda.menuAction())

        self.retranslateUi(ayuda_2)
        QtCore.QMetaObject.connectSlotsByName(ayuda_2)

    def retranslateUi(self, ayuda_2):
        _translate = QtCore.QCoreApplication.translate
        ayuda_2.setWindowTitle(_translate("ayuda_2", "Help"))
        self.Help.setHtml(_translate("ayuda_2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-style:italic;\">Instrucciones de uso.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-style:italic;\">1. C: Limpia el ultimo termino que digito</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-style:italic;\">2. AC: Limpia la pantalla</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-style:italic;\">3. Para los termino, Sin, Cos y Tan:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-style:italic;\">Estan dados en grados, primero digite el numero y despues selecciones la funcion trigonometrica para que arroje el resultado.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-style:italic;\">4. Para los terminos n!, ln, y sqrt:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-style:italic;\">Coloque primero el numero y despues seleccione la tecla para obtener el resultado</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-style:italic;\">8. La calculadora realiza operaciones en grupos, necesita ejecutar bloque a bloque, ejemplo:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-style:italic;\">11+(3*3-19)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-style:italic;\">=1</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-style:italic;\">ln(1)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-style:italic;\">=0</span></p></body></html>"))
        self.ayuda.setTitle(_translate("ayuda_2", "Help"))