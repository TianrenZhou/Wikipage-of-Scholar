from parsel import Selector
from Request import Request
from eduBack import EduBack
import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)

from helper.crawlerHelper import findNum

class DBLP(Request):
    def __init__(self, url) -> None:
        super().__init__(url)
        sel = Selector(text=self.response.text)
        self.affiliation = sel.xpath("/html/body/div[2]/div[5]/div[1]/div/ul/li[1]/span/text()").getall()[0].split(',')[0]
        self.collaboration = sel.xpath("//div[@class='person']/a/text()").getall()
        university = sel.xpath("//div[@class='hide-body']/ul/li/span/text()").getall()[-1].split(',')[0]
        txt = sel.xpath("//div[@class='hide-body']/ul/li/em/text()").getall()[-1]
        idx = findNum(txt)
        year = int(txt[idx:idx+4])
        degree = txt.split(' ')[1].split('(')[1]
        self.edu = EduBack(university,year,degree)