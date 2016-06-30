#Imports
import sys, os, urllib, htmllib
#Base Variables
version = "0.0.1"
versionName = "The Simple One"
html_directory = "HTML"
#Definitions
def get_home_page():
    urllib.urlretrieve("https://github.com/Plailect/Guide/wiki", html_directory+"/home_page.html")

def get_all_pages():
    page_text = open(html_directory+"/pages.txt",'r')
    for link in page_text:
        stripped_link = link.strip("\n")
        urllib.urlretrieve(stripped_link, html_directory+"/"+stripped_link.strip("https://github.com/Plailect/Guide/wiki/Part-"+".html"))


#Main
get_all_pages()
for html_file in os.listdir(html_directory):
    print html_file
print version, "\nPress Enter To Exit"
sys.exit()