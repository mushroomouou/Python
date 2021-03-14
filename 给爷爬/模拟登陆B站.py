import urllib.request
import sys, os

url = 'http://www.bilibili.com'

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.55"
}

req = urllib.request.Request(url,headers=headers,method="GET")
resp = urllib.request.urlopen(req)
print(resp.read().decode('utf-8'))