# -*- coding:utf-8 -*-

import urllib.request as req
import sys
sys.path.append('../common')

import generateConfig
import ssl
import random
import ua


def run():
    context = ssl._create_unverified_context()
    user_agent = random.choice(ua.ua_list)

    headers = generateConfig.addQuotation('headers')
    data = str(generateConfig.addQuotation('params')).encode('utf-8')
    url = req.Request(
        "https://api.weibo.com/webim/2/direct_messages/contacts.json?source=209678993&count=20&add_virtual_user=5,&is_include_group=0&callback=STK_15362164478301", method='GET')
    url.add_header('User-Agent', user_agent)
    for i in headers:
        url.add_header(i, headers[i])
    f = None
    try:

        res = req.urlopen(url, context=context, data=data)
        html = res.read()
        # print(html.decode('unicode-escape'))

        # html = html.decode('unicode-escape').encode('utf-8')
        print(res.getcode())
        print(res.geturl())
        print(res.info())
        f = open('getOrderList.html', 'wb')  # 若是'wb'就表示写二进制文件
        f.write(html)
    # except Exception as e:
    #     print(e)
    finally:
        if f != None:
            f.close


run()
