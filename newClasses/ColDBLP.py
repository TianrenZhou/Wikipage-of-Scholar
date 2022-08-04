from bs4 import BeautifulSoup
from parsel import Selector
from Request import Request

class ColDBLP(Request):
    def __init__(self, url) -> None:
        super().__init__(url)
        soup = BeautifulSoup(self.response.content, features="html.parser")
        res = soup.find_all("div",{"class":"person"})
        out = []
        for i in res:
            out.append(i.get_text())
        self.collaboration = out