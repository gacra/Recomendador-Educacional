# -*- coding: utf-8 -*-

BOT_NAME = 'pre_rec'

SPIDER_MODULES = ['pre_rec.spider']

NEWSPIDER_MODULE = 'pre_rec.spiders'

AUTOTHROTTLE_ENABLED = True
EXPORTER_PATH = 'output_data/'

LOG_LEVEL = 'INFO'

FILES_STORE = './pdfs'