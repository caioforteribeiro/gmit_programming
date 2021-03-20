#Prints out a list of 10 random salaries from a range
#Author: Caio Forte Ribeiro

import numpy as np

minSalary = 20000
maxSalary = 80000
entries = 10

np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, entries)
salariesPlus = salaries + 5000
salariesMult = salaries * 1.05
newSalaries = salariesMult.astype(int)

print(salaries)
print(salariesPlus)
print(newSalaries)