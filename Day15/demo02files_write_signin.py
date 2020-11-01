file_name = 'User.txt'
file_name2 = 'Comment_Language.txt'
# 输入系统：
print('账号：')
address = input('')
print('密码：')
password = input('')

with open(file_name, 'r') as file_object:
    lines = file_object.readlines()
    for line in lines:
        di = eval(line)
        if address in line and password in line:
            print('欢迎' + di['昵称'] + '使用我的Python系统！')

        else:
            print('我很抱歉，可能是你的账号密码错误或者是还未注册')
print('你想进行以下哪种在操作？')
print('评论有关语言学习的建议--------（COMMENT）')
selection = input('')
print('请输入你的看法：')
comment = input('')
print('感谢你的评论！！！')
if selection == 'COMMENT':
    with open(file_name2, 'a') as file_object2:
        file_object2.write(comment + '\n')
        file_object2.close()
        pass
    pass
else:
    print('有些程序还在编写中，请稍等哦！')
