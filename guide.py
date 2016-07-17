#Imports

import os,__main__, html_parsing
from time import sleep

#Variables

links = []
zero = 0

#Functions

def html_file_list():
    for item in os.listdir(__main__.html_directory):
        if item.endswith(".html"):
            links.append(item)
        else:
            pass

def select_files():
    global zero
    html_file_list()
    for item in links:
        print "[{}]".format(zero+1),item
        zero += 1
    try:
        select = int(raw_input("Selection?\n"))-1
    except:
        print "Not a number!"
        sleep(2)
        __main__.restart()
    html_parsing.main(links[select])

#Main

def main():
    print "This is the guide python file. This serves the purpose of parsing and displaying the guide."
    select_files()