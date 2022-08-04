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

class FocusIEEE(Webdriver):
    def __init__(self, url) -> None:
        super().__init__(url)
        sel = Selector(text=self.page_src)
        html = sel.xpath("/html/body/div[5]/div/div/div/div[3]/div/xpl-root/div/xpl-search-results/xpl-author-profile/div[1]/div[3]/div[1]/div/div[2]/xpl-author-keywords/div/div[1]").getall()[0]
        soup = BeautifulSoup(html, features="html.parser")
        self.focus = (soup.text).split(',')