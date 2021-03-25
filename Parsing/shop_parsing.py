import requests
from bs4 import BeautifulSoup

# For 1 page
url = 'https://scrapingclub.com/exercise/list_basic/?page=1'
responce = requests.get(url)
soup = BeautifulSoup(responce.text, 'lxml')
items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
number_items = 1
for n, i in enumerate(items, start=1):
    itemName = i.find('h4', class_='card-title').text.strip()
    itemPrice = i.find('h5').text
    print(f'{n}: {itemName} за {itemPrice}')
    number_items += 1


#Parsing all pages
pages = soup.find('ul', class_='pagination')
urls = []
links = pages.find_all('a', class_='page-link')

for link in links:
    pageNum = int(link.text) if link.text.isdigit() else None
    if pageNum != None:
        hrefval = link.get('href')
        urls.append(hrefval)
        print(urls)

for slug in urls:
    newUrl = url.replace('?page=1', slug)
    responce = requests.get(newUrl)
    soup = BeautifulSoup(responce.text, 'lxml')
    items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
    for n, i in enumerate(items, start=number_items):
        itemName = i.find('h4', class_='card-title').text.strip()
        itemPrice = i.find('h5').text
        print(f'{n}: {itemName} за {itemPrice}')
        number_items += 1

