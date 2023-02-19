##
# 1 Необходимо парсить страницу со свежими вакансиями с поиском по "Python" и городами "Москва" и "Санкт-Петербург". Эти параметры задаются по ссылке
# 2 Нужно выбрать те вакансии, у которых в описании есть ключевые слова "Django" и "Flask".
# 3 Записать в json информацию о каждой вакансии - ссылка, вилка зп, название компании, город.



# from _ast import keyword
import lxml
import re
import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
import json
keywords = ['Django', 'Flask']
HOST = 'https://spb.hh.ru/search/vacancy?text=Python+Django+Flask&salary=&area=1&area=2&ored_clusters=true&enable_snippets=true'

def get_headers():
    headers = Headers(browser='firefox', os='win')
    return headers.generate()

response = requests.get(HOST, headers=get_headers())
hh_main = response.text

soup = BeautifulSoup(hh_main, features='lxml')
main_content = soup.find('div', id="a11y-main-content")
vacanceses = main_content.findAll('div', class_='vacancy-serp-item__layout')

parced = []

for vacancy in vacanceses:
    info = vacancy.find('div', class_='g-user-content').findAll('div', class_='bloko-text')
    desc = []
    for item in info:
        desc.append(item.text)

    if set(keywords).issubset(desc):
        link = vacancy.find('a')['href']
        compensation = vacancy.find('span', class_='bloko-header-section-3')
        company_name = vacancy.find('a', class_='bloko-link bloko-link_kind-tertiary')
        city = vacancy.find('div', class_='bloko-text')
        item ={
            'link': link,
            'compensation': compensation,
            'company_name': company_name,
            'city': city
        }
        parced.append(item)

with open('parsed.json', 'w') as file:
    json.dump(parced, file, indent=5)
