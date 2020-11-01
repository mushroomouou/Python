# def city_country(country ,cityone, citytwo='', citythree=''):
#     if citytwo and citythree:# 这里的操作其实就是可选形参
#         full = '"' + country + ',' + cityone + ',' + citytwo + ',' + citythree + '."'
#         pass
#     elif citytwo:
#         full = '"' + country + ',' + cityone + ',' + citytwo + '."'
#     else:
#         full = '"' + country + ',' + cityone +  '."'
#     return full
#
# stack = city_country('中国','宜昌','武汉','江南')
# print(stack)


#  与GO语言的区别在于这里的函数无需指定返回值 你想让他返回什么就返回什么
#  数字0与空字符都 无填充的列表 元组 字典代表bool中的false
#  相对应的则表示True
def make_album(n, so, nu=0):
    dictionary = dict()
    dictionary['名字'] = n
    dictionary['歌名'] = so
    if nu:
        dictionary['歌曲数量'] = nu
        pass
    return dictionary


while True:
    print('这里是专辑录入系统')
    print('如果向退出可以随时输入“q”以用来退出程序')
    name = input('请输入歌手姓名：')
    if name == 'q':
        print('欢迎下次使用！')
        break
    song = input('请输入专辑名：')
    if song == 'q':
        print('欢迎下次使用！')
        break
    print('请问你是否知道歌曲数')
    print('请回答（Y/N）')
    judge = input('')
    if judge == 'Y':
        num = input('请输入歌曲数：')
        if num == 'q':
            print('欢迎下次使用！')
            break
        print(make_album(name, song, int(num)))
    elif judge == 'q':
        print('欢迎下次使用！')
        break
    else:
        print(make_album(name, song))

# 使用函数仍然可以去修改列表数据  但是对于某县不能修改的列表 可以使用切片以获得复制品  再去操作  而不对 原本值操作
# 晚上看书了明天再战
