import matplotlib.pyplot as plt
import sys
from matplotlib.font_manager import FontProperties

font_set = FontProperties(fname=r"c:\windows\fonts\STXINGKA.TTF", size=40)
# import 语句引用matplotlib中的pyplot模块 当作plt使用   注意这里是习惯用法
# x_des = [x for x in range(-100,101)]
# y_des = [x**2 for x in x_des]
# plt.plot(x_des,y_des)
# plt.plot()
# plt.show()

# 修改标签文字，和线条粗细
# 如上的图形  我们将会用来练习和学习图形的各种可视化设置的设定
x_des = [x for x in range(0, 101)]
y_des = [x ** (1/2) for x in x_des]
plt.plot(x_des, y_des, linewidth=5)  # 可以在函数图像参数设置括号里面设置线条宽度

# 下面将演示图像title的打印规则
plt.title('Function', fontproperties=font_set)  # 给文章注标题
# plt.xlabel();这个用来给x轴命名  plt.ylabel();用来给y轴命名
# 使用size= 来对数据的字体大小进行修改
plt.xlabel("横坐标", fontproperties=font_set,size=30)
plt.ylabel("纵坐标", fontproperties=font_set,size=30)
# 此处将进行坐标轴的数值间隔 labelsize=??  axis=??这个是对两坐标进行描述
plt.tick_params(axis='both',labelsize=10)
plt.axis([0,10,0,10]) # 此处规定了数据输出的起点与终点  方便取局部用以分析！！！
plt.show()
sys.exit()
