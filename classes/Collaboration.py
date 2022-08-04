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

from helper.crawlerHelper import extractName

class Collaboration:
    def __init__(self) -> None:
        self.acm = "/html/body/div[1]/div/main/div[3]/div[1]/div[4]/div/div/div[2]/div[1]"
        self.lst = None
    def postACM(self,soup):
        res = extractName(soup)
        return res.split('\n')
    def postDBLP(self,soup):
        res = soup.find_all("div",{"class":"person"})
        out = []
        for i in res:
            out.append(i.get_text())
        return out
    def crawl(self,url):
        if 'acm' in url:
            driver = webdriver.Chrome("/Users/kola/Desktop/Wikipage-of-Scholar/crawler/chromedriver")
            driver.get(url)
            time.sleep(2)
            src = driver.page_source
            sel = Selector(text=src)
            html = sel.xpath(self.acm).getall()[0]
            soup = BeautifulSoup(html, features="html.parser")
            driver.close()
            self.lst = self.postACM(soup)
        else:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, features="html.parser")
            self.lst = self.postDBLP(soup)