import requests 
from bs4 import BeautifulSoup
from helpers import get_recipe_data_from_legacy_page, get_data_from_span, get_data_from_text

URL = 'https://www.allrecipes.com/recipes/96/salad/'
page_to_scrap = 1
r = requests.get(URL) 


# Visiting https://www.allrecipes.com/recipes/96/salad/?page_id and grab all the links of the recipes available on that page. 
# then store them into an array for later processing.
recipe_links = []
for page_id in range(page_to_scrap + 1):
    r = requests.get(URL + '?page=' + str(page_id)) 
    soup = BeautifulSoup(r.content, 'html.parser') 
    recipes = soup.find_all("article", {"class":"fixed-recipe-card"})
    for recipe in recipes:
        recipe_link = recipe.find('a', href=True)
        if recipe_link:
            recipe_links.append(recipe_link['href'])


recipes_data = {}
for link in recipe_links:
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'html.parser') 
    recipe_data_section = soup.find('section', {"class" : "nutrition-section"})
    if recipe_data_section is None:
        # Probably legacy page desing, that uses different class names. 4
        recipe_data_section_html = soup.find('div', {"class" : "nutrition-summary-facts"})
        if recipe_data_section_html :
            recipes_data[link] = get_data_from_span(str(recipe_data_section_html))
    else: 
        text_data = recipe_data_section.find('div', {"class": "section-body"}).text.strip()
        recipes_data[link] = get_data_from_text(text_data)
        
    

print(recipes_data)



