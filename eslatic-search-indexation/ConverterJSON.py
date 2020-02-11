from elasticsearch import helpers, Elasticsearch
import csv
import json

es = Elasticsearch()


def converter():
    csvfile = open('netflix_shows.csv', 'r')
    jsonfile = open('output.json', 'w')
    fieldname = ("title", "rating", "ratingLevel", "ratingDescription", "release year", "user rating score", "user rating size")
    reader = csv.DictReader(csvfile, fieldname)
    jsonfile.write('[')
    for rows in reader:
        json.dump(rows, jsonfile)
        jsonfile.write(',')
        jsonfile.write('\n')
    jsonfile.write(']')
