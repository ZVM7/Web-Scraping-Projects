import requests
from bs4 import BeautifulSoup
import re

search_term = input("Please Enter Product Name")

url = f"https://www.newegg.com/p/pl?d={search_term}&N=4131"
page = requests.get(url).text
doc = BeautifulSoup(page ,'lxml')

page_text = doc.find('span', class_="list-tool-pagination-text").strong
pages = int(str(page_text).split("/")[-2].split(">")[1][:2])

items_found ={}

for page in range(1, pages + 1):
    url = f"https://www.newegg.com/p/pl?d={search_term}&N=4131&page={page}"
    page = requests.get(url).text
    doc = BeautifulSoup(page, 'lxml')

    div = doc.find(class_="item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell")
    items = div.find_all(text=re.compile(search_term))

    for item in items:
        Parent = item.parent
        if Parent.name != 'a':
            continue

        link = parent['href']
        next_parent = item.find_parent(class_="item-container")
        try:
            price = next_parent.find(class_="price-current").find("strong").string
            items_found[item] = {"price": int(price.replace(",", "")), "link": link}
        except:
            pass

    sorted_items = sorted(items_found.items(), key=lambda x: x[1]['price'])

    for item in sorted_items:
        print(item[0])
        print(f"${item[1]['price']}")
        print(item[1]['link'])
        print("-------------------------------")




