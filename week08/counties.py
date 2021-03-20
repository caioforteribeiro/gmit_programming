#Pie chart of unique occurrences of a value in a pie chart
#Author: Caio Forte Ribeiro

import numpy as np
import matplotlib.pyplot as plt

listOfCounties = ['Mayo', 'Galway', 'Roscommon', 'Dublin', 'Donegal']
counties = np.random.choice(
    listOfCounties,
    p = [0.1, 0.3, 0.2, 0.12, 0.28],
    size = (100)
)

unique, counts = np.unique(counties, return_counts = True)
#plt.pie(counts, labels = unique)

plt.bar(unique, counts)

plt.show()