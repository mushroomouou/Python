# 尝试打印一下e 的值
import matplotlib.pyplot as plt
import sys

# 使用for循环打印你想要打印的精度
cycle = int(input("请输入你想要达到的精度"))
for num1 in range(1, cycle):
    result = (1 + 1 / num1) ** num1
    plt.scatter(num1, result, edgecolors='pink')
    if num1 == cycle:
        print("最后一个数据是：" + str(result))

plt.show()
sys.exit()
