# 爬取昨日之歌番剧


# 起始页 http://www.imomoe.ai/player/7835-0-0.html


# 结束页 http://www.imomoe.ai/player/7835-0-11.html
# 导包
# 爬取iframe时候注意
# 有时候会是一个列表，随意需要选定指定的iframe
# 使用iframe的时候需要使用switch_to.frame()函数调整区块


import requests
import re
import urllib.parse
import os
from selenium import webdriver

s = requests.Session()
edge = webdriver.Edge()

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.50",
    "http": "http://119.28.155.202:9999",
    "https": "https://58.253.159.136:9999"
}


def main():
    global fro
    name = input("请输入12集番的番名:")
    os.mkdir("D://爬虫爬取的网络资源/" + name)
    os.chdir("D://爬虫爬取的网络资源/" + name)
    begin = input("请输入第一集的URL:")
    fro = int(input("从第几集？"))
    to = int(input("到第几集？"))
    for i in range(to - fro + 1):
        print("正在下载第" + str(fro + i) + "集", end="")
        url = urllib.parse.urljoin(begin, "/player" + gettag(begin) + str(i + fro) + ".html")
        print(url)
        moviename = name + "第" + str(fro + i + 1) + "集.mp4"
        movie = findurl(url)
        data = requests.get(movie)
        with open(moviename, "wb") as f:
            f.write(data.content)
        print("        下载完成!")
    pass


def gettag(string: str):
    name = string.split("/")
    number = name[4].split("-")
    return "/" + name[1] + "/" + number[0] + "-0-"


def findurl(url):
    global urls
    edge.get(url)
    ifr = edge.find_elements_by_tag_name("iframe")
    edge.switch_to.frame(ifr[1])
    video = edge.find_elements_by_tag_name("video")
    for i in video:
        urls = i.get_attribute("src")
    return urls


if __name__ == "__main__":
    main()
