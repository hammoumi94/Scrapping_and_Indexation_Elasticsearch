from ConverterJSON import converter
from Index import index
from helpers import get_data_from_text
import re
#converter()
#index()
text = '          375 calories;           28.7 g total fat;           48 mg cholesterol;           184 mg sodium.          14.9 g carbohydrates;           16.8 g protein;         <a href="#" class="recipe-nutrition-section-link link-view" aria-label="Read Full Nutrition"\
                                 "data-tracking-do-not-track="1">Full Nutrition</a>'
text = text.strip()
text = text.replace(" ", "")
data = {}
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

print(final_data)
#get_data_from_text(text)

