from cgi import test
import Affiliation as aff
import Bio as bio
import Collaboration as col
import EduBack as edu
import Focus as fo

print('----------------------TestAffACM----------------------')
testAff = aff.Affiliation()
testAff.crawl("https://dl.acm.org/profile/81100565162")
print(testAff.aff)
print('---------------------TestAffDBLP-----------------------')
testAff.crawl("https://dblp.org/pid/c/KCCChang.html")
print(testAff.aff)
print('---------------------TestAffIEEE-----------------------')
testAff.crawl("https://ieeexplore.ieee.org/author/37295848200")
print(testAff.aff)
print('---------------------TestBio-----------------------')
testBio = bio.Bio()
testBio.crawl("https://ieeexplore.ieee.org/author/37292348800")
print(testBio.txt)
print('---------------------TestCollaborationACM-----------------------')
testCol = col.Collaboration()
testCol.crawl("https://dl.acm.org/profile/81100565162")
print(testCol.lst)
print('---------------------TestCollaborationDBLP-----------------------')
testCol.crawl("https://dblp.org/pid/c/KCCChang.html")
print(testCol.lst)
print('---------------------TestEduDBLP-----------------------')
testEdu = edu.EduBack()
testEdu.crawl("https://dblp.org/pid/c/KCCChang.html")
print(testEdu.university,testEdu.end)
print('---------------------TestFocusACM-----------------------')
testFocus = fo.Focus()
testFocus.crawl("https://dl.acm.org/profile/81100565162")
print(testFocus.lst)
print('---------------------TestFocusIEEE-----------------------')
testFocus.crawl("https://ieeexplore.ieee.org/author/37295848200")
print(testFocus.lst)