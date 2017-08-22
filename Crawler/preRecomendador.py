'''
Módulo responsável pela pré-recomendação (aquisição e preparação dos dados)
'''

import googleAPI
import crawler

def get_itens(termoBusca, chaveAPI, pesquisaID):

    itens = googleAPI.googleSearch(termoBusca, chaveAPI, pesquisaID)

    for item in itens:
        print(".", end="", flush=True)
        result_text = crawler.get_content(item.get('link'), item.get('tipo'))
        if type(result_text) in {list}:
            item['termos'] = result_text

    return itens