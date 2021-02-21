import metadata
import requests

'''
    if server have no data from request it returns zero
'''


class search:
    def __init__(self):
        self.baseUrl = "https://api.themoviedb.org/3/"

    def searchQuery(self, query, page=1):
        r = requests.get(f"{self.baseUrl}search/movie?api_key={metadata.apiKey}&language=en-US&query={query}&page={page}")
        if r.status_code == 200:
            return r.json()
        else:
            return 0

    def searchId(self, id):
        r = requests.get(f"{self.baseUrl}movie/{id}?api_key={metadata.apiKey}&language=en-US")
        if r.status_code == 200:
            return r.json()
        else:
            return 0
