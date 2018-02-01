'''
Módulo principal
'''

#Módulos internos
import preRecomendador
#Módulos externos
import  pickle
import sys
import os

def main():

    #termoBusca = input("Termo de busca: ")
    termosBusca = ["Tipos de dados em C",
                   "Comandos de repetição em C",
                   "Ponteiros em C",
                   "Funções em C",
                   "Recursão em C"]

    chaveAPI = os.environ['CHAVE_API']
    pesquisaID = os.environ['PESQUISA_ID']

    itens, perguntas = preRecomendador.get_itens(termosBusca, chaveAPI, pesquisaID, '../exemploPerguntas.txt')

    i = 0
    print()

    for item in itens:
        i += 1
        print(i)
        print("Titulo: " + item.titulo)
        print("Link: " + item.link)
        print("Resumo: " + item.resumo)
        print("Tipo: " + item.tipo)
        print("TF-IDF:\n" + str(item.termos))
        print()

    for pergunta in perguntas:
        print("ID: " + str(pergunta.id))
        print("Pseudo TF-IDF: " + str(pergunta.termosPerg))

    with open('../itens.re', 'wb') as arquivo:
        pickle.dump(itens, arquivo, pickle.HIGHEST_PROTOCOL)

    with open('../perguntas.re', 'wb') as arquivo:
        pickle.dump(perguntas, arquivo, pickle.HIGHEST_PROTOCOL)

if __name__ == "__main__":
    main()