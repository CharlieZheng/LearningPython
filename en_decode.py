import  urllib.parse
dic = {
    'kj':'借款借款金额'
}
ecode = (urllib.parse.urlencode(dic))
dcode = urllib.parse.unquote(ecode)
print(ecode ,dcode)