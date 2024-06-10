#!/usr/bin/python3
import re,requests as rr

url = "https://api.healthifyme.com/in/"
header = {'User-Agent':'Mozilla/5.0'}
data = rr.get(url, headers=header, timeout=10)
d = data.text.split()
for i in d:
    collect = re.finditer("[\da-zA-Z]+@[\d\w]+\.+[a-zA-Z]{2,3}",i,flags=re.I)
    for x in collect:
        if collect:
            print(x.group())

