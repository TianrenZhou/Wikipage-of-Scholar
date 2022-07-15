import requests
from bs4 import BeautifulSoup
from parsel import Selector
import path
import time
import sys
from selenium import webdriver
# setting path
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)

import classes.Affiliation as aff

def crawlAffiliationIEEE(url,xpath):
    driver = webdriver.Chrome("/Users/kola/Desktop/Wikipage-of-Scholar/crawler/chromedriver")
    driver.get(url)
    time.sleep(1)
    src = driver.page_source
    sel = Selector(text=src)
    html = sel.xpath(xpath).getall()[0]
    soup = BeautifulSoup(html, features="html.parser")
    driver.close()
    return aff.Affiliation(soup.text)

def crawlFocusIEEE(url,xpath):
    driver = webdriver.Chrome("/Users/kola/Desktop/Wikipage-of-Scholar/crawler/chromedriver")
    driver.get(url)
    time.sleep(1)
    src = driver.page_source
    sel = Selector(text=src)
    html = sel.xpath(xpath).getall()[0]
    soup = BeautifulSoup(html, features="html.parser")
    driver.close()
    return (soup.text).split(',')

def crawlBioIEEE(url,xpath):
    driver = webdriver.Chrome("/Users/kola/Desktop/Wikipage-of-Scholar/crawler/chromedriver")
    driver.get(url)
    time.sleep(1)
    src = driver.page_source
    sel = Selector(text=src)
    html = sel.xpath(xpath).getall()[0]
    soup = BeautifulSoup(html, features="html.parser")
    driver.close()
    return soup.text