from book_scraper.url_request import *
from book_scraper.parse_website_html import *
from book_scraper.data_export import *
from bs4 import BeautifulSoup

def parse_content(WEBSITE_URL:str)->BeautifulSoup:
     # Access the website HTML
    page_content = call_url(WEBSITE_URL)

    # Parse the content into pretty HTML
    content_parsed = extract_html(page_content)

    return content_parsed
    
if __name__ == "__main__":

    i = 1

    WEBSITE_URL = f"https://books.toscrape.com/catalogue/page-{i}.html"
    

    # Parse the content into pretty HTML
    content_parsed = parse_content(WEBSITE_URL)

    last_page_index = find_last_page(content_parsed)
    last_page_index=3
    data_results = []

    while i < last_page_index+1:
        WEBSITE_URL = f"https://books.toscrape.com/catalogue/page-{i}.html"

        print(f'Scrapping page {i}')
        # Access the website HTML
        content_parsed = parse_content(WEBSITE_URL)
    

        data=call_scrapping(content_parsed)

        data_results = data_results + data

        i=i+1

    # Save the list to csv
    output_file = "test.csv"

    if export_to_csv(output_file, data_results):
        print(f"Data exported to {output_file}")
    else:
        print("Error while exporting data")
