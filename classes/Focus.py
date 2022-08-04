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

class Focus:
    def __init__(self) -> None:
        self.lst = None
        self.ieee = "/html/body/div[5]/div/div/div/div[3]/div/xpl-root/div/xpl-search-results/xpl-author-profile/div[1]/div[3]/div[1]/div/div[2]/xpl-author-keywords/div/div[1]"
        self.acm = "/html/body/div[1]/div/main/div[3]/div[1]/div[1]/div/div[2]/div/svg/g"
    def postACM(self,soup):
        res_list = []
        res_list = re.findall('[A-Z][^A-Z]*', soup.text)
        return res_list
    def postIEEE(self,soup):
        return (soup.text).split(',')
    def crawl(self,url):
        xpath = self.ieee if 'ieee' in url else self.acm
        driver = webdriver.Chrome("/Users/kola/Desktop/Wikipage-of-Scholar/crawler/chromedriver")
        driver.get(url)
        time.sleep(2)
        src = driver.page_source
        sel = Selector(text=src)
        html = sel.xpath(xpath).getall()[0]
        soup = BeautifulSoup(html, features="html.parser")
        driver.close()
        self.lst = self.postACM(soup) if 'acm' in url else self.postIEEE(soup)