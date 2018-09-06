# -*- coding:utf-8 -*-
'''
如何使用OpenerDirector处理HTTP/HTTPS的高级功能
代理防禁止访问
'''
import urllib.request

http_proxy_handler = urllib.request.ProxyHandler({'http':'118.114.77.47:8080'})
http_handler = urllib.request.HTTPHandler(debuglevel=1)
opener = urllib.request.build_opener(http_proxy_handler)


request = urllib.request.Request('http://www.baidu.com/s')
response = opener.open(request)

print(response.read())