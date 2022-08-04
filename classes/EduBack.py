import requests
from bs4 import BeautifulSoup
from parsel import Selector
import path
import sys
import time
import re
from selenium import webdriver

directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)

from helper.crawlerHelper import findNum
class EduBack:
    def __init__(self,university=None,start=None,end=None) -> None:
        self.university = university
        self.start = start if start != None else -1
        self.end = end if end != None else -1
        self.dblp = "/html/body/div[2]/div[5]/div[1]/div"
    def postDBLP(self,soup):
        text = ((soup.text).split("affiliation"))[-1].split(":")
        end = findNum(text[0])
        university = text[1].split(",")[0]
        university = university[1:]
        return university,end
    def crawl(self,url):
        response = requests.get(url).text
        sel = Selector(text=response)
        html = sel.xpath(self.dblp).getall()[0]
        soup = BeautifulSoup(html, features="html.parser")
        uni,end = self.postDBLP(soup)
        self.university = uni
        self.end = end