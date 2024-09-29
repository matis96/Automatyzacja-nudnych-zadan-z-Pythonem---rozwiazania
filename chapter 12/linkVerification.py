import requests, os
from bs4 import BeautifulSoup
webpage = 'https://nostarch.com'
res = requests.get(webpage)
soup = BeautifulSoup(res.text, 'html.parser')
for link in soup.find_all('a', href=True):
    if link['href'][0] == '/':
        page = webpage + link['href']
    else:
        page = link['href']
    try:
        resTest = requests.get(page)
        if res.status_code == 404:
            print('Blad 404: ' + page)
    except:
        pass
