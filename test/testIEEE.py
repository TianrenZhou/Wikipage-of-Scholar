import path
import sys
# setting path
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)

from crawler.IEEECrawler import crawlAffiliationIEEE, crawlFocusIEEE, crawlBioIEEE
import classes.Affiliation as aff
import unittest

class TestIEEEMethods(unittest.TestCase):
    kevin = "https://ieeexplore.ieee.org/author/37292348800"
    marc = "https://ieeexplore.ieee.org/author/37295848200"
    def test_aff_marc(self):
        res = crawlAffiliationIEEE(self.marc,"/html/body/div[5]/div/div/div/div[3]/div/xpl-root/div/xpl-search-results/xpl-author-profile/div[1]/div[3]/div[1]/div/div[2]/div[1]/div[1]/span")
        self.assertEqual(type(res),aff.Affiliation)

    def test_aff_Kevin(self):
        res = crawlAffiliationIEEE(self.kevin,"/html/body/div[5]/div/div/div/div[3]/div/xpl-root/div/xpl-search-results/xpl-author-profile/div[1]/div[3]/div[1]/div/div[2]/div[1]/div[1]/span")
        self.assertEqual(type(res),aff.Affiliation)

    def test_focus_marc(self):
        res = crawlFocusIEEE(self.marc,"/html/body/div[5]/div/div/div/div[3]/div/xpl-root/div/xpl-search-results/xpl-author-profile/div[1]/div[3]/div[1]/div/div[2]/xpl-author-keywords/div/div[1]")
        self.assertEqual(type(res[0]),str)
        print(res)
    
    def test_focus_Kevin(self):
        res = crawlFocusIEEE(self.kevin,"/html/body/div[5]/div/div/div/div[3]/div/xpl-root/div/xpl-search-results/xpl-author-profile/div[1]/div[3]/div[1]/div/div[2]/xpl-author-keywords/div/div[1]")
        self.assertEqual(type(res[0]),str)
        print(res)
    
    def test_bio_Kevin(self):
        res = crawlBioIEEE(self.kevin,"/html/body/div[5]/div/div/div/div[3]/div/xpl-root/div/xpl-search-results/xpl-author-profile/div[1]/div[3]/div[1]/div/div[2]/div[2]/span[1]")
        self.assertEqual(type(res),str)
        print(res)
    
    def test_bio_marc(self):
        res = crawlBioIEEE(self.marc,"/html/body/div[5]/div/div/div/div[3]/div/xpl-root/div/xpl-search-results/xpl-author-profile/div[1]/div[3]/div[1]/div/div[2]/div[2]/span[1]")
        self.assertEqual(type(res),str)
        print(res)
if __name__ == '__main__':
    unittest.main()