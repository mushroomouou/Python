import requests
from pprint import pprint

response = requests.get("http://httpbin.org/get")

pprint("状态码： {}".format(response.status_code))
pprint(response.text)
# 状态码405 Method Not Allowed 客户端请求中的方法被禁止

response = requests.post("http://httpbin.org/post")

pprint("状态码: {}".format(response.status_code))
pprint(response.text)

response = requests.put("http://httpbin.org/put")

pprint("状态码： {}".format(response.status_code))
pprint(response.text)