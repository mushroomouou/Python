# python爬取网络漫画

# 要求
# 1. 已知漫画名就可以爬取指定集数的漫画并且存储起来
# 2. 有明显的错误处理操作
# 网站   http://www.mangabz.com

# 导包

import requests
from urllib.parse import urlencode
from pyquery import PyQuery
from selenium import webdriver
from pyquery import PyQuery as pq
from pandas import DataFrame
from pandas import Series
import time
import sys
import os
import re

headers = {
    'Referer': 'http://www.mangabz.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.63',
    # 'Cookie':'__cfduid=d870b1530435446c9569b766bccc4ff341612766070; MANGABZ_MACHINEKEY=9eb5b82c-c4ce-4b4d-b98c-ac20e7e4b92a; mangabz_newsearch=%5b%7b%22Title%22%3a%22%e4%b8%80%e6%8b%b3%e8%b6%85%e4%ba%ba%22%2c%22Url%22%3a%22%5c%2fsearch%3ftitle%3d%25E4%25B8%2580%25E6%258B%25B3%25E8%25B6%2585%25E4%25BA%25BA%22%7d%5d; UM_distinctid=1778059aed12c8-04ec26c5e466e98-4c3f217f-1fa400-1778059aed2ab; CNZZDATA1278095929=1314768920-1612762169-http%253A%252F%252Fwww.mangabz.com%252F%7C1612762169; CNZZDATA1278095942=1019928459-16127641…278515277=359794671-1612764736-http%253A%252F%252Fwww.mangabz.com%252F%7C1612764736; _Mangabz_Mangamangabz=AAEAAAD/////AQAAAAAAAAAMAgAAAEJJTGlrZS5Ub29scywgVmVyc2lvbj0xLjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPW51bGwFAQAAABlJTGlrZS5Ub29scy5Vc2VyUHJpbmNpcGFsBgAAAAlfaWRlbnRpdHkHX3VzZXJJRAlfdXNlck5hbWUIX3JvbGVJRHMIX2lzQWRtaW4dTWFyc2hhbEJ5UmVmT2JqZWN0K19faWRlbnRpdHkDAAEHAAIjU3lzdGVtLlNlY3VyaXR5LlByaW5jaXBhbC5JSWRlbnRpdHkICAECAAAACgAAAAAGAwAAABdodWFuZ3hpbmdqaWVna2RAMTYzLmNvbQkEAAAAAAoPBAAAAAAAAAAICw=='
}

oriurl = "http://www.mangabz.com"
baseurl = "http://www.mangabz.com/search?title="  # 后面接的是搜索的参数
imageappend = "chapterimage.ashx?"
imgbase = "http://image.mangabz.com/"

page = 0
cid = 0
mid = 0
key = 0

params = {
    'cid': cid,
    'page': page,
    'key': 0,
    '_cid': cid,
    '_mid': 11075,
    '_dt': '2021-02-08 18:20:06',
    '_sign': '207197d11fd7853fb4e7acdfe5e43e85'
}


def main():
    print("==============================")
    print("=欢迎使用漫画花里胡哨下载脚本=")
    print("=强烈建议在网络良好情况下使用=")
    print("==============================", end="\n\n\n")
    anime = input("请输入你的要下载的漫画名:")
    print("正在搜索，请等待！    🙂", end="\n\n")
    try:
        req = requests.get(baseurl + anime, headers=headers)
    except:
        print("害，🤦，你是不是没联网！‍")
    try:
        urlUpdate = showname(pq(req.text))
    except:
        print("可能网络不行")
    print(urlUpdate)
    checking = input("请确认是哪一个：（如果没有， 输入-----无）")
    url = oriurl + geturlUpdate(checking, urlUpdate)
    check404(url)
    nameTitle = Source(url)
    print("想下载从哪到哪❓")
    frompoint = int(input("从:"))
    topoint = int(input("到:"))
    print("你想存到哪里呢？")
    location = input("请输入正确的路径：")
    os.chdir(location)
    os.mkdir(anime)
    os.chdir(location + "\\" + anime)
    print("ok!", "这就为您效劳！")
    pageurl = getPageUrl(url, begin=frompoint, end=topoint)
    for i, url in enumerate(pageurl):
        os.mkdir(nameTitle[i])
        os.chdir(nameTitle[i] + "\\")
        print("正在下载第" + str(i + 1) + "集")
        getimageurl(url)
        os.chdir('..\\')


