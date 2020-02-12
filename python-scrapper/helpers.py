from bs4 import BeautifulSoup
import re

html = """
<div class="nutrition-summary-facts">
<br/>
<span>Per Serving: </span>
<span itemprop="calories"> calories;</span>
<span itemprop="fatContent"> <span aria-label="grams of fat;"></span></span> <span aria-hidden="true"> fat;</span>
<span itemprop="carbohydrateContent"><span aria-label="grams of carbohydrates;"></span></span> <span aria-hidden="true"> carbohydrates;</span>
<span itemprop="proteinContent"> <span aria-label="grams of protein;"></span></span> <span aria-hidden="true"> protein;</span>
<span itemprop="cholesterolContent"> <span aria-label="milligrams of cholesterol;"></span></span> <span aria-hidden="true"> cholesterol;</span>
<span itemprop="sodiumContent"> <span aria-label="milligrams of sodium."></span></span><span aria-hidden="true"> sodium.</span>
<a class="see-full-nutrition" href="" onclick="openNutritionAndTrack();">Full nutrition</a>
</div>
"""
attrs = ['calories', 'fatContent', 'carbohydrateContent', 'proteinContent', 'cholesterolContent', 'sodiumContent']


def get_data_from_span(spans):
    soup = BeautifulSoup(spans, 'html.parser')
    data = {}
    for attr in attrs:
        span = soup.find('span', {'itemprop': attr})
        if span:
            value = span.text.strip()
            if value:
                data[attr] = value
    return data


def get_recipe_data_from_legacy_page(page_html):
    if page_html: 
        soup = BeautifulSoup(page_html, 'html.parser') 
        # Setting up different soups
        soup_ingredients = soup.select('ul[class*="list-ingredients-"]')
        soup_facts = soup.find('div', {"class" : "nutrition-summary-facts"})
        soup_submitter = soup.find('span', {"class" : "submitter__name"})

        # getting data from soups
        nutrition_facts = get_data_from_span(str(soup_facts))
        submitter = soup_submitter.text.strip()

        print(soup_ingredients)
        # Get ingredients 
        # Get submitter
        # Get description 
        # Get title/name 
    return False

def get_data_from_text(text):
    text = text.strip()
    text = text.replace(" ", "")
    data = {}

    #mapping
    attrs = {'calories' : 'calories', 'gtotalfat' : 'fatContent', 'mgcholesterol' : 'cholesterolContent', 'gprotein' : 'proteinContent', 'mg' : 'sodiumContent', 'gcarbohydrates' : 'carbohydrateContent'}
    final_data = {}
    data = text.split(';')
    for item in  data:
        if 'sodium' in item:
            elem = item.split('sodium.')
            data.append(elem[0])
            data.append(elem[1])
            data.remove(item)
        if '<ahref' in item :
            data.remove(item)


    for item in data :
        match = re.match(r"([0-9^.]+)([a-z]+)", item, re.I)
        key = attrs[match.group(2)]
        final_data[key] = match.group(1)
    
    return final_data




from elasticsearch import Elasticsearch

def connect():
    es = Elasticsearch(['http://localhost:9200/'], verify_certs=True)
    if not es.ping():
        raise ValueError("Connection failed")
        
    print("Vous êtes connectés")