#########
#Modules#
#########

import file_management
import html_parsing
import os
import sys
import time

from PyQt4 import QtCore, QtGui
from gui.gui_main import Ui_Dialog
from gui.parsed import Ui_ParseWindow
from gui.select import Ui_MainWindow

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

#################
#Main gui Window#
#################

class Dialog(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.btnDownload.clicked.connect(self.btnDownload_clicked)
        self.ui.btnCleanup.clicked.connect(self.btnCleanup)
        self.ui.btnGuide.clicked.connect(self.btnGuide_parse)
        self.ui.btnExit.clicked.connect(self.btnExit)

    def btnDownload_clicked(self):
        global Main_Select, down_or_parse
        if self.ui.chkAll.checkState() == 0:
            print 'btnDownload'
            main_gui.hide()
            down_or_parse = 1
            Main_Select = 'Which would you like to download?'
            select.ui.txtHTML.setText(Main_Select)
            select.show()
        elif self.ui.chkAll.checkState() == 2:
            print 'btnDownload -All'
            self.ui.txtUpdateCheck.setText(file_management.get_all_pages())

    def btnGuide_parse(self):
        print 'btnGuide'
        global Main_Select, down_or_parse
        main_gui.hide()
        down_or_parse = 2
        Main_Select = 'Which would you like to view?'
        select.ui.txtHTML.setText(Main_Select)
        select.show()

    def btnCleanup(self):
        print 'btnCleanup'
        file_management.cleanup()

    def btnExit(self):
        print 'btnExit'
        sys.exit()

##################
#Selection Window#
##################

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnSelectDone.clicked.connect(self.btnSelectDone)
        self.ui.btnSelectExit.clicked.connect(self.btnSelectExit)

    def btnSelectDone(self):
        print 'btnSelectDone'
        if down_or_parse == 1:
            self.btnSelectDownload()
        elif down_or_parse == 2:
            self.btnSelectParse()

    def btnSelectDownload(self):
        print 'btnSelectDone -Download'
        file_management.page_list()

        if self.ui.rdoHomebrew.isChecked():
            self.btnSelectDownload_downloading(file_management.pages[0])

        elif self.ui.rdoDowngrade92.isChecked():
            self.btnSelectDownload_downloading(file_management.pages[1])

        elif self.ui.rdoRedNAND.isChecked():
            self.btnSelectDownload_downloading(file_management.pages[2])

        elif self.ui.rdoDowngrade21.isChecked():
            self.btnSelectDownload_downloading(file_management.pages[3])

        elif self.ui.rdoArm9loaderhax.isChecked():
            self.btnSelectDownload_downloading(file_management.pages[4])
        else:
            pass

    def btnSelectDownload_downloading(self, page): #downloading and setting of txtHTML
        text = file_management.download(page)
        self.ui.txtHTML.setText(text)

    def btnSelectExit(self):
        print 'btnSelectExit'
        select.hide()
        main_gui.show()

    def btnSelectParse(self):
        print 'btnSelectParse'
        html_parsing.steps_removed_stripped = []
        html_parsing.html_file_list()
        if self.ui.rdoHomebrew.isChecked():
            html_parsing.parse(html_parsing.links[0])
            parsed.setWindowTitle(_translate("1: Homebrew", "1: Homebrew", None))

        elif self.ui.rdoDowngrade92.isChecked():
            html_parsing.parse(html_parsing.links[1])
            parsed.setWindowTitle(_translate("2: 9.2 Downgrade", "2: 9.2 Downgrade", None))

        elif self.ui.rdoRedNAND.isChecked():
            html_parsing.parse(html_parsing.links[2])
            parsed.setWindowTitle(_translate("3: RedNAND", "3: RedNAND", None))

        elif self.ui.rdoDowngrade21.isChecked():
            html_parsing.parse(html_parsing.links[3])
            parsed.setWindowTitle(_translate("4: 2.1 Downgrade", "4: 2.1 Downgrade", None))

        elif self.ui.rdoArm9loaderhax.isChecked():
            html_parsing.parse(html_parsing.links[4])
            parsed.setWindowTitle(_translate("5: arm9loaderhax", "5: arm9loaderhax", None))

        else:
            pass

        parsed.ui.txtParsed.setText(html_parsing.steps_removed[0])
        parsed.ui.txtPageOf.setText('1')
        parsed.ui.txtPageMax.setText(str(len(html_parsing.steps_removed)-1))
        parsed.number = 0
        select.hide()
        parsed.show()

###############
#Parsed Window#
###############

class ParsedWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_ParseWindow()
        self.ui.setupUi(self)
        self.ui.btnParsedExit.clicked.connect(self.btnParsedExit)
        self.ui.btnParsedNext.clicked.connect(self.btnParsedNext)
        self.ui.btnParsePrevious.clicked.connect(self.btnParsedPrevious)
        self.number = 0

    def btnParsedExit(self):
        print 'btnParsedExit'
        self.ui.txtPageOf.setText('')
        self.ui.txtPageMax.setText('')
        parsed.hide()
        select.show()

    def btnParsedNext(self):
        print 'btnParsedNext'
        if self.number+1 < len(html_parsing.steps_removed)-1:
            self.number += 1
            print self.number
            self.ui.txtParsed.setText(html_parsing.steps_removed[self.number])
            self.ui.txtPageOf.setText(str(self.number+1))
        else:
            print "Above len(html_parsing.steps_removed)"

    def btnParsedPrevious(self):
        print 'btnParsedPrevious'
        if self.number-1 >= 0:
            self.number-=1
            print self.number
            self.ui.txtParsed.setText(html_parsing.steps_removed[self.number])
            self.ui.txtPageOf.setText(str(self.number+1))
        else:
            print 'Below 0'

################
#Base Variables#
################

version = ['Version = 1.0', 'First Release!']
html_directory = "Resources/"
html_pages = html_directory+"/pages.txt"
down_or_parse = 0
update_check = ''
fox_icon = 'Resources/Fox.ico'

###########
#Functions#
###########

def date_check(): #Returns True if same as last checked and False if different
    global last_checked_read, update_check
    current_date = time.localtime()
    current_date = [current_date[0], current_date[1], current_date[2]]
    try:
        last_checked = open(html_directory+'last_checked.txt', 'r+')
        print "last_check exists"
        try:
            last_checked = [int(x) for x in ((last_checked.read()).strip("[]")).split(",")]
            print 'last_checked setup'
        except ValueError:
            print 'No former date'
            last_checked = ['Never', 'Never', 'Never']
        if current_date == last_checked:
            update_check = "Last check was today! {0}-{1}-{2}".format(last_checked[1],
                                                             last_checked[2],
                                                             last_checked[0])
            print 'Last check = Today'
        else:
            update_check = "Last check {0}-{1}-{2}".format(last_checked[1], last_checked[2], last_checked[0])
            last_checked = open(html_directory+'last_checked.txt', 'r+')
            print 'File Reopened'
            last_checked.write(str(current_date))
            print 'File Written To'
            last_checked.close()
            print 'File Closed'
    except IOError:
        print 'last_checked does not exist'
        last_checked = open(html_directory+'last_checked.txt', 'w+')
        print 'File created'
        last_checked.write(str(current_date))
        print 'File written to'
        last_checked.close()
        print 'File Closed'

def dl_chkdir():
    try:
        os.stat(html_directory)
        print 'Directory Exists'
    except:
        os.mkdir(html_directory)
        print 'Directory does not exist, created.'
    finally:
        return file_management.check_resources()

def set_main_gui_up():
    global main_gui
    if dl_chkdir() == 1:
        main_gui = Dialog()
        date_check()
        main_gui.ui.txtUpdateCheck.setText('Thanks for downloading!')
    else:
        main_gui = Dialog()
        date_check()
        main_gui.ui.txtUpdateCheck.setText(update_check)

def set_ver():
    global main_gui
    main_gui.ui.txtVersionName.setText('<p style="text-align: center;">{0}</p>'.format(version[1]))
    main_gui.ui.txtVersionNumber.setText('<p style="text-align: center;">{0}</p>'.format(version[0]))

def set_icons(): #Sets Icons from outside their respective files, since it gets reset with every change.
    global main_gui, select, parsed
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(_fromUtf8(fox_icon)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    main_gui.setWindowIcon(icon)
    select.setWindowIcon(icon)
    parsed.setWindowIcon(icon)


############
#   Main   #
############

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    set_main_gui_up()
    select = MainWindow()
    parsed = ParsedWindow()
    set_ver()
    set_icons()
    main_gui.show()
    sys.exit(app.exec_())