'''
Módulo da API do Google para busca customizada
'''

import pprint
from googleapiclient.discovery import build

'''
Para instalar a API do Google:
pip install --upgrade google-api-python-client
'''

def googleSearch(busca: str, chaveAPI: str, pesquisaID: str):
    """
Faz uma busca no Google
    :param busca: Termo da busca
    :param chaveAPI: Chave da API (https://console.developers.google.com)
    :param pesquisaID: Identificador da busca (https://cse.google.com/cse/all)
    :return: Lista de resultados. Cada resultado é um dicionário contendo: Título, Link, Resumo e Tipo (html, pdf, outro)
    """
    service = build("customsearch", "v1", developerKey=chaveAPI)

    resultado = []

    pageLimit = 2
    startIndex = 1

    for nPage in range(0, pageLimit):
        res = service.cse().list(
            q=busca,
            cx=pesquisaID,
            fileType='.htm, .html',
            lr="lang_pt",
            start=startIndex
        ).execute()
        #pprint.pprint(res)

        startIndex = res.get("queries").get("nextPage")[0].get("startIndex")

        for item in res.get('items'):

            tipoItem = item.get('fileFormat')
            if tipoItem is None:
                tipoItem = 'html'
            elif tipoItem == 'PDF/Adobe Acrobat':
                tipoItem = 'pdf'
            else:
                tipoTitem = 'outro'

            resultado.append({'titulo':item.get('title'),
                          'link':item.get('link'),
                          'resumo':item.get('snippet').replace(u"\n", "").replace(u"\xa0", ""),
                              'tipo': tipoItem})

    return resultado