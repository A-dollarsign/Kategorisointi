msg="Mr. Hackerman"
print(msg)

import requests
from bs4 import BeautifulSoup
from googlesearch import search


def find_on_plandent(item):
    return [url for url in search(f'site:plandent.fi/verkkokauppa {item}', stop=1)]


Res_urls = find_on_plandent('Suunavaaja Molt, 11cm')


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36'}
response = requests.get(Res_urls[0], headers=headers)


print(Res_urls)
print("test1")

