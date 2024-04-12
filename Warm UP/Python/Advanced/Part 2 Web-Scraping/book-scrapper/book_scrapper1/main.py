from url_get import url_get
import soup_parsing
import itertools


if __name__=="__main__":

    results = []
    i=1

    while True:

        WEBURL = f"https://books.toscrape.com/catalogue/page-{i}.html"
        print(f'Scrapping {WEBURL}')
        html = url_get(WEBURL)

        soup = soup_parsing.get_soup(html)
        data = soup_parsing.scrap_soup(soup)

        results.append(data)

        if soup_parsing.is_last_page(soup):

            iter_results = itertools.chain.from_iterable(results)
            break

        i=i+1

