#messing with plottings
#Author: Caio Forte Ribeiro

import matplotlib.pyplot as plt
import numpy as np

x = np.array(range(1,101))
y = x**2

plt.plot(x, y)
plt.show()