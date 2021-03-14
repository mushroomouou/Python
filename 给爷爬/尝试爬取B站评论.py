import re
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import gzip
from io import BytesIO

'''
#--------------------------------------------------------------------------------
操作日志：
请求函数： 返回html文档

#--------------------------------------------------------------------------------
'''
findcomment = re.compile(r'<p class="text">.*</p>',re.S)

def main():
    url = "https://www.bilibili.com/video/BV1ot411y7mU"
    comment = getData(url)
    pass

def getData(url):
    html = askUrl(url)
    bs = BeautifulSoup(html, "html.parser")
    file = str(bs)
    comment = re.findall(findcomment,file)
    print(html)
    for elem in comment:
        print(elem)
    return comment
    pass


def askUrl(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.55"
    }
    resp = urllib.request.Request(url=url, headers=headers, method='GET')
    rep = urllib.request.urlopen(resp)
    html = rep.read()
    buff = BytesIO(html) # 发现我们的函数不可解码，是由于网页的文档被压缩过了，所以需要我们的操作去解码。
    file = gzip.GzipFile(fileobj=buff).read().decode('utf-8')
    return file


if __name__ == "__main__":
    main()
