# 元组   ：   与列表区分的地方在于  元组不能去修改元组中已经储存的相关数值   而列表却可以
dimension = (100, 200)
# dimension[0] = 100# 错误
#元组的遍历
print(dimension)
for num in dimension:
    print(num)

#虽然直接对元组中相关的数据修改不能做到   但是对于整个元组的变量赋值确实可以做到的

dimension = (400, 500)
print(dimension)
