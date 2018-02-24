from rec_edu_utils import Item, Field


class Pergunta(Item):

    _id = Field()
    enunciado = Field()
    alternativas = Field()
    alt_correta = Field()
    tema = Field()
    termos = Field()
