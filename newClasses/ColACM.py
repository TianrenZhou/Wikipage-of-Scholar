import Webdriver as wd
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

class ColACM(wd.Webdriver):
    def __init__(self, url) -> None:
        super().__init__(url)
        sel = Selector(text=self.page_src)
        html = sel.xpath("/html/body/div[1]/div/main/div[3]/div[1]/div[4]/div/div/div[2]/div[1]").getall()[0]
        soup = BeautifulSoup(html, features="html.parser")
        res = extractName(soup)
        self.collaboration = res.split('\n')