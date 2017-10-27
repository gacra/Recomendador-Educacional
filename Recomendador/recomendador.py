from similaridade import Similaridade


def recomendacao(perfilVet: dict, conjItens: list[dict]) -> list[tuple[float, dict]]:
    """
Faz a recomendação dos melhores itens do conjunto, baseado no pefil do usuário
    :param perfilVet: Perfil do usuário: {'termo1Perfil':tf_idf1, 'termo2Perfil':tf_idf2, ...}
    :param conjItens: Conjunto de itens para sererm recomendados: [{'titulo':'...', 'link':'...', 'resumo':'...', 'tipo':'html|pdf|outro', 'tf_idf':{'termo1':tf_idf1, 'termo2':tf_idf2, ...}}, ...]
    :return Lista de tuplas com a silimaridade de cada ítem e o dicionário que o define, ordenado por similaridade: [(similaridade, {'titulo':'...', 'link':'...', 'resumo':'...', 'tipo':'html|pdf|outro'}), ...]
    """
    pass

