import logging
from bs4 import BeautifulSoup
import requests

from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine

def make_soup(url: str):
    """
Cria e retorna um objeto soup
    :param url: URL da página
    :return: Objeto soup
    """
    r = requests.get(url, timeout = 5.0)
    return BeautifulSoup(r.content, "html.parser")

#Usando pdfminer
#Alternativa: pypdf2
def pdf2txt(path: str) -> str:
    """
Transforma um arquivo pdf em uma string
    :param path: Caminho para o arquivo pdf
    :return: String com o texto do pdf
    """
    logging.propagate = False
    logging.getLogger().setLevel(logging.ERROR)
    fp = open(path, 'rb')
    parser = PDFParser(fp)
    doc = PDFDocument()
    parser.set_document(doc)
    doc.set_parser(parser)
    doc.initialize('')
    rsrcmgr = PDFResourceManager()
    '''
    laparams = LAParams()
    laparams.char_margin = 1.0
    laparams.word_margin = 1.0
    '''
    laparams = LAParams()
    for param in ("all_texts", "detect_vertical", "word_margin", "char_margin", "line_margin", "boxes_flow"):
        paramv = locals().get(param, None)
        if paramv is not None:
            setattr(laparams, param, paramv)

    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    extracted_text = ''

    for page in doc.get_pages():
        interpreter.process_page(page)
        layout = device.get_result()
        for lt_obj in layout:
            if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
                extracted_text += lt_obj.get_text()

    fp.close()

    return extracted_text