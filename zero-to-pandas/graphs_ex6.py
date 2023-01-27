'''
Plotting Multiple Charts in a Grid - Example
'''

import matplotlib.pyplot as plt
import seaborn as sns

# Matplotlib and Seaborn support plotting multiple charts in a grid using plt.subplots which returns a set of axis for plotting.
fig, axis = plt.subplots(2, 3, figsize = (16,8))

plt.show()
