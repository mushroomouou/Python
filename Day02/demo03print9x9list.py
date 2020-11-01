#第一实际目标：打印一个直角三角形

# num = 6
# while num >= 0:
#     j = 1
#     while j <= num:
#         print('*',end=' ')
#         j += 1
#         pass
#     print()
#     num -= 1

#打印等腰三角形   打印4行的等腰三角形
#注释：，end=' '为不换行
x = int(input('等腰三角形的层数为：'))
num = 0
while num < x:
    j = 0
    m = 0
    while j < x - num:
        print(' ',end='')
        j += 1
        pass
    while m < 2*num + 1  :
        print('*',end='')
        m += 1
        pass
    num += 1
    print()

#循环之中嵌套着循环  打印与变量有关的各种字符


m = int(input('请输入三角形层数：'))
y = 0
while y < m:
    r = 0
    e = 0
    while r < m - y:
        print(' ',end='')
        r += 1
        pass
    while e < 2*y + 1:
        print('*',end='')
        e += 1
    print()
    y += 1
