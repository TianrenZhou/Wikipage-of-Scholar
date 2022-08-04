import requests
from bs4 import BeautifulSoup
from parsel import Selector
import path
import sys
import time
import re
from selenium import webdriver
# setting path
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)

import classes.EduBack as edu
import classes.Affiliation as aff
from helper.crawlerHelper import extractName

def crawlAffiliationACM(url,xpath):
    driver = webdriver.Chrome("/Users/kola/Desktop/Wikipage-of-Scholar/crawler/chromedriver")
    driver.get(url)
    time.sleep(3)
    src = driver.page_source
    sel = Selector(text=src)
    html = sel.xpath(xpath).getall()[0]
    soup = BeautifulSoup(html, features="html.parser")
    driver.close()
    return aff.Affiliation(soup.text)

def crawlFocusACM(url,xpath):
    driver = webdriver.Chrome("/Users/kola/Desktop/Wikipage-of-Scholar/crawler/chromedriver")
    driver.get(url)
    time.sleep(3)
    src = driver.page_source
    sel = Selector(text=src)
    html = sel.xpath(xpath).getall()[0]
    soup = BeautifulSoup(html, features="html.parser")
    res_list = []
    res_list = re.findall('[A-Z][^A-Z]*', soup.text)
    driver.close()
    return res_list

def crawlCollaborationACM(url,xpath):
    driver = webdriver.Chrome("/Users/kola/Desktop/Wikipage-of-Scholar/crawler/chromedriver")
    driver.get(url)
    time.sleep(3)
    src = driver.page_source
    sel = Selector(text=src)
    html = sel.xpath(xpath).getall()[0]
    soup = BeautifulSoup(html, features="html.parser")
    driver.close()
    res = extractName(soup)
    return res.split('\n')