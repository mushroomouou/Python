# 现在我们将学习散点图的绘制
# scatter函数
import matplotlib.pyplot as plt
import sys
from matplotlib.font_manager import FontProperties

font_set = FontProperties(fname=r"c:\windows\fonts\STXINGKA.TTF", size=40)
for i in range(1,11):
    for j in range(1,11):
        plt.scatter(i,j)  # scatter 函数不仅可以输入数字  同样可以输入列表  键值对应
        # 颜色使用edgecolor=' ' 引号内部是颜色的名称  例如blue green red white brown black
plt.title("散点图", fontproperties=font_set)
plt.show()
sys.exit()
