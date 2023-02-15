##
from _ast import keyword
import lxml
import requests
from bs4 import BeautifulSoup
from fake_headers import Headers

# URL 'https://hh.ru/search/vacancy?text=python&area=1&area=2'
HOST = 'https://hh.ru'

keywords = ['Django', 'Flask']

response = requests.get(HOST)
response_text = response.text
print(response_text)
soup = BeautifulSoup(response_text, features='lxml')
dataqa = soup.find('vacancy-serp__vacancy_snippet_requirement')
span = dataqa.findAll('span')

print(span.text)