#有关if语句的相关练习
#5-3  #外星人的颜色
import random
alien_color = ['green', 'yellow', 'red']
enemy_color = random.choice(alien_color)
print(enemy_color)
#下面进行对于enemy颜色与相关得分的判断语句
if enemy_color == 'green':
    print('+5')
    pass
elif enemy_color == 'yellow':
    print('+10')
    pass
else:
    print('+15')
    pass


#5-8  以特殊的方式与服务员打招呼
# users = ['admin', 'eric', 'mike', 'jone', 'marry']
# logging_user = random.choice(users)
# if not users:
#     print('We may need more users!')
#     exit()#列表长度判断   列表自身判断  借助其他列表判断
# if logging_user == 'admin':
#     print('Hello admin, what would like ti change?')
#     pass
# else:print('Hello' + ' ' + logging_user + ',' + 'thank you for your logging in again!')

#检查是否用户名重名
original_userlist = ['huang xing jie', 'li si mao', 'ou la', 'a', 'b']
user = input('请输入你的用户名:')
for oruser in original_userlist:
    if user.lower() == oruser.lower():
        print('该用户名已被注册，请更改后重试。')
        exit()
        pass
    else:continue
    pass
print('该名称可以使用')
#作业完成！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！1

