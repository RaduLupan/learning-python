'''
Heatmaps - Example
'''

import matplotlib.pyplot as plt
import seaborn as sns

flights_df = sns.load_dataset('flights').pivot('month', 'year', 'passengers')
print(flights_df)


plt.title('No. of Passangers (1000s)')

# sns.heatmap(flights_df)

# We can also add the actual values in the cell blocks by specifying annot=True and using cmap argument to change the color palette. 
sns.heatmap(flights_df, fmt='d', annot=True, cmap='Blues');
plt.show()
