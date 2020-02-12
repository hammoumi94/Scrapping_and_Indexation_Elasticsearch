from elasticsearch import helpers, Elasticsearch
import csv
import json

es = Elasticsearch()


def index():
    settings = {
        "settings": {
            "number_of_shards": 1,
            "number_of_replicas": 0
        },
        "mappings": {

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
                        "type" : "number"
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

    request_body = {
	    "settings" : {
	        "number_of_shards": 5,
	        "number_of_replicas": 1
	    },

	    'mappings': {
	        'examplecase': {
	            'properties': {
	                'address': {'index': 'not_analyzed', 'type': 'string'},
	                'date_of_birth': {'index': 'not_analyzed', 'format': 'dateOptionalTime', 'type': 'date'},
	                'some_PK': {'index': 'not_analyzed', 'type': 'string'},
	                'fave_colour': {'index': 'analyzed', 'type': 'string'},
	                'email_domain': {'index': 'not_analyzed', 'type': 'string'},
	            }}}
	}

    test = {
            "settings": {
                "number_of_shards": 5,
                "number_of_replicas": 1
            },
            "mappings" : {
                "properties": {
                    "rating" : {
                        "type": "double"
                    },
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
                            "properties" : {
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
                            }
                    },
                "ingredients": {
                    "type" : "nested"
                    
                }
            }
            }
        }

    ggg = {
                "mappings": {
                    "properties": {
                    "age":    { "type": "integer" },  
                    "email":  { "type": "keyword"  }, 
                    "name":   { "type": "text"  }     
                    }
                }
            }
    object = {
        "age" : "23",
        "email" : "test@test.com",
        "name" : "test"
    }



    with open('./data.json') as f:
        #es.indices.create(index='kaka', body=test)
        helpers.bulk(es, f, index='kaka', doc_type='pepe')

index()