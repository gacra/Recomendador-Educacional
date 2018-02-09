import scrapy
from rec_edu_utils import Item, Field

class Material(Item):

    titulo = Field()
    link = Field()
    resumo = Field()
    tipo = Field()
    termos = Field()

    # def __str__(self):
    #     return '{' + "'titulo': {}, 'link': {}, 'resumo': {}, 'tipo': {}, 'termos': {}".format(self.titulo, self.link,
    #                                                                                            self.resumo, self.tipo,
    #                                                                                            self.termos) + '}'
    #
    # def __repr__(self):
    #     return '{' + "'titulo': {}, 'link': {}, 'resumo': {}, 'tipo': {}, 'termos': {}".format(self.titulo, self.link,
    #                                                                                            self.resumo, self.tipo,
    #                                                                                            self.termos) + '}'
    #
    # def paraDict(self):
    #     return '{' + "'titulo': {}, 'link': {}, 'resumo': {}, 'tipo': {}".format(self.titulo, self.link,
    #                                                                                            self.resumo, self.tipo)+ '}'