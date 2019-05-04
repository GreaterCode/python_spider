import requests
import json
data = {
    'name': 'renwoxing',
    'age': 25
}
r = requests.get('http://httpbin.org/get',params=data)
print(type(r))
print(r.status_code)
print(type(r.text))

#将返回结果转字典格式
try:
    print(r.json())
except json.decoder.JSONDecodeError as e:
    print(e)
print(type(r.json()))
print(r.text)
print(r.cookies)

# 发送其他类型请求实例
r = requests.post('http://httpbin.org/post')
r = requests.put('http://httpbin.org/put')
r = requests.delete('http://httpbin.org/delete')
r = requests.head('http://httpbin.org/get')
r = requests.options('http://httpbin.org/get')