#%为占位符 %后接变量名称
#常用格式化符号
#%c   字符
#%s   通过str()字符串来实现格式化
#%i    有符号十进制整数
#%d    有符号十进制整数-32767 ~ 32768
#%u    无符号十进制整数0~65535
#%o    八进制整数
#%x    十六进制整数（小写字母）
#%e    索引符号（小写’e‘）
#%E    索引符号（打写’E‘）
#%f    浮点实数
#%g    %f和%e的简写
#%G    %f和%E的简写

#额外知识：  换行操作使用\n
name1 = '欧拉'
country = '瑞士'
print('我的名字是%s，来自%s，是一名顶级数学家'%(name1,country))

qqNumber2 = 1540470295
PhoneNumber2 = 17399983649
name2 = '黄星杰'
address2 = '南湖校区南湖宿舍7栋213室'
print('=====================================')
print('姓名：%s\n'
      'QQ号:%s\n'
      '电话号码:%s\n'
      '家庭住址:%s\n'
      %(name2,qqNumber2,PhoneNumber2,address2))
print('=====================================')

#格式化输出的另外方式.format()
#好处：不需要管数据的类型  直接使用  相当于填空
print('姓名:{}'.format(name2))

# input的练习
#输入的内容是什么  都是自动换成字符串  demo  你可以使用强制转换得到相应的数据格式
name3 = input('请输入你的姓名：')
qqNumber3 = int(input('请输入你的QQ：'))
print(type(qqNumber3))
PhoneNumber3 = input('请输入你的电话：')
address3 = input('请输入你的地址：')
print('=====================================')
print('姓名：%s\n'
      'QQ号:%s\n'
      '电话号码:%s\n'
      '家庭住址:%s\n'
      %(name3,qqNumber3,PhoneNumber3,address3))
print('=====================================')