class Item:

    def __init__(self, titulo: str, link: str, resumo: str, tipo: str, termos: str = None):
        """
Classe representativa de um item (página web).
        :param titulo: Título do item.
        :param link: Link para a página.
        :param tipo: Tipo da página ('html'|'pdf'|'outro')
        :param termos: Termos da página (inicialmente uma lista de termos, depois um dic com (termo, tf_idf)
        """
        self.titulo = titulo
        self.link = link
        self.resumo = resumo
        self.tipo = tipo
        self.termos = termos

    def __str__(self):
        return '{' + "'titulo': {}, 'link': {}, 'tipo': {}, 'termos': {}".format(self.titulo, self.link, self.tipo, self.termos) + '}'

    def __repr__(self):
        return '{' + "'titulo': {}, 'link': {}, 'tipo': {}, 'termos': {}".format(self.titulo, self.link, self.tipo, self.termos) + '}'