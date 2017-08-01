import gCrawler

busca = gCrawler.search_links(input('>> Buscar: '))

i=0

for result in busca[3:4]:
    i += 1
    print("Resultado " + str(i) + " :")
    print("Título: " + result[0])
    print("Link: " + result[1])
    print("Resumo: " + result[2])
    print()
    result_text = gCrawler.see_result(result[1])
    print(result_text)