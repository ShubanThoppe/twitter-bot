import bs4 as _bs4
import requests as _requests

def _get_page(url:str) -> _bs4.BeautifulSoup:
    page = _requests.get(url)
    soup = _bs4.BeautifulSoup(page.content, "html.parser")
    return soup

def _extract_data(li):
    quote_text = li.text.strip()
    return quote_text


def scrape_data():
    collection = list()   
    url = "https://web.z.com/us/blog/100-inspirational-quotes-to-keep-you-inspired-in-2024/"
    soup = _get_page(url)
    raw_quotes = soup.find_all(class_="section-content")
    for quote in raw_quotes:
        li_elements = quote.find_all('li')
        for li in li_elements:
            quote = _extract_data(li)
            info = {"quote":quote}
            collection.append(info)

    return collection

print(scrape_data())