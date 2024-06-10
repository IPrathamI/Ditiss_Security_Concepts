#!/usr/bin/python3
import requests as rr

url = "https://paalam.wellnessforever.in/crm/v2/firstRegisterCustomer"
header = {'User-Agent':'Mozilla/1.0'}

payload = {'method':'firstRegisterApi&data=%7B%22','customerMobile':'%22%3A%229999999999%22%2C%22','generateOtp':'%22%3A%221%22%2C%22','otpchar':'%22%3A%22Y%22%7D'}

data = rr.post(url,params=payload,headers=header,timeout=10)

print(data.status_code)
print(data.text)

