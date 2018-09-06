'''
登录人人网
'''
import urllib.request
import http.cookiejar
import pdb
import json
cookie = http.cookiejar.CookieJar()
cookie_handler = urllib.request.HTTPCookieProcessor(cookie)

opener = urllib.request.build_opener(cookie_handler)
opener.addheaders = [
    ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36')]

url = 'http://www.izuiyou.com/api/index/webrecommend'

data = {
    'ctn'	: 20,
    'direction'	: 'up',
    'filter'	: 'imgtxt',
    'h_av':	'3.0',
    'h_ch':	'web_app',
    'h_dt':	9,
    'h_nt':	9,
    'offset':	0,
    'tab'	: 'rec',
    'ua'	: 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0'

}
for i in range(10):
    print(int(i))
    data['offset'] = i *20


for i in range(10):
    item = int(i)
    data['offset'] = item *20 
    # encode
    data = urllib.parse.urlencode(data).encode(encoding='UTF8')
    # pdb.set_trace()
    request = urllib.request.Request(url, data=data, method='POST')
    response = opener.open(request)

    js_obj = json.loads(response.read())
    print(js_obj['data']['offset'])
