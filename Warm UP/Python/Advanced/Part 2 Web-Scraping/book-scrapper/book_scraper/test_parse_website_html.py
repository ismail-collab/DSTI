import pytest_
from book_scraper.parse_website_html import *

class TextExtractHTML :
    def test_extract_html():

        """

        """
        test = extract_html("<h1>This is a Test</h1>")
        assert str(type(test))=="class 'bs4.BeautifulSoup'"