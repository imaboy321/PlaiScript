#Imports
import sys, os, urllib2
#Base Variables
version = "0.0.1"
versionName = "The Simple One"
html_directory = "HTML"
#Definitions
def get_home_page():
    urllib2.urlopen("https://github.com/Plailect/Guide/wiki")

#Main
get_home_page()
for html_file in os.listdir(html_directory):
    print html_file
print version, "\nPress Enter To Exit"
raw_input()
sys.exit()