import os
import scrapy
from scrapy.pipelines.files import FilesPipeline

from rec_edu_utils.models.material import Material

from pre_rec.pdf_to_text import pdf2txt

class PdfParser(FilesPipeline):
    def open_spider(self, spider):
        self.files_store_path = spider.settings.get('FILES_STORE') + '/'
        return super(PdfParser, self).open_spider(spider)

    def get_media_requests(self, item, info):
        if isinstance(item, Material) and item.type == 'pdf':
            return scrapy.Request(item.link)

    def item_completed(self, results, item, info):
        if results:
            success, file_info = results[0]
            if success:
                text = pdf2txt(self.files_store_path + file_info['path'])
                item.terms = text
                os.remove(self.files_store_path + file_info['path'])
        return item
