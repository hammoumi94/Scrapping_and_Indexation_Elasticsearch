from elasticsearch import helpers, Elasticsearch
import csv
import json

es = Elasticsearch()


def index():
    with open('./output.json') as f:
        helpers.bulk(es, json.load(f), index='films', doc_type='films')
