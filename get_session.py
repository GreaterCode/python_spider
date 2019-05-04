import requests

s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/1234')
r = s.get('http://httpbin.org/cookies')
print(r.text)