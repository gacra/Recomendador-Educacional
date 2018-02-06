from rec_edu_utils.item import Item


class ParserMaterial(object):
    @staticmethod
    def get_metadados(item):
        titulo = item.get('title')
        link = item.get('link')
        resumo = item.get('snippet').replace(u"\n", "").replace(u"\xa0", "")

        tipo_item = item.get('fileFormat')
        if tipo_item is None:
            tipo_item = 'html'
        elif tipo_item == 'PDF/Adobe Acrobat':
            tipo_item = 'pdf'
        else:
            tipo_item = 'outro'

        return Item(titulo=titulo, link=link, resumo=resumo, tipo=tipo_item)
