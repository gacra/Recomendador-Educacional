from rec_edu_utils.models import Item, Field


class Question(Item):
    _id = Field()
    stem = Field()
    alternatives = Field()
    correct_alt = Field()
    topic = Field()
    terms = Field()
