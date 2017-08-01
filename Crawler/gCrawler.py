from urllib.parse import unquote
import crawler


def search_links(busca):
    url = 'https://www.google.com.br/search?q=%(q)s'
    busca = {
        'q': busca,
    }

    #print("URL da busca: " + (url % busca) + "\n")

    soup = crawler.make_soup(url % busca)
    titulo = [title for title in soup.find_all('h3')]

    i = 0

    resultado = []

    for t in titulo:
        i += 1

        #print("Resultado " + str(i) + ":")

        titulo = t.text

        #print("Título:\t" + str(t.text))

        link = t.find_next('a', href=True)
        link = str(str(t.find_next('a', href=True)['href']).replace("/url?q=", "").rsplit("&sa=")[0])
        if link[0] == '/':
            link = "http://www.google.com.br" + link
        #print("Link:\t" + unquote(link, encoding='utf-8', errors='replace'))

        link = unquote(link, encoding='utf-8', errors='replace')

        #print("Resumo:\t" + str(t.find_next('span', class_='st').text))

        resumo = str(t.find_next('span', class_='st').text)
        #print()

        resultado.append((titulo, link, resumo))

    return resultado

def see_result(url):
    soup = crawler.make_soup(url)
    print(soup.text)