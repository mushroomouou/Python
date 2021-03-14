'''
正则表达式:
. 表示任意符号
[ ] 字符集，表示给定字符的取值范围
[^ ] 非字符集， 指定字符的外交
* 前一个字符的0次或者无限次次数展开   如 abc*  表示 abc* abc abcccc
+ 表示前一个字符的1次或者无限次拓展
? 前一个字符的0次或者1次拓展
| 表示左右任意一个 abc|bcf
{m} 拓展前的一个字符出现了m次 ab{2}c 表示 abbc
{m,n} 拓展前一个字符出现了m至n次，包含n
^ 匹配字符串开头 ^abc 表示以abc开头的字符串
$ 匹配字符串的结尾  abc$ 以abc 结尾的字符串
() 分组标记 内部只能使用 | 操作符   （abc|def）表示abc,def
\d 数字，等价于 [0-9]
\w 单词字符 等价于 [A-Za-z0-9_]
'''
'''
re 库
re.search() 在一个字符串中匹配正则表达式的第一个位置， 返回match对象
re,match() 从一个字符串开始的位置起匹配正则表达式，返回match对象
re.findall() 搜索字符串，将所有匹配的子串以列表的形式返回
re.split() 将一个字符串以正则表达式的匹配结果进行分割，返回列表
re.finditer() 搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素都是match对象
re.sub() 在一个字符串中替换所有匹配正则表达式的子串，返回替换后的子串
'''

# 字符串模式：字符串模式 （判断一个字符串是否符合一定的标准）

import re

# pat = re.compile("AA") # 此处的AA是正则表达式的内容
# m = pat.search("AAcAAAAAABBBBAA") # search 方法查找的是第一个返回的是第一个的坐标
# print(m) # compile()就是匹配的模板，
#
# m = re.search("asd","asdASD") # 没有compile的时候可以直接在后面填入被匹配的对象
# print(m)

# print(re.findall("[A-Z]+","ASaaaaaJEFHIEDOCNsfisnecishnfawd"))
# findall 方法就可以实现对所有符合的打印

# sub
print(re.sub("ab","AB","abcdeadae"))
# 第一个是被替换的字符串， 用第二个参数去把第二个替换
# 建议在正则表达式中，被比较的字符串在前面加上r，不用担心转义字符的问题
