import numpy as np
import matplotlib.pyplot as plt

'''
    极坐标分为：极径和角度
    这里讲一下有关numpy中的arrange 与 linespace 之间的关联性 ： 
    arrange（起始值，终点值，间隔）  有点想python标准库中的range 但是好的是这里的间隔可以为任意数
    但是arrange 里面不包含终点值
    linespace （起始值，终点值，值的个数）这个包含有终点值，值的个数越大，则描述的越发精确
'''
theta = np.arange(0,np.pi*2,0.01)

r = 10*(np.cos(theta) - 1)

ax = plt.subplot(111,projection='polar')
#projection = 'polar' 指定为极坐标

ax.plot(theta, r, linewidth=3,color='red')
#第一个参数为角度，第二个参数为极径

ax.grid(True) #是否有网格

plt.show()
