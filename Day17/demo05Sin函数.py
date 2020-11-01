import numpy as np
import matplotlib.pyplot as plt
import sys

# 今天先画个sin函数

x = []
a = float(input("请输入你所希望的精度："))
b = float(input("请输入你的初始值："))
c = float(input("那你的终止值呢："))
plt.axis([b, c, -1.5, 4])
plt.figure()
# figure 方法可以改变图形框的一些参数  在一个figure下可以出现多个图形，但不同的figure将分成多个图
while True:
    x.append(b)
    plt.scatter(b, np.cos(b) + 2, edgecolors='none', s=5)
    b += a
    if b >= c:
        break
    pass
y = [np.sin(x) for x in x]

plt.plot(x, y, linewidth=5, linestyle="--")  # plot 函数可以更改 linewidth linestyle 这些都能使得我们的图形更加多样化
plt.show()
sys.exit()
