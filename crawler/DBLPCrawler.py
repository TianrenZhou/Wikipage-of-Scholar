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
from helper.crawlerHelper import findNum

def crawlEdu(url,xpath):
    response = requests.get(url).text
    sel = Selector(text=response)
    html = sel.xpath(xpath).getall()[0]
    soup = BeautifulSoup(html, features="html.parser")
    text = ((soup.text).split("affiliation"))[-1].split(":")
    end = findNum(text[0])
    university = text[1].split(",")[0]
    university = university[1:]
    background = edu.EduBack(university,None,end)
    return background

def crawlAffiliationDBLP(url,xpath):
    response = requests.get(url).text
    sel = Selector(text=response)
    html = sel.xpath(xpath).getall()[0]
    soup = BeautifulSoup(html, features="html.parser")
    text = ((soup.text).split("affiliation"))
    text = text[1:len(text)-1]
    res = []
    for i in text:
        university = (i.split(":"))[1].split(",")[0]
        university = university[1:]
        res.append(aff.Affiliation(university))
    return res

def crawlCollaborationDBLP(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, features="html.parser")
    res = soup.find_all("div",{"class":"person"})
    out = []
    for i in res:
        out.append(i.get_text())
    return out