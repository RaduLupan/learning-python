'''
Bar Plots with Averages - Example
'''

import matplotlib.pyplot as plt
import seaborn as sns

# Dataset example from Seaborn tips - information about the sex, time of day, total bill, and tip amount for customers visiting a restaurant over a week.
tips_df = sns.load_dataset('tips')

# Bar plots side by side based on hue.
# sns.barplot(x = 'day', y = 'total_bill', hue = 'sex', data = tips_df)


# You can make the bars horizontally simply by switching the axes.
sns.barplot(x='total_bill', y='day', hue='sex', data=tips_df);
plt.show()
