num1 = int(input("请输入你的数字："))
i = 1
while True:
    if num1 % i == 0:
        print(i)
    i += 1
    if i > num1:
        break
