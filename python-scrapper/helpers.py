from bs4 import BeautifulSoup
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


def get_recipe_data_from_legacy_page(html):
    if html: 
        return get_data_from_span(html)
    return False

