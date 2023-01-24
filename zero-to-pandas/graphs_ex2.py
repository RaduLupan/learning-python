'''
More graph examples using the Iris dataset included in Seaborn. 
'''
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
flowers_df = sns.load_dataset('iris')

'''
# Scatter plot.
plt.figure(figsize = (12,6))
plt.title('Sepal Dimensions')

sns.scatterplot(x = 'sepal_length', y = 'sepal_width', hue = 'species', s = 100, data = flowers_df)
'''

# Multiple histograms on the same chart.
setosa_df = flowers_df[flowers_df.species == 'setosa']
versicolor_df = flowers_df[flowers_df.species == 'versicolor']
virginica_df = flowers_df[flowers_df.species == 'virginica']


# Draw multiple histograms on the same chart with reduced opacity so that the bars don't hide each other.
# plt.hist(setosa_df.sepal_width, alpha=0.4, bins=np.arange(2,5,0.25))
# plt.hist(versicolor_df.sepal_width, alpha=0.4, bins=np.arange(2,5,0.25))
# plt.hist(virginica_df.sepal_width, alpha=0.4, bins=np.arange(2,5,0.25))

# We can also stack the histograms one on top of each other.
plt.hist([setosa_df.sepal_width, versicolor_df.sepal_width, virginica_df.sepal_width],
          bins=np.arange(2,5,0.25),
          stacked=True)

plt.title('Sepal Width Distribution')
plt.legend(['Setosa', 'Versicolor', 'Virginica'])
plt.show()
