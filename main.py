#Imports

import sys, os, time, downloader, html_parsing
from time import sleep




#PyQT Setup
from PyQt4 import QtCore, QtGui

from gui_main import Ui_Dialog
from select import Ui_MainWindow

#Main GUI Window

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
            downloader.get_all_pages()

    def btnGuide_parse(self):
        global Main_Select, down_or_parse
        main_gui.hide()
        down_or_parse = 2
        Main_Select = 'Which would you like to parse?'
        select.ui.txtHTML.setText(Main_Select)
        select.show()



#Selection Window

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
            downloader.download(downloader.pages[0])

        elif self.ui.rdoDowngrade92.isChecked():
            downloader.download(downloader.pages[1])

        elif self.ui.rdoRedNAND.isChecked():
            downloader.download(downloader.pages[2])

        elif self.ui.rdoDowngrade21.isChecked():
            downloader.download(downloader.pages[3])

        elif self.ui.rdoArm9loaderhax.isChecked():
            downloader.download(downloader.pages[4])
        else:
            pass

    def btnSelectExit(self):
        select.hide()
        main_gui.show()

    def btnSelectParse(self):
        html_parsing.html_file_list()

        if self.ui.rdoHomebrew.isChecked():
            html_parsing.main(html_parsing.links[0])

        elif self.ui.rdoDowngrade92.isChecked():
            html_parsing.main(html_parsing.links[1])

        elif self.ui.rdoRedNAND.isChecked():
            html_parsing.main(html_parsing.links[2])

        elif self.ui.rdoDowngrade21.isChecked():
            html_parsing.main(html_parsing.links[3])

        elif self.ui.rdoArm9loaderhax.isChecked():
            html_parsing.main(html_parsing.links[4])

        else:
            pass

#Base Variables

version = "0.1"
versionName = "Oh look a GUI!"
html_directory = "html"
html_pages = html_directory+"/pages.txt"
html_directory_files = []
python = sys.executable
current_date = time.localtime()
current_date = [current_date[0], current_date[1], current_date[2]]
last_checked_read = ""
down_or_parse = 0

#Functions

def list_html():
    for html_file in os.listdir(html_directory):
        html_directory_files.append(html_file)

def cleanup():
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
                print "Deleted ", cleanup_html
        else:
            pass

def date_check():
    #Returns True if same as last checked and False if different
    global last_checked_read
    list_html()
    if "last_checked.txt" in html_directory_files:
        pass
    else:
        last_checked = open(html_directory+"/last_checked.txt", 'w+')
    last_checked = open(html_directory+"/last_checked.txt", 'r')
    try:
        last_checked_read = [int(x) for x in ((last_checked.read()).strip("[]")).split(",")]
    except ValueError:
        last_checked_read = ["Never", "Never", "Never"]
    if current_date == last_checked_read:
        return True
    else:
        last_checked = open(html_directory+"/last_checked.txt", 'w')
        last_checked.write(str(current_date))
        return False
    last_checked.close()

def html_update_check():
    global last_checked_read
    update_check_result = date_check()
    if update_check_result == False:
        print "Last check {0}-{1}-{2}".format(last_checked_read[1], last_checked_read[2], last_checked_read[0])
        update_date_file = open(html_directory+"/last_checked.txt", 'w')
        update_date_file.write(str(current_date))
    elif update_check_result == True:
        print "Last check was today! {0}-{1}-{2}".format(last_checked_read[1], last_checked_read[2], last_checked_read[0])

def restart():
    os.execl(python, python, * sys.argv)

def select_download():
    try:
        download_select = int(raw_input("\nWhich would you like to download?\n"
                                    "  1. All\n"
                                    "  2. Single File\n"))
    except:
        print "Not a selection!"
        restart()
    if download_select == 1:
        downloader.get_all_pages()
    elif download_select == 2:
        downloader.get_page()
    else:
        print "Not a selection!"
        restart()

def update_check():
    html_update_check()
    print "Version: " + version + " " + versionName

def dl_chkdir():
    try:
        os.stat(html_directory)
    except:
        os.mkdir(html_directory)
        downloader.get_pages()



#Main
def main():
    update_check()
    while True:
        main_selection = raw_input(" \nSelection:\n" +
                                   "   1. Download html files \n   2. Cleanup Files \n"
                                   "   3. Start Guide \n   Anything else to exit.\n")
        try:
            main_selection = int(main_selection)
        except:
            print "Exiting..."
            break
        if main_selection == 1:
            select_download()
        elif main_selection == 2:
            cleanup()
        elif main_selection == 3:
            guide.main()
        elif main_selection == 4:
            downloader.main()
        else:
            print "Exiting..."
            sleep(2)
            sys.exit()




if __name__ == '__main__':
    dl_chkdir()
    update_check()
    app = QtGui.QApplication(sys.argv)
    select = MainWindow()
    main_gui = Dialog()
    main_gui.show()
    sys.exit(app.exec_())
