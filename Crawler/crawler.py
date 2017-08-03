from bs4 import BeautifulSoup
import requests

def make_soup(url: str):
    """
Cria e retorna um objeto soup
    :param url: URL da página
    :return: Objeto soup
    """
    r = requests.get(url, timeout = 5.0)
    return BeautifulSoup(r.content, "html.parser")
