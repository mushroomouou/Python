# 本节中，我们要提取 猫眼电影 TOPlOO 的电影名称、时间、评分、图片等信息，提取的站点 URL
# http ://maoyan com/board/4 提取的结果会以文件形式保存下来

import re
import requests
import os
import urllib.parse
import time
from pandas import DataFrame
import pandas as pd

s = requests.Session()
# 爬取分析
# https://maoyan.com/board/4?offset=0 起始页， 换页多一10， 爬取到100的时候是90

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.50",
    "cookies": "uuid_n_v=v1; _lxsdk_cuid=1773d49f1ce6f-06289f2542f84a-50391c46-1fa400-1773d49f1cfc8; _lx_utm=utm_source%3Dbing%26utm_medium%3Dorganic; uuid=CA236F805FA311EBA30AA5079F202D9C7300AC663FFE4D7B807AB54E0D165841; _csrf=3b3a4761012d9683a4d92142b269e7d7c7fdc631b9db2b51ef5ccf44883aa136; lt=xuMuAA0uTY_laq7XDqwRkU9bU6gAAAAApgwAAMDWXKxsT7bq6-73YrLtrz29RQY1_2efwa5wNJva5R13HWQWjHSGIBs0OpPQGDp8Hw; lt.sig=_UNyHylKkpCmKKW5xzESJcvai_I; uid=3128199430; uid.sig=RtDIzC-Z0SLX99xkd4KYJFfpido; _lxsdk=CA236F805FA311EBA30AA5079F202D9C7300AC663FFE4D7B807AB54E0D165841; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1611640992,1611644187,1611644268; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1611644268; __mta=53768983.1611644267971.1611644267971.1611644267971.1; _lxsdk_s=1773d7ab194-0d2-c2f-5ee%7C%7C4",
    "http": "http://119.28.155.202:9999",
    "https": "https://58.253.159.136:9999"
}


def main():
    begin = "https://maoyan.com/board/4?offset=0"
    titletotal = []
    timeset = []
    scores = []
    img = []
    mainacctress = []
    html = htmlget(begin)
    for i in range(10):
        url = urllib.parse.urljoin(begin, "/board/4?offset=" + str(10 * i))
        print("正在爬取第" + str(i + 1) + "页!")
        html = htmlget(url)
        titletotal += title(html)
        img += imgs(html)
        scores += score(html)
        mainacctress += mainaccter(html)
        time.sleep(1)
    result = DataFrame({"电影名:": titletotal,
                        "得分:": scores,
                        "主演:": mainacctress,
                        "图片地址:": img})

    result.to_excel("猫眼爬取TOP100.xlsx")
    print("爬取完成！！")
def htmlget(url):
    r = s.get(url, headers=headers, )
    return r.text


def title(html):
    pattern = re.compile(
        r'<p class="name"><a href="/films/\d*" title=".*?" data-act="boarditem-click" data-val="{movieId:\d*}">(.*?)</a></p>',
        re.S)
    result = re.findall(pattern, html)
    return result


def imgs(html):
    pattern = re.compile(r'<img data-src="(.*?)" alt=".*?" class="board-img" />', re.S)
    result = re.findall(pattern, html)
    return result


def score(html):
    intpattern = re.compile(r'<i class="integer">(\d).</i>', re.S)
    fracpattern = re.compile(r'<i class="fraction">(\d)</i>', re.S)
    intresult = re.findall(intpattern, html)
    fracresult = re.findall(fracpattern, html)
    for i in range(len(intresult)):
        intresult[i] = int(intresult[i])
        intresult[i] += 0.1 * int(fracresult[i])
    return intresult


def mainaccter(html):
    pattern = re.compile(r'<p class="star">(.*?)</p>', re.S)
    result = re.findall(pattern, html)
    result = map(str.strip, result)
    return list(result)


if __name__ == "__main__":
    print("nihao")
    main()
    html = htmlget("https://maoyan.com/board/4?offset=0")
    # print(html)
    # print(imgs(html))
    # print(score(html))
    # print(mainaccter(html))
