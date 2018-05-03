import scrapy
from tqdm import tqdm

from rec_edu_utils.models.topics import Topics

from pre_rec.spider.parser_material import ParserMaterial
from pre_rec.google_api.search import googleSearch

class SpiderMaterials(scrapy.Spider):
    name = 'ext_edu_mat'

    custom_settings = {
        "ITEM_PIPELINES": {
            'pre_rec.pipelines.pdf_parser.PdfParser': 101,
            'pre_rec.pipelines.freq_calc.FreqCalc': 201,
            'pre_rec.pipelines.json_export.JsonExport': 301
        }
    }

    p_bar = None

    def start_requests(self):
        result_list = []

        for search_term in tqdm(Topics, desc='GoogleSearch'):
            result_list += googleSearch(search_term)

        self.p_bar = tqdm(desc='Materials', total=len(result_list))

        for result in result_list:
            material = ParserMaterial.get_metadata(result)
            yield scrapy.Request(material['link'],
                                 meta={'Material': material},
                                 callback=self.parse,
                                 errback=self.errback)

    def parse(self, response):
        status = ParserMaterial.get_content(self, response)
        if status:
            yield response.meta['Material']

    def errback(self, failure):
        self.logger.warning('{} | {}'.format(failure.type, failure.value))
        self.p_bar.total -= 1
        self.p_bar.refresh()
