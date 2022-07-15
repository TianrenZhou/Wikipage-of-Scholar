class Affiliation:
    def __init__(self,aff,start=None,end=None) -> None:
        self.aff = aff
        self.start = start if start != None else -1
        self.end = end if end != None else -1