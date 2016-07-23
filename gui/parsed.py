# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PlaiScript_Parsed.ui'
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

class Ui_ParseWindow(object):
    def setupUi(self, ParseWindow):
        ParseWindow.setObjectName(_fromUtf8("ParseWindow"))
        ParseWindow.resize(861, 391)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Fox.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ParseWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(ParseWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 330, 160, 71))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnParsePrevious = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btnParsePrevious.setObjectName(_fromUtf8("btnParsePrevious"))
        self.horizontalLayout.addWidget(self.btnParsePrevious)
        self.btnParsedNext = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btnParsedNext.setObjectName(_fromUtf8("btnParsedNext"))
        self.horizontalLayout.addWidget(self.btnParsedNext)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(770, 329, 81, 71))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.btnParsedExit = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.btnParsedExit.setObjectName(_fromUtf8("btnParsedExit"))
        self.horizontalLayout_2.addWidget(self.btnParsedExit)
        self.txtParsed = QtGui.QTextEdit(self.centralwidget)
        self.txtParsed.setGeometry(QtCore.QRect(10, 10, 841, 331))
        self.txtParsed.setReadOnly(True)
        self.txtParsed.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.txtParsed.setObjectName(_fromUtf8("txtParsed"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(180, 330, 166, 80))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.txtPageOf = QtGui.QLineEdit(self.gridLayoutWidget)
        self.txtPageOf.setObjectName(_fromUtf8("txtPageOf"))
        self.gridLayout.addWidget(self.txtPageOf, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.txtPageMax = QtGui.QLineEdit(self.gridLayoutWidget)
        self.txtPageMax.setObjectName(_fromUtf8("txtPageMax"))
        self.gridLayout.addWidget(self.txtPageMax, 0, 3, 1, 1)
        ParseWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ParseWindow)
        QtCore.QMetaObject.connectSlotsByName(ParseWindow)

    def retranslateUi(self, ParseWindow):
        ParseWindow.setWindowTitle(_translate("ParseWindow", "ParseWindow", None))
        self.btnParsePrevious.setText(_translate("ParseWindow", "Previous", None))
        self.btnParsedNext.setText(_translate("ParseWindow", "Next", None))
        self.btnParsedExit.setText(_translate("ParseWindow", "Exit", None))
        self.label.setText(_translate("ParseWindow", "Page:", None))
        self.label_2.setText(_translate("ParseWindow", "of", None))

