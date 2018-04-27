import scrapy
from tqdm import tqdm
import logging

from rec_edu_utils.models.temas import Temas

from pre_rec.spider.parser_material import ParserMaterial
from pre_rec.google_api.busca import googleSearch

logging.getLogger().setLevel(logging.ERROR)

class SpiderMateriais(scrapy.Spider):
    name = 'ext_mat_edu'

    custom_settings = {
        "ITEM_PIPELINES": {
            'pre_rec.pipelines.pdf_parser.PdfParser': 101,
            'pre_rec.pipelines.freq_calc.FreqCalc': 201,
            'pre_rec.pipelines.json_export.JsonExport': 301
        }
    }

    p_bar = None

    def start_requests(self):
        lista_resultados = []

        for termo_busca in tqdm(Temas, desc='GoogleSearch'):
            lista_resultados += googleSearch(termo_busca)

        self.p_bar = tqdm(desc='Materiais', total=len(lista_resultados))

        for resultado in lista_resultados:
            material = ParserMaterial.get_metadados(resultado)
            yield scrapy.Request(material['link'],
                                 meta={'Material': material},
                                 callback=self.parse,
                                 errback=self.errback)

    def parse(self, response):
        status = ParserMaterial.get_conteudo(self, response)
        if status:
            yield response.meta['Material']

    def errback(self, failure):
        self.logger.warning('{} | {}'.format(failure.type, failure.value))
        self.p_bar.total -= 1
        self.p_bar.refresh()
