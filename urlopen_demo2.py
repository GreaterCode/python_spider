import urllib.request
import urllib.parse
import socket

data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
try:
    response = urllib.request.urlopen('http://httpbin.org/post', data=data, timeout=3)
    print(response.read())
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print("timeout")