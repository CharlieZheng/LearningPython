import re

import requests
from bs4 import BeautifulSoup, NavigableString
from bs4.diagnose import diagnose

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
def save_to_file(file_name, contents):
    fh = open(file_name, 'w')
    fh.write(contents)
    fh.close()


def read_file(file_name):
    with open(file_name) as f:  # 默认模式为‘r’，只读模式
        return f.read()


'''
print(soup.a['href'])
print(soup.a.get('href2'))#print(soup.a['href2'])
contents = ""
for item in soup.html.contents:
    contents +=str(item)
children = ""
for item in soup.html.children:
    children +=str(item)

print(contents == children)

'''
'''
def surrounded_by_strings(tag):
    return (isinstance(tag.next_element, NavigableString)
            and isinstance(tag.previous_element, NavigableString))

for tag in soup.find_all(surrounded_by_strings):
    print (tag.name)
    

'''
# html = requests.get('http://sports.sina.com.cn/g/pl/fixtures.html').content

file_name = './index.html'
# file_name = './kkk.html'
# save_to_file(file_name, soup.text)
# file_text = read_file(file_name)


# soup = BeautifulSoup(file_text, 'html.parser')  # html.parser, lxml
soup = BeautifulSoup(open(file_name), 'html.parser')  # html.parser, lxml
# print(soup.prettify())
'''
div = soup.find("div", attrs={"id": re.compile(r'^roun')})\
    .find("div", class_='sr-box')\
    .find("p", class_='team')\
    .find("a").text# 和get_text()等效'''
div = soup.find_all('p')
'''
div = soup.name
for itme in soup.stripped_strings:
    print(itme)
    '''
# div = soup.find("div", attrs={"id":re.compile(r'^roun')})['id'] # id属性为roundCtr
# print(div[0])
# ['schedule-round']['current']['sr-ctr']['st-ctr-in udv-clearfix']
# print("sibling"+last_a_tag.next_sibling)
# print("element"+last_a_tag.next_element)
if div is not None:
    print(len(div))
print(div)


z1 = [4, 3,3,2]
z2 = 5
print(z1 * z2)