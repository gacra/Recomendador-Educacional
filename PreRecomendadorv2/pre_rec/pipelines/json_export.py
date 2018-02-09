from scrapy.exporters import JsonLinesItemExporter
import os

class JsonExport(object):

    def open_spider(self, spider):
        if spider.settings.get('EXPORTER_PATH'):
            path = spider.settings.get('EXPORTER_PATH')
        else:
            path = '../' + os.getcwd().split('/')[-1] + 'Data'

        nome_arq = spider.name + '.json'

        self._arq = open(path + nome_arq, 'w+b')
        self._exporter = JsonLinesItemExporter(self._arq)

    def process_item(self, item, spider):
        self._exporter.export_item(item)
        spider.p_bar.update()
        return item

    def close_spider(self, spider):
        self._arq.close()