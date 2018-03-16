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

def googleSearch(termo_busca):

    service = build("customsearch", "v1", developerKey=chave_api)

    resultado = []

    pageLimit = 2
    startIndex = 1

    busca = termo_busca.value

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
            item['termo_busca'] = termo_busca.name
            resultado.append(item)


    return resultado