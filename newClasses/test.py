from IEEE import IEEE
from DBLP import DBLP
from ACM import ACM

print("------------------------TestACM---------------------------")
acm = ACM("https://dl.acm.org/profile/81100565162")
print(acm.affiliation)
print(acm.collaboration)
print(acm.focus)
print("------------------------TestIEEE--------------------------")
ieee = IEEE("https://ieeexplore.ieee.org/author/37295848200")
print(ieee.affiliation)
print(ieee.bio)
print(ieee.focus)
print("------------------------TestDBLP--------------------------")
dblp = DBLP("https://dblp.org/pid/c/KCCChang.html")
print(dblp.affiliation)
print(dblp.collaboration)
dblp.edu.printEdu()
