from bs4 import BeautifulSoup
import requests

def make_soup(url):
    r = requests.get(url)
    return BeautifulSoup(r.content, "html.parser")