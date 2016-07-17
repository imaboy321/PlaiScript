#Imports

import sys, os, time, guide, downloader
from time import sleep

#Base Variables

version = "0.0.1"
versionName = "The Simple One"
html_directory = "html"
html_pages = html_directory+"/pages.txt"
html_directory_files = []
python = sys.executable
current_date = time.localtime()
current_date = str([current_date[0], current_date[1],current_date[2]])

#Functions

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


#Main

def main():
    html_update_check()
    print "Version: " + version + " " + versionName
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
        else:
            print "Exiting..."
            sleep(2)
            sys.exit()




if __name__ == '__main__':
    main()
