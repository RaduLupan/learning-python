'''
More graph examples using the Iris dataset included in Seaborn. 
'''
import matplotlib.pyplot as plt
import seaborn as sns

flowers_df = sns.load_dataset('iris')

plt.figure(figsize = (12,6))
plt.title('Sepal Dimensions')

sns.scatterplot(x = 'sepal_length', y = 'sepal_width', hue = 'species', s = 100, data = flowers_df)

plt.show()
