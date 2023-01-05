import requests  # импортируем наш знакомый модуль
import lxml.html
from lxml import etree

html = requests.get('https://www.python.org/').content
tree = etree.parse('Welcome to Python.org.html', lxml.html.HTMLParser())

ul = tree.findall('/body/div/div[3]/div/section/div[3]/div[1]/div/ul/li')


for li in ul:
    a = li.find('a') # в каждом элементе находим где хранится название. У нас это тег <a>
    time = li.find('time')
    print(time.get('datetime'), a.text) # из этого тега забираем текст - это и будет нашим названием
