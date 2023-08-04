from bs4 import BeautifulSoup
import requests
import lxml
from lxml import html
import re
import json


# найти загловки статей

url = "https://www.oreilly.com/radar/"
req = requests.get(url)
soup = BeautifulSoup(req.text, "lxml")
find_all_tittle = soup.find_all("h2", class_="post-title")
for post in find_all_tittle:
    print(post.text)


# найти сколько раз в статье встречается слово

url = "https://azku.ru/russkie-narodnie-skazki/kolobok.html"
req = requests.get(url)
soup = BeautifulSoup(req.text, "lxml")

find_word_in_text = soup.find_all(text=re.compile("([Кк]олобок)"))
for word in find_word_in_text:
    print(word.text)


# составить рейтинг топ-100 лучших триллеров на основе спика с одного сайта

url = "https://www.livelib.ru/genre/%D0%A2%D1%80%D0%B8%D0%BB%D0%BB%D0%B5%D1%80%D1%8B/top"
req = requests.get(url)
soup = BeautifulSoup(req.content, "lxml")
find_titles = soup.find_all("a", class_="brow-book-name with-cycle")
find_authors = soup.find_all("a", class_="brow-book-author")
find_rating = soup.find_all("span", class_="rating-value stars-color-orange")
i = 1
for t, a, r in zip(find_titles, find_authors, find_rating):
    print(f'{i}. "{t.get_text()}", {a.get_text()} - {r.get_text()}')
    i += 1

