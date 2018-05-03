from googleapiclient.discovery import build

from pre_rec.google_api import api_key, search_id

'''
To install Google API:
pip install --upgrade google-api-python-client
'''

def googleSearch(search_term):

    service = build("customsearch", "v1", developerKey=api_key)

    result = []

    pageLimit = 2
    startIndex = 1

    search = search_term.value

    for nPage in range(0, pageLimit):
        res = service.cse().list(
            q=search,
            cx=search_id,
            fileType='.htm, .html',
            lr="lang_pt",
            start=startIndex
        ).execute()

        startIndex = res.get("queries").get("nextPage")[0].get("startIndex")

        for item in res.get('items'):
            item['search_term'] = search_term.name
            result.append(item)


    return result