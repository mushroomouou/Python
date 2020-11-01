for num in range(1, 21):
    print(num)

numberlist = range(1, 10001)
for num in numberlist:
    print(num)
b = sum(numberlist)
print(b)

mutiple = []
numlist = range(1, 30)
for num1 in numlist:
    if num1 % 3 == 0:
        mutiple.append(num1)
        pass
    pass
print(mutiple)
for numi in mutiple:
    print(str(numi) + ' ', end='')
    pass

# 列表解释
list_number = [num2 ** 3 for num2 in range(1, 11, 3)]
# 列表解析  首先写上列表定义方式  再在括号里写上变量储存方式  再利用for循环去实现数组实现
#
#
#
print()
print(list_number, end='\n')
