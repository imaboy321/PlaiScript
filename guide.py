#Imports
import os
import __main__

#Variables

#Functions
def html_file_list():
    for item in os.listdir(__main__.html_directory):
        print item













def main():
    print "This is the guide python file. This serves the purpose of parsing and displaying the guide."
    html_file_list()