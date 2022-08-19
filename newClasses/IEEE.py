from parsel import Selector
from newClasses.Webdriver import Webdriver

class IEEE(Webdriver):
    def __init__(self, url) -> None:
        super().__init__(url)
        sel = Selector(text=self.page_src)
        self.affiliation = sel.xpath("/html/body/div[5]/div/div/div/div[3]/div/xpl-root/div/xpl-search-results/xpl-author-profile/div[1]/div[3]/div[1]/div/div[2]/div[1]/div[1]/span/text()").getall()[0]
        self.bio = sel.xpath("/html/body/div[5]/div/div/div/div[3]/div/xpl-root/div/xpl-search-results/xpl-author-profile/div[1]/div[3]/div[1]/div/div[2]/div[2]/span[1]/text()").getall()[0]
        self.focus = sel.xpath("//span[@class='text-base-md-lh']/a/text()").getall()
