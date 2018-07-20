from rec_edu_utils.models import Item, Field


class Material(Item):
    _id = Field()
    title = Field()
    link = Field()
    summary = Field()
    type = Field()
    topic = Field()
    terms = Field()
