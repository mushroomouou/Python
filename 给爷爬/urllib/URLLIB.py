import urllib.request
import urllib.parse

# rsp = urllib.request.urlopen("http://www.baidu.com")
# print(rsp.read().decode('utf-8'))
# 在使用的urllib的时候我们一定记得加上编码，加上我们的utf-8的编码否则会效果会很糟糕。

# 我们现在的方式就是get方式的请求。
# rsp = urllib.request.urlopen("http://httpbin.org/post")
# print(rsp.read().decode('utf-8'))
# 发现有问题 无法访问 URL无法使用 不能post 我们需要一些表单信息

# data = bytes(urllib.parse.urlencode({"hello": "world"}),encoding="utf-8")
# # 上面这个data里面就有些信息，可以帮助我们输入到服务端
# rsp = urllib.request.urlopen("http://httpbin.org/post",data=data)
# print(rsp.read().decode('utf-8'))
# 相当于是什么，我们post方法一定得有我们的想要传入的数据，需要data数据的传入。
# 经过与http://httpbin.org 的官方代码的比对，我们发现User-Agent不是一样的，
# 我们这里是以urllib进行访问的不是浏览器，会被发现的！！

# 超时处理：
# try:
#     rsp = urllib.request.urlopen("http://httpbin.org/get", timeout=0.01)
#     print(rsp.read().decode('utf-8'))
# except urllib.error.URLError as e:
#     print("time out!")


# rsp = urllib.request.urlopen("http://douban.com")
# print(rsp.status) # 状态码，200 成功访问
# HTTP Error 418 你被发现是个爬虫了。

# rsp = urllib.request.urlopen("http://www.baidu.com")
# print(rsp.getheader("Server"))
# 上面发现我们的getheader就可以得到指定的头文件，而getheaders()可以获得所有的header

# 豆瓣说我是个茶壶，我们需要对自己进行封装
# url = "http://www.douban.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.55"
}
# 使用headers表示我们是一个浏览器，当然我们还可以加更多的请求。
# 在对指定的网站访问的时候我们就得在对应网站查询headers 全部封装好就加进去。
# url = "http://httpbin.org/post"
# data = bytes(urllib.parse.urlencode({"name": "eric"}),encoding='utf-8')
# req = urllib.request.Request(url=url, headers=headers, data=data,method="POST")
# resp = urllib.request.urlopen(req)
# print(resp.read().decode("utf-8"))w
# 这样就实现了我们的访问操作。而且是对自己包装后的效果

url = "http://douban.com"
req = urllib.request.Request(url=url, headers=headers, method="GET")
resp = urllib.request.urlopen(req)
print(resp.read().decode('utf-8'))

# 我们不是茶壶了，很成功！！
