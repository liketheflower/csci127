import matplotlib.pyplot as plt

import pandas as pd
pop = pd.read_csv('nycHistPop.csv',skiprows=5)
print (pop)
print(pop['Bronx'])
pop.plot(x="Year")

plt.show()
