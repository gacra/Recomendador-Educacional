'''
Módulo responsável pela pré-recomendação (aquisição e preparação dos dados)
'''

#Módulos internos usados
import crawler
import perguntas as _perguntas
import pesagem

#Módulos externos usados
import googleAPI

def get_itens(termosBusca: str, chaveAPI: str, pesquisaID: str, arqPerguntas: str):

    """
A partir de um termo de busca retorna os resultados.
    :param termosBusca: Termo da busca
    :param chaveAPI: Chave da API (https://console.developers.google.com)
    :param pesquisaID: Identificador da busca (https://cse.google.com/cse/all)
    :param arqPerguntas: Caminho do arquivo contendo as perguntas
    :return: Lista de resultados. Cada resultado é um dicionário contendo: Título, Link, Resumo, Tipo (html, pdf, outro) e lista de termos
    """
    itens = []
    for termoBusca in termosBusca:
        itens += googleAPI.googleSearch(termoBusca, chaveAPI, pesquisaID)

    for item in itens[:]:
        print(".", end="", flush=True)
        result_text = crawler.get_content(item.link, item.tipo)
        if type(result_text) in {list} and len(result_text)!=0:
            item.termos = result_text
        else:
            itens.remove(item)

    perguntas = _perguntas.get_perguntas(arqPerguntas)

    pesagem.tf_idf(itens, perguntas)

    return itens, perguntas
