from bs4 import BeautifulSoup
import requests
from urllib.parse import unquote

url = 'https://www.google.com.br/search?q=%(q)s'
busca = {
    'q': input('>> Buscar: '),
}

print("URL da busca: " + (url % busca) + "\n")

r = requests.get(url % busca)
soup = BeautifulSoup(r.content, "html.parser")
titulo = [title for title in soup.find_all('h3')]

i = 0

for t in titulo:
    i += 1

    print("Resultado " + str(i) + ":")

    print("Título:\t" + str(t.text))

    link = t.find_next('a', href=True)
    link = str(str(t.find_next('a', href=True)['href']).replace("/url?q=", "").rsplit("&sa=")[0])
    if link[0] == '/':
        link = "http://www.google.com.br" + link
    print("Link:\t" + unquote(link, encoding='utf-8', errors='replace'))

    print("Resumo:\t" + str(t.find_next('span', class_='st').text))
    print()