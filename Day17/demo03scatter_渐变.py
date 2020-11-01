import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import sys


font_set = FontProperties(fname=r"c:\windows\fonts\STXINGKA.TTF", size=40)

x_values = list(range(1, 1001))
y_values = [x for x in x_values]
plt.scatter(x_values, y_values, s=40,c=y_values,  cmap=plt.get_cmap('Blues'), edgecolors='none' )
# 注意python3.8以后只能使用plt.get_cmap('颜色s') 以达到渐变的效果

plt.show()
sys.exit()
