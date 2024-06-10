#!/usr/bin/python3
import requests as rr

url = "https://api.sfox.com/v1/users/authenticate"
header = {'User-Agent':'Mozilla/1.0'}

payload = '{username: "adsdad", password: "sdgffg"}'

data = rr.post(url,data=payload,headers=header,timeout=10)

print(data.status_code)
print(data.text)

