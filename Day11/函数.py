# 定义一个函数
def say_hello():
    print('你好啊')
    pass

say_hello()
print('============================================')

# 向函数传递一个参数         添加默认值  =''
def say_hello_to_somebody(username='黄星杰'):
    print('你好啊'+username+ '!' +'\n今天也好是要努力呢！')
    pass
say_hello_to_somebody()
print('============================================')


# 可以使用关键字对实参进行引导
say_hello_to_somebody(username='李斯茂')
# break 语句用以跳出循环
# 非空字符串翻译为True   反之空字符串翻译为False
def get_format_person(first_name,last_name,age=''):
    person = {'姓': first_name , '名':last_name}
    if age:
        person['age'] = age
    return person

one_person = get_format_person('黄','星杰',str(25))
print(one_person)

# 