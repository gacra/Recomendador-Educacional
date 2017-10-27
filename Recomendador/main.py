if __name__ == "__main__":
    teste = [(4, {"nome": "Jão", "idade": 17}), (2, {"nome": "Marcos", "idade": 29})]
    print(teste)
    teste.sort(key=lambda tup: tup[0])
    print(teste)