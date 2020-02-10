import requests
from bs4 import BeautifulSoup

def getHTMLContent(url): 
    res = requests.get(url)
    return res.content

soup = BeautifulSoup(getHTMLContent('https://www.allrecipes.com/recipes/96/salad/'), 'html.parser')
results = soup.find_all("article", class_="fixed-recipe-card")

print(results)

with open("getHTMLContent('https://www.allrecipes.com/recipes/96/salad/')", "r") as f:
    
    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')

    print(soup.h2)
    print(soup.head)
    print(soup.li)