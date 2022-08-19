class EduBack():
    def __init__(self,university,year,degree) -> None:
        self.university = university
        self.year = year
        self.degree = degree
    
    def printEdu(self):
        print(self.university)
        print(self.year)
        print(self.degree)