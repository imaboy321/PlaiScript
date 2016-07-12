#Imports
import sys, os, urllib, htmllib, time
from sys import exit
#Base Variables
version = "0.0.1"
versionName = "The Simple One"
html_directory = "HTML"
html_directory_files = []
python = sys.executable
current_date = time.localtime()
current_date = str([current_date[0], current_date[1],current_date[2]])
guide = "guide.py"
#Definitions
def get_all_pages():
    page_text = open(html_directory+"/pages.txt",'r')
    for link in page_text:
        stripped_link = link.strip("\n")
        urllib.urlretrieve(stripped_link, (html_directory+"/"+stripped_link.strip("https://github.com/Plailect/Guide/wiki/Part-")+".html"))
        print "downloaded",stripped_link.strip("https://github.com/Plailect/Guide/wiki/Part-")
    urllib.urlretrieve("https://github.com/Plailect/Guide/wiki", html_directory + "/home_page.html") #Home Page

def list_html():
    for html_file in os.listdir(html_directory):
        html_directory_files.append(html_file)

def cleanup():
    for cleanup_html in os.listdir(html_directory):
        if cleanup_html != "pages.txt":
            if cleanup_html != "last_checked.txt":
                os.remove(html_directory+"/"+cleanup_html)
                print "Deleted ", cleanup_html
        else:
            pass

def date_check():
    list_html()
    if "last_checked.txt" in html_directory_files:
        pass
    else:
        last_checked = open(html_directory+"/last_checked.txt", 'w+')
    last_checked = open(html_directory+"/last_checked.txt", 'r')
    last_checked_read = last_checked.read()
    if current_date == last_checked_read:
        return False
    else:
        last_checked = open(html_directory+"/last_checked.txt", 'w')
        last_checked.write(current_date)
        return True
    last_checked.close()

def html_update_check():
    update_check_result = date_check()
    if update_check_result == True:
        print "Probably needs an update!"
        update_date_file = open(html_directory+"/last_checked.txt", 'w')
        update_date_file.write(str(current_date))
    elif update_check_result == False:
        print "Last check today!"


def restart():
    os.execl(python, python, * sys.argv)
#Main
html_update_check()
main_selection = raw_input("Version: "+ version + " " + versionName+"\nSelection:\n 1. Download all html files \n 2. Cleanup Files \n Anything else to exit\n")
try:
    main_selection = int(main_selection)
except:
    exit()
if main_selection == 1:
    get_all_pages()
elif main_selection == 2:
    cleanup()
elif main_selection == 3:
    os.execl(guide, "")
else:
    sys.exit()
restart()