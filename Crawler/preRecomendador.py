'''
Módulo responsável pela pré-recomendação (aquisição e preparação dos dados)
'''

import googleAPI
import crawler

def get_itens(termoBusca: str, chaveAPI: str, pesquisaID: str):

    """
A partir de um termo de busca retorna os resultados
    :param termoBusca: Termo da busca
    :param chaveAPI: Chave da API (https://console.developers.google.com)
    :param pesquisaID: Identificador da busca (https://cse.google.com/cse/all)
    :return: Lista de resultados. Cada resultado é um dicionário contendo: Título, Link, Resumo, Tipo (html, pdf, outro) e lista de termos
    """
    itens = googleAPI.googleSearch(termoBusca, chaveAPI, pesquisaID)

    for item in itens:
        print(".", end="", flush=True)
        result_text = crawler.get_content(item.get('link'), item.get('tipo'))
        if type(result_text) in {list} and len(result_text)!=0:
            item['termos'] = result_text
        else:
            itens.remove(item)

    return itens
