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

    headers = generateConfig.addQuotation('../common/headers')
    data = str(generateConfig.addQuotation('getOrderListParams')).encode('utf-8')
    url = req.Request(
        'https://kyfw.12306.cn/otn/queryOrder/queryMyOrder', method='POST')
    url.add_header('User-Agent', user_agent)
    for i in headers:
        url.add_header(i, headers[i])
    f = None
    try:

        res = req.urlopen(url, context=context, data=data)
        html = res.read()
        print(res.getcode())
        print(res.geturl())
        print(res.info())
        f = open('getOrderList.html', 'wb')  # 若是'wb'就表示写二进制文件
        f.write(html)
    # except Exception as e:
    #     print('发生了错误', e)
    finally:
        if f != None:
            f.close


run()
