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


def get_nutrition_facts_from_span(spans):
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
        data = {
            'ingerdients': [],
        }

        soup = BeautifulSoup(page_html, 'html.parser') 
        # Setting up different soups
        soup_ingredients = soup.select('ul[class*="list-ingredients-"]')
        soup_facts = soup.find('div', {"class" : "nutrition-summary-facts"})
        soup_submitter = soup.find('span', {"class" : "submitter__name"})
        soup_description = soup.find('div', {"class": "submitter__description"})
        soup_title = soup.find('h1', {"class": "recipe-summary__h1"})
        soup_ratings = soup.find('div', {"class": "rating-stars"})
        # getting data from soups
        nutrition_facts = get_nutrition_facts_from_span(str(soup_facts))
        submitter = soup_submitter.text.strip()
        description = soup_description.text.strip()
        title = soup_title.text.strip()
        rating = soup_ratings.get('data-ratingstars')
        # Get ingredients 
        for ul in soup_ingredients: 
            data['ingerdients'] += get_text_from_ul_legacy(ul)
        # Get submitter
        data['submitter'] = submitter
        # Get description 
        data['description'] = description
        # Get title/name 
        data['title'] = title
        # nutrition facts
        data['nutrition_facts'] = nutrition_facts
        #rating
        data['rating'] = rating
        return data
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



def get_text_from_ul_legacy(ul):
    titles = [] 
    for li in ul.findAll('li'):
        label = li.find('label')
        title = label.get('title')
        if(title) :
            titles.append(title)

    return titles

def check_es_connect(es): 
    if es.ping():
        print("You are connected") 
    else: 
        print("You are not connected") 