# 字典啊和Java的对象很想   Java里面就是new一个对象  这里使用的时dictionary 也就是字典去定义一个对象  具体操作如下
alien_0 = {'color': 'white',
           'move_speed': 5,
           'killscore': 3}
print(alien_0['color'])
print(alien_0['move_speed'])
print(alien_0['killscore'])
# 添加与删除变量
alien_0['x_positions'] = 11
alien_0['y_positions'] = 22
print(alien_0)
del alien_0['move_speed']
alien_0['move_speed'] = 'fast'
print(alien_0)
# 修改直接使用赋值操作
#自增的速度变化
if alien_0['move_speed'] == 'fast':
    incress_x = 5
    pass
else:
    incress_x = 3
    pass
alien_0['x_positions'] += incress_x
print(alien_0)

# 字典这一章的一些例题
my_bestfriend = {'first_name': 'li',
          'last_name': ' si mao',
          'age': 18,
          'city': 'wu han'}
# 有数字参与时尽量使用str  以输出
print(my_bestfriend)
for variable, information in my_bestfriend.items():
    print('\nvariable:' + variable)
    print('information:' + str(information))
    pass
for variable in my_bestfriend.keys():
    print('\n信息种类：' + variable)
    pass
for information in my_bestfriend.values():
    print('\n信息内容：' + str(information))
    # .items()方法是针对于键和值的数据来打印的一种选定方法
    # .keys()方法是针对键的打印来的一种方法
    # 。values()方法是针对于值打印的一种选定方法

    # 对于列表  元组  字典的访问都是用[]来访问！！！！