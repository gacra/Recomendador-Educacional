#Múdulos externos
import  pickle

if __name__ == "__main__":
    with open('../itens.re', 'rb') as arquivo:
        dado = pickle.load(arquivo)

    for site in dado:
        print(site.titulo)
    print()

    with open('../perguntas.re', 'rb') as arquivo:
        dado = pickle.load(arquivo)

    for pergunta in dado:
        print(str(pergunta.id) + "\n" + str(pergunta.termosPerg))