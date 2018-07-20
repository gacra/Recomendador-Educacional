from enum import Enum
from collections import OrderedDict


class Topics(Enum):
    COMPUTADOR = 'Funcionamento do computador'
    SOFTWARE_HARDWARE = 'Software e hardware'
    NUMERACAO = 'Sistema de numeração'
    BOOLEANA = 'Álgebra booleana'
    ALGORITMO = 'Algoritmo e lógica de programação'

    INTRODUCAO_C = 'Introdução ao C'
    TIPOS_DADOS = 'Tipos de dados em C'
    ENTRADA_SAIDA = 'Entrada e saída em C'
    OPERADORES = 'Operadores em C'
    COMANDOS_REPETICAO = 'Comandos de repetição em C'
    COMANDOS_SELECAO = 'Comandos de seleção em C'
    FUNCOES = 'Funções em C'

    VETORES = 'Vetores em C'
    STRINGS = 'Strings em C'
    MATRIZES = 'Matrizes em C'
    PONTEIROS = 'Ponteiros em C'
    ALOCACAO = 'Alocação dinâmica em C'
    RECURSAO = 'Recursão em C'
    ARQUIVOS = 'Arquivos em C'
    STRUCTS = 'Structs em C'

super_topics = OrderedDict([
    ('Introdução a Ciência da Computação', (0, 5)),
    ('Programação C: Básico', (5, 12)),
    ('Programação C: Avançado', (12, 20))
])