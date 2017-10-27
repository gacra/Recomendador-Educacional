'''
Módulo principal
'''

#Módulos internos
import preRecomendador
#Módulos externos
import  pickle
import sys

def main():

    #termoBusca = input("Termo de busca: ")
    termosBusca = ["Ponteiros em C", "Funções em C"]

    if len(sys.argv) != 3:
        return

    chaveAPI = sys.argv[1]
    pesquisaID = sys.argv[2]

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