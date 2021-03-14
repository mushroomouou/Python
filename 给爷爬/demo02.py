import requests
from pprint import pprint
response = requests.get("http://www.baidu.com")

response.encoding =response.apparent_encoding
# encoding是从http中的header中的charset字段中提取的编码方式，若header中没有charset字段则默认为ISO-8859-1编码模式，则无法解析中文，这是乱码的原因
# apparent_encoding会从网页的内容中分析网页编码的方式，所以apparent_encoding比encoding更加准确。当网页出现乱码时可以把apparent_encoding的编码格式赋值给encoding。
print("状态码: {}".format(response.status_code))
pprint(response.text)