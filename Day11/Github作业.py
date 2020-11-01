# #
# 写一个程序，找出所有能被7整除但不是5的倍数的数，
# 2000至3200（均包括在内）。
# 获得的数字应以逗号分隔的顺序打印在单行上。

# for num in range(2000, 3201):
#     if num % 7 == 0 and num % 5 != 0:
#         print(str(num) + ',',end='')


#Question:
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

#不就是阶乘吗
# i = int(input('请输入阶乘的数字：'))
# if i == 0:
#     print(1)
#     exit()
# num = 1
# while i >0 :
#     num = num*i
#     i-=1
#     pass
# print(num)

#标准答案
# def fact(x):
#     if x == 0:
#         return 1
#     return x * fact(x - 1)
#
# x=int(input())
# print(fact(x))

# Question:
# With a given integral number n, write a program to generate a dictionary that contains (i, i*i)
# such that is an integral number between 1 and n (both included). and then the program
# should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}


#
# def get_two_square(i,dictionary):
#     for num in range(1,i + 1):
#         double = num**2
#         dictionary[num] = double
#     return dictionary
#     pass
#
# i = int(input('请输入数字：'))
# dic = {}
# dictionary =  get_two_square(i,dic)
# print(dictionary)



#Question:
# Write a program which accepts a sequence of comma-separated numbers from console and
# generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')


# values=input()
# l=values.split(",")
# t=tuple(l)
# print(l)
# print(t)

#.split( 字符名 , 索引值 不写默认全切  )  且完后可以得到一个列表
# 使用 tuple()函数可以进行强制转换成元组



class InputOutString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input()

    def printString(self):
        print(self.s.upper())

strObj = InputOutString()
strObj.getString()
strObj.printString()












