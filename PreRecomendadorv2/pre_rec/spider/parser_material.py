import re
from bs4 import BeautifulSoup
from uuid import uuid5, NAMESPACE_X500

from rec_edu_utils.models.material import Material
from pre_rec import RE_TERMS


class ParserMaterial(object):

    @staticmethod
    def get_metadata(result):
        title = result.get('title')
        link = result.get('link')
        summary = result.get('snippet')
        summary = summary.replace(u"\n", "").replace(u"\xa0", "")
        topic = result.get('search_term')
        _id = 're_material.' + uuid5(NAMESPACE_X500, link).hex

        type_item = result.get('fileFormat')
        if type_item is None:
            type_item = 'html'
        elif type_item == 'PDF/Adobe Acrobat':
            type_item = 'pdf'
        else:
            type_item = 'other'

        return Material(_id=_id,
                        title=title,
                        link=link,
                        summary=summary,
                        type=type_item,
                        topic=topic)

    @staticmethod
    def get_content(spider, response):
        material = response.meta['Material']
        spider.logger.info(response.meta['Material']['title'])

        if material.type == 'pdf':
            return True
        if material.type == 'other':
            spider.logger.info('[Dropped item] Unsupported type')
            spider.p_bar.total -= 1
            spider.p_bar.refresh()
            return False

        soup = BeautifulSoup(response.body, "html.parser")

        for script in soup.find_all(['script', 'style']):
            script.extract()

        content = re.findall(RE_TERMS, soup.getText(separator=u" ").lower())

        material.terms = content
        return True
