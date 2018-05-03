from scrapy.exporters import JsonLinesItemExporter
import os


class JsonExport(object):

    def open_spider(self, spider):
        if spider.settings.get('EXPORTER_PATH'):
            path = spider.settings.get('EXPORTER_PATH')
        else:
            path = '../' + os.getcwd().split('/')[-1] + 'Data'

        file_name = spider.name + '.json'

        self._file = open(path + file_name, 'w+b')
        self._exporter = JsonLinesItemExporter(self._file)

    def process_item(self, item, spider):
        self._exporter.export_item(item)
        spider.p_bar.update()
        return item

    def close_spider(self, spider):
        self._file.close()
