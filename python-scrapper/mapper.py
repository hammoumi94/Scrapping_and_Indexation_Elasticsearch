from elasticsearch import Elasticsearch
import pandas as pd

def create_index(es_object, index_name='recipes', types="recipe"):
    created = False
    # index settings
    settings = {
        "settings": {
            "number_of_shards": 1,
            "number_of_replicas": 0
        },
        "mappings": {
            "members": {
                "dynamic": "strict",
                "properties": {
                    "title": {
                        "type": "text"
                    },
                    "submitter": {
                        "type": "text"
                    },
                    "description": {
                        "type": "text"
                    },
                    "nutrition_facts": {
                        "calories": {

                        }, 
                        "fatContent" :{

                        }
                    },
                }
            }
        }
    }
    try:
        if not es_object.indices.exists(index_name):
                # Ignore 400 means to ignore "Index Already Exist" error.
            es_object.indices.create(index=index_name, type=types, ignore=400, body=settings)
            print('Created Index')
            created = True
    except Exception as ex:
        print(str(ex))
    finally:
            return created


es = Elasticsearch(['http://localhost:9200/'], verify_certs=True)
create_index(es)