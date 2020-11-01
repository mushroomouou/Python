magicians = ['alice', 'david', 'carolian']
for magician in magicians:
    print(magician.title())
    #循环体中可以输入任何代码  都可以运行
    #注意缩进问题  不要随意增减空格


#数字列表
#range()函数
for num in range(0, 9):
    print(num)

#list函数将数字列表转化为真列表
numlist1 = list(range(1, 9))
print(numlist1)
#range函数默认情况下默认方差为1   其余情况下特殊说明  操作如下、
numlist2 = list(range(0,17,5))
print(numlist2)
i = 0
while i < len(numlist2):#模仿Java中的编程习惯
    if numlist2[i] % 2 != 0:
        del numlist2[i]
    i += 1  #不要掉  ！！！！！！！！！！！
print(numlist2)


#编辑出一个出平方数的数组
number = []
for value in range(1, 11):
    number.append(value**2)
print(number)
number2 = [haha**2 for haha in range(1 , 11)]
print(number2)
exit()






