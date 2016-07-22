#########
#Imports#
#########

from bs4 import BeautifulSoup
import os,__main__

###########
#Variables#
###########

exludes = ['<h4>','<ul>','</li>','</div>','</ol>','</ul>','</img></br></li>', '<ol>', '<li>',
           '</br></li>','<div class="wiki-body gollum-markdown-content instapaper_body" id="wiki-body">',
           '<div class="markdown-body">',
           '<div class="wiki-footer gollum-markdown-content boxed-group" id="wiki-footer">',
           '<div class="boxed-group-inner wiki-auxiliary-content markdown-body">']
steps_removed = []
links = []

#Functions
def html_file_list():
    global links
    links = []
    for item in os.listdir(__main__.html_directory):
        if item.endswith(".html"):
            links.append(item)
        else:
            pass

#Main

def parse(html_file):
    del steps_removed[:]
    soup = BeautifulSoup(open(__main__.html_directory+"/"+html_file), "lxml")
    steps = str(soup.find("div", class_="wiki-body gollum-markdown-content instapaper_body"))
    step = steps.split("\n")

    for item in step:
        if item not in exludes:
            steps_removed.append(item)
        else:
            pass