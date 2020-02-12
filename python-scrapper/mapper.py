from elasticsearch import Elasticsearch
import pandas as pd

def create_index(es_object, index_name='RECIPES', types="RECIPE"):
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
                            "type" : "double"
                        }, 
                        "fatContent" :{
                            "type" : "double"
                        },
                        "carbohydrateContent" :{
                            "type" : "double"
                        },
                        "cholesterolContent" :{
                            "type" : "double"
                        },
                        "proteinContent" :{
                            "type" : "double"
                        },
                        "sodiumContent" :{
                            "type" : "double"
                        }
                    },
                    "ingredients": {
                        "type": "nested"
                    }
                }
            }
        }
    }
    try:
        if not es_object.indices.exists(index_name):
                # Ignore 400 means to ignore "Index Already Exist" error.
            es_object.indices.create(index=index_name, ignore=400, body=settings)
            print('Created Index')
            created = True
    except Exception as ex:
        print(str(ex))
    finally:
        return created


es = Elasticsearch()
create_index(es)