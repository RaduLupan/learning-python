'''
Plotting Multiple Charts in a Grid - Example
'''

import matplotlib.pyplot as plt
import seaborn as sns

# Data for chart 1.
years = range(2000, 2012)
apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931, 0.934, 0.936, 0.937, 0.9375, 0.9372, 0.939]
oranges = [0.962, 0.941, 0.930, 0.923, 0.918, 0.908, 0.907, 0.904, 0.901, 0.898, 0.9, 0.896]

# Data for chart 2.
flowers_df = sns.load_dataset("iris")

# Matplotlib and Seaborn support plotting multiple charts in a grid using plt.subplots which returns a set of axis for plotting.
fig, axes = plt.subplots(2, 3, figsize = (16,8))

# Use the axis for plotting.
axes[0,0].plot(years, apples, 's-b')
axes[0,0].plot(years, oranges, 'o-r')
axes[0,0].set_xlabel('Year')
axes[0,0].set_ylabel('Yield (tons per hectare)')
axes[0,0].legend(['Apples', 'Oranges'])
axes[0,0].set_title('Crop Yields in Kanto')

# Pass the axes into seaborn.
axes[0,1].set_title('Sepal Length vs Sepal Width')
sns.scatterplot(x = flowers_df.sepal_length,
                y = flowers_df.sepal_width,
                hue = flowers_df.species,
                s = 100,
                ax = axes[0,1])

plt.show()
