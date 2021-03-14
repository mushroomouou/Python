import requests
from pprint import pprint

response = requests.get("http://www.zhihu.com")

pprint(response.status_code)

# 发现返回值为400 Bad Request 客户端请求的语法错误，服务器无法理解
# 头文件没有写好

headers = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
}

response = requests.get("http://www.zhihu.com",headers=headers)
pprint("状态码: {}".format(response.status_code))
pprint(response.text)
# 上面使用的headers实际上就是在模拟计算机的操作，进行一些操作。模拟浏览器，随意这时候返回值是200了而不是奇奇怪怪的数字了。