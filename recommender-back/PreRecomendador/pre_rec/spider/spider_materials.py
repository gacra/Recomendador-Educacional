import scrapy
from rec_edu_utils.models.topics import Topics
from tqdm import tqdm

from pre_rec.google_api.search import googleSearch
from pre_rec.spider.parser_material import ParserMaterial


class SpiderMaterials(scrapy.Spider):
    name = 'ext_edu_mat'

    custom_settings = {
        "ITEM_PIPELINES": {
            'pre_rec.pipelines.pdf_parser.PdfParser': 101,
            'pre_rec.pipelines.requirements.CheckRequirements': 201,
            'pre_rec.pipelines.freq_calc.FreqCalc': 301,
            'pre_rec.pipelines.json_export.JsonExport': 401,
            'pre_rec.pipelines.db_export.Neo4jDBExport': 501
        }
    }

    p_bar = None
    tqdm.monitor_interval = 0

    def start_requests(self):
        self.crawler.stats.set_value('itens_extracted', [])

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
            material = response.meta['Material']
            self.add_to_stats('itens_extracted', material.title)
            yield material

    def errback(self, failure):
        self.logger.warning('{} | {}'.format(failure.type, failure.value))
        self.p_bar.total -= 1
        self.p_bar.refresh()

    def add_to_stats(self, stat_name, value):
        stat_value = self.crawler.stats.get_value(stat_name)
        stat_value.append(value)
        self.crawler.stats.set_value(stat_name, stat_value)
