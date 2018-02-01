#Classes
from rec_edu_utils.item import Item
from rec_edu_utils.pergunta import Pergunta
#Módulos internos
import perfil
import recomendador
#Módulos externos
import pickle
#Documentação
from typing import List

def getItens(arqItens: str) -> List[Item]:
    """
Obtem a lista de itens do arquivo
    :param arqItens: Caminho para o arquivo de itens
    :return: Lista de objetos Item (termos com tf_idf)
    """
    try:
        with open(arqItens, 'rb') as arquivo:
            return pickle.load(arquivo)
    except FileNotFoundError:
        return None


def getPerguntas(arqPerguntas: str) -> List[Pergunta]:
    """
Obtem a lista de perguntas do arquivo
    :param arqPerguntas: Caminho para o arquivo de perguntas
    :return: Lista de objetos Pergunta (termosPerg com (freq, idf)
    """
    try:
        with open(arqPerguntas, 'rb') as arquivo:
            return pickle.load(arquivo)
    except FileNotFoundError:
        return None

if __name__ == "__main__":

    erradas = [0, 4, 5]

    itens = getItens('../itens.re')
    perguntas = getPerguntas('../perguntas.re')

    pergErradas = [perguntas[i] for i in erradas]

    perfilVet = perfil.montarPerfil(pergErradas)

    recomendacoes = recomendador.recomendacao(perfilVet, itens)

    for recomendacao in reversed(recomendacoes):
        print("Similaridade: " + str(recomendacao[0]))
        print(recomendacao[1])
        print()