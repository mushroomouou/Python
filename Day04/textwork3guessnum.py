import random
original_userlist = ['huang xing jie', 'li si mao', 'ou la', 'a', 'b']
user = input('请输入你的用户名:')
for oruser in original_userlist:
    if user.lower() == oruser.lower():
        print('该用户名已被注册，请更改后重试。')
        exit()
        pass
    else:continue
    pass
original_userlist.insert(0,user)
print(original_userlist)
print('该名称可以使用')

a = random.randint(1, 100)
b = 0
while b < 7:
    b += 1
    c = int(input('请输入你所想的数字：'))
    if c == a:
        print('厉害啊！ 只花了' + str(b) + '次' + '就猜出来了！')
        break
    elif c > a:
        print('猜大了')
    else:
        print('猜小了')
if b == 7:
    print('你输了，' + '本次数字炸弹为：' + str(a))
exit()
