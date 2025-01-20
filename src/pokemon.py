# import bs4 as _bs4
# import requests as _requests

# def _get_page(url:str) -> _bs4.BeautifulSoup:
#     page = _requests.get(url)
#     soup = _bs4.BeautifulSoup(page.content, "html.parser")
#     return soup

# def _extract_data(data):
#     code_text = data.contents[0].text
#     name_text = data.find(class_="ent-name").text
#     type_text = data.find(class_= "itype").text
#     return code_text, name_text, type_text

# def scrape_data():
#     collection = list()   
#     url = "https://pokemondb.net/pokedex/national"
#     soup = _get_page(url)
#     raw_data = soup.find_all(class_= "infocard-lg-data text-muted")
#     for data in raw_data:
#         code, name, type = _extract_data(data)
#         info = {"code":code, "name":name, "type":type}
#         collection.append(info)

#     return collection

# print(scrape_data())