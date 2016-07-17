#Imports

from bs4 import BeautifulSoup
import os,__main__

#Variables

exludes = ['<h4>','<ul>','</li>','</div>','</ol>','</ul>','</img></br></li>', '<ol>', '<li>',
           '</br></li>','<div class="wiki-body gollum-markdown-content instapaper_body" id="wiki-body">',
           '<div class="markdown-body">']
steps_removed = []

#Main

def main(html_file):
    soup = BeautifulSoup(open(__main__.html_directory+"/"+html_file), "lxml")
    steps = str(soup.find("div", class_="wiki-body gollum-markdown-content instapaper_body"))
    step = steps.split("<li>")
    step = steps.split("\n")

    for item in step:
        if item not in exludes:
            steps_removed.append(item)
        else:
            pass

    for item in steps_removed:
        if item.endswith("</li>"):
            item = item[4:]
            item = item[:-5]
            print item + "\n"
        elif item.endswith("</p>"):
            item = item[3:]
            item = item[:-4]
            print item + "\n"
        elif item.endswith("</h4>"):
            pass
        else:
            print "!!", item, "??\n"