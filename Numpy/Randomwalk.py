import numpy as np
from matplotlib import pyplot as plt
# 实现折线形式的随机漫步
# n = int(input("请输入你想要慢步的次数"))
# y_values = []
# for y in range(0,n):
#     y_values.append(np.random.sample())
# x_values = [x for x in np.arange(0,n)]
# plt.figure()
# plt.plot(x_values,y_values,linewidth=1,color='red')
# plt.show()

#随机点式的漫步：
#如上换成scatter就可以了。，
# 注意点的随机漫步也要随机x轴
n = int(input("请输入你想要漫步的次数："))
x_values = []
y_values = []
for x in range(n):
    x_values.append(np.random.randint(low=-2,high=3))
x = np.cumsum(x_values)
for y in range(n):
    y_values.append(np.random.rand())
y = np.cumsum(y_values)
plt.figure()
plt.scatter(x,y,edgecolors='blue')
plt.show()
