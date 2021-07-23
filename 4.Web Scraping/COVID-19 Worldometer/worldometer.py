"""

- This script is scraping Worldometer website.
- This aims ready to use.
- For step by step and details, Worldometer.ipynb is preferable.

"""

import requests
from bs4 import BeautifulSoup

base_url = 'https://www.worldometers.info/coronavirus/'

country = input('Enter country: ')
url = base_url + '/country/' + country

# fetch HTML data
html_text = requests.get(url).text

# parse HTML text using 'lxml'
soup = BeautifulSoup(html_text, 'lxml')
print(soup.prettify())

info_divs = soup.find('div', class_="content-inner").findAll('div', id='maincounter-wrap')
print(info_divs)

for block in info_divs[:3]:
    title = block.h1.text
    number = block.span.text
    print(title, number)