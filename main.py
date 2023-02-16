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

response = requests.get(HOST)
response_text = response.text
print(response_text)
soup = BeautifulSoup(response_text, features='lxml')
dataqa = soup.find('vacancy-serp__vacancy_snippet_requirement')
span = dataqa.findAll('span')

print(span.text)