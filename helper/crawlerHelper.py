def findNum(str):
    for i in range(len(str)):
        if str[i].isdigit():
            return i
    return -1
def extractText(soup):
    for script in soup(["script", "style"]):
        script.extract()  
    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)
    return text

def extractName(soup):
    for script in soup(["script", "style"]):
        script.extract()  
    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk and "Paper" not in chunk)
    return text