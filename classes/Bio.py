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

class Bio:
    def __init__(self) -> None:
        self.ieee = "/html/body/div[5]/div/div/div/div[3]/div/xpl-root/div/xpl-search-results/xpl-author-profile/div[1]/div[3]/div[1]/div/div[2]/div[2]/span[1]"
        self.txt = None
    def postIEEE(self,soup):
        return soup.text
    def crawl(self,url):
        driver = webdriver.Chrome("/Users/kola/Desktop/Wikipage-of-Scholar/crawler/chromedriver")
        driver.get(url)
        time.sleep(2)
        src = driver.page_source
        sel = Selector(text=src)
        html = sel.xpath(self.ieee).getall()[0]
        soup = BeautifulSoup(html, features="html.parser")
        driver.close()
        self.txt = self.postIEEE(soup)