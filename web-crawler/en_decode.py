# -*- coding: utf-8 -*-
import urllib.parse
dic = {
    '姓名': '郑汉荣'
}
ecode = (urllib.parse.urlencode(dic))
dcode = urllib.parse.unquote(ecode)
print(ecode, dcode)
