import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

font_set = FontProperties(fname=r"c:\windows\fonts\STXINGKA.TTF", size=40)

x_values = list(range(-1000, 1001))
y_values = list(range(-1000, 1001))
z_values = list(range(-1000, 1001))
plt.title('三维图形',fontproperties=font_set)
plt.plot(x_values,y_values,z_values)
plt.show()