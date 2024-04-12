from bs4 import BeautifulSoup
from book_scrapper.soup_parsing import get_soup

def test_soup_conversion():
    html_code = "<p>Test</p>"
    soup = get_soup(html_code)

    assert str(type(soup)) == "<class 'bs4.BeautifulSoup'>"