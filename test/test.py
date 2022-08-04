import path
import sys
# setting path
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)

from crawler.ACMCrawler import crawlAffiliationACM, crawlFocusACM, crawlCollaborationACM
from crawler.BaseCrawler import crawlAllText, crawlPapers
from crawler.DBLPCrawler import crawlAffiliationDBLP, crawlCollaborationDBLP, crawlEdu
from crawler.IEEECrawler import crawlAffiliationIEEE, crawlBioIEEE, crawlFocusIEEE
print("FocusACM: ----------------------------------------")
res = crawlFocusACM("https://dl.acm.org/profile/81502732275","/html/body/div[1]/div/main/div[3]/div[1]/div[1]/div/div[2]/div/svg/g")
print(res)
# print("AffiliationACM: ----------------------------------------")
# res = crawlAffiliationACM("https://dl.acm.org/profile/81502732275","/html/body/div[1]/div/main/div[1]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/ul/li[1]/a")
# print(res.aff)
# print("CollaborationACM: ----------------------------------------")
# res = crawlCollaborationACM("https://dl.acm.org/profile/81502732275","/html/body/div[1]/div/main/div[3]/div[1]/div[4]/div/div/div[2]/div[1]")
# print(res)
# print("EduDBLP: ----------------------------------------")
# res = crawlEdu("https://dblp.org/pid/l/JimingLiu-1.html","/html/body/div[2]/div[5]/div[1]/div")
# print(res.university,res.end)
# print("AffiliationDBLP: ----------------------------------------")
# res = crawlAffiliationDBLP("https://dblp.org/pid/l/JimingLiu-1.html","/html/body/div[2]/div[5]/div[1]/div")
# print(res)
# print("CollaborationDBLP: ----------------------------------------")
# res = crawlCollaborationDBLP("https://dblp.org/pid/c/KCCChang.html")
# print(res)
# print("GoogleScholar: ----------------------------------------")
# res = crawlPapers("https://scholar.google.com/citations?hl=en&user=HaI6LesAAAAJ",6)
# print(res)
# print("AffiliationIEEE: ----------------------------------------")
marc = "https://ieeexplore.ieee.org/author/37295848200"
# res = crawlAffiliationIEEE(marc,"/html/body/div[5]/div/div/div/div[3]/div/xpl-root/div/xpl-search-results/xpl-author-profile/div[1]/div[3]/div[1]/div/div[2]/div[1]/div[1]/span")
# print(res.aff)
print("FocusIEEE: ----------------------------------------")
res = crawlFocusIEEE(marc,"/html/body/div[5]/div/div/div/div[3]/div/xpl-root/div/xpl-search-results/xpl-author-profile/div[1]/div[3]/div[1]/div/div[2]/xpl-author-keywords/div/div[1]")
print(res)
# print("BioIEEE: ----------------------------------------")
# res = crawlBioIEEE(marc,"/html/body/div[5]/div/div/div/div[3]/div/xpl-root/div/xpl-search-results/xpl-author-profile/div[1]/div[3]/div[1]/div/div[2]/div[2]/span[1]")
# print(res)