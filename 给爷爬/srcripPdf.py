import urllib
import time
import urllib.request
from urllib.parse import unquote_plus
import re
import os


def strPlus(stringOne: str, stringTwo: str) -> str:
    return stringOne + stringTwo


def characterTranspose(filename: str) -> str:
    tamp: list = filename.split('%')
    name = ""
    for elem in tamp:
        if elem == tamp[0] or elem == tamp[-1]:
            name = strPlus(name, elem)
            continue
        else:
            elem = "\\" + elem
            name = strPlus(name, elem)
    return name


def getPdf(url: str) -> None:
    fileName = url.split('/')[-1]
    fileName = unquote_plus(fileName)
    f = open(r"C:\Users\HP2\Desktop\文献\\" + fileName, 'wb')
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.57"}
    req = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(req)

    book_sz = 8193
    while True:
        time.sleep(2)
        buffer = response.read(book_sz)
        if not buffer:
            break
        f.write(buffer)
    print("下载成功！")
    f.close()


if __name__ == "__main__":
    os.chdir("C:/Users/HP2/Desktop/文献")
    url: str = input("请输入你的url：")
    getPdf(url)

# Bug,在爬取文献pdf的时候，我们的urlopen的频率过快被误以为是爬虫了，所以使用time里面的sleep函数稍微停一会，免得被认出来了。
