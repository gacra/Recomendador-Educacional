#Classe usada
from rec_edu_utils.pergunta import Pergunta
#Módulos usados
import io
import re
#Documentação
from typing import List

def get_perguntas(arqPerguntas: str) -> List[Pergunta]:
    """
Obtem as perguntas do arquivo (TODO: Base de dados), e retorna em formato conveniente.
    :param arqPerguntas: Caminho do arquivo contendo as perguntas
    :return: Lista de objetos Pergunta
    """
    try:
        with io.open(arqPerguntas, 'r', encoding='utf8') as arquivo:
            retorno = [Pergunta(re.findall('[\w-]+', termosPeg.lower())) for termosPeg in arquivo.read().splitlines()]
            arquivo.close()
        return retorno
    except FileNotFoundError:
        print("ERRO: Arquivo de perguntas não existe")
        return []

#PARA TESTE
if __name__ == '__main__':
    print(get_perguntas('../exemploPerguntas.txt'))