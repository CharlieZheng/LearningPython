# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
if __name__ == '__main__':
    target = 'http://www.biqukan.com/1_1094/5403177.html'
    html = requests.get(url=target).text
    bf = BeautifulSoup(html)
    texts = bf.find_all('div', id = 'content', class_ = 'showtxt')
    print(texts[0].text.replace('\xa0' * 8, '\n\n'))