from bs4 import BeautifulSoup
from typing import List

RATING_TO_NUM = {'One':1,'Two':2,'Three':3,'Four':4,'Five':5
                 }
def extract_html(html_doc: str) -> BeautifulSoup:
    soup = BeautifulSoup(html_doc, 'html.parser')
    return soup 

# Example usage of the function
def find_last_page(html: BeautifulSoup) -> int:
    pages = html.find_all('li')

    last_page = pages[-2].contents[0].strip()
    last_page = int(last_page.split(' ')[-1])
    return last_page

def _parse_book_title(html: BeautifulSoup) -> str :

    links=html.find_all('a')
    title=links[1]['title']
    return title

def parse_book_price(html: BeautifulSoup) -> float : 
    links=html.find_all('p')
    price=links[1].contents[0]
    price=float(price[2:])
    return price

def parse_book_rating(html: BeautifulSoup) -> int : 
    links=html.find_all('p')
    rating=links[0]['class']
    return RATING_TO_NUM[rating[1]]

def call_scrapping(html: BeautifulSoup) ->  List:
    data=[]
    for article  in html.find_all('article'):
        price=parse_book_price(article)
        title=_parse_book_title(article)
        rating=parse_book_rating(article)
        data.append(f'"{title}",{price},{rating}')

    return data
        

