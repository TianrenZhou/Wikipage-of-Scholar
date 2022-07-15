import path
import sys
# setting path
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)

from crawler.ACMCrawler import crawlAffiliationACM, crawlFocusACM, crawlCollaborationACM
import unittest



class TestACMethods(unittest.TestCase):

    def test_focus_marc(self):
        res = crawlFocusACM("https://dl.acm.org/profile/81502732275","/html/body/div[1]/div/main/div[3]/div[1]/div[1]/div/div[2]/div/svg/g")
        print(res)

    def test_affiliation_marc(self):
       res = crawlAffiliationACM("https://dl.acm.org/profile/81502732275","/html/body/div[1]/div/main/div[1]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/ul/li[1]/a")
       self.assertEqual(res.aff,"University of Illinois Urbana-Champaign")

    def test_focus_david(self):
        res = crawlFocusACM("https://dl.acm.org/profile/81100565162","/html/body/div[1]/div/main/div[3]/div[1]/div[1]/div/div[2]/div/svg/g")
        print(res)

    def test_affiliation_david(self):
       res = crawlAffiliationACM("https://dl.acm.org/profile/81100565162","/html/body/div[1]/div/main/div[1]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/ul/li[1]/a")
       self.assertEqual(res.aff,"University of California, Berkeley")
    
    def test_collaboration_david(self):
        res = crawlCollaborationACM("https://dl.acm.org/profile/81100565162","/html/body/div[1]/div/main/div[3]/div[1]/div[4]/div/div/div[2]/div[1]")
        print(res)
        self.assertEqual(type(res[0]),str)
    
    def test_collaboration_marc(self):
        res = crawlCollaborationACM("https://dl.acm.org/profile/81502732275","/html/body/div[1]/div/main/div[3]/div[1]/div[4]/div/div/div[2]/div[1]")
        print(res)
        self.assertEqual(type(res[0]),str)
if __name__ == '__main__':
    unittest.main()