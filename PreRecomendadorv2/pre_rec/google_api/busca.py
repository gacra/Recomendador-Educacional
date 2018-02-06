'''
Módulo da API do Google para busca customizada
'''

from googleapiclient.discovery import build
from typing import List

from pre_rec.google_api import chave_api, pesquisa_id

'''
Para instalar a API do Google:
pip install --upgrade google-api-python-client
'''

def googleSearch(busca: str) -> List:
    """
Faz uma busca no Google
    :param busca: Termo da busca
    :param chaveAPI: Chave da API (https://console.developers.google.com)
    :param pesquisaID: Identificador da busca (https://cse.google.com/cse/all)
    :return: Lista de resultados (objetos Item).
    """
    service = build("customsearch", "v1", developerKey=chave_api)

    resultado = []

    pageLimit = 2
    startIndex = 1

    for nPage in range(0, pageLimit):
        res = service.cse().list(
            q=busca,
            cx=pesquisa_id,
            fileType='.htm, .html',
            lr="lang_pt",
            start=startIndex
        ).execute()

        startIndex = res.get("queries").get("nextPage")[0].get("startIndex")

        for item in res.get('items'):

            # tipoItem = item.get('fileFormat')
            # if tipoItem is None:
            #     tipoItem = 'html'
            # elif tipoItem == 'PDF/Adobe Acrobat':
            #     tipoItem = 'pdf'
            # else:
            #     tipoTitem = 'outro'

            resultado.append(item)
            # resultado.append(Item(titulo=item.get('title'), link=item.get('link'),
            #                       resumo=item.get('snippet').replace(u"\n", "").replace(u"\xa0", ""),
            #                       tipo= tipoItem))

    return resultado