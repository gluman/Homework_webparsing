##
from _ast import keyword
import lxml
import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
keywords = ['Django', 'Flask']


HOST = 'https://hh.ru/search/vacancy?text=python&area=1&area=2'

def get_headers():
    headers = Headers(browser='firefox', os='win')
    return headers.generate()

response = requests.get(HOST, headers=get_headers())
hh_main = response.text

soup = BeautifulSoup(hh_main, features='lxml')
main_content = soup.find('div', id='ally-main-content')
vacances = main_content.findAll('div', class_='vacancy-serp-item__layout')


for vanvancy in vacances:
    description = vanvancy.find('div', ='vacancy-serp__vacancy_snippet_requirement')
    link
    compensation
    company_name
    city
print(span.text)