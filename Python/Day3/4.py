#!/usr/bin/python3
import re,requests as rr

url = "https://www.bincodes.com/random-creditcard-generator/"
header = {'User-Agent':'Mozilla/5.0'}
data = rr.get(url, headers=header, timeout=10)
d = data.text.split()
for i in d:
    collect = re.findall("[0-9]{14,16}",i)
    if collect:
        print(collect)

