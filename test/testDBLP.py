import path
import sys
# setting path
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)

from crawler.DBLPCrawler import crawlAffiliationDBLP, crawlCollaborationDBLP, crawlEdu
import classes.EduBack as edu
import classes.Affiliation as aff
import unittest

class TestDBLPMethods(unittest.TestCase):
    xpath = "/html/body/div[2]/div[5]/div[1]/div"
    def test_Edu_Liu(self):
        res = crawlEdu("https://dblp.org/pid/l/JimingLiu-1.html",self.xpath)
        self.assertEqual(type(res),edu.EduBack)
        self.assertEqual(res.end,1994)

    def test_Edu_Kevin(self):
        res = crawlEdu("https://dblp.org/pid/c/KCCChang.html",self.xpath)
        self.assertEqual(type(res),edu.EduBack)
        self.assertEqual(res.end,2001)

    def test_Aff_Liu(self):
        res = crawlAffiliationDBLP("https://dblp.org/pid/l/JimingLiu-1.html",self.xpath)
        self.assertEqual(type(res[0]),aff.Affiliation)
        self.assertEqual(len(res),2)
    
    def test_Aff_Kevin(self):
        res = crawlAffiliationDBLP("https://dblp.org/pid/c/KCCChang.html",self.xpath)
        self.assertEqual(type(res[0]),aff.Affiliation)
        self.assertEqual(res[0].aff,"University of Illinois at Urbana-Champaign")
    
    def test_col_Kevin(self):
        res = crawlCollaborationDBLP("https://dblp.org/pid/c/KCCChang.html")
        self.assertEqual(len(res),192)
if __name__ == '__main__':
    unittest.main()