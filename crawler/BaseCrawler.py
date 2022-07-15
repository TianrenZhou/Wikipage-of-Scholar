from gettext import find
import re
import requests
from bs4 import BeautifulSoup
from parsel import Selector
import path
import sys
# setting path
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)

import classes.EduBack as edu
import classes.Affiliation as aff
from helper.crawlerHelper import findNum,extractText

def crawlPapers(url,k):
    response = requests.get(url)
    soup = BeautifulSoup(response.content,"html.parser")
    articles = soup.findAll("a",{"class":"gsc_a_at"})
    articles = articles[0:k] if len(articles) > k else articles
    res = []
    for i in articles:
        res.append(i.get_text())
    return res

def crawlAllText(url):
    response = requests.get(url).text
    soup = BeautifulSoup(response,"html.parser")
    return extractText(soup)