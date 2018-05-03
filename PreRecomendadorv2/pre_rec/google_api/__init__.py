import os
import logging

logging.getLogger('googleapiclient.discovery').setLevel(logging.ERROR)
logging.getLogger('googleapiclient.discovery_cache').setLevel(logging.ERROR)

api_key = os.environ['API_KEY']
search_id = os.environ['SEARCH_ID']
