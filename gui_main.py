# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PlaiScript_Main.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setEnabled(True)
        Dialog.resize(366, 79)
        Dialog.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        Dialog.setToolTip(_fromUtf8(""))
        Dialog.setWhatsThis(_fromUtf8(""))
        Dialog.setAccessibleName(_fromUtf8(""))
        Dialog.setAccessibleDescription(_fromUtf8(""))
        Dialog.setAutoFillBackground(False)
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 371, 241))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.layoutWidget = QtGui.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 360, 41))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnDownload = QtGui.QPushButton(self.layoutWidget)
        self.btnDownload.setCheckable(False)
        self.btnDownload.setChecked(False)
        self.btnDownload.setObjectName(_fromUtf8("btnDownload"))
        self.horizontalLayout.addWidget(self.btnDownload)
        self.chkAll = QtGui.QCheckBox(self.layoutWidget)
        self.chkAll.setObjectName(_fromUtf8("chkAll"))
        self.horizontalLayout.addWidget(self.chkAll)
        self.btnCleanup = QtGui.QPushButton(self.layoutWidget)
        self.btnCleanup.setEnabled(True)
        self.btnCleanup.setObjectName(_fromUtf8("btnCleanup"))
        self.horizontalLayout.addWidget(self.btnCleanup)
        self.btnGuide = QtGui.QPushButton(self.layoutWidget)
        self.btnGuide.setObjectName(_fromUtf8("btnGuide"))
        self.horizontalLayout.addWidget(self.btnGuide)
        self.btnExit = QtGui.QPushButton(self.layoutWidget)
        self.btnExit.setObjectName(_fromUtf8("btnExit"))
        self.horizontalLayout.addWidget(self.btnExit)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.textBrowser = QtGui.QTextBrowser(self.tab_2)
        self.textBrowser.setGeometry(QtCore.QRect(70, 10, 231, 41))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "PlaiScript", None))
        self.btnDownload.setText(_translate("Dialog", "Download", None))
        self.chkAll.setText(_translate("Dialog", "All", None))
        self.btnCleanup.setText(_translate("Dialog", "Cleanup", None))
        self.btnGuide.setText(_translate("Dialog", "Guide", None))
        self.btnExit.setText(_translate("Dialog", "Exit", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Main", None))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Created by RedSoloFox!</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/RedSoloFox/PlaiScript\"><span style=\" font-size:8pt; text-decoration: underline; color:#0000ff;\">https://github.com/RedSoloFox/PlaiScript</span></a></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Extras", None))

