from urllib.parse import unquote
import re
import utils
import requests

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

    soup = utils.make_soup(url % busca)
    titulo = [title for title in soup.find_all('h3')]

    resultado = []

    for t in titulo:

        titulo = ""
        link = ""
        resumo = ""

        try:
            titulo = t.text

            link = t.find_next('a', href=True)['href']
            link = str(str(link).replace("/url?q=", "").rsplit("&sa=")[0])
            if link[0] == '/':
                link = "http://www.google.com.br" + link

            link = unquote(link, encoding='utf-8', errors='replace')

            resumo_tag = t.find_next('span', class_='st')

            if resumo_tag is not None:
                resumo = str(resumo_tag.text)

        finally:
            resultado.append((titulo, link, resumo))

    return resultado


def get_content_html(url: str):
    """
Retorna uma lista de termos de uma página HTML
    :param url: URL da página HTML
    :return: Lista de termos da página HTML
    """
    try:
        soup = utils.make_soup(url)
    except:
        return "Não respondeu"

    for script in soup.find_all(['script', 'style']):
        script.extract()

    retorno = re.findall('[\w-]+', soup.getText(separator=u" "))

    return retorno


def get_content_pdf(url: str):
    """
Obtem uma lista de termos de um documento pdf
    :param url: URL para baixar o pdf
    :return: Lista de termos do documento
    """

    try:
        r = requests.get(url, stream=True)

        nome = url.split('/')[-1]

        with open('./PDFs/' + nome, 'wb') as fd:
            for chunk in r.iter_content(2000):
                fd.write(chunk)
            fd.close()
    except:
        return "Não respondeu"

    texto = utils.pdf2txt('./PDFs/' + nome)

    retorno = re.findall('[\w-]+', texto)

    return retorno


def get_content(url: str):
    """
Obtem uma lista de termos da página
    :param url: URL da página para se obter uma lista de termos
    :return: Lista de termos da página
    """

    if url.endswith(".pdf"):
        return get_content_pdf(url)
    else:
        return get_content_html(url)
