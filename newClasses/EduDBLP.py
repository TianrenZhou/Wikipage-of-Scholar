from bs4 import BeautifulSoup
from parsel import Selector
from Request import Request
import path
import sys

directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)

from helper.crawlerHelper import findNum

class EduDBLP(Request):
    def __init__(self, url) -> None:
        super().__init__(url)
        soup = BeautifulSoup(self.response.content, features="html.parser")
        sel = Selector(text=self.response.text)
        html = sel.xpath("/html/body/div[2]/div[5]/div[1]/div").getall()[0]
        soup = BeautifulSoup(html, features="html.parser")
        text = ((soup.text).split("affiliation"))[-1].split(":")
        end = findNum(text[0])
        university = text[1].split(",")[0]
        university = university[1:]
        self.university = university
        self.endYear = end