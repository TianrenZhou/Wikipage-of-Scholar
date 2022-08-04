import requests
from bs4 import BeautifulSoup
from parsel import Selector
import path
import sys
import time
import re
from selenium import webdriver
class Webdriver():
    def __init__(self,url) -> None:
        driver = webdriver.Chrome("/Users/kola/Desktop/Wikipage-of-Scholar/crawler/chromedriver")
        driver.get(url)
        time.sleep(1)
        self.page_src = driver.page_source
        driver.close()