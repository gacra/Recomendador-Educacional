#Classes
import sys
sys.path.append('../Utils')
from item import Item
from similaridade import Similaridade
#Documentação
from typing import List, Tuple

def recomendacao(perfilVet: dict, conjItens: List[Item]) -> List[Tuple[float, dict]]:
    """
Faz a recomendação dos melhores itens do conjunto, baseado no pefil do usuário
    :param perfilVet: Perfil do usuário: {'termo1Perfil':tf_idf1, 'termo2Perfil':tf_idf2, ...}
    :param conjItens: Conjunto de itens para sererm recomendados: [{'titulo':'...', 'link':'...', 'resumo':'...', 'tipo':'html|pdf|outro', 'tf_idf':{'termo1':tf_idf1, 'termo2':tf_idf2, ...}}, ...]
    :return Lista de tuplas com a silimaridade de cada ítem e o dicionário que o define, ordenado por similaridade: [(similaridade, {'titulo':'...', 'link':'...', 'resumo':'...', 'tipo':'html|pdf|outro'}), ...]
    """
    simCalc = Similaridade(perfilVet)
    retorno = []

    for item in conjItens:
        similaridade = simCalc.simCosseno(item.termos)
        retorno.append((similaridade, item.paraDict()))

    retorno.sort(key=lambda tup: tup[0], reverse=True)

    return retorno