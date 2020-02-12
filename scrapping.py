
from elasticsearch import Elasticsearch

def connect():
    es = Elasticsearch(['http://localhost:9200/'], verify_certs=True)
    if not es.ping():
        raise ValueError("Connection failed")
        
    print("Vous êtes connectés")

