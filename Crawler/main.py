import gCrawler

#busca = gCrawler.search_links(input('>> Buscar: '))
busca = gCrawler.search_links("Programação C")  #Para testes

i=0

for result in busca:
    i += 1
    print("Resultado " + str(i) + " :")
    print("Título: " + result[0])
    print("Link: " + result[1])
    print("Resumo: " + result[2])
    print()
    result_text = gCrawler.get_content(result[1])
    if type(result_text) is list or str:
        print("Conteúdo:")
        print(result_text)
        print()