
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QPushButton, QToolButton, QFileDialog


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(354, 233)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 200, 301, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 0, 251, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 311, 71))
        self.label_2.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_2.setObjectName("label_2")
        self.toolButton = QtWidgets.QToolButton(Dialog)
        self.toolButton.setGeometry(QtCore.QRect(10, 210, 16, 16))
        self.toolButton.setObjectName("toolButton")

        ########### file browse is the function ################################
        self.toolButton_2 = QtWidgets.QToolButton(Dialog, clicked = lambda: self.filebrowse())
        self.toolButton_2.setGeometry(QtCore.QRect(280, 120, 21, 22))
        self.toolButton_2.setObjectName("toolButton_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(80, 120, 191, 20))
        self.label_3.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(150, 160, 49, 16))
        self.label_4.setObjectName("label_4")
        #########
        #########
        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    ### Defining file browse function #############
    def filebrowse(self):
        fname = QFileDialog.getOpenFileName(None,'open file', 'D:\\')



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Orientation - Bootstrapped (String) "))
        self.label_2.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:700;\">Note : The dip {and dip direction, in 3D} are bootstrapped </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:700;\">from the file s. This must obey the bootstrapped</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:700;\">distribution file format given in DFN-Related File Formats.</span></p></body></html>"))
        self.toolButton.setText(_translate("Dialog", "?"))
        self.toolButton_2.setText(_translate("Dialog", "..."))
        self.label_3.setText(_translate("Dialog", "Browse the file"))
        self.label_4.setText(_translate("Dialog", "File:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
