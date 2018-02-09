import os
import logging

logging.getLogger('googleapiclient.discovery').setLevel(logging.ERROR)
logging.getLogger('googleapiclient.discovery_cache').setLevel(logging.ERROR)

chave_api = os.environ['CHAVE_API']
pesquisa_id = os.environ['PESQUISA_ID']
