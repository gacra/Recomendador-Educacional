from scrapy.exporters import JsonLinesItemExporter
from pre_rec.settings import EXPORTER_PATH
import os


class JsonExport(object):

    def open_spider(self, spider):
        if spider and spider.settings.get('EXPORTER_PATH'):
            path = spider.settings.get('EXPORTER_PATH')
            file_name = spider.name + '.json'
        else:
            path = EXPORTER_PATH
            file_name = 'questions.json'

        self._file = open(path + file_name, 'w+b')
        self._exporter = JsonLinesItemExporter(self._file)

    def process_item(self, item, spider):
        self._exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self._file.close()
