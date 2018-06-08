# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    server = 'http://www.biqukan.com/'
    target = 'http://www.biqukan.com/0_973/'
    req = requests.get(url=target)
    html = req.text

    div_bf = BeautifulSoup(html)
    div = div_bf.find_all('div', class_='listmain')

  
    dd = BeautifulSoup(str(div[0])).find_all('a')
    print(len(dd))
    dd_set = set(dd)
    print(len(dd_set))
    for each in dd_set:
        print(each.get('href'))
