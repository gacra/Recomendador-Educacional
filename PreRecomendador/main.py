'''
Módulo principal
'''

import sys
import preRecomendador
import json

def main():

    #termoBusca = input("Termo de busca: ")
    termosBusca = ["Ponteiros em C", "Funções em C"]

    if len(sys.argv) != 3:
        return

    chaveAPI = sys.argv[1]
    pesquisaID = sys.argv[2]

    itens = preRecomendador.get_itens(termosBusca, chaveAPI, pesquisaID)

    i = 0
    print()

    for item in itens:
        i += 1
        print(i)
        print("Titulo: " + item.get('titulo'))
        print("Link: " + item.get('link'))
        print("Resumo: " + item.get('resumo'))
        print("Tipo: " + item.get('tipo'))
        print("TF-IDF:\n" + str(item.get('tf_idf')))
        print()


    with open('../data.re', 'w') as arquivo:
        json.dump(itens, arquivo)

if __name__ == "__main__":
    main()