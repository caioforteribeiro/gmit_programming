#Plots random salaries from a range
#Author: Caio Forte Ribeiro

import numpy as np
import matplotlib.pyplot as plt

minSalary = 20000
maxSalary = 80000
entries = 100

np.random.seed(1)

salaries = np.random.randint(minSalary, maxSalary, entries)
ages = np.random.randint(low = 21, high = 65, size = entries)
plt.scatter(salaries, ages, label = "salaries")

x = np.array(range(1,101))
y = x**2

plt.plot(x, y, color = "r", label = "x squared")

plt.title("random plot")
plt.xlabel("salaries")
plt.ylabel("age")
plt.legend()
plt.savefig("prettier-plot.png")
plt.show()
