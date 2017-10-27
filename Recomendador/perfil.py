def montarPerfil(perguntasErradas: list[dict]) -> dict:
    """
Monta o perfil do aluno baseado nas perguntas respondidas erradas
    :param perguntasErradas: Lista de perguntas erradas: [{'pergunta': X, 'pre_tf_idf':{'termo1':(freq, idf), 'termo2':(freq, idf), ...]
    :return Perfil do usuário (Dicionário com chaves=termos e valores=tf_idf)
    """
    pass