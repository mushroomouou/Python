import requests
import pymongo
from urllib.parse import urlparse, urlencode, parse_qs
import time

OFFSET = str(0)
params = {
    'aid': '24',
    'app_name': 'web_search',
    'offset': OFFSET,  # 记录到200
    'format': 'json',
    'keyword': '街拍',
    'autoload': 'true',
    'count': '20',
    'en_qc': '1',
    'cur_tab': '1',
    'from': 'search_tab',
    'pd': 'synthesis',
    'timestamp': '1612528164242',
    '_signature': '_02B4Z6wo00f01vEUsMQAAIDDP7qtgPz2CF7xMbRAANxlthUO7IcFD2uVqtP2Qo5UJ.KNMc6sBEt4I8pNF8AFeHkONeTsxlHlH1tdEtrYlwLXuRiJ23VvuoYWoVnJ22QLal6p2liMTZSda6dOec'
}

baseurl = 'https://www.toutiao.com/api/search/content/?'

testurl = baseurl + urlencode(params)

headers = {
    'Host': 'www.toutiao.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0',
    'Accept': 'application/json, text/javascript',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate, br',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Connection': 'keep-alive',
    'Referer': 'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D',
    'Cookie': 'tt_webid=6925754511811266062; ttcid=6e4facfe848c4894995c72a21d3c054336; csrftoken=7d3074bdc7143167f3f5001b84ab5077; s_v_web_id=verify_kks9h28w_HrNrcqeQ_kHZo_41U0_9fMX_K4kdCd0SUkfC; MONITOR_WEB_ID=935ec94f-b3a6-490b-9e63-e11bd6456e6e; tt_webid=6925754511811266062; __tasessionId=f4yf1xhxl1612527975095; csrftoken=7d3074bdc7143167f3f5001b84ab5077; tt_scid=HMeRGKJ4bR7zIIR2COiC1eOJNn2.Iv6e9oUF5nAQ3naUpZfntdR2Qj7mwbxdWXEI4ffc',
    'TE': 'Trailers',
}


def main():
    title = []
    abstract = []
    imgurl = []
    timelist = []
    for page in range(10):
        OFFSET = str(20 * page)
        params['offset'] = OFFSET
        print("正在爬取第" + str(page + 1) + "页")
        url = baseurl + urlencode(params)
        jsondata = getjson(url)
        content = list(getcontent(jsondata))
        print("爬取完成", "填入数据！")
        title += content[0]
        abstract += content[1]
        imgurl += content[2]
        timelist += content[3]
    print("====================")
    print("正在存储到Mongo")
    Savedata(title=title, abstract=abstract, imgurl=imgurl, timeset=timelist)
    print("存储完成！", time.strftime("%Y-%m-%d %H:%M:%S"))
    print("====================")
    pass


def getjson(url):
    jsondata = requests.get(url=url, headers=headers).json()['data']
    return jsondata
    pass


def getimg(obj: dict):
    imgurllist = []  # 这里输入的是一个类，是隶属于今日头条的一行
    # print(obj)
    for elem in obj:
        # print(elem)
        if 'image' in elem:
            # print(obj[elem])
            # print(type(obj[elem]))
            if obj[elem] == 'image_list':
                for imgurl in obj[elem]:
                    imgurllist.append(imgurl['url'])
            elif isinstance(obj[elem], bool):
                pass
            elif isinstance(obj[elem], int):
                pass
            elif obj[elem] == None:
                pass
            elif 'http' in obj[elem]:
                # print(obj[elem])
                imgurllist.append(obj[elem])
        # elif 'queries' == elem:
        #     imgurls = obj[elem]
        #     for img in imgurls:
        #         imgurllist.append(img['url'])
        # 可能会返回空list
        if len(imgurllist) == 0:
            imgurllist.append("NULL")
    return imgurllist[-1]  # 返回最后一个url


def getcontent(jsondata):
    positionRecord = []
    titleRecord = []
    abstract = []
    img = []
    timeset = []
    for i, obj in enumerate(jsondata):
        if 'title' in obj.keys():
            positionRecord.append(i)
            titleRecord.append(obj['title'])
        if 'abstract' in obj.keys():
            abstract.append(obj['abstract'])
        elif 'title' in obj.keys():
            abstract.append(obj['title'])
        img.append(getimg(obj))
        timeset.append(time.strftime("%Y-%m-%d %H:%M:%S"))
    return titleRecord, abstract, img, timeset
    pass


def Savedata(title, abstract, imgurl, timeset):
    client = pymongo.MongoClient('localhost', port=27017)
    db = client['spider']
    collection = db['toutiao']
    for i, (ti, ab, im, times) in enumerate(zip(title, abstract, imgurl, timeset)):
        data = {
            "id": 400001 + i,
            "date": times,
            "title": ti,
            "abstract": ab,
            "imageurl": im,
        }
        collection.insert_one(data)


if __name__ == "__main__":
    main()
