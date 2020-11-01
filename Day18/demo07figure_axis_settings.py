import matplotlib.pyplot as plt
import numpy as np

x_values = np.arange(-5,5,0.1)
y1 = [x**2 for x in x_values]
y2 = [x + 2 for x in x_values]
plt.plot(x_values,y1)
plt.plot(x_values,y2,linestyle="--")
plt.show()
