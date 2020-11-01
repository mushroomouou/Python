#循环流程使用while for in  实现
#while 循环
#语法特点
#1.有初始值
#2.条件表达式
#3.变量要自增自减否则死循环
#求取100个整数的和
num1 = 1
num2 = 0
while num1 <= 100:
    num2 += num1
    num1 += 1
print(num2)
