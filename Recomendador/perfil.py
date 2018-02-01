#Classes
from rec_edu_utils.pergunta import Pergunta
#Módulos externos
import math
#Documentação
from typing import List, Dict

def montarPerfil(perguntasErradas: List[Pergunta]) -> Dict[str, float]:
    """
Monta o perfil do aluno baseado nas perguntas respondidas erradas
    :param perguntasErradas: Lista de perguntas erradas: [{'pergunta': X, 'pre_tf_idf':{'termo1':(freq, idf), 'termo2':(freq, idf), ...]
    :return Perfil do usuário (Dicionário com chaves=termos e valores=tf_idf)
    """
    retorno = {}

    for pergunta in perguntasErradas:
        termosPerg = pergunta.termosPerg
        for termo in termosPerg.keys():
            valueTermo = termosPerg[termo]
            valueRetorno = retorno.get(termo)
            if valueRetorno is not None:
                retorno[termo] = (valueRetorno[0]+valueTermo[0], valueRetorno[1])
            else:
                retorno[termo] = valueTermo

    for termo in retorno.keys():
        valueRetorno = retorno.get(termo)
        retorno[termo] = tf(valueRetorno[0]) * valueRetorno[1]

    return retorno

def tf(freq: int) -> float:
    if freq > 0:
        tf = 1 + math.log2(freq)
    else:
        tf = 0
    return tf