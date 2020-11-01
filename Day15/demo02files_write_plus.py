user_list = 'User.txt'
ulist = {}

def password_select(passw):
    while True:
        pass_again = input('请再输入一遍密码：')
        if passw != pass_again:
            print('两次密码不一致请重试')
            pass
        else:
            return passw


print('你好啊！欢迎使用黄星杰的注册系统！')
name = input('请输入你的姓名：')
address = int(input('请输入你的账号：'))
password = input('请输入你的密码：')
password_select(password)
ulist['昵称'] = name
ulist['账号'] = address
ulist['密码'] = password

with open(user_list,'a') as file_object:
    file_object.write("\n")
    file_object.write(str(ulist))
    file_object.close()
