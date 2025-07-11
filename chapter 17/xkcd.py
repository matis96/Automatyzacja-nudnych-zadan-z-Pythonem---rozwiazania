import requests, os, bs4

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
targetPath = os.path.join(desktop, 'xkcd')
os.makedirs(targetPath, exist_ok=True)  # Komiksy są przechowywane w katalogu ./xkcd.

# xkcd
url = 'https://xkcd.com'  # Początkowy adres URL.

# Pobranie strony.
print('Pobranie strony %s...' % url)
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
comicElem = soup.select('#comic img')
comicUrl = 'https:' + comicElem[0].get('src')
res = requests.get(comicUrl)
res.raise_for_status()

# Zapis obrazu w katalogu ./xkcd.
#imageFile = open(os.path.join(targetPath, os.path.basename(comicUrl)), 'wb')
imageFile = open(os.path.join(targetPath, 'xkcd.png'), 'wb')
for chunk in res.iter_content(100000):
    imageFile.write(chunk)
imageFile.close()

# left-handed Toons
url = 'https://www.lefthandedtoons.com/'
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
comicElem = soup.select('#comicwrap img')
comicUrl = comicElem[3].get('src')
res = requests.get(comicUrl)
res.raise_for_status()

# Zapis obrazu w katalogu ./xkcd.
#imageFile = open(os.path.join(targetPath, os.path.basename(comicUrl)), 'wb')
imageFile = open(os.path.join(targetPath, 'lhT.gif'), 'wb')
for chunk in res.iter_content(100000):
    imageFile.write(chunk)
imageFile.close()

# buttersafe
url = 'https://www.buttersafe.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
comicElem = soup.select('#comic img')
comicUrl = comicElem[0].get('src')
res = requests.get(comicUrl, headers=headers)
res.raise_for_status()

#imageFile = open(os.path.join(targetPath, os.path.basename(comicUrl)), 'wb')
imageFile = open(os.path.join(targetPath, 'buttersafe.jpg'), 'wb')
for chunk in res.iter_content(100000):
    imageFile.write(chunk)
imageFile.close()

# extra ordinary
url = 'https://www.exocomics.com/'  # Początkowy adres URL.

# Pobranie strony.
print('Pobranie strony %s...' % url)
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
comicElem = soup.select('#main-comic img')
comicUrl = 'https://www.exocomics.com/' + comicElem[0].get('src')
res = requests.get(comicUrl)
res.raise_for_status()

# Zapis obrazu w katalogu ./xkcd.
#imageFile = open(os.path.join(targetPath, os.path.basename(comicUrl)), 'wb')
imageFile = open(os.path.join(targetPath, 'exocomic.jpg'), 'wb')
for chunk in res.iter_content(100000):
    imageFile.write(chunk)
imageFile.close()

# wonderella
url = 'https://nonadventures.com/'  # Początkowy adres URL.

# Pobranie strony.
print('Pobranie strony %s...' % url)
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
comicElem = soup.select('#comic img')
comicUrl = comicElem[0].get('src')
res = requests.get(comicUrl)
res.raise_for_status()

# Zapis obrazu w katalogu ./xkcd.
#imageFile = open(os.path.join(targetPath, os.path.basename(comicUrl)), 'wb')
imageFile = open(os.path.join(targetPath, 'wonderella.png'), 'wb')
for chunk in res.iter_content(100000):
    imageFile.write(chunk)
imageFile.close()
