import requests
import re
import json


# 通过cookies参数设置

cookie='d_c0="AICi4CUL_gyPTrryn2WGt98K_4r3Oai765M=|1515987004"; _zap=3202ce39-479f-4c98-b0c8-a572b0661e3c; _xsrf=EQpsGlzS58HNaXb0qS9M7xkCtPB6X8vb; q_c1=3968a252d5d144d4a2ade78b24006f5c|1553997216000|1515987001000; __utma=51854390.1287153146.1523586964.1536226978.1553997219.3; __utmc=51854390; __utmz=51854390.1553997219.3.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.000--|2=registration_date=20140620=1^3=entry_date=20180115=1; capsion_ticket="2|1:0|10:1553999683|14:capsion_ticket|44:YmIyMDAzNWMzY2IxNDk3ZThkMGU3YmQ3ZWU2NmNkNjY=|8694104a2d4660c18e06d1375ed9f430c058fd7c70038dc7a0e1f4eded3e87e0"; l_n_c=1; r_cap_id="MzQwNzg0OGFhZDRlNDQ1NWE1MWJlZDhiNzY4ZTRjZTI=|1553999687|880f8f4a1ac912148d5d885c6ca69641c1d0f6c6"; cap_id="MmEyOTRhMmIwYTMxNGI1YjkxYjIxNzRhNmNjNzhlMDk=|1553999687|3133a048c6d363a4653cc854d45c83e2e78a3874"; l_cap_id="MjA1ZTc2NTBlOTk3NGUwN2FiODM5YWQ0YWNhYTM0YzA=|1553999687|4108da702662f2928ee435e5d9a85ef3a43738c8"; z_c0=Mi4xMkxGa0FBQUFBQUFBZ0tMZ0pRdi1EQmNBQUFCaEFsVk5WM1dOWFFBdkV0YUxMSUVXSXZDM2lMSExWbWpBN1h3MlJ3|1553999703|b5a8b69df7f16d263b79f3b74e9a104c69ee98d6; n_c=1; tst=r'
jar = requests.cookies.RequestsCookieJar()
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'Host': 'www.zhihu.com'
}
for cookie in cookie.split(';'):
    key, value = cookie.split('=', 1)
    jar.set(key, value)
r = requests.get('https://www.zhihu.com/', cookies=jar, headers=headers)
print("++++++++++++++++++++++++++")
print(r.text)
# # 将cookies 添加到headers中
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
#     'Host': 'www.zhihu.com',
#     'Cookie': 'd_c0="AICi4CUL_gyPTrryn2WGt98K_4r3Oai765M=|1515987004"; _zap=3202ce39-479f-4c98-b0c8-a572b0661e3c; _xsrf=EQpsGlzS58HNaXb0qS9M7xkCtPB6X8vb; q_c1=3968a252d5d144d4a2ade78b24006f5c|1553997216000|1515987001000; __utma=51854390.1287153146.1523586964.1536226978.1553997219.3; __utmc=51854390; __utmz=51854390.1553997219.3.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.000--|2=registration_date=20140620=1^3=entry_date=20180115=1; capsion_ticket="2|1:0|10:1553999683|14:capsion_ticket|44:YmIyMDAzNWMzY2IxNDk3ZThkMGU3YmQ3ZWU2NmNkNjY=|8694104a2d4660c18e06d1375ed9f430c058fd7c70038dc7a0e1f4eded3e87e0"; l_n_c=1; r_cap_id="MzQwNzg0OGFhZDRlNDQ1NWE1MWJlZDhiNzY4ZTRjZTI=|1553999687|880f8f4a1ac912148d5d885c6ca69641c1d0f6c6"; cap_id="MmEyOTRhMmIwYTMxNGI1YjkxYjIxNzRhNmNjNzhlMDk=|1553999687|3133a048c6d363a4653cc854d45c83e2e78a3874"; l_cap_id="MjA1ZTc2NTBlOTk3NGUwN2FiODM5YWQ0YWNhYTM0YzA=|1553999687|4108da702662f2928ee435e5d9a85ef3a43738c8"; z_c0=Mi4xMkxGa0FBQUFBQUFBZ0tMZ0pRdi1EQmNBQUFCaEFsVk5WM1dOWFFBdkV0YUxMSUVXSXZDM2lMSExWbWpBN1h3MlJ3|1553999703|b5a8b69df7f16d263b79f3b74e9a104c69ee98d6; n_c=1; tst=r'
# }
# r = requests.get('https://www.zhihu.com/explore', headers=headers)


exit() if not  r.status_code == requests.codes.ok else print('Request Successfully')
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
title = re.findall(pattern, r.text)
print(r.text)



# print(type(r.status_code), r.status_code)
# print(type(r.headers), r.headers)
# print(type(r.cookies), r.cookies)
# print(type(r.url), r.url)
# print(type(r.history), r.history)


data = {
    'name': 'renwoxing',
    'age': '24'
}
response = requests.post('http://httpbin.org/post', data)
print(response.text)
