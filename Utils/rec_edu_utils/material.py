from rec_edu_utils import Item, Field

class Material(Item):

    _id = Field()
    titulo = Field()
    link = Field()
    resumo = Field()
    tipo = Field()
    termos = Field()
