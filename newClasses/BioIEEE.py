import Webdriver as wd
import requests
from bs4 import BeautifulSoup
from parsel import Selector
import path
import sys
import time
import re
from selenium import webdriver
class BioIEEE(wd.Webdriver):
    def __init__(self, url) -> None:
        super().__init__(url)
        sel = Selector(text=self.page_src)
        html = sel.xpath("/html/body/div[5]/div/div/div/div[3]/div/xpl-root/div/xpl-search-results/xpl-author-profile/div[1]/div[3]/div[1]/div/div[2]/div[2]/span[1]").getall()[0]
        soup = BeautifulSoup(html, features="html.parser")
        self.bio = soup.text