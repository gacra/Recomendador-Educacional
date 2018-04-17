from rec_edu_utils.models import Item, Field


class Material(Item):

    _id = Field()
    titulo = Field()
    link = Field()
    resumo = Field()
    tipo = Field()
    tema = Field()
    termos = Field()
