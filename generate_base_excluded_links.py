#########
#Imports#
#########

import os
import sys

from time import sleep

from bs4 import BeautifulSoup, SoupStrainer

################
#Base Variables#
################
pages = ['Part-1-(Homebrew).html',
         'Part-2-(9.2.0-Downgrade).html',
         'Part-3-(RedNAND).html',
         'Part-4-(2.1.0-Downgrade).html',
         'Part-5-(arm9loaderhax).html',
         'DSiWare-Downgrade.html']

links_removed = ''
links_excluded = []

###########
#Functions#
###########

def get_excluded_pages():
    global links_removed
    check_excluded_exists()
    text = open('Resources/excluded_links.txt', 'r').read()
    links_removed = text
    for item in text.split('\n'):
        links_excluded.append(item.strip('\n'))

def get_page_links(html_page):
    print 'Link get start {}'.format(html_page)
    links = []
    link_page = open('Resources/'+html_page, 'r')
    link_page = BeautifulSoup(link_page, 'lxml')
    for item in link_page.find_all('a', href=True):
        links.append(str(item['href']))
    return links

def add_to_excluded_links():
    global links_removed
    links_excluded_temp = links_excluded
    for page in pages:
        for link in get_page_links(page):
            if link[:4] == 'http':
                if link not in links_excluded and link not in links_excluded_temp:
                    links_removed += link+'\n'
                    links_excluded_temp.append(link)
                    print link+'\n'
                else:
                    print 'Already here'

def check_excluded_exists():
    try:
        open('Resources/excluded_links.txt', 'r')
    except IOError:
        open('Resources/excluded_links.txt', 'w+')
##########
#  Main  #
##########

if __name__ == '__main__':
    get_excluded_pages()
    l1 = len(links_removed.split('\n'))
    add_to_excluded_links()
    l2 = len(links_removed.split('\n'))
    print 'Before:',l1, 'After:', l2

    text = open('Resources/excluded_links.txt', "w+")
    text.write(links_removed)