# _*_ coding:utf-8 _*_
import urllib.request as req
import random
import sys
sys.path.append('../common')
import ua


user_agent = random.choice(ua.ua_list)
url = req.Request('http://www.baidu.com/')
url.add_header('User-Agent', user_agent)
#服务器返回的类文件对象支持python文件对象的操作方法
#read()方法就是读取文件里的全部内容，返回字符串
res = req.urlopen(url)
html = res.read()
print (html)

print(res.getcode())
print(res.geturl())
print(res.info())