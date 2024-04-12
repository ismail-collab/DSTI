import requests

def url_get(url: str) -> str:
    """Get the HTML code of an URL

    Parameters
    ----------
    url : str
        url to return

    Returns
    -------
    str
        HTML code of the page
    """

    page = requests.get(url)

    if page.status_code < 200 or page.status_code > 299:
        return ''
    else:
        return page.text