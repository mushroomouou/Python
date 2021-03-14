import requests
import pymongo
import urllib.parse
import re
import json
from pyquery import PyQuery as pq
import time
from lxml import etree
import numpy as np
from bs4 import BeautifulSoup

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",
    "referer": "https://weibo.com/cuiqingcai?profile_ftype=1&is_all=1",
    "Cookie": "SUB=_2A25NH8OXDeThGeNK6FoT8izJwz6IHXVu4-3frDV8PUJbkNANLWLzkW1NSX-YdFwNIXMzPUUdEMpNPfvL_gwb2MW4; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5LJmdgJh-6VjHihKaaANPj5NHD95QfSheReozESKnEWs4DqcjZIspNeKz0eKMpeBtt; _s_tentry=passport.weibo.com; Apache=2712885447143.7856.1612428220197; SINAGLOBAL=2712885447143.7856.1612428220197; ULV=1612428220360:1:1:1:2712885447143.7856.1612428220197:; WBtopGlobal_register_version=2021020416; SSOLoginState=1612428231; wvr=6; wb_view_log_5438222582=1920*10801; webim_unReadCount=%7B%22time%22%3A1612429251007%2C%22dm_pub_total%22%3A2%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A42%2C%22msgbox%22%3A0%7D"
}

baseurl = 'https://weibo.com/p/aj/v6/mblog/mbloglist?'
PAGES = 5
stamp = '&script_uri=/cuiqingcai&feed_type=0&page=1&pre_page=1&domain_op=100505&__rnd=1612427038839'


def main():
    like = []
    content = []
    for page in range(PAGES):
        print("正在爬取第" + str(page + 1) + "页", end="-----")
        textDataOne = getjson(page + 1, 0)
        textDataTwo = getjson(page + 1, 1)
        likeOne, contentOne = parsejson(textDataOne)
        likeTwo, coutentTwo = parsejson(textDataTwo)
        tamplike = likeOne + likeTwo
        tampcontent = contentOne + coutentTwo
        like += tamplike
        content += tampcontent
        print("爬取完成！")
        sleep = np.random.randint(1, 3)
        print("睡眠" + str(sleep) + "秒")
        time.sleep(sleep)
    like = process(like)
    print("正在存储")
    savedatatoMongo(like, content)
    print("存储结束！感谢使用！")
def process(like: list):
    for i, elem in enumerate(like):
        if elem == "赞":
            like[i] = 0
    return like
    pass

def savedatatoMongo(like, content):
    client = pymongo.MongoClient('localhost', port=27017)
    db = client['test']
    collection = db['cuiqingcaiWeiBo']
    for i, (like, cont) in enumerate(zip(like, content)):
        data = {
            'id': 230000 + i + 1,
            'content': cont,
            'like': like
        }
        collection.insert_one(data)
    return True
def getjson(page, pre):
    update = {
        'ajwvr': 6,
        'domain': 100505,
        'profile_ftype': 1,
        'is_all': 1,
        'pagebar': 0,
        'pl_name': 'Pl_Official_MyProfileFeed__20',
        'id': 1005052830678474,
        'script_uri': '/cuiqingcai',
        'feed_type': 0,
        'page': page + 1,
        'pre_page': 1,
        'domain_op': 100505,
        '__rnd': 1612427038839,
    }
    url = baseurl + urllib.parse.urlencode(update)
    req = requests.get(url=url, headers=headers)
    text = req.json()
    return text['data']
    pass


def parsejson(text):
    doc = pq(text)
    html = etree.HTML(text)
    content = list(map(str.split, html.xpath(
        '//div[@class="WB_text W_f14" and @node-type="feed_list_content" and @nick-name="崔庆才丨静觅"]/text()')))
    likes = html.xpath(
        '//li[@class]/a[@href="javascript:void(0);" and @suda-uatrack and @action-type="fl_like"]//span/em[last()]/text()')
    return likes, content
    pass


if __name__ == "__main__":
    main()
