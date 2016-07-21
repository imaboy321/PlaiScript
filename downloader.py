#Modules
import urllib, __main__,os,sys
from time import sleep



#Variables
pages = []
selection = ""
dowloader_select_text = "Which item would you like?"

#Functions
def page_list():
    page_text = open(__main__.html_pages, "r")
    number = 0
    for item in page_text:
        pages.append(item.strip("\n"))

def download(page):
    stripped_link = page.strip("\n")
    urllib.urlretrieve(stripped_link, (__main__.html_directory + "/" +
                                       stripped_link.strip("https://github.com/Plailect/Guide/wiki/Part-") + ".html"))
    print "downloaded", stripped_link.strip("https://github.com/Plailect/Guide/wiki/Part-")

def get_all_pages():
    page_text = open(__main__.html_pages,'r')
    for link in page_text:
        download(link)
    print "Done!"

def get_page():
    global selection
    for item in range(len(pages)):
        print "["+str(number+1)+"]",pages[number]
        number += 1
    try:
        global selection
        selection = int(raw_input("Which page would you like?\n"))
    except:
        print "Not a number!"
        sleep(2)
        __main__.restart()
    selection -= 1
    download(pages[selection])

def dl_chkdir():
    try:
        os.stat(__main__.html_directory+"/"+str(__main__.current_date))
        print "Already Here"
    except:
        os.mkdir(__main__.html_directory+"/"+str(__main__.current_date))
        print "Created"
