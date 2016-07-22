#########
#Modules#
#########

import sys, os, time, downloader, html_parsing
from time import sleep

############
#PyQT Setup#
############
from PyQt4 import QtCore, QtGui
from gui.gui_main import Ui_Dialog
from gui.select import Ui_MainWindow
from gui.parsed import Ui_ParseWindow
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
        self.ui.btnCleanup.clicked.connect(cleanup)
        self.ui.btnGuide.clicked.connect(self.btnGuide_parse)
        self.ui.btnExit.clicked.connect(sys.exit)

    def btnDownload_clicked(self):
        global Main_Select, down_or_parse
        if self.ui.chkAll.checkState() == 0:
            main_gui.hide()
            down_or_parse = 1
            Main_Select = 'Which would you like to download?'
            select.ui.txtHTML.setText(Main_Select)
            select.show()
        elif self.ui.chkAll.checkState() == 2:
            self.ui.txtUpdateCheck.setText(downloader.get_all_pages())

    def btnGuide_parse(self):
        global Main_Select, down_or_parse
        main_gui.hide()
        down_or_parse = 2
        Main_Select = 'Which would you like to view?'
        select.ui.txtHTML.setText(Main_Select)
        select.show()

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
        if down_or_parse == 1:
            self.btnSelectDownload()
        elif down_or_parse == 2:
            self.btnSelectParse()

    def btnSelectDownload(self):
        downloader.page_list()

        if self.ui.rdoHomebrew.isChecked():
            self.ui.txtHTML.setText(downloader.download(downloader.pages[0]))

        elif self.ui.rdoDowngrade92.isChecked():
            self.ui.txtHTML.setText(downloader.download(downloader.pages[1]))

        elif self.ui.rdoRedNAND.isChecked():
            self.ui.txtHTML.setText(downloader.download(downloader.pages[2]))

        elif self.ui.rdoDowngrade21.isChecked():
            self.ui.txtHTML.setText(downloader.download(downloader.pages[3]))

        elif self.ui.rdoArm9loaderhax.isChecked():
            self.ui.txtHTML.setText(downloader.download(downloader.pages[4]))
        else:
            pass

    def btnSelectExit(self):
        select.hide()
        main_gui.show()

    def btnSelectParse(self):
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
        parsed.hide()
        select.show()

    def btnParsedNext(self):
        if self.number+1 < len(html_parsing.steps_removed)-1:
            self.number += 1
            self.ui.txtParsed.setText(html_parsing.steps_removed[self.number])
            self.ui.txtPageOf.setText(str(self.number+1))
        else:
            print "Nope"

    def btnParsedPrevious(self):
        if self.number-1 >= 0:
            self.number-=1
            self.ui.txtParsed.setText(html_parsing.steps_removed[self.number])
            self.ui.txtPageOf.setText(str(self.number+1))
        else:
            print "Nope"

################
#Base Variables#
################

version = ['1.0', 'Completely Usable!']
html_directory = "Resources/"
html_pages = html_directory+"/pages.txt"
down_or_parse = 0
update_check = ''

###########
#Functions#
###########

def cleanup(): #Removes most files and folders from html
    for cleanup_html in os.listdir(html_directory):
        if cleanup_html != "pages.txt":
            if cleanup_html != "last_checked.txt":
                try:
                    os.remove(html_directory+"/"+cleanup_html)
                except WindowsError:
                    try:
                        os.rmdir(html_directory+"/"+cleanup_html)
                    except WindowsError:
                        for item in os.listdir(html_directory+"/"+cleanup_html):
                            os.remove(html_directory+"/"+cleanup_html+"/"+item)
                            print "Deleted", item
                        os.rmdir(html_directory+"/"+cleanup_html)
        else:
            pass
    main_gui.ui.txtUpdateCheck.setText("Cleaned!")

def date_check(): #Returns True if same as last checked and False if different
    global last_checked_read, update_check
    current_date = time.localtime()
    current_date = [current_date[0], current_date[1], current_date[2]]
    try:
        last_checked = open(html_directory+'last_checked.txt', 'r+')
        try:
            last_checked = [int(x) for x in ((last_checked.read()).strip("[]")).split(",")]
        except ValueError:
            last_checked = ['Never', 'Never', 'Never']
        if current_date == last_checked:
            update_check = "Last check was today! {0}-{1}-{2}".format(last_checked[1],
                                                             last_checked[2],
                                                             last_checked[0])
        else:
            update_check = "Last check {0}-{1}-{2}".format(last_checked[1], last_checked[2], last_checked[0])
            last_checked = open(html_directory+'last_checked.txt', 'r+')
            last_checked.write(str(current_date))
            last_checked.close()
    except IOError:
        last_checked = open(html_directory+'last_checked.txt', 'w+')
        last_checked.write(str(current_date))
        last_checked.close()

def dl_chkdir():
    try:
        os.stat(html_directory)
    except:
        os.mkdir(html_directory)
    finally:
        downloader.check_resources()


############
#   Main   #
############

if __name__ == '__main__':
    dl_chkdir()
    date_check()
    app = QtGui.QApplication(sys.argv)

    select = MainWindow()
    main_gui = Dialog()
    parsed = ParsedWindow()
    main_gui.ui.txtVersionName.setText(version[1])
    main_gui.ui.txtVersionNumber.setText('Version='+version[0])
    main_gui.ui.txtUpdateCheck.setText(update_check)
    main_gui.show()

    sys.exit(app.exec_())