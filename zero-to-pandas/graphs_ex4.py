'''
Heatmaps - Example
'''

import matplotlib.pyplot as plt
import seaborn as sns

flights_df = sns.load_dataset('flights').pivot('month', 'year', 'passengers')
print(flights_df)

plt.title('No. of Passangers (1000s)')
sns.heatmap(flights_df)


plt.show()
