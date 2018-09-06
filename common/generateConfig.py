import re


def addQuotation(fileName):
    with open(fileName) as file_object:
        rs = {}
        content = file_object.read()
        arr = content.split('\n')
        for i in arr:
            temp = re.match('(\S+)\s*:\s*([\S+\s]+)', i)
            if temp != None:
                rs .update({temp.group(1): temp.group(2)})

        return rs