def getimageurl(url: str, ):
    req = requests.get(url, headers=headers)
    doc = pq(req.text)
    maxpage = int(doc('#lbcurrentpage').parent().text().split('-')[-1])  # 获得最大页数
    print('Max Page', maxpage)
    cid = int(url.split('/')[-2][1:])  # 正确
    pattern = re.compile(r'dm5imagefun(.*?)_', re.S)
    params['_cid'] = cid
    params['cid'] = cid
    params['page'] = 1
    imgreq = url + imageappend + urlencode(params)
    text: str = str(requests.get(imgreq, headers=headers).text)
    result = str(re.findall(pattern, text)[0]).split('|')
    Index1 = 0
    Index2 = 0
    key: str
    imgoriurl: str
    index: str = ""
    if result[-3].isdigit():
        Index1 = str(result[-2])
        Index2 = str(result[-3])
        key = str(result[-4])
    else:
        Index1 = "1"
        Index2 = str(result[-2])
        key = str(result[-3])
    param = {
        'cid': cid,
        'key': key,
        'uk': ""
    }
    for i in range(maxpage):
        params['page'] = i + 1
        print("Page" + str(i + 1) + '正在下载', end='----------')
        imgreq = url + imageappend + urlencode(params)
        req = requests.get(imgreq, headers)
        doc = str(req.text)
        spldoc = doc.split('|')
        if i + 1 != maxpage:
            index = spldoc[-14]
        else:
            index = spldoc[-15]
        imgurl = imgbase + Index1 + '/' + Index2 + '/' + str(cid) + '/' + index + '.jpg?' + urlencode(param)
        img = requests.get(imgurl, headers)
        with open(str(i + 1) + '.jpg', 'wb') as f:
            f.write(img.content)
        print('下载完成！')


def getPageUrl(url, begin, end):
    req = requests.get(url, headers=headers)
    doc = pq(req.text)
    aTag = doc('div .detail-list-form-con').children('a')
    href = []
    for elem in aTag.items():
        href.append(oriurl + elem.attr.href)
    href = href[::-1][begin - 1:end]
    return href


def Source(url):
    req = requests.get(url, headers=headers)
    doc = pq(req.text)
    tagA = doc('div .detail-list-form-con').children('a')
    nameTitle = []
    for a in tagA.items():
        nameTitle.append(a.text().split()[0] + a.text().split()[1])
    nameTitle = nameTitle[::-1]
    nameresult = Series(nameTitle, index=range(len(nameTitle)))
    for i, name in nameresult.items():
        print(int(i) + 1, name)
    print('总:', len(nameTitle))
    return nameTitle


def geturlUpdate(checking: str, urlUpdate: DataFrame) -> str:
    animeIndex = -1
    if checking == "无":
        print("谢谢使用！")
        sys.exit()
    if checking.isdigit():
        animeIndex = urlUpdate.index.to_list()[int(checking)]
    elif checking in urlUpdate['漫画名'].values.tolist():
        animeIndex = urlUpdate[urlUpdate['漫画名'] == checking].index.to_list()[0]
    elif checking in urlUpdate['网站后缀'].values.tolist():
        animeIndex = urlUpdate[urlUpdate['网站后缀'] == checking].index.to_list()[0]
    else:
        print("😂😂")
        print("请不要试图嘲讽我这一个简单的脚本！")
        print("我只想好好的爬资源！")
        print("---------------")
        print("还是付错了人！！！")
        sys.exit()
    return str(urlUpdate['网站后缀'][animeIndex])
    pass


def check404(url):
    print("正在检测是否还有资源！")
    req = requests.get(url, headers=headers)
    doc = pq(req.text)
    if doc('.img-404'):
        print("这个漫画被禁了，没有资源！")
        sys.exit()
    else:
        print("OK")
        print("这就着手下载。")
    pass


def showname(text: PyQuery):
    text = text('h2 a')
    hrefUrl = []
    animeName = []
    for a in text.items():
        hrefUrl.append(a.attr.href)
        animeName.append(a.attr.title)
    anime_href = DataFrame({
        "漫画名": animeName,
        "网站后缀": hrefUrl,
    })

    return anime_href


if __name__ == "__main__":
    main()
    print("谢谢使用!😀😀😀😀😀😀😀😀")
    pass
