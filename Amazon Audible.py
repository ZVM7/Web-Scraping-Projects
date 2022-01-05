import requests
from bs4 import BeautifulSoup
import pandas as dt

url =  "https://www.audible.com/adblbestsellers?source_code=GO1DH13310082090OE&cvosrc=ppc.google.audible&cvo_campaign=13262341844&cvo_crid=524136974615&Matchtype=e&gclid=EAIaIQobChMI0b3UncH49AIVzxbUAR1BYArJEAAYASACEgIcqvD_BwE&gclsrc=aw.ds"
response = requests.get(url)
soup = BeautifulSoup(response.content,'lxml')

Title = []
Sub_Title = []
Author = []
Narrator = []
Run_Time = []
Ratings = []
Price = []


Entire_web = soup.find('div', class_= "adbl-impression-container")
All_the_books = Entire_web.find_all('li',class_="bc-list-item productListItem")

for info in All_the_books:
    title = info.find('ul',class_="bc-list").li.h2.text
    Title.append(title)



sub_title = Entire_web.find_all('li',class_="bc-list-item subtitle")

for info in sub_title:
    sub_Title = info.find('span').text
    Sub_Title.append(sub_Title)


Author_name = Entire_web.find_all('li',class_="bc-list-item authorLabel")

for info in Author_name:
    author = info.find('a').text
    Author.append(author)

Narrated_by = Entire_web.find_all('li',class_="bc-list-item narratorLabel")

for info in Narrated_by:
    narrator = info.find('a').text
    Narrator.append(narrator)


Movie_length = Entire_web.find_all('li',class_="bc-list-item runtimeLabel")

for info in Movie_length:
    run_time = info.find('span').text.strip("Length:")
    Run_Time.append(run_time)

ratings = Entire_web.find_all('li',class_="bc-list-item ratingsLabel")

for info in ratings:
    Movie_score = info.find('span',class_="bc-text bc-size-small bc-color-secondary").text
    Ratings.append(Movie_score)


Book_price = Entire_web.find_all('p',class_="bc-text buybox-regular-price bc-spacing-none bc-spacing-top-none")

for price in Book_price:
    srice = price.find_next_sibling()
    Real_Price = srice.find('span',class_="bc-text bc-size-base bc-color-price").text
    Price.append(Real_Price)



Audible = dt.DataFrame({"Book Title":Title,"Author Of The Book": Author,"Narrator": Narrator,"Run Time": Run_Time,
                      "Ratings": Ratings,"Book Price":Price})
Audible.to_excel('Audible.xlsx',index=False)
