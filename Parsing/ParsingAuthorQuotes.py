import requests
from bs4 import BeautifulSoup

# В url сохраняем адрес страницы с которой будет поступать информация
url = "https://quotes.toscrape.com/"
# передаём её в метод get
responce = requests.get(url)
# в responce ответ 200
# print(responce)
# Зашли в html разметку
soup = BeautifulSoup(responce.text, 'lxml')


# print(soup)
# Находим данные из тэгов(некий шаблон на странице, а полсле этого создать код для работы с ним)
# C BeautifulSoup удобно находить нужные данные
# Найти все теги span с калссом text

# find_all() - если нужно найти несколько одинаковых тегов

quotes = soup.find_all('span', class_='text')
# print(quotes)
# Возвращается разметка с цитатами

# done
# for quote in quotes:
#     print(quote.text)

# Ищем авторов тег small
authors = soup.find_all('small', class_='author')

# for author in authors:
#     print(author.text)

# Получение тегов для каждой цитаты
tags = soup.find_all('div', class_='tags')

# Пробегаемся по всем авторам
for i in range(len(quotes)):
    print(quotes[i].text)
    print('-- ' + authors[i].text)
    tagsforquote = tags[i]('a', class_='tag')
    # Заходим в тэги класса tag d div класса tag
    for tagforquote in tagsforquote:
        print(tagforquote.text)
    print('\n')

