#########
#Modules#
#########

import urllib, __main__,os,sys
from time import sleep


################
#Base Variables#
################

pages = []
selection = ""
dowloader_select_text = "Which item would you like?"
pagestxt_url = 'https://RedSoloFox.github.io/pages.txt'
fox_icon_url = 'https://RedSoloFox.github.io/Fox.ico'

###########
#Functions#
###########

def get_pages():
    urllib.urlretrieve(pagestxt_url, __main__.html_directory+'pages.txt')

def page_list():
    page_text = open(__main__.html_pages, "r")
    number = 0
    for item in page_text:
        pages.append(item.strip("\n"))

def download(page):
    stripped_link = page.strip("\n")
    urllib.urlretrieve(stripped_link, (__main__.html_directory + "/" +
                                       stripped_link.strip("https://github.com/Plailect/Guide/wiki/Part-") + ".html"))
    return str('Downloaded '+stripped_link.strip("https://github.com/Plailect/Guide/wiki/Part-"))

def get_all_pages():
    page_text = open(__main__.html_pages,'r')
    for link in page_text:
        download(link)
        print 'Downloaded',link+'!'
    return "Downloaded!"

def check_resources():
    Fox, Pages = 0, 0
    resources = os.listdir(__main__.html_directory)
    if "Fox.ico" not in resources:
        urllib.urlretrieve(fox_icon_url, __main__.html_directory+"Fox.ico")
        Fox = 1
    else:
        pass
    if "pages.txt" not in resources:
        urllib.urlretrieve(pagestxt_url, __main__.html_directory+'pages.txt')
        Pages = 1
    else:
        pass
    print 'All files accounted for, sir!'
    if Fox == 1 and Pages == 1:
        return 1
    else:
        return 0


def cleanup(): #Removes most files and folders from html
    clean_exclude = ['pages.txt','last_checked.txt', 'Fox.ico']
    for cleanup_html in os.listdir(__main__.html_directory):
        if cleanup_html not in clean_exclude:
            try:
                os.remove(__main__.html_directory+"/"+cleanup_html)
                print cleanup_html, 'removed.'
            except WindowsError:
                try:
                    os.rmdir(__main__.html_directory+"/"+cleanup_html)
                    print 'Directory', cleanup_html , 'removed.'
                except WindowsError:
                    for item in os.listdir(__main__.html_directory+"/"+cleanup_html):
                        os.remove(__main__.html_directory+"/"+cleanup_html+"/"+item)
                        print item, 'removed.'
                    os.rmdir(__main__.html_directory+"/"+cleanup_html)
                    print "Directory", cleanup_html , 'removed.'
        else:
            pass
    __main__.main_gui.ui.txtUpdateCheck.setText("Cleaned!")