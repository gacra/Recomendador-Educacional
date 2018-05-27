from scrapy.exceptions import DropItem

from pre_rec import MAX_TERMS


class CheckRequirements(object):

    def process_item(self, item, spider):
        if not item.terms:
            message = u'Item without terms'
            raise DropItem(message)
        elif len(item.terms) > MAX_TERMS:
            message = u'Very large material ({} terms)'.format(len(item.terms))
            raise DropItem(message)
        else:
            missing_fields = item.check_requirements()
            if missing_fields:
                message = u'Missing following fields: {}'.format(missing_fields)
                raise DropItem(message)
            else:
                return item
