def isValid(link):
    if ".gov" in link or ".edu" in link or ".org" in link:
        return True
    return False