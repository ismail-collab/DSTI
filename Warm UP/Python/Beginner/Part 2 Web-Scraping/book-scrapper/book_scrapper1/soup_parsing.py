from bs4 import BeautifulSoup
from typing import List

def get_soup(html_code: str) -> BeautifulSoup:
    """Converting the HTML the bs4 format

    Parameters
    ----------
    html_code : str
        HTML code to convert

    Returns
    -------
    BeautifulSoup
        BS4 formatted html
    """
    soup = BeautifulSoup(html_code, 'html.parser')

    return soup

def is_last_page(soup: BeautifulSoup) -> List:
    return True

def scrap_soup(soup: BeautifulSoup) -> List:
    """Main scrapping function that will hold all the logic

    Parameters
    ----------
    soup : BeautifulSoup
        bs4 formatted HTML

    Returns
    -------
    List
        List of dictionnary that will hold the data extracted
    """
    # List that will contain the results
    data = []

    # We are extracting <article> tags as they hold the information of interest
    for article in soup.find_all('article'):
        # Calling the function to extract the title
        title = _get_title(article)
        # Calling the function to extract/convert the price
        price = _get_price(article=article)

        stock = _get_avaibility(article=article)

        rating = _get_rating(article=article)
        # Append the result with the data formatted as a dictionnary
        data.append(f'"{title}";{rating};{price};{stock}')

    return data

def _get_title(article) -> str:
    """Extracting the title from the html page

    Parameters
    ----------
    article : _type_
        extract of the HTML containing <article> tag

    Returns
    -------
    str
        title of the book
    """
    # In the <article> tag, the title is in one of  the href
    links = article.find_all('a')
    # The title is in the second link
    title = links[1]['title']
    
    return title

def _get_rating(article) -> str:
    """Get the rating of the book

    Parameters
    ----------
    article : _type_
        Book we are scraping

    Returns
    -------
    str
        Rating as a string
    """
    p_part = article.find_all('p')
    rating = p_part[0]['class'][1]
    return rating

def _get_price(article) -> float:
    """Extracting the price of a book from the HTML

    Parameters
    ----------
    article : _type_
        Extract of the HTML containing <article> tag

    Returns
    -------
    float
        _description_
    """
    # Getting the p part to extract the price
    p_part = article.find_all('p')

    # The price is in the second p
    price = p_part[1].contents[0]
    # Removing the first 2 characters and cast it to float
    price = float(price[2:])

    return price

def _get_avaibility(article) -> str:
    """Get the availbility of a book

    Parameters
    ----------
    article : _type_
        book we are extracting

    Returns
    -------
    str
        Availbility in the store
    """
    # Extracting all <p> tags
    p_part = article.find_all('p')
    #Find the availbility of the book
    stock = p_part[2].contents[2].strip()

    return stock