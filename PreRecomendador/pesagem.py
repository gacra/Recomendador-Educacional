#Classes
import sys
sys.path.append('../Utils')
from item import Item
from pergunta import Pergunta
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
    doc3 = {'titulo': "Doc 3", 'link': "link 3", 'resumo': 'resumo 3', 'tipo': 'tipo 3', 'termos': ['linguagem', 'c', 'endereços', 'e', 'ponteiros', 'projeto', 'de', 'algoritmos', 'linguagem', 'c', 'índice', 'endereços', 'e', 'ponteiros', 'os', 'conceitos', 'de', 'endereço', 'e', 'ponteiro', 'são', 'fundamentais', 'em', 'qualquer', 'linguagem', 'de', 'programação', 'embora', 'fiquem', 'ocultos', 'em', 'algumas', 'linguagens', 'em', 'c', 'esses', 'conceitos', 'são', 'explícitos', 'dominar', 'o', 'conceito', 'de', 'ponteiro', 'exige', 'algum', 'esforço', 'e', 'uma', 'boa', 'dose', 'de', 'prática', 'endereços', 'a', 'memória', 'ram', 'de', 'qualquer', 'computador', 'é', 'uma', 'sequência', 'de', 'bytes', 'cada', 'byte', 'armazena', 'um', 'de', '256', 'possíveis', 'valores', 'os', 'bytes', 'são', 'numerados', 'sequencialmente', 'e', 'o', 'número', 'de', 'um', 'byte', 'é', 'o', 'seu', 'endereço', 'address', 'cada', 'objeto', 'na', 'memória', 'do', 'computador', 'ocupa', 'um', 'certo', 'número', 'de', 'bytes', 'consecutivos', 'um', 'char', 'ocupa', '1', 'byte', 'um', 'int', 'ocupa', '4', 'bytes', 'e', 'um', 'double', 'ocupa', '8', 'bytes', 'em', 'muitos', 'computadores', 'o', 'número', 'exato', 'de', 'bytes', 'de', 'um', 'objeto', 'é', 'dado', 'pelo', 'operador', 'sizeof', 'a', 'expressão', 'sizeof', 'int', 'por', 'exemplo', 'dá', 'o', 'número', 'de', 'bytes', 'de', 'um', 'int', 'no', 'seu', 'computador', 'cada', 'objeto', 'na', 'memória', 'tem', 'um', 'endereço', 'na', 'maioria', 'dos', 'computadores', 'o', 'endereço', 'de', 'um', 'objeto', 'é', 'o', 'endereço', 'do', 'seu', 'primeiro', 'byte', 'por', 'exemplo', 'depois', 'das', 'declarações', 'char', 'c', 'int', 'i', 'struct', 'int', 'x', 'y', 'ponto', 'int', 'v', '4', 'os', 'endereços', 'das', 'variáveis', 'poderiam', 'ser', 'os', 'seguintes', 'c', '89421', 'i', '89422', 'ponto', '89426', 'v', '0', '89434', 'v', '1', '89438', 'v', '2', '89442', 'o', 'endereço', 'de', 'um', 'objeto', 'como', 'uma', 'variável', 'por', 'exemplo', 'é', 'dado', 'pelo', 'operador', 'se', 'i', 'é', 'uma', 'variável', 'então', 'i', 'é', 'o', 'seu', 'endereço', 'não', 'confunda', 'esse', 'uso', 'de', 'com', 'o', 'operador', 'lógico', 'and', 'que', 'se', 'escreve', 'em', 'c', 'no', 'exemplo', 'acima', 'i', 'vale', '89422', 'e', 'v', '3', 'vale', '89446', 'um', 'exemplo', 'o', 'segundo', 'argumento', 'da', 'função', 'de', 'biblioteca', 'scanf', 'é', 'o', 'endereço', 'da', 'variável', 'onde', 'deve', 'ser', 'depositado', 'o', 'objeto', 'lido', 'do', 'dispositivo', 'padrão', 'de', 'entrada', 'int', 'i', 'scanf', 'd', 'i', 'exercícios', '1', 'tamanhos', 'compile', 'e', 'execute', 'o', 'seguinte', 'programa', 'int', 'main', 'void', 'typedef', 'struct', 'int', 'dia', 'mes', 'ano', 'data', 'printf', 'sizeof', 'data', 'd', 'n', 'sizeof', 'data', 'ponteiros', 'um', 'ponteiro', 'apontador', 'pointer', 'é', 'um', 'tipo', 'especial', 'de', 'variável', 'que', 'armazena', 'endereços', 'um', 'ponteiro', 'pode', 'ter', 'o', 'valor', 'especial', 'null', 'que', 'não', 'é', 'endereço', 'de', 'lugar', 'algum', 'a', 'macro', 'null', 'está', 'definida', 'na', 'interface', 'stdlib', 'h', 'e', 'seu', 'valor', 'é', '0', 'na', 'maioria', 'dos', 'computadores', 'se', 'um', 'ponteiro', 'p', 'armazena', 'o', 'endereço', 'de', 'uma', 'variável', 'i', 'podemos', 'dizer', 'p', 'aponta', 'para', 'i', 'ou', 'p', 'é', 'o', 'endereço', 'de', 'i', 'em', 'termos', 'um', 'pouco', 'mais', 'abstratos', 'diz-se', 'que', 'p', 'é', 'uma', 'referência', 'à', 'variável', 'i', 'se', 'um', 'ponteiro', 'p', 'tem', 'valor', 'diferente', 'de', 'null', 'então', 'p', 'é', 'o', 'valor', 'do', 'objeto', 'apontado', 'por', 'p', 'não', 'confunda', 'esse', 'uso', 'de', 'com', 'o', 'operador', 'de', 'multiplicação', 'por', 'exemplo', 'se', 'i', 'é', 'uma', 'variável', 'e', 'p', 'vale', 'i', 'então', 'dizer', 'p', 'é', 'o', 'mesmo', 'que', 'dizer', 'i', 'figura', 'esquerda', 'um', 'ponteiro', 'p', 'armazenado', 'no', 'endereço', '60001', 'contém', 'o', 'endereço', 'de', 'um', 'inteiro', 'figura', 'direita', 'representação', 'esquemática', 'da', 'situação', 'há', 'vários', 'tipos', 'de', 'ponteiros', 'ponteiros', 'para', 'bytes', 'ponteiros', 'para', 'inteiros', 'ponteiros', 'para', 'ponteiros', 'para', 'inteiros', 'ponteiros', 'para', 'registros', 'etc', 'o', 'computador', 'precisa', 'saber', 'de', 'que', 'tipo', 'de', 'ponteiro', 'você', 'está', 'falando', 'para', 'declarar', 'um', 'ponteiro', 'p', 'para', 'um', 'inteiro', 'diga', 'int', 'p', 'para', 'declarar', 'um', 'ponteiro', 'p', 'para', 'um', 'registro', 'reg', 'diga', 'struct', 'reg', 'p', 'um', 'ponteiro', 'r', 'para', 'um', 'ponteiro', 'que', 'apontará', 'um', 'inteiro', 'é', 'declarado', 'assim', 'int', 'r', 'veja', 'por', 'exemplo', 'a', 'declaração', 'de', 'uma', 'matriz', 'de', 'números', 'inteiros', 'exemplos', 'suponha', 'que', 'a', 'b', 'e', 'c', 'são', 'variáveis', 'inteiras', 'e', 'veja', 'um', 'jeito', 'bobo', 'de', 'fazer', 'c', 'a', 'b', 'int', 'p', 'p', 'é', 'um', 'ponteiro', 'para', 'um', 'inteiro', 'int', 'q', 'p', 'a', 'o', 'valor', 'de', 'p', 'é', 'o', 'endereço', 'de', 'a', 'q', 'b', 'q', 'aponta', 'para', 'b', 'c', 'p', 'q', 'outro', 'exemplo', 'bobo', 'int', 'p', 'int', 'r', 'r', 'é', 'um', 'ponteiro', 'para', 'ponteiro', 'para', 'inteiro', 'p', 'a', 'p', 'aponta', 'para', 'a', 'r', 'p', 'r', 'aponta', 'para', 'p', 'e', 'r', 'aponta', 'para', 'a', 'c', 'r', 'b', 'aplicação', 'suponha', 'que', 'precisamos', 'de', 'uma', 'função', 'que', 'troque', 'os', 'valores', 'de', 'duas', 'variáveis', 'inteiras', 'digamos', 'i', 'e', 'j', 'é', 'claro', 'que', 'a', 'função', 'void', 'troca', 'int', 'i', 'int', 'j', 'errado', 'int', 'temp', 'temp', 'i', 'i', 'j', 'j', 'temp', 'não', 'produz', 'o', 'efeito', 'desejado', 'pois', 'recebe', 'apenas', 'os', 'valores', 'das', 'variáveis', 'e', 'não', 'as', 'variáveis', 'propriamente', 'ditas', 'a', 'função', 'recebe', 'cópias', 'das', 'variáveis', 'e', 'troca', 'os', 'valores', 'dessas', 'cópias', 'enquanto', 'as', 'variáveis', 'originais', 'permanecem', 'inalteradas', 'para', 'obter', 'o', 'efeito', 'desejado', 'é', 'preciso', 'passar', 'à', 'função', 'os', 'endereços', 'das', 'variáveis', 'void', 'troca', 'int', 'p', 'int', 'q', 'int', 'temp', 'temp', 'p', 'p', 'q', 'q', 'temp', 'para', 'aplicar', 'essa', 'função', 'às', 'variáveis', 'i', 'e', 'j', 'basta', 'dizer', 'troca', 'i', 'j', 'ou', 'talvez', 'int', 'p', 'q', 'p', 'i', 'q', 'j', 'troca', 'p', 'q', 'exercícios', '2', 'verifique', 'que', 'a', 'troca', 'de', 'valores', 'de', 'variáveis', 'discutida', 'acima', 'poderia', 'ser', 'obtida', 'por', 'meio', 'de', 'uma', 'macro', 'do', 'pré-processador', 'define', 'troca', 'x', 'y', 'int', 't', 'x', 'x', 'y', 'y', 't', 'troca', 'i', 'j', 'por', 'que', 'o', 'código', 'abaixo', 'está', 'errado', 'void', 'troca', 'int', 'i', 'int', 'j', 'int', 'temp', 'temp', 'i', 'i', 'j', 'j', 'temp', 'um', 'ponteiro', 'pode', 'ser', 'usado', 'para', 'dizer', 'a', 'uma', 'função', 'onde', 'ela', 'deve', 'depositar', 'o', 'resultado', 'de', 'seus', 'cálculos', 'escreva', 'uma', 'função', 'hm', 'que', 'converta', 'minutos', 'em', 'horas-e-minutos', 'a', 'função', 'recebe', 'um', 'inteiro', 'mnts', 'e', 'os', 'endereços', 'de', 'duas', 'variáveis', 'inteiras', 'digamos', 'h', 'e', 'm', 'e', 'atribui', 'valores', 'a', 'essas', 'variáveis', 'de', 'modo', 'que', 'm', 'seja', 'menor', 'que', '60', 'e', 'que', '60', 'h', 'm', 'seja', 'igual', 'a', 'mnts', 'escreva', 'também', 'uma', 'função', 'main', 'que', 'use', 'a', 'função', 'hm', 'escreva', 'uma', 'função', 'mm', 'que', 'receba', 'um', 'vetor', 'inteiro', 'v', '0', 'n-1', 'e', 'os', 'endereços', 'de', 'duas', 'variáveis', 'inteiras', 'digamos', 'min', 'e', 'max', 'e', 'deposite', 'nessas', 'variáveis', 'o', 'valor', 'de', 'um', 'elemento', 'mínimo', 'e', 'o', 'valor', 'de', 'um', 'elemento', 'máximo', 'do', 'vetor', 'escreva', 'também', 'uma', 'função', 'main', 'que', 'use', 'a', 'função', 'mm', 'vetores', 'e', 'endereços', 'os', 'elementos', 'de', 'qualquer', 'vetor', 'array', 'têm', 'endereços', 'consecutivos', 'na', 'memória', 'do', 'computador', 'na', 'verdade', 'os', 'endereços', 'não', 'são', 'consecutivos', 'uma', 'vez', 'que', 'cada', 'elemento', 'do', 'vetor', 'pode', 'ocupar', 'vários', 'bytes', 'mas', 'o', 'compilador', 'c', 'acerta', 'os', 'detalhes', 'internos', 'de', 'modo', 'a', 'criar', 'a', 'ilusão', 'de', 'que', 'a', 'diferença', 'entre', 'os', 'endereços', 'de', 'elementos', 'consecutivos', 'vale', '1', 'por', 'exemplo', 'depois', 'da', 'declaração', 'int', 'v', 'v', 'malloc', '100', 'sizeof', 'int', 'o', 'ponteiro', 'v', 'aponta', 'o', 'primeiro', 'elemento', 'de', 'um', 'vetor', 'de', '100', 'elementos', 'o', 'endereço', 'do', 'segundo', 'elemento', 'do', 'vetor', 'é', 'v', '1', 'e', 'o', 'endereço', 'do', 'terceiro', 'elemento', 'é', 'v', '2', 'se', 'i', 'é', 'uma', 'variável', 'do', 'tipo', 'int', 'então', 'v', 'i', 'é', 'o', 'endereço', 'do', 'i', '1', '-ésimo', 'elemento', 'do', 'vetor', 'as', 'expressões', 'v', 'i', 'e', 'v', 'i', 'têm', 'exatamente', 'o', 'mesmo', 'valor', 'e', 'portanto', 'as', 'atribuições', 'v', 'i', '87', 'v', 'i', '87', 'têm', 'o', 'mesmo', 'efeito', 'analogamente', 'qualquer', 'dos', 'dois', 'fragmentos', 'de', 'código', 'abaixo', 'pode', 'ser', 'usado', 'para', 'preencher', 'o', 'vetor', 'v', 'for', 'i', '0', 'i', '100', 'i', 'scanf', 'd', 'v', 'i', 'for', 'i', '0', 'i', '100', 'i', 'scanf', 'd', 'v', 'i', 'todas', 'essas', 'considerações', 'também', 'valem', 'se', 'o', 'vetor', 'for', 'alocado', 'estaticamente', 'pela', 'declaração', 'int', 'v', '100', 'mas', 'nesse', 'caso', 'v', 'é', 'uma', 'espécie', 'de', 'ponteiro', 'constante', 'cujo', 'valor', 'não', 'pode', 'ser', 'alterado', 'exercícios', '3', 'suponha', 'que', 'os', 'elementos', 'de', 'um', 'vetor', 'v', 'são', 'do', 'tipo', 'int', 'e', 'cada', 'int', 'ocupa', '8', 'bytes', 'no', 'seu', 'computador', 'se', 'o', 'endereço', 'de', 'v', '0', 'é', '55000', 'qual', 'o', 'valor', 'da', 'expressão', 'v', '3', 'suponha', 'que', 'v', 'é', 'um', 'vetor', 'declarado', 'assim', 'int', 'v', '100', 'descreva', 'em', 'português', 'a', 'sequência', 'de', 'operações', 'que', 'deve', 'ser', 'executada', 'para', 'calcular', 'o', 'valor', 'da', 'expressão', 'v', 'k', '9', 'suponha', 'que', 'v', 'é', 'um', 'vetor', 'descreva', 'a', 'diferença', 'conceitual', 'entre', 'as', 'expressões', 'v', '3', 'e', 'v', '3', 'o', 'que', 'faz', 'a', 'seguinte', 'função', 'void', 'imprime', 'char', 'v', 'int', 'n', 'char', 'c', 'for', 'c', 'v', 'c', 'v', 'n', 'v', 'printf', 'c', 'c', 'o', 'seguinte', 'fragmento', 'de', 'código', 'pretende', 'decidir', 'se', 'abacate', 'vem', 'antes', 'ou', 'depois', 'de', 'uva', 'no', 'dicionário', 'o', 'que', 'há', 'de', 'errado', 'char', 'a', 'b', 'a', 'abacate', 'b', 'uva', 'if', 'a', 'b', 'printf', 's', 'vem', 'antes', 'de', 's', 'n', 'a', 'b', 'else', 'printf', 's', 'vem', 'depois', 'de', 's', 'n', 'a', 'b', 'veja', 'o', 'verbete', 'pointer', 'computer', 'programming', 'na', 'wikipedia', 'aula', 'em', 'vídeo', 'sobre', 'ponteiros', 'no', 'academic', 'earth', 'usa', 'c', 'mas', 'os', 'conceitos', 'são', 'os', 'mesmos', 'de', 'c', 'aula', 'em', 'vídeo', 'sobre', 'aritmética', 'de', 'ponteiros', 'na', 'the', 'open', 'academy', 'atualizado', 'em', '2016-04-01', 'http', 'www', 'ime', 'usp', 'br', 'pf', 'algoritmos', 'paulo', 'feofiloff', 'dcc', '-', 'ime', '-', 'usp']}
    doc4 = {'titulo': "Doc 4", 'link': "link 4", 'resumo': 'resumo 4', 'tipo': 'tipo 4',
            'termos': ['como', 'declarar', 'inicializar', 'e', 'usar', 'ponteiros', 'em', 'c', '-', 'a', 'constante', 'null', '-', 'c', 'progressivo', 'net', 'c', 'progressivo', 'net', 'apostila', 'de', 'c', 'online', 'e', 'gratuita', 'como', 'declarar', 'inicializar', 'e', 'usar', 'ponteiros', 'em', 'c', '-', 'a', 'constante', 'null', 'agora', 'que', 'já', 'vimos', 'os', 'conceitos', 'teóricos', 'sobre', 'memória', 'blocos', 'de', 'memória', 'endereçamento', 'e', 'do', 'uso', 'da', 'função', 'sizeof', 'vamos', 'de', 'fato', 'usar', 'os', 'ponteiros', 'nesse', 'tutorial', 'de', 'c', 'de', 'nossa', 'apostila', 'vamos', 'ensinar', 'como', 'declarar', 'ponteiros', 'fazê-los', 'apontarem', 'para', 'alguma', 'variável', 'ou', 'vetor', 'e', 'manipulá-los', 'clique', 'aqui', 'e', 'saiba', 'como', 'tirar', 'seu', 'certificado', 'de', 'programação', 'c', 'como', 'declarar', 'ponteiros', 'em', 'c', 'para', 'declarar', 'um', 'ponteiro', 'ou', 'apontador', 'em', 'c', 'basta', 'colocarmos', 'um', 'asterisco', '-', '-', 'antes', 'do', 'nome', 'desse', 'ponteiro', 'sintaxe', 'tipo', 'nome_do_ponteiro', 'por', 'exemplo', 'int', 'ponteiro_pra_inteiro', 'float', 'ponteiro_pra_float', 'char', 'ponteiro_pra_char', 'na', 'verdade', 'esse', 'asterisco', 'pode', 'ser', 'encostado', 'no', 'tipo', 'ou', 'entre', 'o', 'tipo', 'e', 'o', 'nome', 'aqui', 'se', 'você', 'estiver', 'com', 'os', 'conceitos', 'de', 'ponteiro', 'na', 'cabeça', 'pode', 'surgir', 'uma', 'pergunta', 'se', 'os', 'ponteiros', 'são', 'tipos', 'que', 'armazenam', 'endereço', 'e', 'endereço', 'são', 'apenas', 'números', 'por', 'quê', 'ter', 'que', 'declarar', 'ponteiros', 'com', 'os', 'tipos', 'int', 'float', 'char', 'etc', 'a', 'resposta', 'é', 'dada', 'no', 'artigo', 'passado', 'em', 'que', 'falamos', 'sobre', 'o', 'tamanho', 'que', 'as', 'variáveis', 'ocupam', 'em', 'memória', 'vimos', 'que', 'as', 'variáveis', 'ocupam', 'posições', 'vizinhas', 'e', 'contíguas', 'em', 'seqüência', 'de', 'memória', 'exceto', 'claro', 'o', 'tipo', 'char', 'que', 'ocua', 'só', '1', 'byte', 'ou', 'seja', 'só', 'um', 'bloco', 'vamos', 'pegar', 'o', 'exemplo', 'da', 'variável', 'inteira', 'em', 'minha', 'máquina', 'ela', 'ocupa', '4', 'bytes', 'ou', 'seja', '4', 'blocos', 'de', 'memória', 'cada', 'bloco', 'com', 'um', 'endereço', 'mas', 'o', 'ponteiro', 'armazena', 'apenas', 'um', 'endereço', 'de', 'memória', 'e', 'não', '4', 'então', 'o', 'ponteiro', 'irá', 'sempre', 'armazenar', 'o', 'endereço', 'do', 'primeiro', 'bloco', 'do', 'primeiro', 'byte', 'e', 'os', 'outros', 'ué', 'se', 'o', 'c', 'sabe', 'quantos', 'bytes', 'cada', 'variável', 'ocupa', 'que', 'elas', 'são', 'blocos', 'vizinhos', 'de', 'memória', 'e', 'o', 'ponteiro', 'sabe', 'o', 'endereço', 'do', 'primeiro', 'bloco', 'ele', 'vai', 'saber', 'dos', 'outros', 'também', 'é', 'por', 'isso', 'que', 'precisamos', 'dizer', 'o', 'tipo', 'de', 'variável', 'antes', 'de', 'declarar', 'o', 'ponteiro', 'se', 'for', 'um', 'ponteiro', 'de', 'inteiro', 'estamos', 'dizendo', 'ponteiro', 'guarde', 'esse', 'endereço', 'e', 'os', 'próximos', '3', 'pois', 'o', 'inteiro', 'tem', '4', 'bloco', 'se', 'for', 'um', 'double', 'ponteiro', 'armazene', 'o', 'primeiro', 'endereço', 'e', 'saiba', 'que', 'os', 'próximos', '7', 'blocos', 'são', 'dessa', 'mesma', 'variável', 'ponteiros', 'e', 'vetores', 'em', 'c', 'já', 'explicamos', 'sobre', 'a', 'relação', 'dos', 'ponteiros', 'com', 'os', 'diversos', 'tipos', 'de', 'blocos', 'de', 'memória', 'de', 'cada', 'variável', 'e', 'a', 'relação', 'dos', 'ponteiros', 'com', 'os', 'vetores', 'que', 'possuem', 'diversas', 'variáveis', 'pois', 'bem', 'eles', 'têm', 'ponteiros', 'e', 'vetores', 'possuem', 'uma', 'relação', 'especial', 'quando', 'declaramos', 'um', 'vetor', 'estamos', 'declarando', 'um', 'conjunto', 'de', 'variáveis', 'também', 'contíguas', 'e', 'cada', 'uma', 'dessas', 'variáveis', 'ocupam', 'vários', 'bytes', 'ou', 'só', '1', 'byte', 'se', 'for', 'char', 'então', 'um', 'vetor', 'é', 'um', 'conjunto', 'maior', 'ainda', 'de', 'bytes', 'de', 'blocos', 'de', 'memória', 'como', 'você', 'sabe', 'quando', 'apontamos', 'um', 'ponteiro', 'para', 'uma', 'variável', 'esse', 'ponteiro', 'armazena', 'o', 'endereço', 'do', 'primeiro', 'byte', 'do', 'menor', 'endereço', 'da', 'variável', 'a', 'relação', 'com', 'vetores', 'é', 'análoga', 'o', 'nome', 'do', 'vetor', 'é', 'na', 'verdade', 'o', 'endereço', 'do', 'primeiro', 'elemento', 'desse', 'vetor', 'ou', 'seja', 'se', 'declararmos', 'um', 'vetor', 'de', 'nome', 'vetor', 'não', 'importando', 'o', 'número', 'de', 'elementos', 'se', 'imprimirmos', 'o', 'nome', 'vetor', 'dentro', 'de', 'um', 'printf', 'veremos', 'o', 'endereço', 'da', 'primeira', 'variável', 'daquele', 'vetor', 'podemos', 'ver', 'um', 'vetor', 'como', 'um', 'ponteiro', 'isso', 'explica', 'o', 'fato', 'de', 'que', 'quando', 'passamos', 'um', 'vetor', 'para', 'uma', 'função', 'essa', 'função', 'altera', 'de', 'fato', 'o', 'valor', 'do', 'vetor', 'isso', 'ocorre', 'pois', 'não', 'estamos', 'passando', 'uma', 'cópia', 'do', 'vetor', 'como', 'acontece', 'com', 'as', 'variáveis', 'isso', 'ocorre', 'porque', 'quando', 'passamos', 'o', 'nome', 'do', 'vetor', 'estamos', 'passando', 'um', 'ponteiro', 'pra', 'função', 'ou', 'seja', 'estamos', 'passando', 'um', 'endereço', 'onde', 'a', 'função', 'vai', 'atuar', 'e', 'endereço', 'de', 'memória', 'é', 'o', 'mesmo', 'dentro', 'ou', 'fora', 'de', 'uma', 'função', 'rode', 'o', 'seguinte', 'exemplo', 'para', 'se', 'certificar', 'do', 'que', 'foi', 'ensinado', 'aqui', 'exemplo', 'de', 'código', 'em', 'c', 'crie', 'um', 'programa', 'que', 'mostre', 'que', 'o', 'nome', 'de', 'um', 'vetor', 'é', 'na', 'verdade', 'um', 'ponteiro', 'para', 'a', 'primeira', 'posição', 'que', 'o', 'vetor', 'ocupa', 'na', 'memória', 'ou', 'seja', 'um', 'vetor', 'sempre', 'aponta', 'para', 'o', 'elemento', '0', 'include', 'stdio', 'h', 'curso', 'c', 'progressivo', 'www', 'cprogessivo', 'net', 'o', 'melhor', 'curso', 'de', 'c', 'online', 'e', 'gratuito', 'artigos', 'apostilas', 'tutoriais', 'e', 'vídeo-aulas', 'sobre', 'a', 'linguagem', 'de', 'programação', 'c', 'int', 'main', 'void', 'int', 'teste', '10', 'printf', 'imprimindo', 'o', 'vetor', 'teste', 'd', 'n', 'teste', 'printf', 'imprimindo', 'o', 'endereço', 'do', 'primeiro', 'elemento', 'd', 'n', 'teste', '0', 'return', '0', 'ou', 'seja', 'para', 'declararmos', 'um', 'ponteiro', 'ptr', 'para', 'um', 'vetor', 'vet', 'fazemos', 'ptr', 'vet', 'pois', 'o', 'nome', 'do', 'vetor', 'é', 'um', 'ponteiro', 'que', 'não', 'muda', 'para', 'o', 'primeiro', 'elemento', 'então', 'poderíamos', 'fazer', 'assim', 'também', 'ptr', 'vet', '0', 'como', 'inicializar', 'um', 'ponteiro', 'em', 'c', 'a', 'constante', 'null', 'já', 'vimos', 'como', 'declarar', 'um', 'ponteiro', 'então', 'é', 'hora', 'de', 'fazer', 'com', 'que', 'eles', 'cumpram', 'sua', 'missão', 'vamos', 'fazer', 'os', 'ponteiros', 'apontarem', 'lembra', 'que', 'ensinamos', 'como', 'checar', 'o', 'endereço', 'de', 'uma', 'variável', 'ou', 'vetor', 'apenas', 'usando', 'o', 'símbolo', 'antes', 'da', 'variável', 'agora', 'vamos', 'fazer', 'isso', 'novamente', 'mas', 'é', 'para', 'pegar', 'esse', 'endereço', 'e', 'armazenar', 'em', 'um', 'ponteiro', 'por', 'exemplo', 'se', 'quisermos', 'armazenar', 'o', 'endereço', 'do', 'inteiro', 'numero', 'no', 'ponteiro', 'numeroptr', 'fazemos', 'int', 'numero', '5', 'int', 'numeroptr', 'numero', 'pronto', 'agora', 'nosso', 'ponteiro', 'está', 'apontando', 'para', 'a', 'variável', 'numero', 'pois', 'o', 'ponteiro', 'guardou', 'o', 'endereço', 'do', 'inteiro', 'na', 'sua', 'posição', 'de', 'memória', 'muito', 'cuidado', 'ponteiros', 'armazenam', 'endereços', 'e', 'não', 'valores', 'ou', 'seja', 'se', 'fizer', 'int', 'numeroptr', 'numero', 'estará', 'comentendo', 'um', 'erro', 'é', 'sempre', 'bom', 'inicializarmos', 'os', 'ponteiros', 'pois', 'senão', 'eles', 'podem', 'vir', 'com', 'lixo', 'e', 'você', 'se', 'esquecer', 'posteriormente', 'de', 'inicializar', 'então', 'quando', 'for', 'usar', 'pensará', 'que', 'está', 'usando', 'o', 'ponteiro', 'de', 'modo', 'correto', 'mas', 'estará', 'usando', 'o', 'ponteiro', 'com', 'ele', 'apontando', 'para', 'um', 'lixo', 'endereço', 'qualquer', 'de', 'memória', 'uma', 'boa', 'prática', 'é', 'apontar', 'os', 'ponteiros', 'para', 'a', 'primeira', 'posição', 'de', 'memória', 'que', 'é', 'conhecida', 'como', 'null', 'sempre', 'que', 'terminar', 'de', 'usar', 'um', 'ponteiro', 'coloque', 'ele', 'pra', 'apontar', 'para', 'a', 'posição', 'null', 'para', 'fazer', 'isso', 'faça', 'tipo', 'nome_do_ponteiro', 'null', 'exemplo', 'de', 'código', 'como', 'usar', 'ponteiros', 'crie', 'um', 'programa', 'em', 'c', 'que', 'declara', 'um', 'inteiro', 'e', 'uma', 'variável', 'do', 'tipo', 'double', 'em', 'seguida', 'crie', 'dois', 'ponteiros', 'apontando', 'para', 'essas', 'variáveis', 'e', 'mostre', 'o', 'endereço', 'de', 'memória', 'das', 'variáveis', 'e', 'mostre', 'o', 'endereço', 'de', 'memória', 'que', 'cada', 'ponteiro', 'armazenou', 'por', 'fim', 'coloque', 'esses', 'ponteiros', 'para', 'a', 'primeira', 'posição', 'null', 'de', 'memória', 'para', 'saber', 'o', 'endereço', 'de', 'uma', 'variável', 'dentro', 'do', 'printf', 'colocamos', 'o', 'd', 'e', 'depois', 'nome_variavel', 'para', 'saber', 'que', 'endereço', 'um', 'ponteiro', 'armazena', 'no', 'printf', 'também', 'colocamos', 'o', 'd', 'entre', 'as', 'aspas', 'e', 'fora', 'colocamos', 'apenas', 'o', 'nome', 'do', 'ponteiro', 'veja', 'como', 'ficou', 'nosso', 'código', 'sobre', 'como', 'fazer', 'esse', 'programa', 'em', 'c', 'include', 'stdio', 'h', 'curso', 'c', 'progressivo', 'www', 'cprogessivo', 'net', 'o', 'melhor', 'curso', 'de', 'c', 'online', 'e', 'gratuito', 'artigos', 'apostilas', 'tutoriais', 'e', 'vídeo-aulas', 'sobre', 'a', 'linguagem', 'de', 'programação', 'c', 'int', 'main', 'void', 'int', 'inteiro', 'int', 'inteiro_ptr', 'inteiro', 'double', 'double1', 'double', 'double_ptr', 'double1', 'printf', 'endereco', 'da', 'variariavel', 'inteiro', 'd', 'n', 'inteiro', 'printf', 'endereco', 'armazenado', 'no', 'ponteiro', 'inteiro_ptr', 'd', 'n', 'n', 'inteiro_ptr', 'printf', 'endereco', 'da', 'variariavel', 'double1', 'd', 'n', 'double1', 'printf', 'endereco', 'armazenado', 'no', 'ponteiro', 'double_ptr', 'd', 'n', 'n', 'double_ptr', 'printf', 'apos', 'o', 'uso', 'dos', 'ponteiros', 'vamos', 'aponta-los', 'para', 'null', 'n', 'n', 'inteiro_ptr', 'null', 'double_ptr', 'null', 'printf', 'endereco', 'armazenado', 'no', 'ponteiro', 'inteiro_ptr', 'd', 'n', 'inteiro_ptr', 'printf', 'endereco', 'armazenado', 'no', 'ponteiro', 'double_ptr', 'd', 'n', 'double_ptr', 'return', '0', 'tags', 'apostila', 'de', 'c', 'como', 'programar', 'em', 'c', 'tutorial', 'de', 'c', 'vetores', '6', 'comentários', 'brittivaldo', 'disse', 'apostila', 'c', 'progressivo', 'é', 'a', 'melhor', 'que', 'existe', 'em', 'nome', 'de', 'todos', 'os', 'leitores', 'meus', 'parabéns', '16', 'de', 'agosto', 'de', '2014', '06', '58', 'roberto', 'gmj', 'disse', 'quem', 'só', 'usou', 'ctrl', 'c', 'ctrl', 'v', 'ta', 'com', 'variariavel', 'no', 'printf', 'além', 'de', 'que', 'provavelmente', 'não', 'aprendeu', 'direito', 'aqui', 'to', 'adorando', 'o', 'curso', 'obrigado', 'e', 'parabéns', 'estudando', 'e', 'praticando', 'muito', '24', 'de', 'outubro', 'de', '2014', '07', '02', 'andré', 'de', 'souza', 'disse', 'include', 'curso', 'c', 'progressivo', 'www', 'cprogessivo', 'net', 'o', 'melhor', 'curso', 'de', 'c', 'online', 'e', 'gratuito', 'artigos', 'apostilas', 'tutoriais', 'e', 'vídeo-aulas', 'sobre', 'a', 'linguagem', 'de', 'programação', 'c', 'int', 'main', 'void', 'int', 'teste', '10', 'printf', 'imprimindo', 'o', 'vetor', 'teste', 'd', 'n', 'teste', 'printf', 'imprimindo', 'o', 'endereço', 'do', 'primeiro', 'elemento', 'd', 'n', 'teste', '0', 'return', '0', 'na', 'apostila', 'anterior', 'aconteceu', 'a', 'mesma', 'coisa', 'o', 'programa', 'nao', 'é', 'compilado', 'pq', 'aparece', 'a', 'mensagem', 'linha', '13', 'aviso', 'formato', 'd', 'espera', 'argumento', 'do', 'tipo', 'int', 'orem', 'o', 'argumento', '2', 'possui', 'tipo', 'int', '-wformat', 'pelo', 'que', 'eu', 'entendi', 'o', 'compilador', 'nao', 'esta', 'tratando', 'o', 'numero', 'do', 'endereço', 'como', 'um', 'numero', 'inteiro', 'por', 'isso', 'nao', 'esta', 'aceitando', 'd', 'é', 'isso', 'mesmo', '31', 'de', 'dezembro', 'de', '2014', '18', '47', 'kile', 'volpw', 'disse', 'blogger', 'roberto', 'gmj', 'disse', 'quem', 'só', 'usou', 'ctrl', 'c', 'ctrl', 'v', 'ta', 'com', 'variariavel', 'no', 'printf', 'além', 'de', 'que', 'provavelmente', 'não', 'aprendeu', 'direito', 'aqui', 'to', 'adorando', 'o', 'curso', 'obrigado', 'e', 'parabéns', 'estudando', 'e', 'praticando', 'muito', 'que', 'eu', 'saiba', 'aquilo', 'era', 'um', 'exemplo', 'não', 'uma', 'questão', '22', 'de', 'novembro', 'de', '2015', '04', '26', 'rayller', 'disse', 'este', 'comentário', 'foi', 'removido', 'pelo', 'autor', '14', 'de', 'junho', 'de', '2017', '09', '22', 'rayller', 'disse', 'não', 'consegui', 'entender', 'claramente', 'a', 'necessidade', 'de', 'apontar', 'para', 'null', 'se', 'depois', 'eu', 'precisar', 'utilizar', 'o', 'ponteiro', 'novamente', 'vou', 'ter', 'que', 'declarar', 'ele', 'para', 'o', 'endereço', 'da', 'variável', 'novamente', 'se', 'alguem', 'puder', 'esclarecer', 'melhor', 'esse', 'conceito', 'de', 'apontar', 'para', 'null', 'eu', 'agradeço', '16', 'de', 'junho', 'de', '2017', '06', '30', 'postar', 'um', 'comentário', 'postagem', 'mais', 'recente', 'postagem', 'mais', 'antiga', 'página', 'inicial', 'assinar', 'postar', 'comentários', 'atom', 'gostou', 'desse', 'tutorial', 'de', 'c', 'sabia', 'que', 'o', 'acervo', 'do', 'portal', 'c', 'progressivo', 'é', 'o', 'mesmo', 'ou', 'maior', 'que', 'de', 'um', 'livro', 'ou', 'curso', 'presencial', 'e', 'o', 'melhor', 'totalmente', 'gratuito', 'mas', 'para', 'nosso', 'projeto', 'se', 'manter', 'é', 'preciso', 'divulgação', 'para', 'isso', 'basta', 'curtir', 'nossa', 'página', 'no', 'facebook', 'e', 'ou', 'clicar', 'no', 'botão', '1', 'do', 'google', 'contamos', 'e', 'precisamos', 'de', 'seu', 'apoio', 'livro', 'recomendado', 'linguagem', 'c', 'review', 'gostou', 'dos', 'tutoriais', 'ajude', 'a', 'divulgar', 'conteúdo', 'original', '-', 'todos', 'os', 'direitos', 'reservados', 'política', 'de', 'privacidade', 'sumário', 'do', 'curso', 'índice', 'básico', 'teste', 'e', 'laços', 'função', 'vetores', 'ponteiros', 'strings', 'structs', 'alocação', 'arquivos', 'fórum', 'contato', 'ajude', 'nosso', 'projeto', 'gostou', 'do', 'conteúdo', 'te', 'ajudou', 'que', 'tal', 'nos', 'ajudar', 'qualquer', 'valor', 'para', 'manter', 'o', 'projeto', 'e', 'continuarmos', 'a', 'crescer', 'pagseguro', 'paypal', 'artigos', 'populares', 'gerando', 'números', 'aleatórios', 'em', 'c', 'rand', 'srand', 'e', 'seed', 'você', 'pode', 'nunca', 'ter', 'ficado', 'atento', 'para', 'isso', 'mas', 'números', 'aleatórios', 'são', 'vitais', 'em', 'praticamente', 'todos', 'os', 'ramos', 'da', 'computação', 'em', 'jogos', 'que', 'os', 'tipos', 'float', 'e', 'double', '-', 'números', 'decimais', 'ou', 'reais', 'em', 'c', 'no', 'artigo', 'passado', 'de', 'nosso', 'curso', 'de', 'c', 'estudamos', 'sobre', 'o', 'tipo', 'inteiro', 'int', 'como', 'declarar', 'imprimir', 'e', 'inicializar', 'tal', 'tipo', 'de', 'dado', 'agor', 'o', 'que', 'são', 'vetores', 'como', 'declarar', 'e', 'quando', 'usar', 'dando', 'início', 'a', 'mais', 'uma', 'importante', 'unidade', 'em', 'nosso', 'curso', 'online', 'e', 'gratuito', 'de', 'c', 'vamos', 'iniciar', 'nossos', 'estudos', 'sobre', 'as', 'estruturas', 'de', 'dados', 'lendo', 'arquivos', 'em', 'c', 'as', 'funções', 'fgetc', 'fscanf', 'e', 'fgets', 'agora', 'que', 'já', 'aprendemos', 'a', 'escrever', 'em', 'arquivos', 'em', 'c', 'vamos', 'aprender', 'agora', 'em', 'nossa', 'apostila', 'de', 'c', 'a', 'outra', 'parte', 'aprender', 'como', 'ler', 'informaç', 'lendo', 'e', 'escrevendo', 'strings', 'em', 'c', 'que', '99', '99', 'dos', 'aplicativos', 'em', 'c', 'ou', 'de', 'qualquer', 'outra', 'linguagem', 'usam', 'strings', 'e', 'caracteres', 'para', 'mostrar', 'textos', 'nós', 'já', 'convencemos', 'você', 'a', 'função', 'scanf', '-', 'recebendo', 'números', 'do', 'usuário', 'até', 'o', 'momento', 'os', 'artigos', 'de', 'nosso', 'curso', 'c', 'progressivo', 'tem', 'mostrado', 'diversos', 'programas', 'porém', 'todos', 'estáticos', 'sem', 'controle', 'e', 'sem', 'interação', 'o', 'tipo', 'char', '-', 'escrevendo', 'na', 'linguagem', 'c', 'agora', 'que', 'você', 'já', 'sabe', 'como', 'lidar', 'com', 'inteiros', 'e', 'decimais', 'na', 'linguagem', 'c', 'está', 'na', 'hora', 'de', 'estudarmos', 'como', 'escrever', 'caracteres', 'operações', 'matemáticas', 'em', 'c', '-', 'soma', 'subtração', 'multiplicação', 'divisão', 'e', 'módulo', 'ou', 'resto', 'da', 'divisão', 'e', 'precedência', 'dos', 'operadores', 'operações', 'matemáticas', 'básicas', 'fácil', 'não', 'por', 'exemplo', 'quanto', 'é', '1', '1', 'x', '2', 'pode', 'ser', '3', '1', '1x2', '1', '2', '3', 'ou', 'pode', 'ser', '4', '1', '1', 'x2', 'criando', 'e', 'compilando', 'seu', 'primeiro', 'programa', 'na', 'linguagem', 'c', 'no', 'artigo', 'passado', 'do', 'curso', 'c', 'progressivo', 'você', 'baixou', 'e', 'instalou', 'a', 'ide', 'clode', 'blocks', 'que', 'é', 'o', 'programa', 'necessário', 'mais', 'recomendado', 'e', 'melhor', 'questões', 'resolvidas', 'sobre', 'laço', 'while', 'em', 'c', 'vamos', 'agora', 'resolver', 'as', 'questões', 'sobre', 'o', 'laço', 'while', 'que', 'havíamos', 'proposto', 'no', 'artigo', 'anterior', 'de', 'nosso', 'curso', 'de', 'c', 'se', 'não', 'conseguiu', 'lei', 'publicidade', 'melhor', 'visualizado', 'com', 'google', 'chrome', 'e', 'mozilla', 'firefox']}
    doc5 = {'titulo': "Doc 5", 'link': "link 5", 'resumo': 'resumo 5', 'tipo': 'tipo 5',
            'termos' : ['programação', 'em', 'c', '-', 'uso', 'de', 'funções', 'programação', 'c', 'c', 'prof', 'márcio', 'sarroglia',
     'pinho', 'subalgoritmos', 'funções', 'definição', 'porque', 'usar', 'as', 'funções', 'primeiro', 'exemplo',
     'formato', 'geral', 'parâmetros', 'localização', 'das', 'funções', 'no', 'programa-fonte', 'verificação', 'dos',
     'tipos', 'dos', 'parâmetros', 'escopo', 'de', 'variáveis', 'funções', 'e', 'procedimentos', 'passagem', 'de',
     'parâmetros', 'por', 'referência', 'passagem', 'de', 'vetores', 'por', 'parâmetros', 'definição', 'conjunto', 'de',
     'comandos', 'agrupados', 'em', 'um', 'bloco', 'que', 'recebe', 'um', 'nome', 'e', 'através', 'deste', 'pode',
     'ser', 'evocado', 'porque', 'usar', 'funções', 'para', 'permitir', 'o', 'reaproveitamento', 'de', 'código', 'já',
     'construído', 'por', 'você', 'ou', 'por', 'outros', 'programadores', 'para', 'evitar', 'que', 'um', 'trecho', 'de',
     'código', 'que', 'seja', 'repetido', 'várias', 'vezes', 'dentro', 'de', 'um', 'mesmo', 'programa', 'para',
     'permitir', 'a', 'alteração', 'de', 'um', 'trecho', 'de', 'código', 'de', 'uma', 'forma', 'mais', 'rápida', 'com',
     'o', 'uso', 'de', 'uma', 'função', 'é', 'preciso', 'alterar', 'apenas', 'dentro', 'da', 'função', 'que', 'se',
     'deseja', 'para', 'que', 'os', 'blocos', 'do', 'programa', 'não', 'fiquem', 'grandes', 'demais', 'e', 'por',
     'conseqüência', 'mais', 'difíceis', 'de', 'entender', 'para', 'facilitar', 'a', 'leitura', 'do', 'programa-fonte',
     'de', 'uma', 'forma', 'mais', 'fácil', 'para', 'separar', 'o', 'programa', 'em', 'partes', 'blocos', 'que',
     'possam', 'ser', 'logicamente', 'compreendidos', 'de', 'forma', 'isolada', 'primero', 'exemplo', 'em', 'primeiro',
     'lugar', 'imaginemos', 'que', 'você', 'necessite', 'várias', 'vezes', 'em', 'seu', 'programa', 'imprimir', 'a',
     'mensagem', 'pressione', 'a', 'tecla', 'enter', 'e', 'esperar', 'que', 'o', 'usuário', 'tecle', 'enter', 'caso',
     'o', 'usuário', 'tecle', 'algo', 'diferente', 'o', 'programa', 'deve', 'imitir', 'um', 'beep', 'você', 'pode',
     'fazer', 'um', 'laço', 'de', 'while', 'sempre', 'que', 'isto', 'fosse', 'necessário', 'uma', 'alternativa', 'é',
     'criar', 'uma', 'função', 'com', 'o', 'uso', 'de', 'funções', 'este', 'processo', 'de', 'repetição', 'fica',
     'simplificado', 'observe', 'o', 'exemplo', 'a', 'seguir', 'include', 'stdio', 'h', 'void', 'esperaenter',
     'definição', 'da', 'função', 'esperaenter', 'int', 'tecla', 'printf', 'pressione', 'enter', 'n', 'do', 'tecla',
     'getchar', 'if', 'tecla', '13', 'se', 'nao', 'for', 'enter', 'printf', 'digite', 'enter', 'n', 'while', 'tecla',
     '13', '13', 'e', 'o', 'codigo', 'ascii', 'do', 'enter', 'void', 'main', 'esperaenter', 'chamada', 'da', 'função',
     'definida', 'antes', 'esperaenter', 'chamada', 'da', 'função', 'definida', 'antes', 'esperaenter', 'chamada', 'da',
     'função', 'definida', 'antes', 'f', 'ormato', 'geral', 'de', 'uma', 'função', 'em', 'c', 'tipo_da_funcao',
     'nomedafuncao', 'lista_de_parametros', 'corpo', 'da', 'função', 'a', 'lista_de_parametros', 'também', 'é',
     'chamada', 'de', 'lista_de_argumentos', 'é', 'opcional', 'parâmetros', 'a', 'fim', 'de', 'tornar', 'mais', 'amplo',
     'o', 'uso', 'de', 'uma', 'função', 'a', 'linguagem', 'c', 'permite', 'o', 'uso', 'de', 'parâmetros', 'este',
     'parâmetros', 'possibilitam', 'que', 'se', 'definida', 'sobre', 'quais', 'dados', 'a', 'função', 'deve', 'operar',
     'a', 'função', 'sound', 'freq', 'por', 'exemplo', 'recebe', 'como', 'parâmetro', 'a', 'freqüência', 'do', 'som',
     'a', 'ser', 'gerado', 'permitindo', 'que', 'se', 'defina', 'seu', 'comportamento', 'a', 'partir', 'deste', 'valor',
     'para', 'definir', 'os', 'parâmetros', 'de', 'uma', 'função', 'o', 'programador', 'deve', 'explicitá-los', 'como',
     'se', 'estive', 'declarando', 'uma', 'variável', 'entre', 'os', 'parênteses', 'do', 'cabeçalho', 'da', 'função',
     'caso', 'precise', 'declarar', 'mais', 'de', 'um', 'parâmetro', 'basta', 'separá-los', 'por', 'vírgulas', 'no',
     'exemplo', 'a', 'seguir', 'temos', 'a', 'função', 'soma', 'que', 'possui', 'dois', 'parâmetros', 'sendo', 'o',
     'primeiro', 'um', 'float', 'e', 'o', 'segundo', 'um', 'int', 'void', 'soma', 'float', 'a', 'int', 'b', 'basta',
     'separar', 'por', 'vírgulas', 'float', 'result', 'a', 'declaração', 'de', 'variáveis', 'é', 'igual', 'ao', 'que',
     'se', 'faz', 'na', 'função', 'main', 'result', 'a', 'b', 'printf', 'a', 'soma', 'de', '6', '3f', 'com', 'd', 'é',
     '6', '3f', 'n', 'a', 'b', 'result', 'os', 'parâmetros', 'da', 'função', 'na', 'sua', 'declaração', 'são',
     'chamados', 'parâmetros', 'formais', 'na', 'chamada', 'da', 'função', 'os', 'parâmetros', 'são', 'chamados',
     'parâmetros', 'atuais', 'reais', 'os', 'parâmetros', 'são', 'passados', 'para', 'uma', 'função', 'de', 'acordo',
     'com', 'a', 'sua', 'posição', 'ou', 'seja', 'o', 'primeiro', 'parâmetro', 'atual', 'da', 'chamada', 'define', 'o',
     'valor', 'o', 'primeiro', 'parâmetro', 'formal', 'na', 'definição', 'da', 'função', 'o', 'segundo', 'parâmetro',
     'atual', 'define', 'o', 'valor', 'do', 'segundo', 'parâmetro', 'formal', 'e', 'assim', 'por', 'diante', 'os',
     'nomes', 'dos', 'parâmetros', 'na', 'chamada', 'não', 'tem', 'relação', 'com', 'os', 'nomes', 'dos', 'parâmetros',
     'na', 'definição', 'da', 'função', 'no', 'código', 'a', 'seguir', 'por', 'exemplo', 'a', 'função', 'soma', 'é',
     'chamada', 'recebendo', 'como', 'parâmetros', 'as', 'variáveis', 'b', 'e', 'a', 'nesta', 'ordem', 'include',
     'stdio', 'h', 'void', 'soma', 'float', 'a', 'int', 'b', 'basta', 'separar', 'os', 'parâmetros', 'por', 'vírgulas',
     'float', 'result', 'a', 'declaração', 'de', 'variáveis', 'é', 'igual', 'ao', 'que', 'se', 'faz', 'na', 'função',
     'main', 'result', 'a', 'b', 'printf', 'a', 'soma', 'de', '6', '3f', 'com', 'd', 'é', '6', '3f', 'n', 'a', 'b',
     'result', 'int', 'main', 'int', 'a', 'float', 'b', 'a', '10', 'b', '12', '3', 'soma', 'b', 'a', 'chamada', 'da',
     'função', 'soma', '12', '3', '10', 'return', '0', 'o', 'resultado', 'do', 'programa', 'é', 'a', 'impressão', 'da',
     'seguinte', 'mensagem', 'a', 'soma', 'de', '12', '300', 'com', '10', 'é', '22', '300', 'localização', 'das',
     'funções', 'no', 'fonte', 'a', 'princípio', 'podemos', 'tomar', 'com', 'regra', 'a', 'seguinte', 'afirmativa',
     'toda', 'função', 'deve', 'ser', 'declarada', 'antes', 'de', 'ser', 'usada', 'a', 'declaração', 'de', 'uma',
     'função', 'em', 'linguagem', 'c', 'não', 'é', 'exatamente', 'o', 'que', 'fizemos', 'até', 'agora', 'o', 'que',
     'estamos', 'fazendo', 'é', 'a', 'definição', 'da', 'função', 'antes', 'de', 'seu', 'uso', 'na', 'definição', 'da',
     'função', 'está', 'implícita', 'a', 'declaração', 'alguns', 'programadores', 'preferem', 'que', 'o', 'início',
     'do', 'programa', 'seja', 'a', 'primeira', 'parte', 'de', 'seu', 'programa', 'para', 'isto', 'a', 'linguagem', 'c',
     'permite', 'que', 'se', 'declare', 'uma', 'função', 'antes', 'de', 'defini-la', 'esta', 'declaração', 'é', 'feita',
     'através', 'do', 'protótipo', 'da', 'função', 'o', 'protótipo', 'da', 'função', 'nada', 'mais', 'é', 'do', 'que',
     'o', 'trecho', 'de', 'código', 'que', 'especifica', 'o', 'nome', 'e', 'os', 'parâmetros', 'da', 'função', 'no',
     'exemplo', 'a', 'seguir', 'a', 'função', 'soma', 'é', 'prototipada', 'antes', 'de', 'ser', 'usada', 'e', 'assim',
     'pôde', 'ser', 'chamada', 'antes', 'de', 'ser', 'definida', 'include', 'stdio', 'h', 'void', 'soma', 'float', 'a',
     'int', 'b', 'protótipo', 'da', 'função', 'soma', 'void', 'main', 'soma', '16', '7', '15', 'chamada', 'da',
     'função', 'soma', 'antes', 'de', 'sua', 'definição', 'mas', 'após', 'sua', 'prototipação', 'int', 'soma', 'float',
     'a', 'int', 'b', 'definição', 'da', 'função', 'soma', 'float', 'result', 'a', 'declaração', 'de', 'variáveis', 'é',
     'igual', 'ao', 'que', 'se', 'faz', 'na', 'função', 'main', 'result', 'a', 'b', 'printf', 'a', 'soma', 'de', 'f',
     'com', 'd', 'é', '6', '3f', 'n', 'a', 'b', 'result', 'return', '0', 'atenção', 'existem', 'compiladores', 'mais',
     'simplificados', 'ou', 'antigos', 'que', 'não', 'obrigam', 'a', 'declaração', 'da', 'funçãoantes', 'de', 'seu',
     'uso', 'muito', 'cuidado', 'com', 'eles', 'veja', 'no', 'item', 'a', 'seguir', 'verificação', 'dos', 'tipos',
     'dos', 'parâmetros', 'a', 'princípio', 'dados', 'usados', 'parâmetros', 'atuais', 'aqueles', 'da', 'chamada', 'da',
     'função', 'devem', 'ser', 'dos', 'mesmos', 'tipos', 'dos', 'parâmetros', 'formais', 'se', 'isto', 'não', 'ocorrer',
     'mas', 'a', 'declaração', 'da', 'função', 'vier', 'antes', 'de', 'seu', 'uso', 'os', 'compiladores', 'c',
     'modernos', 'se', 'encarregam', 'de', 'converter', 'automaticamente', 'os', 'tipos', 'como', 'se', 'estivesemos',
     'usando', 'um', 'cast', 'entretanto', 'tenha', 'muito', 'cuidado', 'se', 'as', 'três', 'condições', 'a', 'seguir',
     'se', 'verificarem', 'se', 'você', 'estiver', 'usando', 'um', 'compilador', 'que', 'não', 'exige', 'a',
     'declaração', 'antes', 'da', 'função', 'antes', 'de', 'seu', 'uso', 'se', 'voce', 'usar', 'uma', 'função', 'antes',
     'de', 'tê-la', 'prototipado', 'declarado', 'se', 'os', 'parâmetros', 'formais', 'e', 'reais', 'não', 'forem',
     'exatamente', 'do', 'mesmo', 'tipo', 'se', 'as', 'três', 'condições', 'se', 'verificarem', 'o', 'resultado', 'da',
     'execução', 'da', 'função', 'é', 'ímprevisível', 'no', 'caso', 'de', 'você', 'declarar', 'corretamente', 'a',
     'função', 'antes', 'de', 'usá-la', 'a', 'conversão', 'de', 'tipos', 'é', 'feita', 'como', 'no', 'caso', 'de',
     'variáveis', 'no', 'exemplo', 'a', 'seguir', 'a', 'função', 'soma', 'é', 'chamada', 'com', 'os', 'parâmetros',
     'reais', 'dos', 'tipos', 'int', 'e', 'float', 'nesta', 'ordem', 'como', 'na', 'declaração', 'da', 'função', 'o',
     'primeiro', 'parâmetro', 'é', 'float', 'e', 'o', 'segundo', 'é', 'int', 'é', 'feita', 'uma', 'conversão', 'de',
     'int', 'para', 'floa', 't', 'no', 'caso', 'do', 'primeiro', 'parâmetro', 'e', 'de', 'float', 'para', 'int', 'no',
     'caso', 'do', 'segundo', 'parâmetro', 'include', 'stdio', 'h', 'void', 'soma', 'float', 'a', 'int', 'b',
     'protótipo', 'da', 'função', 'soma', 'void', 'main', 'float', 'f', 'f', '20', '7', 'soma', '16', 'f', 'neste',
     'exemplo', 'o', 'primeiro', 'parâmetro', 'é', 'convertido', 'para', '16', '0', 'e', 'o', 'segundo', 'para', '20',
     'o', 'que', 'ocorre', 'de', 'fato', 'é', 'que', 'a', 'chamada', 'da', 'função', 'é', 'feita', 'como', 'se',
     'mesma', 'fosse', 'substituída', 'por', 'soma', 'float', '16', 'int', 'f', 'escopo', 'de', 'variáveis', 'por',
     'escopo', 'de', 'uma', 'variável', 'entende-se', 'o', 'bloco', 'de', 'código', 'onde', 'esta', 'variável', 'é',
     'válida', 'com', 'base', 'nisto', 'temos', 'as', 'seguintes', 'afirmações', 'as', 'variáveis', 'valem', 'no',
     'bloco', 'que', 'são', 'definidas', 'as', 'variáveis', 'definidas', 'dentro', 'de', 'uma', 'função', 'recebem',
     'o', 'nome', 'de', 'variáveis', 'locais', 'os', 'parâmetros', 'formais', 'de', 'uma', 'função', 'valem', 'também',
     'somente', 'dentro', 'da', 'função', 'uma', 'variável', 'definida', 'dentro', 'de', 'uma', 'função', 'não', 'é',
     'acessível', 'em', 'outras', 'funções', 'mesmo', 'estas', 'variáveis', 'tenham', 'nome', 'idênticos', 'no',
     'trecho', 'de', 'código', 'a', 'seguir', 'tem-se', 'um', 'exemplo', 'com', 'funções', 'e', 'variáveis', 'com',
     'nomes', 'iguais', 'include', 'stdio', 'h', 'void', 'func1', 'int', 'b', 'b', '-100', 'printf', 'valor', 'de', 'b',
     'dentro', 'da', 'função', 'func1', 'd', 'n', 'b', 'void', 'func2', 'int', 'b', 'b', '-200', 'printf', 'valor',
     'de', 'b', 'dentro', 'da', 'função', 'func2', 'd', 'n', 'b', 'void', 'main', 'int', 'b', 'b', '10', 'printf',
     'valor', 'de', 'b', 'd', 'n', 'b', 'b', '20', 'func1', 'printf', 'valor', 'de', 'b', 'd', 'n', 'b', 'b', '30',
     'func2', 'printf', 'valor', 'de', 'b', 'd', 'n', 'b', 'getch', 'saída', 'valor', 'de', 'b', '10', 'valor', 'de',
     'b', 'dentro', 'da', 'função', 'func1', '-100', 'valor', 'de', 'b', '20', 'valor', 'de', 'b', 'dentro', 'da',
     'função', 'func2', '-200', 'valor', 'de', 'b', '30', 'sugere-se', 'antes', 'da', 'leitura', 'das', 'próximas',
     'seções', 'a', 'consulta', 'à', 'página', 'sobre', 'ponteiros', 'passagem', 'de', 'parâmetros', 'por',
     'referência', 'a', 'passagem', 'de', 'parâmetros', 'apresentada', 'a', 'até', 'aqui', 'é', 'chamada', 'de',
     'passagem', 'por', 'valor', 'nesta', 'modalidade', 'a', 'chamada', 'da', 'função', 'passa', 'o', 'valor', 'do',
     'parâmetro', 'para', 'a', 'função', 'desta', 'forma', 'alterações', 'do', 'parâmetro', 'dentro', 'da', 'função',
     'não', 'afetarão', 'a', 'variável', 'usada', 'na', 'chamada', 'da', 'função', 'no', 'exemplo', 'a', 'seguir', 'a',
     'variável', 'f', 'passada', 'por', 'parâmetro', 'para', 'a', 'função', 'zera', 'não', 'será', 'alterado', 'dentro',
     'da', 'função', 'include', 'stdio', 'h', 'void', 'zera', 'float', 'a', 'a', '0', 'void', 'main', 'float', 'f', 'f',
     '20', '7', 'zera', 'f', 'printf', 'd', 'f', 'o', 'valor', 'impresso', 'será', '20', '7', 'pois', 'o', 'parâmetro',
     'da', 'função', 'foi', 'passado', 'por', 'valor', 'para', 'permitir', 'a', 'alteração', 'da', 'variável', 'usada',
     'como', 'parâmetro', 'é', 'preciso', 'passar', 'o', 'endereço', 'da', 'variável', 'caracterizando', 'desta',
     'forma', 'uma', 'passagem', 'por', 'referência', 'para', 'passar', 'o', 'endereço', 'de', 'uma', 'variável',
     'para', 'uma', 'função', 'deve-se', 'tomar', 'as', 'seguintes', 'providências', '-', 'na', 'chamada', 'da',
     'função', 'deve-se', 'usar', 'o', 'operador', 'antes', 'do', 'nome', 'da', 'variável', '-', 'no', 'cabeçalho',
     'da', 'função', 'declarar', 'o', 'parâmetro', 'como', 'um', 'ponteiro', '-', 'dentro', 'da', 'função', 'deve-se',
     'usar', 'o', 'operado', 'de', 'derreferência', 'para', 'alterar', 'o', 'conteúdo', 'da', 'variável', 'o',
     'exemplo', 'a', 'seguir', 'apresenta', 'uma', 'nova', 'versão', 'da', 'função', 'zera', 'desta', 'feita', 'com',
     'o', 'uso', 'de', 'um', 'parâmetro', 'passado', 'por', 'referência', 'include', 'stdio', 'h', 'void', 'zera',
     'float', 'a', 'define', 'que', 'o', 'parâmetro', 'é', 'uma', 'referência', 'à', 'outra', 'variável', 'a', '0',
     'utiliza', 'o', 'operador', 'de', 'derreferência', 'para', 'alterar', 'o', 'conteúdo', 'da', 'variável', 'void',
     'main', 'float', 'f', 'f', '20', '7', 'zera', 'f', 'passa', 'o', 'endereço', 'da', 'variável', 'f', 'para', 'a',
     'função', 'printf', 'd', 'f', 'o', 'valor', 'impresso', 'será', '0', '0', 'pois', 'o', 'parâmetro', 'da', 'função',
     'foi', 'passado', 'por', 'referência', 'passagem', 'de', 'vetores', 'por', 'parâmetros', 'a', 'passagem', 'de',
     'vetores', 'por', 'parâmetro', 'é', 'sempre', 'por', 'referência', 'isto', 'significa', 'que', 'não', 'se', 'deve',
     'na', 'chamada', 'da', 'função', 'passar', 'o', 'endereço', 'do', 'vetor', 'isto', 'ocorre', 'pois', 'por',
     'convenção', 'o', 'nome', 'do', 'vetor', 'já', 'representa', 'o', 'endereço', 'inicial', 'deste', 'vetor',
     'namemória', 'no', 'cabeçalho', 'da', 'função', 'que', 'recebe', 'um', 'vetor', 'há', 'duas', 'formas', 'de',
     'definir', 'o', 'parâmetro', 'que', 'é', 'um', 'vetor', 'na', 'primeira', 'declara-se', 'o', 'vetor', 'como', 'se',
     'faz', 'normalmente', 'na', 'linguagem', 'o', 'exemplo', 'a', 'seguir', 'mostra', 'o', 'uso', 'desta', 'abordagem',
     'void', 'zeravet', 'float', 'v', '10', 'int', 'qtd', 'int', 'i', 'for', 'i', '0', 'i', 'qtd', 'i', 'v', 'i', '0',
     '0', 'void', 'main', 'int', 'i', 'float', 'vet', '10', 'zeravet', 'vet', '10', 'passa', 'o', 'nome', 'do', 'vetor',
     'como', 'parâmetro', 'for', 'i', '0', 'i', '10', 'i', 'printf', 'd', 'vet', 'i', 'todos', 'os', 'elementos',
     'terão', 'valor', '0', '0', 'na', 'segunda', 'abordagem', 'pode-se', 'declarar', 'o', 'parâmetro', 'como', 'um',
     'ponteiro', 'para', 'o', 'tipo', 'de', 'dado', 'que', 'forma', 'o', 'vetor', 'no', 'caso', 'do', 'exemplo', 'a',
     'seguir', 'como', 'o', 'vetro', 'foi', 'declarado', 'com', 'um', 'vetor', 'de', 'float', 'o', 'parâmetro', 'da',
     'função', 'deve', 'ser', 'float', 'v', 'no', 'código', 'da', 'função', 'o', 'acesso', 'aos', 'dados', 'do',
     'vetor', 'é', 'feito', 'da', 'mesma', 'maneira', 'que', 'é', 'feito', 'quando', 'se', 'declara', 'o', 'vetor',
     'explicitamente', 'void', 'zeravet2', 'float', 'v', 'int', 'qtd', 'int', 'i', 'for', 'i', '0', 'i', 'qtd', 'i',
     'v', 'i', '0', 'void', 'main', 'int', 'i', 'float', 'vet', '10', 'zeravet', 'vet', '10', 'passa', 'o', 'nome',
     'do', 'vetor', 'como', 'parâmetro', 'for', 'i', '0', 'i', '10', 'i', 'printf', 'd', 'vet', 'i', 'todos', 'os',
     'elementos', 'terão', 'valor', '0', '0']}

    perg1 = Pergunta(['ponteiros', 'Python', 'abacate', 'são', 'legal', 'legal'])


    tf_idf([doc1, doc2], [perg1])
    print(doc1)
    print(doc2)
    print(perg1)
    #print(doc3)
    #print(doc4)
    #print(doc5)