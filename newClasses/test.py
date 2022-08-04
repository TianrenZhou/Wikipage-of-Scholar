from AffiliationACM import AffiliationACM
from AffiliationDBLP import AffiliationDBLP
from AffiliationIEEE import AffiliationIEEE
from BioIEEE import BioIEEE
from ColACM import ColACM
from ColDBLP import ColDBLP
from EduDBLP import EduDBLP
from FocusACM import FocusACM
from FocusIEEE import FocusIEEE
print('----------------------TestAffACM----------------------')
testAff = AffiliationACM("https://dl.acm.org/profile/81100565162")
print(testAff.affiliation)
print('---------------------TestAffDBLP-----------------------')
testAff = AffiliationDBLP("https://dblp.org/pid/c/KCCChang.html")
print(testAff.affiliation)
print('---------------------TestAffIEEE-----------------------')
testAff = AffiliationIEEE("https://ieeexplore.ieee.org/author/37295848200")
print(testAff.affiliation)
print('---------------------TestBio-----------------------')
testBio = BioIEEE("https://ieeexplore.ieee.org/author/37292348800")
print(testBio.bio)
print('---------------------TestCollaborationACM-----------------------')
testCol = ColACM("https://dl.acm.org/profile/81100565162")
print(testCol.collaboration)
print('---------------------TestCollaborationDBLP-----------------------')
testCol = ColDBLP("https://dblp.org/pid/c/KCCChang.html")
print(testCol.collaboration)
print('---------------------TestEduDBLP-----------------------')
testEdu = EduDBLP("https://dblp.org/pid/c/KCCChang.html")
print(testEdu.university,testEdu.endYear)
print('---------------------TestFocusACM-----------------------')
testFocus = FocusACM("https://dl.acm.org/profile/81100565162")
print(testFocus.focus)
print('---------------------TestFocusIEEE-----------------------')
testFocus = FocusIEEE("https://ieeexplore.ieee.org/author/37295848200")
print(testFocus.focus)