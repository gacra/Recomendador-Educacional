import re
import os
import scrapy
from scrapy.pipelines.files import FilesPipeline

from pre_rec import RE_TERMS

from pre_rec.pdf_to_text import pdf2txt

class PdfParser(FilesPipeline):
    def open_spider(self, spider):
        self.file_path = spider.settings.get('FILES_STORE') + '/'
        return super(PdfParser, self).open_spider(spider)

    def get_media_requests(self, item, info):
        if item.type == 'pdf':
            return scrapy.Request(item.link)

    def item_completed(self, results, item, info):
        if results:
            success, file_info = results[0]
            if success:
                text = pdf2txt(self.file_path + file_info['path'])
                item.terms = re.findall(RE_TERMS, text.lower())
                os.remove(file_info['path'])
        return item
