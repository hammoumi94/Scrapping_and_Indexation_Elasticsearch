from helpers import get_data_from_text, get_recipe_data_from_page
import requests

URL = 'https://www.allrecipes.com/recipe/15735/fruited-curry-chicken-salad/'
page_to_scrap = 1
r = requests.get(URL)
get_recipe_data_from_page(str(r.content))