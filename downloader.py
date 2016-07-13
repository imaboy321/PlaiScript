#Modules
import urllib, __main__,sys

#Variables
pages = []
selection = ""

#Functions
def download(page):
    stripped_link = page.strip("\n")
    urllib.urlretrieve(stripped_link, (__main__.html_directory + "/" +
                                       stripped_link.strip("https://github.com/Plailect/Guide/wiki/Part-") + ".html"))
    print "downloaded", stripped_link.strip("https://github.com/Plailect/Guide/wiki/Part-")

def get_all_pages():
    page_text = open(__main__.html_pages,'r')
    for link in page_text:
        download(link)

def get_page():
    global selection
    page_text = open(__main__.html_pages,"r")
    number = 0
    for item in page_text:
        pages.append(item.strip("\n"))
    for item in range(len(pages)):
        print "["+str(number+1)+"]",pages[number]
        number += 1
    try:
        global selection
        selection = int(raw_input("Which page would you like?"))
    except:
        print "Not a number!"
        __main__.restart()
    selection -= 1
    download(pages[selection])

