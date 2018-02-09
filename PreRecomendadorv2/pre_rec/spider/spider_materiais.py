import scrapy
from tqdm import tqdm

from pre_rec.spider.parser_material import ParserMaterial

from pre_rec.google_api.busca import googleSearch
from pre_rec.spider import lista_termos_busca

class SpiderMateriais(scrapy.Spider):
    name = 'ext_mat_edu'

    custom_settings = {
        "ITEM_PIPELINES": {
            'pre_rec.pipelines.json_export.JsonExport': 101
        }
    }

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
        status = ParserMaterial.get_conteudo(self, response)
        if status:
            yield response.meta['Material']