import Webdriver as wd
import requests
from bs4 import BeautifulSoup
from parsel import Selector
import path
import sys
import time
import re
from selenium import webdriver

from newClasses.Webdriver import Webdriver

class FocusACM(Webdriver):
    def __init__(self, url) -> None:
        super().__init__(url)
        sel = Selector(text=self.page_src)
        html = sel.xpath("/html/body/div[1]/div/main/div[3]/div[1]/div[1]/div/div[2]/div/svg/g").getall()[0]
        soup = BeautifulSoup(html, features="html.parser")
        res_list = []
        res_list = re.findall('[A-Z][^A-Z]*', soup.text)
        self.focus = res_list