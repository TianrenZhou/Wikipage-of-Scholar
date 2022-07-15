class EduBack:
    def __init__(self,university,start=None,end=None) -> None:
        self.university = university
        self.start = start if start != None else -1
        self.end = end if end != None else -1