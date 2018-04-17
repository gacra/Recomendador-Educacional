from rec_edu_utils.models import Item, Field


class Pergunta(Item):

    _id = Field()
    enunciado = Field()
    alternativas = Field()
    alt_correta = Field()
    tema = Field()
    termos = Field()
