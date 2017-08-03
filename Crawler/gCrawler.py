from urllib.parse import unquote
import re

import crawler

def search_links(busca: str):
    """
Faz buscas no Google
    :param busca: Termo a ser buscado
    :return: Lista de tuplas para cada página: (Título, Link, Resumo)
    """
    url = 'https://www.google.com.br/search?q=%(q)s'
    busca = {
        'q': busca,
    }

    # print("URL da busca: " + (url % busca) + "\n")

    soup = crawler.make_soup(url % busca)
    titulo = [title for title in soup.find_all('h3')]

    i = 0

    resultado = []

    for t in titulo:
        i += 1

        # print("Resultado " + str(i) + ":")

        titulo = t.text

        # print("Título:\t" + str(t.text))

        link = t.find_next('a', href=True)['href']
        link = str(str(link).replace("/url?q=", "").rsplit("&sa=")[0])
        if link[0] == '/':
            link = "http://www.google.com.br" + link
        # print("Link:\t" + unquote(link, encoding='utf-8', errors='replace'))

        link = unquote(link, encoding='utf-8', errors='replace')

        # print("Resumo:\t" + str(t.find_next('span', class_='st').text))

        resumo = str(t.find_next('span', class_='st').text)
        # print()

        resultado.append((titulo, link, resumo))

    return resultado

def get_content(url: str):
    """
Obtem uma lista de termos da página
    :param url: URL da página para se obter uma lista de termos
    :return: Lista de termos da página
    """

    if url.endswith(".pdf"):
        return "Página é um PDF"
    try:
        soup = crawler.make_soup(url)
    except:
        return -1

    for script in soup.find_all(['script', 'style']):
        script.extract()

    retorno = soup.get_text().replace("\n", "\t").replace("\t", " ").replace(u"\xa0", u" ")
    retorno = re.sub(" +", " ", retorno).strip()

    return retorno.split(" ")