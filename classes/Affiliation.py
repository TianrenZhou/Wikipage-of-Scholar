import requests
from bs4 import BeautifulSoup
from parsel import Selector
import path
import sys
import time
import re
from selenium import webdriver
class Affiliation():
    ##### input xpath 
    # derive acm dblp aff classes from base class affiliation
    # review the idea of oop
    def __init__(self,aff=None,start=None,end=None) -> None:
        self.aff = aff
        self.start = start if start != None else -1
        self.end = end if end != None else -1
        self.ieee = "/html/body/div[5]/div/div/div/div[3]/div/xpl-root/div/xpl-search-results/xpl-author-profile/div[1]/div[3]/div[1]/div/div[2]/div[1]/div[1]/span"
        self.acm = "/html/body/div[1]/div/main/div[1]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/ul/li[1]/a"
        self.dblp = "/html/body/div[2]/div[5]/div[1]/div"

    def postACM(self,soup):
        return (soup.text)
    def postIEEE(self,soup):
        return (soup.text)
    def postDBLP(self,soup):
        text = ((soup.text).split("affiliation"))
        text = text[1:len(text)-1]
        res = []
        for i in text:
            university = (i.split(":"))[1].split(",")[0]
            university = university[1:]
            res.append(university)
        return res[0]
    def crawl(self,url):
        if 'ieee' in url or 'acm' in url:
            xpath = self.ieee if 'ieee' in url else self.acm
            driver = webdriver.Chrome("/Users/kola/Desktop/Wikipage-of-Scholar/crawler/chromedriver")
            driver.get(url)
            time.sleep(2)
            src = driver.page_source
            sel = Selector(text=src)
            html = sel.xpath(xpath).getall()[0]
            soup = BeautifulSoup(html, features="html.parser")
            driver.close()
            if 'ieee' in url:
                self.aff = self.postIEEE(soup)
            else:
                self.aff = self.postACM(soup)
        else:
            response = requests.get(url).text
            sel = Selector(text=response)
            html = sel.xpath(self.dblp).getall()[0]
            soup = BeautifulSoup(html, features="html.parser")
            self.aff = self.postDBLP(soup)
