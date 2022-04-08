import os
from elasticsearch import Elasticsearch

def init_elasticsearch():
    es_client = None
    print('Connecting to Elasticsearch')
    try:
        es_client = Elasticsearch(
            os.environ.get('ELASTICSEARCH_HOST'),
            basic_auth=(os.environ.get('ELASTICSEARCH_USERNAME'), os.environ.get('ELASTICSEARCH_PASSWORD'))
        )
        print('* ELK: OK')
    except Exception as e:
        print('* ELK: ' + str(e))

    return es_client
