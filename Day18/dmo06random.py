from Day18.demo06_随机漫步 import RandomWalk
import matplotlib.pyplot as plt

import sys


# 渐变符号是  cmap  而不是camp
# 不能在类中调用类  ！！！！！
rm = RandomWalk(10000)
rm.fill_walk()
points = list(range(rm.num_points))
plt.scatter(rm.x_values, rm.y_values, c=points, cmap=plt.get_cmap('Blues'), edgecolors='none', s=1)
plt.scatter(rm.x_values[0],rm.x_values[0],s=1,c='white')
plt.scatter(rm.x_values[-1],rm.y_values[-1],s=100,c='black')
plt.show()
sys.exit()
