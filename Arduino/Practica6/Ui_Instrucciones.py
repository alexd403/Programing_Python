# Form implementation generated from reading ui file 'c:\Users\aleva\OneDrive - Instituto Politecnico Nacional\Desktop\Documentos\Programing_Python\Arduino\Practica6\Instrucciones.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(676, 403)
        self.scrollArea = QtWidgets.QScrollArea(parent=Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(10, 20, 641, 300))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1301, 298))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.label_12.setObjectName("label_12")
        self.verticalLayout.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.label_13.setObjectName("label_13")
        self.verticalLayout.addWidget(self.label_13)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Inicia el juego: Presiona el botón de inicio o el botón de encendido para comenzar una nueva partida."))
        self.label_2.setText(_translate("Dialog", "Observa la secuencia: El juego comenzará mostrando una secuencia de luces y sonidos. Presta atención a la secuencia, ya que tendrás que repetirla exactamente como la veas."))
        self.label_3.setText(_translate("Dialog", "Repite la secuencia: Después de que \"Simon\" muestre la secuencia, toca los botones o colores correspondientes en el mismo orden en que los viste y los escuchaste. Si lo haces correctamente, el juego te mostrará una nueva secuencia más larga."))
        self.label_4.setText(_translate("Dialog", "TextLabel"))
        self.label_5.setText(_translate("Dialog", "TextLabel"))
        self.label_6.setText(_translate("Dialog", "TextLabel"))
        self.label_7.setText(_translate("Dialog", "TextLabel"))
        self.label_8.setText(_translate("Dialog", "TextLabel"))
        self.label_9.setText(_translate("Dialog", "TextLabel"))
        self.label_10.setText(_translate("Dialog", "TextLabel"))
        self.label_11.setText(_translate("Dialog", "TextLabel"))
        self.label_12.setText(_translate("Dialog", "TextLabel"))
        self.label_13.setText(_translate("Dialog", "TextLabel"))
