# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 11:00:51 2021

@author: zlewis
"""

from bs4 import BeautifulSoup
from requests_html import HTMLSession
import re
import sys
import time

def get_google_results(word):
    """
    Returns the number of Google results for a 
    given search string. 
    
    word: str
    """
    
    url='http://www.google.com/search?q='
    address = url + word
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)\
               AppleWebKit/537.36 (KHTML, like Gecko) Cafari/537.36'}
    #Start HTML Session
    session=HTMLSession()
    r=session.get(address, headers=headers)

    #Render address in HTML and get Soup
    r.html.render()
    soup = BeautifulSoup(r.html.html, 'lxml')
    
    #Extract Results
    result = soup.find(id='result-stats')
    num_results = re.search(r'(\d.*)\s', result.contents[0]).group(1)
    print(f"Total Google Results for {word}: {num_results}")
    return num_results
 
if __name__=='__main__':
    
    word_search = sys.argv[1].split(",")
    for word in word_search:
        get_google_results(word)
        time.sleep(10)    





