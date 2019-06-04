# -*- coding:utf-8 -*-
# 使用 Python 2
'''
安装：
    pip3 install bs4
    pip3 install requests
    pip3 install lxml
'''
import re

import requests
from bs4 import BeautifulSoup, NavigableString
from bs4.diagnose import diagnose
 


# http://sports.sina.com.cn/g/pl/fixtures.html


# file_name = './index.html'
file_name = './fixtures.html'



url = 'http://product.auto.163.com/rank/hotIndices_priceRegion_0_6_liangxiang.html#fixedpos'
 
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text,'lxml')

#soup = BeautifulSoup(open(file_name), 'html.parser')  # html.parser, lxml
''' 1. prettify 

print(soup.prettify())
'''
''' 2. stripped_strings 
for item in soup.stripped_strings:
     print(item)
'''
''' 3. find 只匹配一个 '''

# div = soup.find("div", attrs={"id": re.compile(r'^roun')})\
#     .find("div", class_='sr-box')\
#     .find("p", class_='team')\
#     .find("a").text # 和 get_text() 等效

# div = soup.find("div", attrs={"id": re.compile(r'^roun')})[
#     'id']  # id 属性为 roundCtr
# for i in div:
#     print(i), # 这里的逗号是必须的
''' 4. find_all '''

div = soup.find_all('div', class_="rankcell_d") # div 的类型为 <Tag>[]

div = div[0].find('a').find('img')
img = div.attrs["src"] # 图片
''' 5. next_sibling next_element '''
# div = soup.name
# print(str(div))

# ['schedule-round']['current']['sr-ctr']['st-ctr-in udv-clearfix']
# div = soup.find("div", attrs={"id": re.compile(r'^roun')})\
#     .find("div", class_='sr-box')\
#     .find("p", class_='team')

# print("sibling"+div.next_sibling)
# print("element"+div.next_element)
# print(div)
# for i in div:
#   print(i),

''' 6. 第一个 a 标签的 href 属性 '''
# print(soup.a['href']) # print(soup.a.get('href'))

''' 7. contents 和 children '''
# contents = ""
# for item in soup.html.contents:
#     contents +=str(item)

# children = ""
# for item in soup.html.children:
#     children +=str(item)

# print(contents == children)


''' 8. find_all 参数可以为函数 '''
# def surrounded_by_strings(tag):
#     return (isinstance(tag.next_element, NavigableString)
#             and isinstance(tag.previous_element, NavigableString))

# def surrounded_by_strings(tag):
#     return tag.name == 'style'

# for tag in soup.find_all(surrounded_by_strings):
#     print (tag.name)


# re.compile 所产生对象的用处
# match = re.compile(r'^My') # 试试把 ^ 去掉观察结果的异同
# text = 'My name is Zheng Hanrong.\n\
# My name is Zheng Hanrong.'
# temp = re.sub(match,'His',text)
# print(temp)
