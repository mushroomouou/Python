from bs4 import BeautifulSoup
import re

file = open("./百度一下，你就知道.html", "rb")
html = file.read().decode('utf-8')
bs = BeautifulSoup(html, "html.parser")  # 通过这个方法实现把这个文件解析称为了一个树形结构
# 解析谁，解析器的选择！
# print(bs.title)
# print(bs.a) # <class 'bs4.element.Tag'> 是这个内容！！拿到的是第一个东西！
# 这时侯我们解析器会帮我们把第一个拿到的东西打印出来
# print(bs.title.string) # 加上我们的string就打出唯一的内容
# <class 'bs4.element.NavigableString'>标签里的字符串
# 可以获得属性值！是以字典方式返回的

# print(type(bs))
# print(type(bs.a.string))
# 1.Tag 标签及其对象 但是默认只拿到第一个内容。
# 2. NavugableString 标签里面的内容，字符串
# 3. attrs这里是字典的内容。把刚刚标签里面的东西放进字典构造器构造。
# 4. beautifulsoup 整个文档。
# 5. elem.Comment 文档的注释

# -------------------------------------------------
#  文档的遍历

# print(bs.head.contents[1]) # 这时以列表的方式拿出

# 更多文件见搜索文档


#  文档的搜索

t_list = bs.find_all('a')
# print(t_list)

# 正则表达式搜索， 使用search（） 找到所有匹配的内容
t_list2 = bs.find_all(re.compile("a"))

# print(t_list)

# 根据函数来搜索：
def name_is_exits(tag):
    return tag.has_attr("name")

t_list3 = bs.find_all(name_is_exits)
# print(t_list3)

t_list4 = bs.find_all(id = "head")

t_list5 = bs.find_all(hred="http://www.baidu.com")


t_list6 = bs.find_all(text = re.compile("\d"))

# print(t_list5)
# print(t_list6)

# css 选择器：
# print(bs.select("title"))  # 按照title来查找

# print(bs.select(".mnav"))  # 按照类名来查找

# print(bs.select("a[class='bri']")) # 通过属性查找

list =  bs.select(".mnav")
print(list[0].get_text())
