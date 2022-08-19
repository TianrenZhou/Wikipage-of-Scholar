import Webdriver as wd
from parsel import Selector

class ACM(wd.Webdriver):
    def __init__(self, url) -> None:
        super().__init__(url)
        sel = Selector(text=self.page_src)
        self.affiliation = sel.xpath("/html/body/div[1]/div/main/div[1]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/ul/li[1]/a/text()").getall()[0]
        self.collaboration = sel.xpath("//div[@class='title']/a/text()").getall()
        self.focus = sel.xpath("/html/body/div[1]/div/main/div[3]/div[1]/div[1]/div/div[2]/div/svg/g/text/text()").getall()