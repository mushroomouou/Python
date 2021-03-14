import requests

URL: str = "http://c.biancheng.net/uploads/course/python_spider/191009.html"

res = requests.get(URL)

res.encoding = 'utf-8'

with open('test01.txt','a+') as file:
    file.write(res.text)
    