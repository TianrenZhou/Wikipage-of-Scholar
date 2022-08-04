from bs4 import BeautifulSoup
from parsel import Selector
from Request import Request

class AffiliationDBLP(Request):
    def __init__(self, url) -> None:
        super().__init__(url)
        sel = Selector(text=self.response.text)
        html = sel.xpath("/html/body/div[2]/div[5]/div[1]/div").getall()[0]
        soup = BeautifulSoup(html, features="html.parser")
        text = ((soup.text).split("affiliation"))
        text = text[1:len(text)-1]
        res = []
        for i in text:
            university = (i.split(":"))[1].split(",")[0]
            university = university[1:]
            res.append(university)
        self.affiliation = res[0]