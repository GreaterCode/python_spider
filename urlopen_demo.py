import urllib.request

response = urllib.request.urlopen('https://www.baidu.com/')
print(response.read().decode('utf-8'))
print(type(response))
print(response.status)
print(response.getheader('Cache-Control'))
print(response.getheaders())
print(response.version)
print(response.read())