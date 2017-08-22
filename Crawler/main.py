'''
Módulo principal
'''

import sys
import preRecomendador

def main():

    termoBusca = input("Termo de busca: ")
    #termoBusca = "Programação em C"

    if len(sys.argv) != 3:
        return

    chaveAPI = sys.argv[1]
    pesquisaID = sys.argv[2]

    itens = preRecomendador.get_itens(termoBusca, chaveAPI, pesquisaID)

    i = 0
    print()

    for item in itens:
        i += 1
        print(i)
        print("Titulo: " + item.get('titulo'))
        print("Link: " + item.get('link'))
        print("Resumo: " + item.get('resumo'))
        print("Tipo: " + item.get('tipo'))
        print("Vetor de termos:\n" + str(item.get('termos')))
        print()

if __name__ == "__main__":
    main()