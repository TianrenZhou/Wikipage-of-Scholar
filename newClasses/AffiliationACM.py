import Webdriver as wd
import requests
from bs4 import BeautifulSoup
from parsel import Selector
import path
import sys
import time
import re
from selenium import webdriver
class AffiliationACM(wd.Webdriver):
    def __init__(self, url) -> None:
        super().__init__(url)
        sel = Selector(text=self.page_src)
        html = sel.xpath("/html/body/div[1]/div/main/div[1]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/ul/li[1]/a").getall()[0]
        soup = BeautifulSoup(html, features="html.parser")
        self.affiliation = soup.text