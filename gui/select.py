# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PlaiScript_Select.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(228, 213)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Resources/Resources/Fox.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 141, 181))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.rdoHomebrew = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.rdoHomebrew.setObjectName(_fromUtf8("rdoHomebrew"))
        self.verticalLayout.addWidget(self.rdoHomebrew)
        self.rdoDowngrade92 = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.rdoDowngrade92.setObjectName(_fromUtf8("rdoDowngrade92"))
        self.verticalLayout.addWidget(self.rdoDowngrade92)
        self.rdoRedNAND = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.rdoRedNAND.setObjectName(_fromUtf8("rdoRedNAND"))
        self.verticalLayout.addWidget(self.rdoRedNAND)
        self.rdoDowngrade21 = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.rdoDowngrade21.setObjectName(_fromUtf8("rdoDowngrade21"))
        self.verticalLayout.addWidget(self.rdoDowngrade21)
        self.rdoArm9loaderhax = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.rdoArm9loaderhax.setObjectName(_fromUtf8("rdoArm9loaderhax"))
        self.verticalLayout.addWidget(self.rdoArm9loaderhax)
        self.rdoDSiWareDowngrade = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.rdoDSiWareDowngrade.setObjectName(_fromUtf8("rdoDSiWareDowngrade"))
        self.verticalLayout.addWidget(self.rdoDSiWareDowngrade)
        self.txtHTML = QtGui.QLineEdit(self.centralwidget)
        self.txtHTML.setGeometry(QtCore.QRect(10, 10, 211, 20))
        self.txtHTML.setReadOnly(True)
        self.txtHTML.setObjectName(_fromUtf8("txtHTML"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(140, 130, 81, 80))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.btnSelectDone = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.btnSelectDone.setObjectName(_fromUtf8("btnSelectDone"))
        self.verticalLayout_2.addWidget(self.btnSelectDone)
        self.btnSelectExit = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.btnSelectExit.setObjectName(_fromUtf8("btnSelectExit"))
        self.verticalLayout_2.addWidget(self.btnSelectExit)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Selection", None))
        self.rdoHomebrew.setText(_translate("MainWindow", "1. Homebrew", None))
        self.rdoDowngrade92.setText(_translate("MainWindow", "2. 9.2.0 Downgrade", None))
        self.rdoRedNAND.setText(_translate("MainWindow", "3. RedNAND", None))
        self.rdoDowngrade21.setText(_translate("MainWindow", "4. 2.1.0 Downgrade", None))
        self.rdoArm9loaderhax.setText(_translate("MainWindow", "5. arm9loaderhax", None))
        self.rdoDSiWareDowngrade.setText(_translate("MainWindow", "DSiWare Downgrade", None))
        self.btnSelectDone.setText(_translate("MainWindow", "Confirm", None))
        self.btnSelectExit.setText(_translate("MainWindow", "Exit", None))

import PlaiScript_rc
