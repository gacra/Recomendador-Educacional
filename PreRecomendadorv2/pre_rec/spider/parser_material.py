import re
from bs4 import BeautifulSoup
from uuid import uuid5, NAMESPACE_X500

from rec_edu_utils.models.material import Material
from pre_rec import RE_TERMOS


class ParserMaterial(object):
    @staticmethod
    def get_metadados(resultado):
        titulo = resultado.get('title')
        link = resultado.get('link')
        resumo = resultado.get('snippet')
        resumo = resumo.replace(u"\n", "").replace(u"\xa0", "")
        tema = resultado.get('termo_busca')
        _id = 're_material.' + uuid5(NAMESPACE_X500, link).hex

        tipo_item = resultado.get('fileFormat')
        if tipo_item is None:
            tipo_item = 'html'
        elif tipo_item == 'PDF/Adobe Acrobat':
            tipo_item = 'pdf'
        else:
            tipo_item = 'outro'

        return Material(_id=_id,
                        titulo=titulo,
                        link=link,
                        resumo=resumo,
                        tipo=tipo_item,
                        tema=tema)

    @staticmethod
    def get_conteudo(spider, response):
        material = response.meta['Material']
        spider.logger.info(response.meta['Material']['titulo'])

        if material.tipo == 'pdf':
            return True
        if material.tipo == 'outro':
            return False

        soup = BeautifulSoup(response.body, "html.parser")

        for script in soup.find_all(['script', 'style']):
            script.extract()

        conteudo = re.findall(RE_TERMOS, soup.getText(separator=u" ").lower())

        material.termos = conteudo
        return True
