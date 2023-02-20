##
# 1 Необходимо парсить страницу со свежими вакансиями с поиском по "Python" и городами "Москва" и "Санкт-Петербург". Эти параметры задаются по ссылке
# 2 Нужно выбрать те вакансии, у которых в описании есть ключевые слова "Django" и "Flask".
# 3 Записать в json информацию о каждой вакансии - ссылка, вилка зп, название компании, город.
from time import sleep
import lxml
import re
import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
import json



def get_headers():
    headers = Headers(browser='firefox', os='win')
    return headers.generate()
def get_response(n):
    HOST = f'https://spb.hh.ru/search/vacancy?text=Python&salary=&area=1&area=2&ored_clusters=true&enable_snippets=true&page={n}'
    response = requests.get(HOST, headers=get_headers())
    hh_main = response.text
    if response.status_code == 200:
        return hh_main
    else:
        return False

pattern1 = f'([Ff]lask)'
pattern2 = f'([Dd]jango)'
count = 0
run = True
parced = []
while run:
    sleep(1)
    content = get_response(count)
    if content:
        soup = BeautifulSoup(content, features='lxml')
        main_content = soup.find('div', id="a11y-main-content")
        vacanceses = main_content.findAll('div', class_='vacancy-serp-item__layout')

        for vacancy in vacanceses:
            info = vacancy.find('div', class_='g-user-content').findAll('div', class_='bloko-text')
            desc = []
            for i in info:
                desc.append(i.text)
            str = ','.join(desc)
            find_1 = re.findall(pattern1, str)
            find_2 = re.findall(pattern2, str)
            if len(find_1) and len(find_2):
                link = vacancy.find('a')['href']
                try:
                    compensation = vacancy.find('span', class_='bloko-header-section-3').text
                except:
                    compensation = None
                company_name = vacancy.find('a', class_='bloko-link bloko-link_kind-tertiary').text
                city = vacancy.find('div', {'data-qa':"vacancy-serp__vacancy-address", 'class':'bloko-text'}).text
                print(f'Найдено на листе: {count + 1} link:{link}, compensation:{compensation}, company:{company_name}, city:{city}')
                data = dict()
                data['link'] = link
                data['compensation'] = compensation
                data['company_name'] = company_name
                data['city'] = city
                print(f'Cформирован словарь {data}')
                parced.append(data)
                print('Добавлено в список')

        count += 1
    else:
        run = False

with open('parsed.json', 'w', encoding='utf8') as file:
    json.dump(parced, file, indent=5, ensure_ascii=False)
    print('Записано в файл')