import requests 
from bs4 import BeautifulSoup
from helpers import get_recipe_data_from_legacy_page, get_recipe_data_from_page
import json

URL = 'https://www.allrecipes.com/recipes/96/salad/'
page_to_scrap = 20
r = requests.get(URL) 


# Visiting https://www.allrecipes.com/recipes/96/salad/?page_id and grab all the links of the recipes available on that page. 
# then store them into an array for later processing.
recipe_links = []
for page_id in range(page_to_scrap + 1):
    r = requests.get(URL + '?page=' + str(page_id)) 
    print('Visting page : ' + URL + '?page=' + str(page_id))
    soup = BeautifulSoup(r.content, 'html.parser') 
    recipes = soup.find_all("article", {"class":"fixed-recipe-card"})
    for recipe in recipes:
        recipe_link = recipe.find('a', href=True)
        if recipe_link:
            recipe_links.append(recipe_link['href'])


recipes_data = {}
for link in recipe_links:
    try :
        r = requests.get(link)
        soup = BeautifulSoup(r.content, 'html.parser') 
        recipe_data_section = soup.find('section', {"class" : "nutrition-section"})
        body = soup.find('body')
        print('Visting page : ' + link)

        if recipe_data_section is None:
            # Probably legacy page desing, that uses different class names. 4
            
            recipes_data[link] = get_recipe_data_from_legacy_page(str(body))
        else: 
            recipes_data[link] = get_recipe_data_from_page(str(body))
    except Exception as error:
        print(error) 
    
#print(recipes_data)

jsonfile = open('final_data.json', 'w')

jsonfile.write('[')
for row in recipes_data :
    #print(recipes_data[row])
    json.dump(recipes_data[row], jsonfile)
    jsonfile.write(',')
    jsonfile.write('\n')

jsonfile.write(']')
#print(jsonfile)


