#Classes
from rec_edu_utils.item import Item
from rec_edu_utils.pergunta import Pergunta
#Módulos externos
import math
#Documentação
from typing import List

def tf_idf(conj_itens: List[Item], conj_perguntas: List[Pergunta]) -> float:
    """
Calcula o tf_idf de um conjunto de itens
    :param conj_itens: Conjunto de ítens (dicionário com a chave 'termos' sendo a lista de termos do ítem)
    """
    conj_itens_tam = len(conj_itens) + len(conj_perguntas)
    termos_cont = {}

    for item in conj_itens:
        vet_termos = item.termos
        tf_vet = {}
        for termo in vet_termos:
            if tf_vet.get(termo) is None:
                tf_vet[termo] = tf(vet_termos, termo)
                addTermo(termos_cont, termo)
        item.termos = tf_vet

    for pergunta in conj_perguntas:
        vet_termos = pergunta.termosPerg
        tf_vet = {}
        for termo in vet_termos:
            if tf_vet.get(termo) is None:
                tf_vet[termo] = vet_termos.count(termo)
                addTermo(termos_cont, termo)
        pergunta.termosPerg = tf_vet

    for item in conj_itens:
        vet_termos_tf = item.termos
        for termo in vet_termos_tf.keys():
            idf_v = idf(termos_cont, termo, conj_itens_tam)
            vet_termos_tf[termo] *= idf_v

    for pergunta in conj_perguntas:
        vet_termos_tf = pergunta.termosPerg
        for termo in vet_termos_tf.keys():
            idf_v = idf(termos_cont, termo, conj_itens_tam)
            vet_termos_tf[termo] = (vet_termos_tf[termo], idf_v)

def tf(vet_termos: list, termo: str) -> float:
    """
Calcula a parte tf do tf_idf para um termo
    :param vet_termos: Vetor de termos
    :param termo: Termo para o qual se deseja calcular o tf
    :return: Valor do tf
    """
    freq = vet_termos.count(termo)
    if freq > 0:
        tf = 1 + math.log2(freq)
    else:
        tf = 0
    return tf

def idf(termos_cont: dict, termo: str, conj_intens_tam: int) -> float:
    """
Calula a parte idf do tf_idf para um termo
    :param termos_cont: Dicionário com chave sendo cada termo e valor o número de documentos em que esse termo aparece
    :param termo: Termo para o qual se deseja calcular o idf
    :param conj_intens_tam: Quantidade de ítens
    :return: Valro do idf
    """
    if termos_cont.get(termo) is not None:
        idf =  math.log2(conj_intens_tam/termos_cont[termo])
    else:
        idf =  0
    return idf

def addTermo(termos_cont, termo):
    """
Incrementa o número de cocumentos que o termo aparece.
    :param termos_cont: Dicionário que armazena o número de documentos que um termo aparece
    :param termo: Termo
    """
    if termos_cont.get(termo) is None:
        termos_cont[termo] = 1
    else:
        termos_cont[termo] = termos_cont[termo] + 1

if __name__ == '__main__':
    doc1 = Item("Doc 1", 'link1', 'resumo 1', 'tipo 1', ["python", "é", "uma", "linguagem", "bem", "legal", "o", "python", "é", "sensacional", "é", "sim", "legal"])
    doc2 = Item("Doc 2", "link 2", 'resumo 2', 'tipo 2', ["Python", "não", "sei", "se", "sei", "como", "o", "chão", "é", "firme"])
    perg1 = Pergunta(['ponteiros', 'Python', 'abacate', 'são', 'legal', 'legal'])


    tf_idf([doc1, doc2], [perg1])
    print(doc1)
    print(doc2)
    print(perg1)