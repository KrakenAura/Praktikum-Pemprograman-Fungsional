import matplotlib.pyplot as plt
import numpy as np

x=[1,2,3,4,5,6]
y=[3,7,2,8,5,7]

colors = np.array(["red", "green", "blue", "yellow", "black","purple"])
plt.scatter(x, y, c=colors)
plt.show()
plt.show()