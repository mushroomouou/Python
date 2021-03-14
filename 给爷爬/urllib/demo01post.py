from urllib import request
from urllib import parse
from pprint import pprint
data = bytes(parse.urlencode({'word': 'hello'}), encoding='utf-8')
response = request.urlopen("http://httpbin.org/post",data=data)

# print("{}".format(response.read().decode('utf-8')))
pprint(response.read())
print("{}".format(response.status))
print("{}".format((response.getheaders())))
print("{}".format(response.getheader('Server')))  # 表示这个网站是用什么框架搭建的
