""" 
This script will be used to make a web request to https://books.toscrape.com/

REQUIREMENT : 

"""
import requests
import bs4 


def call_url(url: str) -> str:
    """
    this function will make a web request
    """
    # Make a call to the specific URL 
    response = requests.get(url, timeout=None)
    if response.status_code < 200 or response.status_code > 299 :
        result = ''
        print("Invalid URL Response")
    else:   
        result = response.text

    return  result
