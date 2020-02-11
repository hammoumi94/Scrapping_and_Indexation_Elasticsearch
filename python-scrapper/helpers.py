from bs4 import BeautifulSoup

html = """<span>Per Serving: </span>
            <span itemprop="calories">187 calories;</span>
                    <span itemprop="fatContent">15.6 <span aria-label="grams of fat;"></span>
                    </span> <span aria-hidden="true">g fat;</span>
                    <span itemprop="carbohydrateContent">8.3<span aria-label="grams of carbohydrates;"></span></span> <span aria-hidden="true">g carbohydrates;</span>
                    <span itemprop="proteinContent">5 <span aria-label="grams of protein;"></span></span> <span aria-hidden="true">g protein;</span>
                    <span itemprop="cholesterolContent">22 <span aria-label="milligrams of cholesterol;"></span></span> <span aria-hidden="true">mg cholesterol;</span>
                    <span itemprop="sodiumContent">347 <span aria-label="milligrams of sodium."></span></span><span aria-hidden="true">mg sodium.</span>
        <a href="" onclick="openNutritionAndTrack();" class="see-full-nutrition">Full nutrition</a>"""

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
