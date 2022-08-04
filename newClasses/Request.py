import requests

class Request():
    def __init__(self,url) -> None:
        self.response = requests.get(url)