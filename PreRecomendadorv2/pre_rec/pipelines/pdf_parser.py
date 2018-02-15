import scrapy
from scrapy.pipelines.files import FilesPipeline
import logging
import re

from pre_rec.pdf_to_text import pdf2txt

logger = logging.getLogger(__name__)

class PdfParser(FilesPipeline):

    def open_spider(self, spider):
        self.arq_path = spider.settings.get('FILES_STORE') + '/'
        return super(PdfParser, self).open_spider(spider)

    def get_media_requests(self, item, info):
        if item.tipo == 'pdf':
            return scrapy.Request(item.link)

    def item_completed(self, results, item, info):
        if results:
            sucesso, info_arq = results[0]
            if sucesso:
                texto = pdf2txt(self.arq_path + info_arq['path'])
                item.termos = re.findall('[\d\-_]*[^\W\d_][\w-]*', texto.lower())
        return item
