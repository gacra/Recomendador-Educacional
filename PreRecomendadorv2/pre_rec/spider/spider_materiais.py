import scrapy
from tqdm import tqdm

from pre_rec.spider.parser_material import ParserMaterial

from pre_rec.google_api.busca import googleSearch
from pre_rec.spider import lista_termos_busca

class SpiderMateriais(scrapy.Spider):
    name = 'ext_mat_edu'

    p_bar = None

    def start_requests(self):
        lista_resultados = []

        for termo_busca in tqdm(lista_termos_busca, desc='GoogleSearch'):
            lista_resultados += googleSearch(termo_busca)

        self.p_bar = tqdm(desc='Materiais', total=len(lista_resultados))

        for resultado in lista_resultados:
            material = ParserMaterial.get_metadados(resultado)
            yield scrapy.Request(material['link'], meta={'Material': material})

    def parse(self, response):
        self.p_bar.update()
        self.logger.info(response.meta['Material']['titulo'])