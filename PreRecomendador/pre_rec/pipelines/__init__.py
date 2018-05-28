import logging

from scrapy import logformatter


class PoliteLogFormatter(logformatter.LogFormatter):
    def dropped(self, item, exception, response, spider):
        return {
            'level': logging.WARNING,
            'msg': logformatter.DROPPEDMSG,
            'args': {
                'exception': exception,
                'item': {'title': item.title,
                         'link': item.link,
                         '_id': item._id},
            }
        }
