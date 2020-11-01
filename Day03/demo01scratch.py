# massage = "Hello Python Crash Course reader!"
# print(masage)
#编译器不会帮你纠正拼写、
# massage_one = 'hello , how are you?'
# massage_two = 'I am fine !'
# massage_thr = 'really?'
# print(massage_two)
#
#关于String 的一些其他东西
name = 'hang xing jie'
print(name.title())#'.'表示对变量执行’。‘后接的方法  每个方法后面都会跟上一个括号  但是由于title 方法不需要括号里额外的信息  故可以直接运行
print(name.upper())#表示全部打写
print(name.lower())#表示全部小写
#String字符串的拼接直接使用’+‘
print('Python')
print('\tPython')
print('Language:\n\tPython\n\tC\n\tJavaScripy')#\n表示换行  \t 表示制表符空格
#字符串中额外空白的删除
favorite_language = ' Python '
favorite_language = favorite_language.strip()#.strip表示完全删除两边空白  而rstrip 与  lstrip  分别为右左边
print(favorite_language)
famous_person = 'albert einstein'
famous_person = famous_person.title()
print(famous_person + " " + "once said" + ":" +'"A person who never made mistake never tried anything new."'+''
                                                                                                             '\n                                                                           -----' + famous_person)

age = 18#使用str()方法把age int类型转化为str
print('Happy' + ' ' + str(age) + 'th' + ' ' + 'birthday!')

import this