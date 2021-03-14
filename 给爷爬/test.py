from bs4 import BeautifulSoup  # 网页解析
import re  # 正则表达式搜索
import urllib.request, urllib.error  # 指定URL文件
import xlwt  # 进行excel操作
import sqlite3  # 对SQL 数据库惊醒操作

findlink = re.compile(r'<a class=".*?">')  # 表示规则
findtitle = re.compile(r'<span class="title">.*</span>')
findImg = re.compile(r'<img width=.*" class="">', re.S)
findRating = re.compile(r'<span class="rating_num" property="v:average">.*</span>')
findJudge = re.compile(r'<span>\d*人评价</span>')
findinq = re.compile(r'<span class="inq">.*</span>')
finddetial = re.compile(r'<p class="">(.*?)</p>',re.S)

def main():
    baseUrl = "https://movie.douban.com/top250?start="
    datalist = getData(baseUrl)
    # savepath = ".\\豆瓣电影Top250.xls"
    # saveData(savepath)


def getData(baseurl):
    # 获取数据
    datalist = []
    for i in range(0, 25):
        url = baseurl + str(i * 25)
        html = askURL(url)
        soup = BeautifulSoup(html, "html.parser")
        data = []
        for item in soup.find_all('div', class_="item"):
            titles = []
            item = str(item)

            link = re.search(findlink, item)[0]  # 使用re库去查找符合震泽的字符串
            title = re.findall(findtitle, item)  # 片名可能还有其他的名字
            rating = re.findall(findRating, item)[0]
            img = re.findall(findImg, item)
            inq = re.findall(findinq, item)
            detil = re.findall(finddetial, item)[0]
            if len(title) == 2:
                data.append(title[0])
                otitle = title[1].replace('/','') # 去掉无关的符号
                data.append(otitle)
            else:
                data.append(title[0])
                data.append(" ")
            if len(inq) != 0:
                inq = inq[0].replace('。','') # 替换句号
                data.append(inq[0])
            else:
                data.append(" ")
            db = detil[0]
            db = re.sub('<br(\s+)?/>(\s+)?',' ',db)
            data.append(db.split())
            data.append(rating)
            data.append(link)
            data.append(rating)
        datalist.append(data)
    print(datalist)
    return datalist


def askURL(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.55",
    }
    # 告诉豆瓣，我们是什么东西，本质上是我们可以接受什么信息。
    request = urllib.request.Request(url, headers=headers)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
        # 打印一些结果是否成立，是否有结果。

    return html


# 保存数据
def saveData(path):
    pass


if __name__ == "__main__":
    main()
