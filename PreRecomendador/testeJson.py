import json

if __name__ == "__main__":
    with open('../data.re', 'r') as arquivo:
        dado = json.load(arquivo)

    for site in dado:
        print(site['titulo'])