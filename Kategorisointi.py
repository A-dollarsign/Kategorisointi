msg="Mr. Hackerman"
print(msg)

import csv
import pandas as pd
import requests
from bs4 import BeautifulSoup
from googlesearch import search

def find_on_plandent(item):
    return [url for url in search(f'site:plandent.fi/verkkokauppa {item}', stop=1)]

df=pd.read_csv("C:\Users\Atte\kategoriat\kategorisointi\input.csv")
df = pd.read_csv("data/input.csv")
print(df.head(1))
Res_urls = find_on_plandent('Intraoraalikärki Aquasil Ultra+')

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36'}
response = requests.get(Res_urls[0], headers=headers)


filename="test1.csv"
fields=['Linkki']
rows=[Res_urls]
with open(filename,'w') as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerows(rows)

print(df.head(1))
print(Res_urls)
print("test1")
